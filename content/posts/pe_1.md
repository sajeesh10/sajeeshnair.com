---
title: Path to Performance Engineering, Part I: Approach Shift
date: 2016-08-12
topic: Performance engineering
series: Path to Performance Engineering
archive: yes
---

This is the first part of a 3 part series on creating a performance engineering trajectory for yourself.

It is important to find inroads within your projects to develop skills. It is never prudent to wait for that right project to make your move to performance engineering. In this part I talk about how you can start shifting your approach from a black box performance testing to performance engineering. And along the way pick up skills through the projects that you are working on. I also try to throw some light on how to mold your mindset for performance engineering.

### **Mindset Change**

Performance Testing vs Engineering can be looked at from several lenses but fundamentally it is a mindset change. The skill set will follow intuitively once you have the mindset. You have to start approaching every application with the intent of improving its performance. (Yes, Even when it may not really need improvement). Think - Engineering is building, Testing is validation*. 

### **Know the application**

The main problem that I see is that we test applications without really knowing it. We take a very black box approach.  Simulate critical transactions w. load, measure response times and report them. At times may be we go one step ahead measure the CPU and Memory. 

When you start a project, start by exploring the application as deeply as you can. (And not by trying to find what Load Runner Protocol to use). Your application design has to be an integral part of your NFRs and Test Design. If you know the application well, you will know how to simulate the load even without Load Runner. Aim to understand the performance characteristics of the application, not just to measure it.

### **How do I get to know the application?**

I tend to look at the application from two dimensions : 1. How is the application used, 2. How does the application work/ behave. 

*I assume you already have a decent understanding of the application functionality. If not start with that. Know what problem does the application solve for its users. This is the base for both the dimensions.*

**I. How is the application used:** 

A great way to develop perspective on user expectation is by understanding the customer JTBD (Job To Be Done). This is helpful in understanding what type of response times(performance) will delight the customer and what may be just about acceptable. 

This also helps  build thought process around managing(manipulating) user perception in the solution. But user perception is content for a later post.

**Workload Modeling:** 

This is a term that is abused a lot(IMHO). For effective Load/Scale testing you need to mimic a scenario that will happen in production. This scenario is what we typically refer to as peak period. Workload Modeling means to understand these peak scenarios and build a simulation for them. Get as detailed in this as possible. The accuracy of your modeling determines the value of your test. Poorly modeled tests can result in either false confidence in application or  chasing pseudo bottlenecks. Both can be dangerous.

Typically I try to cover the below areas(but not limited to it):

1. Identifying peak scenarios: there can be different type of peaks depending on the application usage. Different type of transactions can dominate different peaks. These transactions in turn could be heavier on different application components and even hardware resources. For example your application may have a peak load period which is Compute heavy and another that is IO heavy. It is important to have some idea of the relative footprint transactions have on the application. 

    ***This is why I highly recommend doing workload analysis after you have gained some application knowledge. (which is the step2)***

2. Transactions and their mix: Once we know what slices of time to simulate(from #1), we try to cover as much detail as possible in simulating it. This means know what users actually do in a session. For ex. most websites have a funnel type traffic pattern, where your landing pages get higher hits and subsequent navigation sees users drop off. So knowing usage pattern is key. Same principle can be applied to job based workloads. 
3. Transaction data: mimicking the data that is used in a user transaction/session.  This means to have the same data as user would have in his or her profile for each page/transaction. For example: if you are simulating a payment flow you would probably add a dummy credit card to user's profile and perform multiple credit card transactions for generating load. However the page can slow down if the customer has 4-5 credit cards added to their profile. This effect can compound when all 1000s of your users have 3-4 credit cards in their profile. Being diligent and paying attention to every small detail is key to getting workload model right.
4. Data Volume: along with transaction data(data that is touched by a simulated user transaction) , it is also important to have right volume of data residing in your data stores. Hence populating data to represent prod like volume is important step is getting predictable DB performance. This can get a bit tricky when you don't have a production size environment available. However with some experience you will get hang of how to scale the DB and data for effective testing.

Workload load modeling is a complex topic and there are different approaches for greenfield and brownfield applications. I will keep it brief here and as this topic needs a dedicated essay. 

Note: Some basic understanding of statistics goes a long a way in effectively modeling your workloads. More about this in [Part -III](/posts/pe_3/)

**II. How does the application work:**

**Architecture:**

Step out of the performance role for a bit. Start with high level architecture. Chances are you will not understand a lot of the tech used. That's OK. Even the top architects don't know all the tech in the world. Note down every term in the architecture you don't understand. Spend time reading about them. More about this in [Part -III](/posts/pe_3/)

**Call Flows:**

Once you have a fair idea of what every component in your architecture does, start tying together these components with the application transactions. When a user does a particular step(or transaction) how does it use each of these components. Every transaction may not use every component. Start by understanding these call flows. I usually try to get the sequence diagrams. It gives a pretty wholesome picture with right level of details most of the times. Once you know this it is also easier to start deep diving when you find a transaction to be slow.

**Application Runtime:**

Understand the runtime(s) that your application uses. For ex. Java has JVM, Go has Go Runtime, Kafka and ES are build on java so they have JVMs as runtime.  Every language has its own runtime. Here are few axes along which you can start exploring: 

1. Is the language interpreted or compiled? How does this affect performance?
2. Does the runtime manage memory? A managed runtime takes care of memory and scheduling for you. For ex. Java manages memory allocation and thread/process allocations for you. If you write in C++ or Rust you have to do this by yourself. Managed code comes with its own set of (management) overheads. It also gives developers less granular control over memory and CPU utilization.
3. Runtime Memory Management: How is memory allocation managed? How does the runtime use Stack and Heap. How does GC work in this language? How does the runtime's memory cost translate to Operating System memory.
4. Runtime Task Management/Scheduling: what constructs do this language use, for ex Java has threads, python has threads as well as greenlets, Go has goroutines and so on. Understand how the scheduling of these entities work, i.e. how do they actually get to execute on a CPU. how are they context switched in/out etc.
5. Application Configuration: You will also come across a lot of enterprise solutions, like SAP or Oracle Coherence etc. These products have their own predefined custom configuration options that you will have to learn about if you are working on them. These are levers provided to be able to tune the performance of these applications. 

    The above approach typically holds good for everything except databases. Databases have their own constructs and concepts. I will cover them separately. 

    Quick Note on DB performance: In my experience a lot of the tuning can be handled by decent DB developers and config changes can be handled by Admins. As long as you can point out slow queries and look for low hanging items like lack of index(full scans) or hardware bottlenecks, there are mostly people from database teams who can fix these. A basic understanding of AWR(for oracle) and query plan will take you a long way. This is also one of the reasons I have never gained much expertise in complex performance tuning of relational databases. I have often limited myself to problem identification. I am trying to change this with nosql DBs :)    

**Operating System:**

Irrespective to what transpires in the above layers, everything runs on the Operating System. OS intermediates the hardware resources for the applications above. So it is important to understand some key concepts:

1. How does the OS manage/allocate memory - learn about physical memory, swap space etc. 
2. How does OS run processes on CPU? Learn about context switches, load averages etc.
3. How do File System and Disk Operations happen?
4. How do Network Operations happen?
5. Learn about the Speed to Cost trade off in [Memory Hierarchy](https://en.wikipedia.org/wiki/Memory_hierarchy) -  CPU Registers > CPU Cache > Physical Memory > Flash drives > Disk(spindles) > Tape

*It doesn't matter what application or database you are working on, remember every software has these abstract layers : Code(or libraries) > Run-time > Operating System > Hardware.*

The last two are usually very tightly knit. 

Armed with the above knowledge, now approach the performance & scalability of your application.

**Lets Tie it all up :** 

When a single user does a Transaction: 

- What is the response time/throughput?
- What components does it hit?
- How many threads does the component(say jvm) has to execute for this transaction?
- How much CPU does it consume?
- How much memory does it consume?
- Where does it spend time at - CPU, Disk IO, Network IO?

When many(1+) users do the same transaction:

- How much does it slow down as compared to above?
- Why does it slow down with load? Does it lack a hardware resource? If yes which one?
- Is it slow but none of the hardware resources are saturated?
- Is the component waiting on a response from downstream? Is the downstream slow to respond?
- Ask same questions on downstream.

These are just some of the questions you can start asking. But I think by now you get the point. Don't restrict yourself to load simulation(script, execute, report). 

You will find very less to learn in the black box space after a few years and projects will stop being exciting. Or you will move into management roles. If you aim to grow into a tech-inclined career path, then focus on learning technology.

*One could argue that testing is also technically part of engineering since its feed into the development cycle. In that pure sense performance engineering lies somewhere between traditional development and testing.

Go back to [Intro](/posts/pe_0/)
