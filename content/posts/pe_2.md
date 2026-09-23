---
title: Path to Performance Engineering, Part II: Tactical Challenges
date: 2020-08-13
topic: Performance engineering
series: Path to Performance Engineering
---

This is the second part of a 3 part series on creating a performance engineering trajectory for yourself. In [Part -I](/posts/pe_1/) we looked at how to start shifting your approach towards performance engineering. 

We all want to go down the path we talked about in Part 1. But there are several day-to-day challenges in actually being able to do so. And this can turn out to be a major impedance in your learning trajectory. 

So lets address some of the tactical challenges that you may be facing in the field.

## **Problem #1: Lack Of Information Sharing**

Every project poses certain challenges in terms of acquiring necessary information from the incumbent people. The reasons for lack of information sharing can range from customer-vendor barrier, onsite-offshore barrier, lack of documentation, lack of bandwidth and so on. A second major reason is also the fact that many a times performance testers don't ask the right questions. Whatever the reason may be you end up testing an application that you don't understand.

**Solution - Go White Box!**

At the very beginning, set the tone for a white box performance testing, not black box. Make application understanding a prerequisite for starting performance testing. Make sure everyone (including your client and seniors) understand that testing without understanding the application is a sin. It is the absolute wrong way of doing it. Your clients will love you for this later. (Your senior may hate you). 

Following are areas you can target for asking questions to gather as much information as possible:

**Agreement to Monitor:** When I run a test I need to measure the health of transactions and systems. If I don't measure adequately how do I know if performance is good or bad(performance is not just response times). If response times turn out bad, without monitoring there is no next step for troubleshooting. We will end up repeating tests with monitoring anyways.

**Agreement on System Understanding:** In order to monitor, I need to identify the metrics. In order to know metrics I need to know the components in the application. In order to breakdown and trace a slow transaction I need to understand the call flow. And so on..

**Agreement on Metrics:** once you have the above agreements, list down exhaustive metrics that you want to monitor for each component, each layer etc. Just make sure you keep reasonable sampling frequency. Keep in mind that you may not even actually analyze all the metrics. But you can't know where your investigation will go before you run the test.

This discussion becomes very easy, when you are already actively trying to troubleshoot a performance issue. 

**Agreement on Instrumentation:** Once you have an agreement on what metrics to capture, you can start discussing how to capture them. Metrics and how to capture them is where true engineering skills will be tested. The tooling can range from APM to custom logging with parsing scripts. Or building your own timeseries+dashboard setup like TICK/TIG stack etc. But its very important to know your metrics.

There will be skepticism(and rightly so) - "Oh these many captures are going to create overhead on the servers!" Well, they might. So to know what is the impact do a dry run with all the monitoring on.

**Agreement on Analysis:** be careful how much you commit in terms of actual analysis. Some metrics understanding can be subjective(app specific). Make sure to enlist developer support in your plan for these areas. As a rule of thumb, it is a good idea to loop in infra folks for OS/Hardware/capacity related analysis and Developers for runtime/code related analysis. Because they are the experts in those areas. As your knowledge of application grows, your dependency on them will naturally reduce.

**How Do I Analyze?**

If you have reached this point in your engagement, then you are not hindered by lack of info or lack of access. Now you are purely limited by your knowledge of analyzing metrics of a software system.  This is THE SPOT you want to be in.This is where your analytical skills meet your technical knowledge of the system(remember? runtimes, OS, network etc.). The analytics skills will help you see trends, patterns and correlations. Your technical knowledge will help you understand the cause-and-effect relationship. 

This is another area were some basic understanding of statistics can boost your analytical skills.More about this in [Part -III](https://www.notion.so/Part-III-Learning-Path-9368fa4d13c94bb9afddd2271405c183)

**How Do I Tune/Recommend?**

This will come with time. It also depends a lot on problem solving abilities. In fact in my experience the best tuning recommendations have come as a result of a person's problem solving ability. So if you are just getting started, don't worry about this for now. And in most places problem identification is a bigger challenge that problem solving.

## **Problem #2 : Lack of Access**

Follow same steps as Problem #1. 

At Instrumentation step, you will probably be denied access. You can have two(maybe three) types of access:

- First Hand: you have all the access you need to setup the monitoring, capture and report. Great!
- Second Hand: someone(admins/devs) else will setup monitoring, but you will have access to the captured data.(either dashboards or exports etc.). You will have to tell them what metrics to monitor where, and sometimes even how(so yes, you need the technical knowledge). A lot of time you will get raw logs which you will have to parse to get metrics and create plots. So some scripting and dash-boarding skills will come handy. This is the most common scenario in a lot of the projects that I worked as consultant.
- Third Hand: a possible third way is where you can sit with some who has First hand access and do the whole exercise. I have had to do this a couple of times. And its a nightmare approach.

If you are just getting started, or you are new to a particular tech, Second approach may be a good way to go.

## **Problem #3: No Scope for PE**

For all the talk about PT vs PE, its actually not possible to draw a line. Where does PT stop and PE start? Use this to your advantage when you talk to stakeholders. 

If you are performing the steps in the above sections, then you are already doing a lot of engineering. And if you have got some good findings from the tests and monitoring, customers won't stop you from going deeper.

## Special Mentions

**Profiling**

There are things like Profiling which I agree can be difficult due to all the above 3 problems. However in my entire experience the number(or rather impact) of performance issues identified by doing the things I listed and far more than the number issues I identified with pure profiling. And I can say this for lot of other folks that I have worked with too. Also, in lot of cases profiling needs access to Build and the deployed server. Only in some cases it requires access to code(uncompiled). 

If you have done all the above things and you know that the only way to dig further into the performance issue is to profile, then the project also would probably have no option but to find a way to provide access. And hopefully by now you have racked up some goodwill with the customer :)

Note: This changes drastically when you are in product company. Here profiling becomes a go to approach. But also there are no access restrictions.

**Code Access**

You can be a star performance engineer without looking at code. That's right. There is a major misconception that you need to be able to read code to find performance issues. Unless you or your team has written the code I think this is the wrong way to do it. Typical stuff that you want to find in code are time and space complexity, faulty/redundant logic, race conditions etc. It is much better to do dynamic analysis of code to do this. i.e. even if you must analyze the code, do so by running it yourself in a controlled environment. I have heard a lot of people brag about how they identified performance issue by reading the code. It is very likely that they wasted a lot of time doing this(unless they wrote the code). I recommend finding a smarter way to do it!  

**An Alternate Perspective**

No matter how we put it, these are all things that you can do to convince the stakeholders to allow your team to do some level of deeper engineering. It could sometimes feel like a lot of energy spent just to get a seat at the table.

IMHO, the best way to skip all the tactical challenges mentioned above is to just move to Product industry. You will save a lot of the energy trying to find your way around these restrictions. 

In [Part -III](/posts/pe_3/) we will take a look at the learning path that you can create for yourself, irrespective of what projects you work on.

Go back to [Intro](/posts/pe_0/)
