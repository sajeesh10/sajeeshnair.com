---
title: Performance Engineering of Backups
date: 2018-05-01
topic: Performance engineering
archive: yes
---

![](/images/tapes.jpg)



Two years ago I quit my consulting job to work on the Performance Engineering of one of the most boring sounding workloads in the world of tech: BACKUP.

Before this I had worked on performance and scalability across the breadth of technology & domain. Enterprise applications, hyper-scale web applications, high throughput banking/finance back-ends, legacy healthcare workflow systems you name it. However **Data-Protection** was absolutely new to me.

In these 2 years, I had the opportunity to work on the forefront of technology in the Cloud based Data Protection space. What I did not realize at the time was that, since we were the first company to protect data by natively backing it up to Cloud(AWS), a huge part of the tech being developed was novel in nature. Most of the reference material available were very On-Premise-Backup inclined, which was the incumbent ecosystem. However, when you backup the data to cloud the rules of the game are very different.

As a performance engineer I realized that on-premise backups never had to solve the problem of moving data over the Network. The only network they dealt with were the quick-n-fat pipes of LAN.

As simple as it may sound, moving huge amounts of data over network is very hard. And solving this is at the heart of performance engineering of cloud based backups(among several other fun stuff of-course). And that is what makes backup an interesting workload for some hard core performance engineering.

In this post I want to share a few things I learnt about performance and scalability of cloud based backup while trying to keep it light on technical details.
#
#
#
The architecture typically looks like this: there is an agent that is installed on source system(e.g. a server in customer data center) and there is a server(cloud) that ingests and stores data sent by the agent. Performance engineering involves making sure that agent can push data fast enough and the server can ingest that data at the same pace.
##
**Less is better:** Our objective is to protect the data by moving it to cloud. But we want to do this by moving as less of it as possible from premise to cloud. Lesser data to be moved means lesser network traffic, and better performance. As simple as this sounds, this philosophy goes a long way in influencing the core solution.

This is primarily achieved by two mechanisms: Compression and De-duplication.
##
**Compression:** compression is very key to moving data(remember Pied Piper from Silicon Valley?). Compression gives us the potential to reduce the amount of data sent on the wire drastically. However, this also has performance implications, since it adds a step of data processing. Compression is also a compute intense activity, so it comes at a price that we have to be mindful of. More we compress the data higher the cpu cost, but lower the network and storage costs. There are several compression algorithms that are available. Evaluating and choosing the right one that balances compression ratio and compute needs is key to scalability. Squash Compression Benchmark is a good place to find some very useful statistics.
##
**De-duplication:** dedupe simply means you only backup unique blocks of data and maintain references for every place a block is used. And if dedupe is done before you send data over the wire(source side dedupe) then this gives major gains in performance. However, dedupe checks itself has some cost to performance as it adds one more step in processing of data and it is important to balance the cost vs. benefits while designing the feature.
##
**IO sensitivity:** unlike other workloads that I have worked on before, with data-protection, you become very mindful of IO and its cost at every step of the way. In a nutshell the data is read from one end(source systems) and transmitted out the other end(on network to cloud). And between these two resides your logic and secret ingredient to backup. If your secret ingredient is good, then with minimal compute the application can scale infinitely to exploit all the source IOPs and/or Network bandwidth available. This balancing of compute, disk and network is a major part of day-to-day scalability engineering.

**Encryption:** No data-protection is complete without encrypting the data. Encryption is another level of processing that needs to be done with the data. Typically all encryption is compute intense and hence has major performance impact. Every time data is encrypted(subsequently decrypted) it comes at a cost to performance. Managing this cost is key to scalability of backup solution.

**Its not all about IO:** data backup sounds like a predominantly IO intense activity. But it is also an extremely compute hungry activity. Compression and Encryption both have heavy CPU costs. Even the typical SSL encryption(and decryption) of every payload sent over the network racks up sizeable amount of CPU usage. Other than this there are always activities like splitting and stitching of data blocks etc. which requires CPU. It is critical to tune these CPU bound areas to deliver high performance backups.

**One size does not fit all:** Different customers have different appetite for backup workloads. Some customers are willing to provide as much resources required to backup the data as soon as possible. This includes very high compute and high bandwidth network like AWS Direct Connect. Some others set aside only few cores and few Mbps of their network to let backups run in the background. The agent needs to be able to shrink or expand to fit the available resources(like occamy). This along with all its performance implications needs to be taken into consideration while designing the product.

**Different workload different performance:** the nature of data that is being backed up is perhaps the biggest deciding factor of backup performance. Files, virtual machines, databases, containers all these workloads have totally different performance dynamics when it comes to backup. How compressible the data is also plays an important part determining performance of backup. On one end of the spectrum there could be text files which compress very well and on the other hand could be media files(movies/images) which are already a compressed format and don’t compress further. Compressing data with low compressiblity also requires higher cpu cycles.

The ratio of size of data to the number of files also has a major impact. If the data is fragmented across many small files the IO efficiency at source(reads) and cloud(writes) reduces drastically. And this has major implications for performance of the backup.

There are several other ways in which nature of data and workloads determine the backup solution from a performance standpoint. It is a topic worthy of a post for itself.

**Petabyte scale data ingestion:** Cloud based data protection requires hosting several petabytes of data in the cloud. There are several thousand backups pushing several Terabytes of data every day. It is important to ensure that the servers can scale to ingest all this data, do the necessary processing and write it to underlying storage layer. All this while keeping Compute and IO at optimum levels, since in AWS every CPU core and every IO is billed. Hence a lot of thought during design process goes into optimizing/minimizing the compute intense activities and IO operations that are done.

**All things AWS:** The backup solution is built and hosted ground up in AWS Cloud. This means that for effective performance engineering we need to pay close attention to:

- Compute : EC2 instance families/types their cpu speeds, EBS bandwidth & Network bandwidth limitations.
- Block storage: volumes types — ST1/GP2/IO1, their baseline and burst IOPs/throughput specs.
- Object storage: S3, S3-IA, Glacier, Deep Archive — get/put latency, throughput limits etc.
- Databases: RDS, DynamoDB and their performance characteristics.

Conclusion: Cloud based backups offer a plethora of problems to be solved as a performance engineer. It ranges from kernel to application runtime to cloud deployments. Certainly not so boring!
