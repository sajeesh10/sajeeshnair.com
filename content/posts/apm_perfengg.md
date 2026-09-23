---
title: APM and Performance Engineers
date: 2020-07-07
topic: Performance engineering
---

This is probably just me getting old...

I see a major generation gap when I talk to engineers who have been in the field for under 5-6 years. They describe their primary performance engineering skill set as an APM tool. They mostly haven't even heard of Brendan Gregg or fundamental tracing methods.

The engineers are well versed with Dynatrace, AppD and the likes. But they lack the knowledge of underlying concepts. You take the shiny(and pricey) tool away, and they would not know how to find their way around systems. Let alone identifying performance issues.

I have used these tools extensively myself. I have been a fan of Dynatrace since their early days of UI centric Ajax-Edition. But it seems like these tools can actually make engineers skip a significant learning curve. Especially if the tools are offered to them when they are just getting started. APM tools significantly simplify the monitoring and deep dive for performance issues. To an extent that it actually spoon feeds RCA and recommendations to the performance engineer/developer.

They don’t actually take time to build their concepts around understanding system architecture, application runtimes and OS behavior. I remember when I started my career one of our mentors made us write code on notepad and stressed on not using an IDE.

When it comes to deep diving for performance issues, IMHO there are some very basic concepts that an engineer should absolutely know before they start using a tool.

You should have a good fundamental understanding of following areas and how to monitor them:

**1. OS/System Concepts**

- Threads, Process, Context Switching, Load Averages
- Memory – Physical and Virtual , Swapping and paging
- Disks/Storage – IO performance (SSDs vs HDDs)
- Network – Bandwidth, Latency, Bandwidth-Delay-product, OSI Stack(at least TCP layer).

Any One Operating System would do, I have found Linux to be a good foundation to build this knowledge on.

**2. App/Runtime Concepts**

- Memory Management – Garbage Collection, Memory allocation mechanisms(stack/heap)
- Workers – Threads, Thread States, Race Conditions (and how these relate to process)

Any Application runtime is fine. Java is typically a good starting point because of the abundance of content available on its performance/scalability.

**Special Mention:** Database performance. If you are just getting started you should be able to get by as long as you can point out Slow Queries/Stored Procs.

Each of the bullets above can itself take a lifetime to become an expert. The idea is to be able to understand at least the basics of these as it applies to the world of performance engineering.

The APM tools can abstract a lot of these nuances to provide high level views. At the same time these tools also provide an ocean of data points that you can deep dive into. However if you do not understand the significance of these metrics, it is hard to do anything with that information.

For a good performance engineer an APM tool should be an enabler. It should enable you to get metrics/data that otherwise you would spend longer to dig out. But you would still know how to dig them out. The tool shouldn’t be your strategy.

Note: APM tools provide a lot of other benefits like Production monitoring, CI/CD streamlining for performance etc. I am not contesting the use of APM tools itself. I am offering my view on how people may prematurely adopt them.
