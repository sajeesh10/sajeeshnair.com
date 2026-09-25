---
title: Building High Performance Cloud Data Protection
date: 2021-07-08
topic: Performance engineering
---

*Originally published on the [Druva blog](https://www.druva.com/blog/building-high-performance-cloud-data-protection/).*

For the last 3 years I have had the opportunity to work on some of the hardest problems of scale and performance in the storage domain. Druva's data protection is the first of its kind: cloud-native and SaaS from the ground up. This means we are the first ones to solve some of the technical challenges in this space.

There are several challenges to be solved in building a successful cloud-based data protection platform, with performance and scalability being especially important. The performance dynamics of a cloud backup solution are completely different from traditional on-premises products, and require a massive shift in how we architect backup solutions.

In this essay I cover the factors affecting the performance of cloud backups (for datacenter workloads), and how we at Druva solved them. We break these down in four key focus areas:

1. Network
2. RTO anxiety
3. Hyperscale cloud file system
4. TCO balance

## 1. Network

Any architecture for cloud-based backup requires taking into consideration the network between customer data centers and the cloud. Moving TBs of data across a network is a hard problem to solve. In addition, the quality of the network can vary greatly based on customers and their ISPs. This begs the question, how do we design a product that reliably meets RPOs and RTOs in the face of these impediments?

### Bandwidth optimization

Bandwidth is always a sparse commodity. And lesser bandwidth intuitively means lower performance. However, there are a few ways to design around this:

- **Compression at the source:** It is well known that the basic way to improve payload performance over the network is to compress it. On-premises backups often rely on compression as a means to reduce storage needs, and hence compress at the backup device. In the case of cloud backups, it becomes imperative to compress at the source to save bandwidth. There are several compression algorithms that can be used, and it is important to understand the tradeoff between them. Usually, algorithms are compared on the basis of speed (data compressed per unit time), compression ratios yielded, and the CPU footprint that they require. Higher compression ratios require more CPU for a given algorithm. Each algorithm has its strengths: some compress data at a high ratio, but do so at slower speeds resulting in lower throughput.

    To increase backup efficiency, we implemented methods to skip already compressed files like zip and images. Attempting to compress these formats usually costs CPU cycles and does not yield any compression. Choosing the right compression algorithm for the use case is key for performance. The [Squash compression benchmark](https://quixdb.github.io/squash-benchmark/) is a good place to compare algorithms.

- **Deduplication:** This process aims to remove duplicate data. By sending only unique data over the network, we further optimize bandwidth usage. Unlike on-premises solutions, Druva does a dedupe check at the source. This is powered by our patented intelligent global deduplication, which checks for dedupe across all data the customer has backed up with Druva to a given AWS region. Our backup sizes are typically only one-third of the customer's source data.

### Network latency

- **Maximize bandwidth usage:** In data-path-heavy applications like backups, network latencies limit the ability to use the available bandwidth efficiently. This happens because network packets have to wait longer to be acknowledged (at the TCP layer), so the application sending data can fill only part of the available network pipe. One way to solve this would be to use more TCP connections. However, a large number of TCP connections is not a scalable approach from a cloud standpoint. Druva has a multi-tenant cloud which hosts tens of thousands of backups each day. This would result in several thousand, or even millions, of TCP connections, which would cause the servers to choke. Hence, it is important to improve bandwidth utilization with an optimal number of connections. We solve this problem in two ways. First, Druva's proprietary protocol (Druva RPC) multiplexes several payloads over a single TCP connection. Second, we use a high number of workers to send a large number of packets without waiting for acknowledgments, to compensate for the delays caused by latency. This enables our agents to use available bandwidth efficiently and overcome the impact of network latency.

- **Request clubbing:** The best way to avoid latency is to minimize the number of network calls. For this, we club the metadata and data calls at multiple layers. This is built into the Druva RPC protocol. Clubbing requires agents to bundle their calls into one request, and the server to unbundle that request into multiple service calls. Once again, tradeoffs need to be made to ensure that the benefits of minimizing calls are larger than the cost of bundling and unbundling.

## 2. RTO anxiety

A common concern when people think about electric cars is range anxiety: the fear that a vehicle has insufficient range to reach its destination and would strand its occupants. For the majority of commutes this is a non-issue. We observed a similar perception mismatch with customers considering cloud-based backup. The prevalent mental model of cloud and networks leads most people to believe that restores over the network will be slow. However, the majority of customer RTO requirements are easily met with Druva's solution, and customers don't need to buy expensive backup appliances just to address RTO concerns. For customers who have narrow RTOs, Druva also offers CloudCache, which accelerates restores for low-bandwidth, high-latency use cases by maintaining a local copy of the data.

To address this perception, we did a detailed exercise in collaboration with AWS. We were able to demonstrate that up to 500 miles from an AWS region, and even with five percent network packet loss, there is marginal impact to restore times compared to local restores. Latency only starts playing a role if a customer on the U.S. East coast tries to restore data from the U.S. West coast (over 2,500 miles). This is unlikely, since customers back up their data to the closest AWS region to get the best possible performance. [Here is the detailed writeup](https://aws.amazon.com/blogs/apn/meet-your-recovery-time-objectives-with-druva-and-aws/) of the exercise done with AWS.

## 3. Hyperscale cloud file system

The sections above focus on how to efficiently send data from the customer's premises to the cloud. On the other end is Druva's own cloud-native file system. Thousands of backups happen every day on the Druva Cloud, which means several terabytes of source data are processed daily. The Druva Cloud is built on a robust cloud-native file system powered by AWS DynamoDB and AWS S3.

It is important to ensure the cloud architecture supports such high throughputs of backup data. Cloud storage provides self-healing properties, which result in continuous consistency and integrity checks of the customer's restore points. This ensures a healthy copy of data is always ready when it needs to be restored. All these jobs mean several compute cores, hundreds of S3 puts per second, and heavy network throughput. Architecting a system with these characteristics requires rethinking data protection entirely.

## 4. TCO balance

One of the key expectations customers have of a cloud and SaaS-based solution is cost effectiveness. A lot of thought goes into designing a solution that keeps total cost of ownership (TCO) as low as possible. However, cost and performance usually sit on opposite sides of the tradeoff. There are a few ways to ensure an optimal balance:

1. **Optimize unit performance:** The proxies we install on customer premises run on customer-provided hardware or VMs. Hence, it is important to keep the footprint low without compromising RPO requirements. Typically, this means optimizing throughput per unit of footprint: we tune our agents for fewer storage reads, CPU cycles, memory usage and network bandwidth, and focus on metrics like GB per hour of throughput per CPU core.
2. **Cloud compute:** Backup is a compute-heavy process in the cloud, primarily due to encryption and metadata operations. On AWS, more compute equates to higher cost, so sizing and efficient provisioning become key to cost efficiency. This also means choosing instance types that give a good cost-to-performance balance.
3. **Storage costs:** S3 storage costs are kept in check with intelligent tiering of customer data under long-term retention. Here, performance is deliberately traded off for lower cost, typically for older or archived data where customers have more relaxed RTOs. S3 PUT costs are kept in check with optimizations like metadata clubbing, or combining data objects into one S3 object. This once again requires understanding the performance tradeoff.

## Conclusion

Building a successful cloud-based data protection platform requires solving the challenges above, and their solutions can often be contradictory. For example, higher throughput may require more powerful infrastructure, but that may increase customer TCO. The key to customer satisfaction lies in finding an optimal solution that doesn't sacrifice performance to meet cost expectations. Any application whose data path traverses large networks will likely have to solve these architectural challenges.
