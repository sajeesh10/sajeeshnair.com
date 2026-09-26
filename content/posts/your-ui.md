---
title: Your UI is not what you think it is
date: 2026-09-07
topic: 0 to 1
---


One thing I learnt building at RunWhen and Druva is the fact that in case of Enterprise products we tend to overestimate the importance of our product's UI. And a mental model shift is required.
We need to think about UI as all interfaces through which the product/platform can be operated. 

#### **Increase your product's user surface area:** 
For  enterprise applications, it is very important that you **don't** try to think of users always starting a journey on your application's UI. Every org already has its own tool stack. Users are used to certain workflows of using those tool chain. Asking them to login to another platform is often a huge friction. 

Hence, we have to think in terms of - how can we make sure we show up in every tool that they use today? 
In case of RunWhen this was making sure we can be used from Collab apps like Slack/Teams, Coding tools like Claude Code/Cursor, ticketing platforms like ServiceNow/Jira. 

This means that all your entry points into your app are through another application. While this seems obvious, it is a fundamental shift in how you think about user journey and how you see your platform fitting into their workflows of the day. 

This also means that you have to focus a lot on your "ui" as it appears on these tools. Example: how does the journey feel on Slack, where does your product show up in ServiceNow, how does Claude Code work with your platform and so on. 

#### Second-order effects:
1. **Invest more in ecosystem UI:** This also means that you probably need to focus very less on your own UI, which may be used very little. 
2. **Being Comfortable with lack of control:** An inevitable factor that I kept running into, is that we are at the mercy of limited affordances provided by the platform we are using as interface. For ex. if you are building on Slack, you have to conform to the constructs that Slack provides. I found building agentic chat flows on MS Teams to be very restrictive and no matter what you did the UX was clunky. This may limit the number of features you could support, and you would have to get creative on how to solve.
3. **Average UX on existing surface >> perfect UX on your UI:** Cont. from #2. What I learn is that, even an average UX on users existing tool chain is much better for them as compared to switching to a product to find a great UX. 
4. **My Product != My UI:** It's possible that a very small percentage of your demo shows anything on your own UI. And it's ok.
5. **Virality**: Your product showing up on other UI, for example a Slack channel is huge lever to quickly get a lot of active users for your product. Leverage this well. 
6. **Jump off Points:** Design the jump off points from the external interface to your product's UI very consciously. This is the single biggest point in user journey where users are likely to "drop-off" from your product.
