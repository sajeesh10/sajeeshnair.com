---
title: First Principles Thinking
date: 2020-09-11
topic: Performance engineering
---

I started noticing this phrase a lot in the last few months. It sounded like this cool concept that I was very late in learning. I don’t know if it was already widely used in conversations or there has been an uptick in the last few months. I could mostly glean from the context of conversations what it meant. But I wanted to understand “first principles thinking” from first principles.



So what is First Principles Thinking anyway?



Here is the Wikipedia definition:

>“A first principle is a basic proposition or assumption that cannot be deduced from any other proposition or assumption.”

That's pretty much it. Assume nothing.



It is basically a mental model for thinking. And apparently Aristotle and Elon Musk seem to be the poster boy for this approach of looking at problem solving.



As it turns out, I have been using this mental model for quite sometime now. Until few years back working as a consultant, I was part of a team that specialized in firefighting production performance issues for various customers. The problem statements ranged from application performance to scalability to availability.

   


### First Principles Thinking & Performance Problems:



Here is how first principles thinking helps crack complex performance/scalability issues:



All these are observations from my first hand experience. YMMV.



**Ignore all analysis.**  Every time I arrived at the scene there were some analysis and theories provided by the teams around possible causes. Consuming this analysis by definition is opposite of First Principles thinking. Because it has perspectives and can be highly subjective to the person analyzing. Focus only on data and not its interpretation. And if those were good analysis, then it would be great a validation when you arrive at them independently. 



**Know the Symptoms.**  It is important to gather as many symptoms of the problem as you can. Symptoms should be derived as much as possible from raw indisputable facts(metrics, metrics, metrics).

For example:

* Good Source for Symptoms: page response times, transaction drop stats, error logs, user error screens, infra metrics etc.

* Bad Symptoms: “users said app is slow”, “application got slower after the patch”

It is very important to differentiate user perception from user experience. Perception by definition is highly subjective and not quantifiable. User Experience can be measured.

Having said that, you can neither quantify nor dispute an “Application has crashed” :)



If you have gathered symptoms well, it gives you a head start into the next step – Defining the problem statement.



**Define Problem Statement.**  This is a much cliched one. But before starting an RCA, define the problem statement. Defining a good problem statement is half the battle won. Good problem statements (pertaining to performance and scalability) usually contain quantification – no subjectivity, no ambiguity. A good problem statement itself describes what is the success criteria for your troubleshooting exercise.



For example:
* Bad Problem statements:
    - “Application is slow under load”
    - “Observed high CPU Usage”


* Good Problem statements:
    - “Add To Cart degraded from 3 seconds to 10 seconds” 
    - “All pages degrade by 40% as the TPS increases beyond 5K (list pages and response times)”



**Focus on Hard/Raw Metrics.**  Once you have defined the problem statement, use raw(indisputable) metrics to draw up your analysis and conclusions. Strip out any analysis that doesn’t have supporting quantifiable metrics.



**Don’t assume correlation as causality.**  It is very common to look at patterns of different metrics and mistake matching trends as spotting a cause. For all we know all these metrics indicate effect of an underlying cause.



**Know when the problem is solved.** Lastly, once the issue has been RCA’d and fixed, it is important to quantify and say that it has been fixed. You should have the required metrics/monitoring in place to say that the issue has actually been resolved. A lot of times the outcome of a fix is left to be subjective. This leads to difficulty in getting a consensus on success of the exercise.If you have set the problem statement well, odds are that this is already taken care of.



I hope write more as I apply the first principles thinking more.
