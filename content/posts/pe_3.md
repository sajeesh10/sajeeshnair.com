---
title: Path to Performance Engineering, Part III: Learning Path
date: 2020-08-14
topic: Performance engineering
series: Path to Performance Engineering
---

This is the last part of a 3 part series on creating a performance engineering trajectory for yourself. In [Part -I](/posts/pe_1/) we looked at how to start shifting your approach towards performance engineering. In [Part -II](/posts/pe_2/) we addressed some of the tactical challenges that performance testers face. In this part we will talk about how to build a learning path for yourself.

Irrespective of the opportunities that you are offered through your projects, you should create your own learning path. In this section I provide some guidance on how you can setup some short and long term learning goals.

To be a good performance engineer, you have to be a good well rounded engineer. You can't be just a performance engineer. 

*Take charge of your learning path. Don't just rely on your job/projects to provide the learning curve. One project at a time is too slow a pace to grow.*

## Build Your Vocabulary

When you study the architecture of an application there will be a lot of terms/tech/products that you will not understand. Research them. Get to the WHY a particular tech/product is being used. 

For Example say you see Memcached in the architecture, read about it. What is its purpose in an application design? What problem does it solve? How have some other folks used it? What are the best practices around it? Are there other similar solutions in market? And if possible try to find out how this product performs and scales. You complete the whole learning cycle. Now, you understand how caching solutions work, what are the types of solutions available and how applications typically implement/leverage them. Next time you see another architecture and see Redis, you already know what it does.

Now come back to your application architecture, look at it with this knowledge you have acquired. You will understand things a bit more than you did last time. Move on to the next term you don't understand. Repeat!

Once you have done this for few different applications, you have automatically increased your tech vocabulary. And this is what helps you mature as an engineer(not just performance engineer). 

I have found this to be the single most effective way to learn. You have to have the passion to learn technology. Because it can get difficult when you have 15 complex load runner scripts to complete on deadline :)

**If  there is one thing that you take away from this write up. It is this!**

## Develop A Performance POV

As you read about new tech, make sure you also do it through the lens of performance. You should find out the performance/scalability characteristics of the product. Few pointers to doing this - Understand how its runtime works, check for datasheet or any published scalability numbers, see if people have reported performance bugs on git or product forums, are there limits to how much it can scale, are there conditions in which it doesn't work well(ex. high latency) etc. This is a long list and one that you will hopefully develop an intuition for over the period of time.

## **Build your own playground**

Setup an environment for yourself where you can do your experiments. This is your way to not slow down due to "lack of access". 

How do you do this?

1.  Invest in a Cloud Account (say AWS?). Its worth it. 
2. Setup/Deploy an application. Chose tech stack of your liking. There are plenty of sample applications you can download and install/setup. Start looking on git. You don't have to write your own application.(Also, See #3)
3. Write your own application: Building your own project is a great way to learn. It could even be a single page with a simple backend. You will learn various cloud constructs(EC2, S3, containers etc.), coding, some database etc. You will also learn how to design an application and get tiers talking to each other. This is a great way to learn. Because now when you read topics you will do so with purpose. Instead of just getting stuck in a training loop.
4. Performance Engineer it: now you have your own environment in your own private cloud. So go crazy on it. Do all the fancy performance engineering on it. Make it go faster, make it go slower, scale it up, tune it. No more excuses!

## Learn Basic Statistics

Workload modeling and Analysis of metrics are couple of areas where I have found basic understand of statistics very useful. It is also important to build the intuition for percentile values, mean, median, standard deviations etc. Understanding basic concepts like variance,co-variance, correlation matrix helps a lot in large scale analysis. Beyond this you should also understand basics of curve fitting, linear regression,log/exponential curves and some elementary probability distribution. The first step is to gain the theoretical understanding of these concepts. The second step is to develop an intuition for applying these to performance related analysis/modeling. 

Personally I have found knowledge of these concepts along with a supporting tool/language like R and Python(pandas/numpy) to be very helpful. 

## Learn One Language

Any language is okay. If you are in the software industry you should know at least one programming/scripting language. Its even more important for a performance engineer. You can "get by" as a performance engineer even without knowing to code. But knowing to code gives you some key advantages:

- You can do a lot of handy things like setting up or parsing custom logs, writing small utilities, automating small repetitive tasks for your day to day activities etc. These are seemingly trivial things for which otherwise you will get held up by a developer. This slows you down. And you don't need to be an ace programmer. Learn enough to be able to handle your day to day stuff. It is a good place to start.

    Note: Unfortunately in consulting companies every small script is glorified as an accelerator and highlighted to customers. Don't fall into this trap. 

- This helps you understand the time and space complexity of code. When you write a piece of code be mindful of the space and time it takes. You don't even necessarily need to understand the BigO notation etc. Just develop the intuition for it. This gives you a peek into typical performance-mistakes that developers make.

Eventually you will realize that everything in Performance Engineering is a Space-Time problem.

## Build Your Support System

This is not an advice specific to Performance Engineering. 

It is very important to have a mentor(or mentors) who you can turn to for advise time to time. If the mentor happens to be your supervisor it works out great. But don't rely on finding a mentor in your manager. It may never happen. Instead when you find people who seem to have sound advise and temperament for mentoring befriend them. It doesn't even have to be a senior, it can be even your developer/performance engineer/architect friend. The person doesn't have to be even from the same organization. 

I also make sure to keep around lot of like minded friends/colleagues. We talk from time to time to brainstorm on technical problems or just to see what new interesting stuff everyone is working on. It keeps every one on toes and helps you learn faster. And everyone gets a sounding board.

I have found my growth to be the fastest when I had very good mentors. I have found the growth to be even faster when I had great colleagues to help me. 

It is not possible for any single person to learn and expertise in every single tech on earth. Hence it is very important to have mentors and friends you can lean on from time to time. This forms your Support System. 

Go back to [Intro](/posts/pe_0/)
