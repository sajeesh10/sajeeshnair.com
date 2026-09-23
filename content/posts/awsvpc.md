---
title: Getting Started with AWS VPC
date: 2019-12-05
topic: Cloud
---

I recently had a chance to deploy an application end to end in AWS. I found the networking part of it especially interesting. I initially tried to just pick up bits of info related to VPC setup and make do, but that turned out to be a challenge. I realized that it is important to understand all the pieces of the puzzle when it comes to your VPC and networking. It is much better to invest in a slightly more methodical approach. If you are getting started on AWS Networking and this is your first stint at trying to setup VPC this read should help.


## My Approach

This may not be the best approach, but this works really well for me:

- Start by listing your application components and all the AWS products it uses. E.g. EC2s, Lambda w. API Gateway, S3, RDS, DynamoDB.. you get the point.
- Be clear on network requirements of each component. At a high level you need to know- Who talks to whom, who will send requests to internet, who will only receive requests from internet, who talks to open AWS resources(like S3, DynamoDB etc.).
- In addition to this you should also know the communication ports and protocols they use. If you are building something from scratch you are probably going to use REST/HTTP.

Don’t worry if you don’t have all the details. At the least you should know the components that needs internet access and the ones that don’t. You can build on top of this as you develop new components.

Rule of thumb: don’t provide internet access unless really required.

### Part 0: IP Addresses

Before we get into VPC make sure we understand how to manage IP Addresses.

**Public IP Address:** If your EC2 instance needs to be accessed from outside your vpc(e.g. over the internet) then it needs to have a Public IP. Public IP is the identity of your instance for outside world. When you launch an instance, AWS lets you auto-assign a Public IP from its pool of IPs.

If you don’t want to access the instance from outside your VPC, then it is a good idea to launch the instance with only Private IP. The option to assign/not assign Public IP automatically is provided at instance launch as shown in snapshot below.


![](/images/vpc-1.png)


**Private IP address:** Private IP is the identity of your instance within your network(vpc). This IP is not visible/accessible to the outside world and hence gives you a basic layer of security. Public IP is mapped to Private IP using a network address translation. A Private IP is automatically assigned to your instance when it is launched.
**Point to Remember #1:** An instance can have a primary and a secondary Private IP Address. If the instance has public IP, it must be mapped to one of the private ips. As you would have guessed by now, private ips do not necessarily need to be mapped to public ips. So you could have 2 private ips and 1 public ip.

**Elastic Network Interface(ENI):** think of ENIs as your NIC cards, only virtual. These are logical components very central to networking in AWS.

You create an ENI into a subnet. Then “typically” associate a primary and a secondary private IP; and 1 or more public/elastic ips corresponding to the private ips. You can also specify security group for the interface. And then you attach the ENI to your EC2 instance(for eg. as eth0 device).

ENI carries its properties with it as it moves. What that means is if you detach an interface from an instance and attach it to another one the IP addresses, security groups and other configs will carry on to the new instance. This feature comes in handy when you want to keep your instance’s network properties consistent(e.g. IPs) between reboots or new launches.

An EC2 instance can have multiple ENIs and each ENI can have multiple IP addresses. The number of ENIs per Instance and number of IPs per ENI is defined by aws limits for each instance type. ENIs can be used to address several other more intricate networking use cases. Further reading.

**Elastic IP:** For the most part you should be able to do with using the default public ips that are associated when you start an ec2 instance. The only challenge with them is that they change if your instance reboots. So if your traffic routing works using Public Ip of the ec2, then after a reboot of the instance things get a bit tricky.

That is where Elastic IP comes into the picture. Elastic IPs are static public IPs that AWS provides to your account. You can associate an EIP with an ENI and attach that ENI to an EC2 or you can directly attach an EIP to an EC2.

You can associate and dis-associate IPs with EC2 while it is running as well.

Public IPs are hard to come by and hence AWS is a bit stringent(rightly so!) when it comes to EIP usage. If you allocate an EIP in your account and don’t attach it an instance then you are charged at an hourly rate for it.

There is a max limit of 5 EIPs from account with the first one being free. Ref: Pricing Details

## CIDR: Classless Inter-Domain Routing

CIDR is method/approach to create/allocate IP addresses. For setting up a vpc you don’t really need to know the details of CIDR. You just need to understand the CIDR Notation of IP Address Ranges.

As we know, IP Address are mentioned as 4 numbers aaa.bbb.ccc.ddd

CIDR Notation specifies a way to convey IP ranges by adding a “/nn” at the end of this.

So for example when an address is mentioned as 10.0.0.0/24,

This specified an IP address range where start is 10.0.0.0 and end is 10.0.0.255.

The 24 indicates that the range as 2(32–24) IPs. That is 256 IPs.

Similarly 172.1.2.0/28 would mean a range of 16 IPs : 2(32–28). I.e. 172.1.2.0 to 172.1.2.15.

It is best to use a IP calculator when working with IP ranges. I find these couple of calculators handy:

http://jodies.de/ipcalc

http://www.subnet-calculator.com/cidr.php

While creating subnets in a VPC, the IP address ranges of subnets should not overlap.

The first four IP addresses and the last IP address in each subnet CIDR block are reserved for internal use of AWS and not available for us to assign to EC2s.

## Part1: Managing Internet Access

There are two components in VPC that allow you to manage EC2’s access to the internet. Internet Gateway and NAT Gateway.

### Internet Gateway:

As the name suggests, this is the component that enables an ec2 instance in your vpc to access internet. If any of your ec2 requires access to the internet (which it will) then you need to create an internet gateway for your VPC.

In order to access internet your ec2 instance needs to have a Public IP(or Elastic IP) and Internet gateway attached.

IGW is what does the network address translation or mapping of the instance’s Public IP to Private IP. That is when you get a request on the Public IP, IGW routes it to the private IP which is the identity of EC2 instance within the VPC.

We will go into more details about routing traffic in VPC when we go over Routing Tables.

### NAT Gateway:

Your Private Subnets are closed to internet. However an EC2 in the private subnet could require internet access . And that’s where NAT Gateway comes into the picture.

NAT(Network Address Translation) Gateway is used when your EC2 needs to initiate connection to internet, but you don’t want anyone on the internet to be able to initiate a connection to the EC2. Typical scenario is say your Database(or any backend) Servers. They would get incoming connections only from other components within your application/vpc. Users on the internet do not need to connect to them. However you may need to do upgrades for say Linux patches or database version etc. For these you need to be able to connect to the internet and download content.

This is accomplished by placing a NATGW in front of your EC2. The NATGW “is given” a public IP when it is created and that is the IP that will be visible to the internet. NATGW will take care of the address translation to your Private IP and route the responses that are intended for your EC2.

The NAT Gateway itself is placed in the Public subnet and uses your VPC’s Internet Gateway to route the requests to the internet and back.

So your requests go like this: EC2 -> NATGW -> IGW -> internet. More on the routing later.

There are two ways to deploy NATGW, one is NAT Gateway an AWS Service. And the second is a NAT Instance. NAT instance is for cases where you want to handle the scalability of NAT by yourself. In most cases you should be able to do with just NAT Gateway service, and that is what we will focus on in this post.

If the flow of traffic is not entirely clear to you now, don’t worry about it. We will go into in detail in the next sections.

## Part 2: Subnets

Think of a VPC as your private and fenced piece of real estate within the AWS cloud. Subnets are smaller logically fenced areas within that. Subnets allows you to create logical separation of application entities within your org’s VPC. This allows you to manage the access/security effectively and easily. For example every layer of your application can have its own subnet. The layers that require public access are put in Public Subnet and other more restricted components can be put in Private subnets.

**Public Subnets:** has access to and from internet

**Private Subnets:** mostly accessible within the vpc with some exceptions for outgoing internet requests.

***Point to remember #2:*** Subnets cannot span across AZs. Just like VPCs cannot span across regions.

### Route Tables:

The VPC needs to have some “intelligence” to ensure that EC2s can talk to each other in different subnets/AZs/Regions and they can talk to the internet or other AWS services as required. This is handled by a Router. When you create a VPC AWS gives you a router with it. It is implicit and not something that you will see as a component with configuration options.

Router routes requests using the Route Tables.

Route Tables are one of the most important things to understand in Subnets and internal traffic routing. This AWS one liner that defines it best: “A route table contains a set of rules, called routes, that are used to determine where network traffic from your subnet is directed.”

Every time a request is sent from an EC2 it goes to the Router. The Router then looks up in the Route table to find the answer to “where should I send this request?” Route table has a list of mappings that tells for a requested Destination what should be Target to route the request to.

Now lets understand how Route Tables work.

Every VPC has a default route table that is created along with VPC by default. Your can either use this and add routes to it or create your own Custom Route Tables. Every VPC has a Main Route Table. This is the table that is attached by default to every subnet created in that vpc. As you might have guessed the default route table is the Main Route table when vpc is created.

You can see a VPC’s Main route table in console(example below):

![](/images/vpc-2.png)


### Routes:

A route table typically has entries in Target : Destination pair as below:

![](/images/vpc-3.png)



Local Route: This is the route that is present by default in a route table. This defines that all traffic with destination “local”(within vpc) to be sent to that vpc’s cidr block.

Route for Internet-Gateway: The 2nd rule in the table above is route to internet gateway. It defines that all traffic(0.0.0.0/0) to be routed to IGW.

Route for NAT-Gateway: If you add a route as below it says that all traffic be routed to NGW.

![](/images/vpc-4.png)



Some of the other routes can include : route to virtual private gateway(required for connecting from cloud to your remote network via Site-to-Site-VPN), Route to peering connection and few others which are we will look at in another post.

Route Priority: Router always selects the rule most specific destination. For example in the above table, we have an entry for (0.0.0.0/0) which basically specifies rule for all traffic. However there is another rule which has specific IP range(172.31.0.0/16) which is actually a subset of 0.0.0.0/0. So if a request arrive with destination with in this CIDR range then routing is done based on the “local” route. For destinations outside of this range it will route to IGW.

### Custom Route Tables:

It is a good practice to create your own route table and associate it with subnets. Managing traffic with finer control would require you to create multiple route tables anyways.

You can also replace the Main Route table of the VPC with your custom route table. After this every subnet you create will by default have this route table.

**Point to Remember#3 :** It is not a good idea to have igw routes in main route table. This RT gets associated with a subnet by default. And that means every subnet you create by default has internet access.

Implicit & Explicit Association: when a subnet is associated to the main RT of the VPC without you explicitly mapping it, that is implicit association. Alternatively you can explicitly associate a route table to a subnet. The end result of both the associations are the same.

**Point to Remember#4 :** one route table can be associated with many subnets, but one subnet can have only 1 route table.

Public vs Private Subnet: Route Table associations are what makes a subnet public or private.

A subnet when created, by itself is neither public nor private. If you attached a route table that has a route to Internet-Gateway then that makes it a Public Subnet. If you have only local route or route to NAT-Gateway, then that makes it a Private Subnet.

Following figure helps summarize this:

Here I have my two route tables, 1 private(local and NGW routes) and 1 public(local and IGW) routes.

The private route table is my main route table. And my public route table has 2 explicit subnet associations.

![](/images/vpc-5.png)

Below you can see 4 Subnets(2 Public and 2 Private) that I have created in my VPC.

The first two are Private Subnet, by being attached to “my_private_rt”. The other 2 are public by being attached to “my_public_rt”.

Also, as you can see I have same route tables associated with multiple subnets.

![](/images/vpc-6.png)


There are other areas like route-propagation and gateways route tables which we will cover in a later post.

## Part 3: Security Groups and Network ACLs:

AWS provides you two ways to manage the security of your VPC.

Security Groups: a list of inbound and outbound rules that defines which traffic is allowed to enter and exit an EC2 instance in your VPC.

Network Access Control Lists(NACL): Which a list of inbound and outbound rules that defines which traffic is allowed to enter and exit a Subnet in your VPC.

Think of NACL as the outer fence in your VPC’s Subnet and Security Groups as the door into your EC2 instance. Any incoming requests have to get through NACL first before it can get through Security Groups.

When a subnet it is associated with a NACL. This is typically the NACL of the VPC. You can also define your own NACL and associate with VPC or subnet. A subnet can have multiple NACLs associate with it.

Similarly when an EC2 instance is launched it either picks the SG from VPC or you can associate one(or more) SGs to it.

Following is a comparison of the two(ref: AWS Documentation):

![](/images/vpc-7.png)



This covers pretty much the basic building blocks that you would require to get started with a simple application deployment in VPC.

In future post we will look at understanding setup for different components like EC2, Lambda, Elasticache etc. We will also look at more advanced networking like VPC peering, connecting to remote networks etc.
