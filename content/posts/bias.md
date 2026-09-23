---
title: Cognitive Biases in Performance Engineering
date: 2021-06-14
topic: Performance engineering
---

I started reading about behavioural psychology a few months back. And I couldn't help thinking about all the cognitive traps that a performance engineer faces every day. In this essay I try to expand my own understanding of cognitive biases and how they are relevant to the field of performance engineering. As I learn more about this topic it is very likely that I may update some of the views expressed in this writeup.

As a performance engineer it should be our objective to be aware of these traps and train our brain to avoid them.

Before we go into the cognitive biases let us understand some of the constructs involved.

### Dual-Systems Theory

Coined by [Daniel Kanheman](https://en.wikipedia.org/wiki/Daniel_Kahneman), this states that our brains consist of two parts - System 1 and System 2. These are not physical parts of the brain. They are more of functional(or logical) separation

- **System 1** is quick, automatic and operates with almost no sense of voluntary control. It is often emotional, stereotypical and takes very less effort.
- **System 2** is the more methodical, analytical and slow part of the brain. System 2 comes into play when you are trying to do effortful mental activities or complex decision making.

One of the key characteristics of system 1 is that it cannot be turned off. System 1 feeds information to System 2. And it's System 2's job to keep a check on System 1.

For example: self control is a function of System 2. which means when you see that chocolate, the jumpy system 1 tells you to eat it. Not eating that chocolate requires system 2 to do its job. This exerts a certain amount of cognitive load. System 2 is lazy by nature. Thus it's difficult to fight those cravings when you are already stressed.

**What does all this have to do with Performance Engineering?**

As a performance engineer our job is to run load experiments and draw conclusions about performance characteristics of applications. This includes finding areas of slowness and identifying its cause(s). It is extremely important to stay objective while dealing with several metrics and making inferences.

**Using data points and models can often give you the false sense of being objective.**

This means that you have to keep your System 2 sharp and on the lookout for these biases.

Here I try to cover some common cognitive traps to watch out for.

### **Narrative Fallacy**

Humans by nature like things that fit together coherently in their brain. Driven by the laziness of System2, we like being able to explain things in simple ways. And we like it when facts are connected by some relationship. It requires less cognitive load to store a bunch of facts tied together by some story, as compared to a lot of disconnected data points.

**Why is this a problem?**

This bias makes us susceptible to over-simplify things and sometimes even overlook certain facts.

Nassim Taleb's Quote on Narrative Fallacy(paraphrased):

> We like stories, we like to summarize, and we like to simplify, i.e., to re­duce the dimension of matters. Narrative fallacy is associated with our vulnerability to overinterpretation and our predilection for compact stories over raw truths.
> 

As a performance engineer this can lead to incorrect analysis.

When we see metrics (usually there are a lot of them when we run performance tests), there is an innate tendency to tie together the behaviour of all the metrics into a story. It is easier for us to comprehend the movement of metrics if we can assign some relationships to different metrics and their behaviour. In case of performance analysis this relationship is usually that of causation. An early assignment of causation to some trends can lead you to provide incorrect conclusions and chase wrong problems.

### **False Confidence**

This bias is very important to consider when you are relying on other people to provide inputs. Consider a scenario where for a performance issue multiple potential explanations are provided. It could be one person providing multiple perspectives or multiple people providing their own point of views. You are very likely to agree with an explanation that "sounds" the most confident. This can lead you to choose the incorrect option. Because "confidence" has very less to do with the underlying data points. It has more to do with what the person thinks about them.

Daniel Kanheman's quote on this:

> Confidence is a feeling, which reflects the coherence of the information and the cognitive ease of processing it. It is wise to take admissions of uncertainty seriously, but declarations of high confidence mainly tell you that an individual has constructed a coherent story in his mind, not necessarily that the story is true.
> 

This is one of the biases that I avoid consciously every day. It is important to ignore the confidence (at least for some time) and look at the raw data points and then draw conclusions. It is especially important when information comes to you from "prevalent wisdom" about the application's behaviour or when you have to make decisions based on your team member's analysis. This also helps a lot while interviewing candidates.

### **WYSIATI - "What you see is all there is"**

This is one of the key biases stated by Kanheman in his book [Thinking Fast and Slow](https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow). Our brain tries to quickly jump to conclusions based on whatever limited data is available. It doesn't always try to stop and think that there could be more information that could potentially change the conclusions. While this would have been a strength during the old hunter-gatherer times, it is a weakness when it comes to performance engineering and any analysis in general.

This, as you can guess, has a huge impact in a performance engineer's analysis. It is very common to see engineers look at only 3-4 metrics like throughput, cpu, memory and start forming their analysis. Since these metrics are commonly and thus easily monitored we are tempted to make conclusions just based on these. However, we should "think slow" and consider that there could be several other factors and metrics that could give a completely different analysis.

### **Causation vs correlation**

This is the most common bias and sort of a consequence of WYSIATI bias mentioned above. We naturally gravitate towards seeing a relationship between two or more metrics that move together. And since performance engineering is all about trying to figure out cause-and-effect, we are very quick to assign causality. I have written more on this in a previous [essay](/posts/firstprinciple/).

Nassim Taleb has written extensively about this in [Fooled by Randomness](https://www.goodreads.com/book/show/38315.Fooled_by_Randomness).

### **Bias to Solve by Addition:**

Humans have an inclination to solve problems by adding things rather than by removing. [This](https://www.nature.com/articles/d41586-021-00592-0) very interesting study published in [Nature.com](http://nature.com/) says that people systematically overlook subtractive changes.

We see this very often when it comes to solving performance issues. For example:

- The default tendency is to add architectural components to solve current application issues. And not to think if some components can be removed. This requires higher cognitive effort.
- Our first ideas to solve performance issues are usually to add cpu, add memory etc. And not to fix or optimise the code that consumes high cpu or memory. Good architects focus on cpu and memory unit economy of the application and their code.

As a performance engineer a good rule of thumb is - "**best code is the one that is not written"**.

A good engineer starts understanding an application architecture by understanding the purpose of each component in it. I wrote about this in another [essay](/posts/pe_1/) in a bit more detail.

### **Effects of Priming**

Priming is a phenomenon whereby exposure to a stimulus influences a response to a subsequent stimulus, without conscious guidance or intention. ([Wikipedia Definition](https://en.wikipedia.org/wiki/Priming_(psychology)))

What this means is that our brain becomes programmed(lightly) to recognise certain things when there has been a past stimuli that has "primed" us. Knowingly or unknowingly.

Here is what Daniel Kanheman has to say about priming:

> your thoughts and behavior may be influenced by stimuli to which you pay no attention at all, and even by stimuli of which you are completely unaware
> 

An example(from Thinking Fast and Slow):

If you came across the word EAT, and then after sometime in an unrelated context if you were asked to complete the word SO_P. It is very likely that you will say SOUP. Whereas if you had seen the word SHOWER it is likely that you would say SOAP.

A typical scenario for a performance engineer: when we talk to developers or architects they usually have some theories on where the performance issues would be, even before we have run our experiments. Usually people point to a component that is developed by another team. This may knowingly or unknowingly incline you to focus more on those suggested components when you run the test. Thus causing your performance experiments to be biased. The probability of you missing an issue in other components now is slightly higher. Hence, it is important to be vigilant against priming effects.

### **Halo effect**

Once again drawing from Think Fast and Slow:

> The tendency to like (or dislike) everything about a person—including things you have not observed—is known as the halo effect.
> 

I find it very important to separate "what" is being said from "who" is saying it. Focus on the content and not the personality. This is harder said than done.

As a performance engineer we often get directions from senior and incumbent folks in the organisation. Some of them we like, and some others we don't. We are likely to agree(or disagree) on a direction to take on certain performance issues because of who is saying it. It is important to not let the Halo effect get in the way of how you tackle performance issues.

Note: this is a generic point. and it applies to all aspects of life in general. Performance engineering is just another one of them.

### **Availability Bias**

The availability heuristic, also known as availability bias, is a mental shortcut that relies on immediate examples that come to a given person's mind when evaluating a specific topic, concept, method or decision. The availability heuristic operates on the notion that if something can be recalled, it must be important, or at least more important than alternative solutions which are not as readily recalled. ([wikipedia definition](https://en.wikipedia.org/wiki/Availability_heuristic))

Note that this is a system 1 behavior, which reacts quickly on easily retrievable information. We must exercise our System 2 to counter this bias and make correct decisions.

I have seen this play out at various occasions as a performance engineer. The most notable is workload modeling. When we are gathering requirements for designing our workload we talk to various stakeholders - Business or PMs, Architects, people in the field etc. It is very likely that their inputs will be skewed towards a recent performance issue that happened for a customer(or customers). And often this customer or scenario may be used as a representative workload for our tests. This is highly incorrect. Because that scenario may represent the best or the worst case or somewhere in between. But without looking at all possible scenarios we cannot know where it sits in the spectrum. Hence, we should look at the possible scenarios based on hard metrics and not just go by anecdotal data points which are prone to availability bias.

There are two specific instances where I find it important to be vigilant about this bias:

1. Business/PMs pointing to a recent or major production incident as a scenario to model. Since it was either recent or major, it is easily recalled and hence considered important.
2. Developers/Architects point to a functionality that they spent most time on or was most challenging for them to build. Since these factors make it easy for them to recall a functionality they are "biased" to think that it is the most critical from a performance standpoint. Which may not be the case.

### **Anchoring Bias**

Anchoring Bias is when the first piece of information that you get influences your thought process and hence decision. A good example of this is when you try to negotiate the price of something you are looking to buy. The seller will usually quote a very high value, which then becomes your anchor for further discussion.

Here is how Daniel Kanheman suggests to deal with it:

> You are always aware of the anchor and even pay attention to it, but you do not know how it guides and constrains your thinking, because you cannot imagine how you would have thought if the anchor had been different (or absent). However, you should assume that any number that is on the table has had an anchoring effect on you, and if the stakes are high you should mobilize yourself (your System 2) to combat the effect.
> 

In performance engineering I have seen this when we rely on past or any available benchmarks. Those data points become our anchor. We don't necessarily consider that those values may not be relevant (due to being too old, or scenarios having changed a lot) and it may not provide us an apples-to-apples comparison in the current situation. A lot of times there is a need to change the baselines(anchor values) itself, and this bias impedes that. We tend to anchor and sometimes over-anchor on past benchmarks.

### **The role of intuition**

I will conclude this essay by talking about Intuition.

Intuition can be a powerful tool if used well. But it can also be prone to all the biases mentioned(and more).

In the context of Performance engineering:

Intuition comes from your existing knowledge and what you have seen in your past experiences of analysis.

The act of attributing causation without much deliberation ( i.e. building a story that ties together metrics in a cause-n-effect relationship) is usually a system 1 behavior.

The problem with this is that once you have a story(or a conclusion), the rest of the analysis will be just trying to find data points that agree with that story.

You also become prone to **confirmation bias**. You will focus more on metrics/trends that support your story and are likely to ignore patterns that conflict your story.

**So, then, intuition is useless??**

No.

This doesn't mean that intuition is useless. Intuitions are important. Lot of performance issues get solved based on "hunches". And the more experienced you become, the more hunches you have.

However, you can be much more effective if you let intuition play in the background and let it come to fore only after you have got all the hard facts.

Daniel Kanhemen advises:

> Delay your intuition until you have gathered all facts (paraphrased)
> 

**What does this mean for a performance engineer?**

It is very common for performance engineers to be under pressure to provide quick results. Developers and other stakeholders often chase them for "initial analysis" or potential cause. It might be better to not give any initial theories - at least when you are dealing with complex performance issues. The correct analysis could be different from initial analysis. In addition to the internal inertia to build a new story, you are also likely to be concerned about externally appearing as someone who keeps changing their conclusions.

Thus, If unavoidable,

1. frame the initial analysis in such a way that it leaves room for you to abandon it totally later on,
2. don't let initial analysis influence your further investigation(easier said than done)

All said and done, it is very likely that you will find yourself in a position having to defend your initial analysis in the face of new contradictory data points.

### Conclusion

Train your brain to spot these biases and to automatically avoid them.

### **References:**

[Thinking Fast and Slow](https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow#) - Daniel Kanheman

[Fooled By Randomness](https://www.goodreads.com/book/show/38315.Fooled_by_Randomness) - N.N. Taleb

[The Black Swan](https://www.goodreads.com/book/show/242472.The_Black_Swan) - N.N. Taleb

[Nature.com](http://nature.com/) article: https://www.nature.com/articles/d41586-021-00592-0
