#!/usr/bin/env python3
import json

data = {
  "date": "2026年3月28日",
  "builders": [
    {
      "name": "Swyx",
      "handle": "swyx",
      "bio": "achieve ambition with intentionality, intensity, integrity & insanity.\n\naffiliations:\n- @dxtipshq \n- @cognition\n- @temporalio\n- @aidotengineer\n- @latentspacepod",
      "tweets": [
        {
          "id": "2037695506055610768",
          "text": "@openclaw @pmarca @latentspacepod we also talk about the need for @alexblania's @worldcoinfnd Proof of Human to fuck over these retards proudly ruining the internet\n\nhttps://t.co/6GkEGPALJW",
          "textZh": "@openclaw @pmarca @latentspacepod 我们还讨论了为什么需要 @alexblania 的 @worldcoinfnd 人类证明，来狠狠治治那些自豪地糟蹋互联网的蠢货\n\nhttps://t.co/6GkEGPALJW",
          "createdAt": "2026-03-28T00:57:21.000Z",
          "url": "https://x.com/swyx/status/2037695506055610768",
          "likes": 6,
          "retweets": 0,
          "replies": 0,
          "isQuote": True
        },
        {
          "id": "2037642679501324438",
          "text": "@openclaw @pmarca @latentspacepod pls like and subscribe i guess https://t.co/0af86LRpmU",
          "textZh": "@openclaw @pmarca @latentspacepod 记得点赞订阅哈 https://t.co/0af86LRpmU",
          "createdAt": "2026-03-27T21:27:27.000Z",
          "url": "https://x.com/swyx/status/2037642679501324438",
          "likes": 5,
          "retweets": 0,
          "replies": 2,
          "isQuote": False
        },
        {
          "id": "2037620876179537989",
          "text": 'just learned about create-context-graph - one command and it sets up key entity relationships for 22 top industry domains. been looking for something like this to "layer on" a social graph to every single app I make! https://t.co/FxBIK0EDrG https://t.co/D8HFstQjjz',
          "textZh": '刚了解到 create-context-graph - 一条命令就能为22个主流行业领域建立关键实体关系。一直在找这样的工具，想把它"叠加"到我做的每个应用里做社交图谱！https://t.co/FxBIK0EDrG https://t.co/D8HFstQjjz',
          "createdAt": "2026-03-27T20:00:48.000Z",
          "url": "https://x.com/swyx/status/2037620876179537989",
          "likes": 382,
          "retweets": 27,
          "replies": 29,
          "isQuote": True
        }
      ]
    },
    {
      "name": "Josh Woodward",
      "handle": "joshwoodward",
      "bio": "VP, @Google @GoogleLabs @GeminiApp @GoogleAIStudio",
      "tweets": [
        {
          "id": "2037674926715605331",
          "text": 'Our "Veo Sailor" from the Veo 3 launch wants to remind you: "You can still make videos in Gemini" :) https://t.co/qX18rDMU2y',
          "textZh": '我们Veo 3发布会上的"Veo Sailor"想提醒你："你还是可以在Gemini里做视频的":) https://t.co/qX18rDMU2y',
          "createdAt": "2026-03-27T23:35:35.000Z",
          "url": "https://x.com/joshwoodward/status/2037674926715605331",
          "likes": 149,
          "retweets": 7,
          "replies": 19,
          "isQuote": True
        }
      ]
    },
    {
      "name": "Peter Yang",
      "handle": "petergyang",
      "bio": "I share extremely practical AI tutorials and interviews | Join 140K+ readers at https://t.co/XYKTmGVH14 | Product at Roblox",
      "tweets": [
        {
          "id": "2037704776331448686",
          "text": "The best way to learn to use Claude Cowork is from the designer who helped build it.\n\nDon't miss my new episode with Jenny this weekend where she shared:\n\n→ How she uses Cowork at Anthropic\n→ Live demo: From feedback to product deck\n→ The real story behind Cowork's creation\n\n📌 Subscribe to get it on Sunday: https://t.co/Ggqaa3F11Z",
          "textZh": "学习使用Claude Cowork的最佳方式是向帮助构建它的设计师请教。\n\n别错过我这周末与Jenny的新节目，她分享了：\n\n→ 她如何在Anthropic使用Cowork\n→ 现场演示：从反馈到产品演示文稿\n→ Cowork背后的真实故事\n\n📌 订阅并在周日获取：https://t.co/Ggqaa3F11Z",
          "createdAt": "2026-03-28T01:34:12.000Z",
          "url": "https://x.com/petergyang/status/2037704776331448686",
          "likes": 74,
          "retweets": 5,
          "replies": 4,
          "isQuote": False
        },
        {
          "id": "2037547513163751764",
          "text": "This is why I love @bentossell lol https://t.co/JmTdhkkDxz",
          "textZh": "这就是为什么我喜欢@bentossell哈哈哈 https://t.co/JmTdhkkDxz",
          "createdAt": "2026-03-27T15:09:17.000Z",
          "url": "https://x.com/petergyang/status/2037547513163751764",
          "likes": 12,
          "retweets": 0,
          "replies": 2,
          "isQuote": True
        },
        {
          "id": "2037543771580289154",
          "text": "Build an /exec-review AI skill to get your leader's product feedback anytime you want.\n\nA simple way to start is with their decision-making framework — what gets support vs. push back.\n\nBelow's a real example from my friend who's a Meta VP. The complete skill has 5 more sections:\n\n→ Core principles\n→ Feedback patterns\n→ Communication style\n→ Review checklist\n→ Example comments\n\n📌 Get the full breakdown here: https://t.co/CyoSh2WEb9",
          "textZh": "创建一个/exec-review AI技能，随时获取老板的产品反馈。\n\n简单的方法是从他们的决策框架开始——什么是会支持的，什么是会反对的。\n\n下面是我一位Meta VP朋友的真实案例。完整技能还有5个部分：\n\n→ 核心原则\n→ 反馈模式\n→ 沟通风格\n→ 审查清单\n→ 示例评语\n\n📌 获取完整分析：https://t.co/CyoSh2WEb9",
          "createdAt": "2026-03-27T14:54:25.000Z",
          "url": "https://x.com/petergyang/status/2037543771580289154",
          "likes": 71,
          "retweets": 8,
          "replies": 4,
          "isQuote": False
        }
      ]
    },
    {
      "name": "Nan Yu",
      "handle": "thenanyu",
      "bio": "head of product @linear",
      "tweets": [
        {
          "id": "2037617782943056148",
          "text": "What if the next few YC batches have overly correlated performance because they all use GStack, which causes them to make the same kinds of mistakes but also biases to them towards being selected for admission.",
          "textZh": "如果接下来几届YC batches的表现都高度相关，因为它们都用GStack，导致它们犯同样的错误，同时也让它们更容易被录取，会怎样？",
          "createdAt": "2026-03-27T19:48:31.000Z",
          "url": "https://x.com/thenanyu/status/2037617782943056148",
          "likes": 8,
          "retweets": 0,
          "replies": 0,
          "isQuote": False
        }
      ]
    },
    {
      "name": "Aaron Levie",
      "handle": "levie",
      "bio": "ceo @box - your business lives in content. unleash it with AI",
      "tweets": [
        {
          "id": "2037744753073385518",
          "text": "The big gap in most enterprises being able to automate work is being able to get right context to the agents.\n\nWe experience a huge benefit in coding in tech because the problem is generally far simpler than other areas of knowledge work. The codebase contains a bunch of necessary context, access controls and permissions are generally not a major concern, the users are technical enough to supply the context, and the final output is generally quickly verifiable. \n\nMost knowledge work doesn't look like this. The data is sitting in legacy silos that don't easily connect to agents, the access controls are all out of whack (people have either too much or too little access), the information isn't agent-ready, and more. \n\nThis is the big context gap for any type of agentic workflows in most organizations right. The platforms that make solving this easy, and the companies that retool their workflows to enable this, will be the winners in a world of agents.",
          "textZh": "大多数企业实现工作自动化的最大障碍，是能否给agent提供正确的上下文。\n\n我们在科技领域的编程中体验到巨大收益，因为问题通常比其他知识工作领域简单得多。代码库包含大量必要的上下文，访问控制通常不是主要问题，用户有足够的技术能力来提供上下文，最终输出通常可以快速验证。\n\n大多数知识工作可不像这样。数据躺在难以与agent连接的遗留数据孤岛里，访问控制完全混乱（人们要么权限太多要么太少），信息对agent不友好，等等。\n\n这就是大多数组织中各类agent化工作流面临的重大上下文缺口。能让解决这个变得容易的平台，以及重新设计工作流程来实现这一点的公司，将在agent时代成为赢家。",
          "createdAt": "2026-03-28T04:13:03.000Z",
          "url": "https://x.com/levie/status/2037744753073385518",
          "likes": 118,
          "retweets": 17,
          "replies": 28,
          "isQuote": True
        }
      ]
    },
    {
      "name": "Garry Tan",
      "handle": "garrytan",
      "bio": "President & CEO @ycombinator —Founder https://t.co/7aoJjp1iIK—designer/engineer who helps founders—SF Dem accelerating the boom loop—haters not allowed in my sauna",
      "tweets": [
        {
          "id": "2037776210898600402",
          "text": "This is why on GStack I usually just run /plan-eng-review and /ship and it works https://t.co/qZ2dYsxrdk",
          "textZh": "这就是为什么在GStack上我通常只跑/plan-eng-review和/ship，而且很有效 https://t.co/qZ2dYsxrdk",
          "createdAt": "2026-03-28T06:18:03.000Z",
          "url": "https://x.com/garrytan/status/2037776210898600402",
          "likes": 19,
          "retweets": 3,
          "replies": 7,
          "isQuote": True
        },
        {
          "id": "2037775207289831910",
          "text": "We live in remarkable times https://t.co/qJkMjZ9bGM",
          "textZh": "我们生活在神奇的时代 https://t.co/qJkMjZ9bGM",
          "createdAt": "2026-03-28T06:14:04.000Z",
          "url": "https://x.com/garrytan/status/2037775207289831910",
          "likes": 16,
          "retweets": 1,
          "replies": 3,
          "isQuote": True
        },
        {
          "id": "2037772478198739346",
          "text": "I have to say this interview changed my life. Hearing how Boris thinks about software spurred me to work much harder on releasing my own way of doing things and on iterating fast on how I build. Hard to believe it has only been a month since this one. https://t.co/y0y5JmQodL",
          "textZh": "我得说这次采访改变了我的生活。听到Boris如何思考软件，促使我在发布自己的方法论和快速迭代构建方式上更加努力。难以相信距离这次才过了一个月。https://t.co/y0y5JmQodL",
          "createdAt": "2026-03-28T06:03:13.000Z",
          "url": "https://x.com/garrytan/status/2037772478198739346",
          "likes": 63,
          "retweets": 5,
          "replies": 8,
          "isQuote": True
        }
      ]
    },
    {
      "name": "Zara Zhang",
      "handle": "zarazhangrui",
      "bio": "Builder. Dangerously skips permissions. Harvard'17. GitHub: https://t.co/KCuEajezlL YouTube: https://t.co/8xzbGWtf6w",
      "tweets": [
        {
          "id": "2037661344154124309",
          "text": "Best Careers page I've ever seen https://t.co/upGQuygOtv",
          "textZh": "这是我见过最棒的招聘页面 https://t.co/upGQuygOtv",
          "createdAt": "2026-03-27T22:41:37.000Z",
          "url": "https://x.com/zarazhangrui/status/2037661344154124309",
          "likes": 93,
          "retweets": 6,
          "replies": 5,
          "isQuote": True
        },
        {
          "id": "2037653942663098556",
          "text": "The next generation of AI products will need to figure out how to reconcile human fallibility with agent infallibility",
          "textZh": "下一代AI产品需要搞清楚如何调和人类的易犯错和agent的不犯错",
          "createdAt": "2026-03-27T22:12:12.000Z",
          "url": "https://x.com/zarazhangrui/status/2037653942663098556",
          "likes": 16,
          "retweets": 2,
          "replies": 3,
          "isQuote": False
        },
        {
          "id": "2037610198349894039",
          "text": "Turns out the bottleneck is the human's context window, not the AI's",
          "textZh": "原来瓶颈在于人类的上下文窗口，而不是AI的",
          "createdAt": "2026-03-27T19:18:22.000Z",
          "url": "https://x.com/zarazhangrui/status/2037610198349894039",
          "likes": 146,
          "retweets": 12,
          "replies": 17,
          "isQuote": False
        }
      ]
    },
    {
      "name": "Nikunj Kothari",
      "handle": "nikunj",
      "bio": "partner @fpvventures - investing in seed/A. previous: early hire @meter, @opendoor, @atlassian & others. love @shimoleejhaveri + 👦👧",
      "tweets": [
        {
          "id": "2037743784210132995",
          "text": 'If X built something like this natively, I\'d honestly pay them $50/mo.. but till then it was fun to run "intelligence" to understand all my followers ✌️ https://t.co/wrcnLLxCcx',
          "textZh": '如果X能原生做出这样的功能，我愿意付$50/月.. 但在那之前，用"intelligence"来了解我的所有粉丝还挺有意思的✌️ https://t.co/wrcnLLxCcx',
          "createdAt": "2026-03-28T04:09:12.000Z",
          "url": "https://x.com/nikunj/status/2037743784210132995",
          "likes": 7,
          "retweets": 0,
          "replies": 1,
          "isQuote": False
        }
      ]
    },
    {
      "name": "Peter Steinberger",
      "handle": "steipete",
      "bio": "Polyagentmorous ClawFather. Came back from retirement to mess with AI and help a lobster take over the world @openclaw🦞",
      "tweets": [
        {
          "id": "2037725493315707290",
          "text": "Another sick upcoming feature:\n\n/acp spawn codex --bind here\nLOOK AT ME, I AM CODEX NOW\n\nYou could bind codex/claude code/opencode already in threads, now you can take over your current session as well.",
          "textZh": "又一个超赞的新功能：\n\n/acp spawn codex --bind here\n看哪，我现在是CODEX了！\n\n之前你可以在thread里绑定codex/claude code/opencode，现在你也可以接管当前的session了。",
          "