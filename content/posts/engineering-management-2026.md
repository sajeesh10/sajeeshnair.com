---
title: Engineering Management in 2026
date: 2026-10-06
topic: Leadership, 0 to 1
---

A common theme that I keep hearing from Engineering Managers, Directors, VPs is : **Managing a team of 8, is now more like managing a team of 30 pre-AI.** 


At RunWhen, there was a point in time when we were 8 engineers, all of them had adopted AI coding well and were churning out e2e features. We were still figuring out code reviews fully, but had decent level of review skills which enabled the senior engineers to manage reviews through claude code.

The team looked very well to build features rapidly. However, a new bottleneck emerged. **ME**. 

The sheer number of product and engg. decisions that I had to make on a day to day basis had gone up a lot. Team was often waiting on me. 

From my perspective, I found myself having to go deep into several product and design areas every day to ensure that I have full context and then to make the decision. Every deep dive was cognitively  heavy. And multiple threads a day meant context switching several times a day on major decisions. This also meant that I had very less time to internalise the ideas and letting them simmer for a bit before making a decision. I was dropping packets all over the place.

This was also the time when people started showing up with "cool" features and prototypes based on their conversations with customers. 
That is when the reality of "building is cheap" really hit me. 

Here are few things that I learned the hard way: 
1. **Document driven decisions**: we were already very documentation heavy, and hence any product or design discussion happened on a document that an owner would create. This helped a lot because this now meant that I could read the docs and comment, others (in diff. time-zones) can see the doc and what others commented and can add thoughts. This helped in few different ways: 
    1.  reduced a lot of  open ended "brainstorming" style discussions with different people. 
    2. we now have an artifact that could be fed to agent for context
    3. Rationale for decisions was recorded, it mostly showed up in the form of comment-exchanges between team members. 
2. **Rethink Sprint**:  We soon realised that Quarterly Plans held very less practical value. So we set some directional guidance and started doing a monthly business plan at the start of every month.  This was coupled with small pod-level-sprints ranging from 1-5 days. Pods were simply aligned by deliverable projects. Most pods were 2 people, some 1, some 3. Never more than 3. 
3. **Default to NO on unplanned PRs:** Engineers would often let Claude code rip over the weekend and turn up with "cool" features on Monday morning. And I suddenly found myself reviewing and gating these features. It also meant senior enggs now had to code review it. All usually unplanned. Turning up with PRs is now a very low bar. Expect them to be thrown away.  
4. **Build UX/UI Guidelines:** For [all interfaces that face user](/posts/your-ui/), have clear templated UX rules, embedded as claude skills. This is something that we got to very late. We didn't want to have full time frontend-dev and hence a lot of my time went in UI nit-pick reviews. All it took was 2 weeks of dev and the product started to show serious signs of *Frankenstein-ish* UI. 
5. **Give yourself a break**: Last but not the least. It took me some time to realise and even longer to internalise, that I was not the bottleneck. I was the last gate of judgement stopping AI Slop from reaching customers. It was okay to be slow and diligent on this. 

As I talk to more leaders, I am eagerly looking to learn from their experiences. No System is perfect and needs evolving. These are just a few things I tried that worked to some extent, and I keep tinkering.
