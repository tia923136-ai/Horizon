---
layout: default
title: "Horizon Summary: 2026-03-23 (EN)"
date: 2026-03-23
lang: en
---

> From 31 items, 10 important content pieces were selected

---

1. [GitHub struggles with three nines availability amid criticism](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 released with ASGI improvements](#item-2) ⭐️ 7.0/10
3. [PC Gamer's 37MB Article Exposes Web Bloat Issues](#item-3) ⭐️ 7.0/10
4. [Comparison of JavaScript Sandboxing Solutions](#item-4) ⭐️ 7.0/10
5. [Interactive CRDT Version Control Visualizer with Pyodide](#item-5) ⭐️ 7.0/10
6. [Simon Willison profiles Hacker News users via comment analysis](#item-6) ⭐️ 7.0/10
7. [Using Git with coding agents for efficient development](#item-7) ⭐️ 7.0/10
8. [MiniMax upgrades Coding Plan with multimodal support and announces MiniMax 2.7 open-source weights](#item-8) ⭐️ 7.0/10
9. [Qianwen Launches AI Ride-Hailing with Natural Language Commands](#item-9) ⭐️ 7.0/10
10. [OpenAI proposes UK include AI chatbots in Google search selection page](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GitHub struggles with three nines availability amid criticism](https://www.theregister.com/2026/02/10/github_outages/) ⭐️ 7.0/10

GitHub has been experiencing poor uptime, achieving only three nines (99.9%) availability, while also facing security vulnerabilities in its GitHub Actions feature that have led to breaches like the recent Aqua Security incident. As the world's largest code hosting platform, GitHub's reliability and security issues directly impact millions of developers and organizations that depend on it for daily operations, potentially causing widespread disruption to software development workflows. The three nines availability means about 8.76 hours of downtime per year, while critics highlight GitHub's continued use of mutable references in Actions despite long-standing community warnings, and its controversial infrastructure migration to Azure.

hackernews · richtr · Mar 23, 10:39

**Background**: High availability is typically measured in 'nines', with three nines (99.9%) considered basic reliability for business-critical systems. GitHub's infrastructure decisions, including its migration to Microsoft's Azure cloud, have been under scrutiny since 2025 when it abandoned its independent data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_availability">High availability - Wikipedia</a></li>
<li><a href="https://github.blog/engineering/infrastructure/">How GitHub approaches infrastructure - The GitHub Blog</a></li>
<li><a href="https://wellarchitected.github.com/library/overview/">Overview – GitHub Well-Architected</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed, with some defending GitHub's challenges during cloud migration while others criticize its prioritization of AI features over core reliability. Several commenters specifically mention security flaws in GitHub Actions that have been known for years but remain unaddressed.

**Tags**: `#github`, `#reliability`, `#security`, `#devops`, `#cloud`

---

<a id="item-2"></a>
## [Starlette 1.0 released with ASGI improvements](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

Starlette 1.0, the foundational Python ASGI framework that powers FastAPI, has been officially released with breaking changes including a new lifespan mechanism replacing on_startup/on_shutdown handlers. The project also transferred maintainership to Marcelo Trylesinski in 2025 after years of development by Kim Christie. This release marks stability for a framework that quietly powers much of Python's modern async web ecosystem through FastAPI, while introducing cleaner patterns for async resource management that could influence future ASGI development. The new lifespan system uses Python's async context managers for resource handling, providing clearer startup/shutdown sequencing. However, the breaking changes may affect AI-generated code compatibility as models were trained on pre-1.0 versions.

rss · Simon Willison · Mar 22, 23:57

**Background**: Starlette is a lightweight ASGI framework designed for building async web services in Python, serving as the foundation for FastAPI. ASGI (Asynchronous Server Gateway Interface) is Python's standard for async web servers and applications, enabling support for WebSockets and other async protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://asgi.readthedocs.io/en/latest/specs/main.html">ASGI (Asynchronous Server Gateway Interface) Specification — ASGI ...</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/starlette: The little ASGI framework that shines. 🌟</a></li>

</ul>
</details>

**Tags**: `#Python`, `#ASGI`, `#Starlette`, `#FastAPI`, `#Web Development`

---

<a id="item-3"></a>
## [PC Gamer's 37MB Article Exposes Web Bloat Issues](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

An analysis of PC Gamer's web performance revealed a 37MB article that kept downloading hundreds more MBs due to auto-playing video ads, using the Rodney tool for investigation. This highlights the severe impact of web bloat on user experience and data usage, particularly from auto-playing ads, which affects major publications and their readers. The Rodney tool, a lightweight CLI for Chrome automation, was used to audit the page, revealing inefficient resource loading and excessive data consumption.

rss · Simon Willison · Mar 22, 22:49

**Background**: Web bloat refers to excessive and inefficient use of resources like scripts, ads, and media that slow down page loading. Auto-playing video ads are a common contributor to this issue, often consuming significant bandwidth without user consent.

<details><summary>References</summary>
<ul>
<li><a href="https://lobehub.com/skills/maragudk-skills-rodney">rodney | Skills Marketplace - LobeHub</a></li>
<li><a href="https://www.digitalcitizen.life/how-to-stop-videos-from-playing-automatically-on-websites/">How to Stop Videos from Playing Automatically on Websites</a></li>

</ul>
</details>

**Tags**: `#web-performance`, `#web-bloat`, `#analysis`, `#rodney`, `#optimization`

---

<a id="item-4"></a>
## [Comparison of JavaScript Sandboxing Solutions](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison published a technical comparison of JavaScript sandboxing approaches, including isolated-vm, vm2, QuickJS, ShadowRealm, and Deno Workers, inspired by research into Node.js worker threads. This research is crucial for developers needing to run untrusted JavaScript code securely, as it evaluates the isolation capabilities and security trade-offs of different sandboxing approaches in the JavaScript ecosystem. The comparison includes both Node.js-specific solutions (isolated-vm, vm2) and alternative engines (QuickJS), plus emerging standards like ShadowRealm and Deno's worker implementation with stronger isolation guarantees.

rss · Simon Willison · Mar 22, 19:53

**Background**: JavaScript sandboxing refers to techniques for running untrusted code in isolated environments to prevent access to sensitive system resources. Traditional approaches like Node.js's vm module have known security limitations, prompting development of more robust solutions. ShadowRealm is a new TC39 proposal for creating isolated JavaScript execution contexts, while Deno Workers offer process-level isolation similar to Web Workers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/patriksimek/vm2">GitHub - patriksimek/vm2: Advanced vm/sandbox for Node.js · GitHub</a></li>
<li><a href="https://medium.com/@asierr/javascripts-new-shadowrealm-secure-and-isolated-javascript-execution-f620350750ed">JavaScript ’s New ShadowRealm : Secure and Isolated... | Medium</a></li>
<li><a href="https://docs.deno.com/api/node/worker_threads/">worker_threads - Node documentation</a></li>

</ul>
</details>

**Tags**: `#javascript`, `#sandboxing`, `#security`, `#runtime`, `#nodejs`

---

<a id="item-5"></a>
## [Interactive CRDT Version Control Visualizer with Pyodide](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison has created an interactive tool that visualizes Bram Cohen's CRDT-based version control system Manyana, using Pyodide to run Python in the browser and Claude's AI-generated explanation of the 470-line Python implementation. This demonstrates a novel approach to version control using Conflict-free Replicated Data Types (CRDTs), which could enable more seamless collaboration and conflict resolution compared to traditional systems like Git, while making the complex concepts accessible through visualization. The visualization focuses on Manyana's core algorithms (still a demo with limitations like no cherry-picking/local undo) and uses Pyodide's WebAssembly-based Python runtime to enable interactive exploration directly in the browser.

rss · Simon Willison · Mar 22, 18:57

**Background**: CRDTs (Conflict-free Replicated Data Types) are data structures that can be replicated across multiple devices and updated independently without coordination, guaranteeing eventual consistency. Pyodide is a Python distribution that compiles to WebAssembly, allowing Python code to run in web browsers. Bram Cohen, creator of BitTorrent, proposed Manyana as a CRDT-based alternative to Git's merge conflicts.

<details><summary>References</summary>
<ul>
<li><a href="https://bramcohen.com/p/manyana">A Coherent Vision for the Future of Version Control</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>
<li><a href="https://pyodide.com/what-is-pyodide/">What is Pyodide? - pyodide</a></li>

</ul>
</details>

**Tags**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-6"></a>
## [Simon Willison profiles Hacker News users via comment analysis](https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything) ⭐️ 7.0/10

Simon Willison developed a method to profile Hacker News users by analyzing their last 1,000 comments using the Algolia API and ChatGPT/Claude Opus, demonstrating its effectiveness with his own profile. This technique showcases the growing capabilities of LLMs in behavioral analysis and raises questions about privacy in public comment spaces, while providing a practical tool for understanding community dynamics. The method leverages Algolia's open CORS API to fetch comment history and uses advanced LLMs like Claude Opus 4.6 for analysis. Willison notes the results feel 'startlingly effective' yet potentially invasive.

rss · Simon Willison · Mar 21, 23:59

**Background**: The Algolia Hacker News API provides programmatic access to Hacker News data including comments, with open CORS headers allowing client-side JavaScript access. CORS (Cross-Origin Resource Sharing) is a security mechanism that enables restricted resources on a web page to be requested from another domain outside the domain from which the first resource was served.

<details><summary>References</summary>
<ul>
<li><a href="https://hn.algolia.com/api">Hacker News Search powered by Algolia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cross-origin_resource_sharing">Cross-origin resource sharing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Hacker News`, `#API`, `#Data Analysis`, `#ChatGPT`, `#User Profiling`

---

<a id="item-7"></a>
## [Using Git with coding agents for efficient development](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything) ⭐️ 7.0/10

The article demonstrates how coding agents can leverage Git's full capabilities for version control, including repository management, commit tracking, and branch operations, through specific command prompts. This matters because it enables developers to delegate complex Git operations to AI agents, improving productivity in AI-assisted development workflows while maintaining robust version control practices. The article provides concrete Git command examples that coding agents understand, such as 'git init', 'git commit', and 'git log', and explains how these can be triggered through natural language prompts.

rss · Simon Willison · Mar 21, 22:08

**Background**: Coding agents are AI systems that assist with software development tasks. Git is a distributed version control system that tracks changes in source code during development. Agentic engineering refers to patterns for effectively working with AI agents in development workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/">Agentic Engineering Patterns - Simon Willison's Weblog</a></li>
<li><a href="https://medium.com/@analyticsinsight/ai-coding-agents-transforming-software-development-e75e098e4603">AI Coding Agents : Transforming Software Development | Medium</a></li>

</ul>
</details>

**Tags**: `#Git`, `#AI-assisted-development`, `#version-control`, `#agentic-engineering`, `#software-engineering`

---

<a id="item-8"></a>
## [MiniMax upgrades Coding Plan with multimodal support and announces MiniMax 2.7 open-source weights](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax has upgraded its Coding Plan to Token Plan, offering Plus and higher-tier users additional quotas for multimodal models including video, audio, music, and images. The company also announced that MiniMax 2.7 open-source weights will be released in about two weeks. This upgrade enables developers to access a comprehensive suite of multimodal AI tools under a single plan, significantly enhancing productivity and creative possibilities. The upcoming open-source release of MiniMax 2.7 weights will provide researchers and developers with valuable resources for AI model development and experimentation. The platform will implement dynamic rate limiting during peak hours (3:00-5:30 PM on weekdays), with weekly usage capped at 10 times the original programming model's 5-hour quota. MiniMax 2.7 has shown significant improvements in the OpenClaw benchmark tests.

telegram · zaihuapd · Mar 23, 02:09

**Background**: MiniMax is a leading Chinese AI company founded in December 2021, specializing in multimodal and trillion-parameter MoE large models. The company has developed native applications like Conch AI and Xingye, and provides API services for enterprises and developers to build AI applications. OpenClaw is a benchmarking system specifically designed to evaluate LLM models as coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.minimaxi.com/subscribe/coding-plan">Token Plan - MiniMax API 平台</a></li>
<li><a href="https://www.aibase.com/news/26453">MiniMax Launches Token Plan: The World's First All-Modal ...</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding agents. Made with 🦀 by the humans at https://kilo.ai</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal-models`, `#open-source`, `#rate-limiting`, `#MiniMax`

---

<a id="item-9"></a>
## [Qianwen Launches AI Ride-Hailing with Natural Language Commands](http://www.ce.cn/cysc/newmain/yc/jsxw/202603/t20260323_2849214.shtml) ⭐️ 7.0/10

On March 23, Qianwen officially launched its ride-hailing feature, allowing users to complete the entire process of booking a ride, including vehicle selection, adding stops, scheduling times, and payment, using natural language commands. The system also supports personalized requests such as 'price under 30 yuan,' 'smooth driving,' and 'fresh air,' and can automatically match vehicle types based on the number of passengers. This development represents a significant step in integrating AI-powered natural language processing with everyday services, enhancing user convenience and personalization in ride-hailing. It also strengthens Alibaba's ecosystem by linking ride-hailing with other services like hotel bookings and food delivery, creating a seamless user experience. The feature supports 'Alipay AI Pay' for seamless payment after the ride and can remember frequently used addresses like home and work. It also allows for scheduling rides at specific times and integrates with other ecosystem services for continuous command execution.

telegram · zaihuapd · Mar 23, 02:50

**Background**: Qianwen is Alibaba's AI platform that leverages natural language processing to provide various digital life services. 'Alipay AI Pay' is a smart payment service launched in 2025, enabling users to complete transactions through voice commands without navigating multiple pages. This ride-hailing feature builds on Qianwen's existing capabilities to further integrate AI into daily conveniences.

<details><summary>References</summary>
<ul>
<li><a href="https://dn.com/en-us/news/detail-4202.html">Alibaba's Qianwen platform launched its AI-powered ride ...</a></li>
<li><a href="https://news.aibase.com/news/26451">Qwen Launches AI Ride-Hailing Service, Supports Alipay AI Payment</a></li>
<li><a href="https://www.oschina.net/news/371606">支付宝推出国内首个 AI 付 - OSCHINA - 中文开源技术交流社区</a></li>

</ul>
</details>

**Tags**: `#AI`, `#ride-hailing`, `#natural-language-processing`, `#personalization`, `#mobile-payments`

---

<a id="item-10"></a>
## [OpenAI proposes UK include AI chatbots in Google search selection page](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 7.0/10

OpenAI submitted a proposal to the UK's Competition and Markets Authority (CMA) on March 6, suggesting that AI chatbots with search capabilities like ChatGPT should be included in Google's search selection page, allowing them to be set as default search services on Android devices and Chrome. This proposal could reshape search engine competition by modernizing the criteria to include AI-driven services, ensuring fair competition between traditional search engines and emerging conversational AI tools like ChatGPT. OpenAI argues that ChatGPT's conversational and multimodal capabilities are functionally similar to Google's AI Overviews and AI Mode, and suggests using transparent, dynamic popularity metrics to determine inclusion, while expanding the selection page to voice, visual, and AI-assisted search entry points.

telegram · zaihuapd · Mar 23, 14:50

**Background**: Google's search selection page allows users to choose default search providers on Android devices and browsers. AI Overviews and AI Mode are Google's own AI-powered search features that provide summarized answers and handle complex queries. OpenAI's proposal seeks to give similar prominence to third-party AI chatbots in this ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/websearch/answer/464?hl=zh-Hans">将 Google 设为您的默认搜索引擎</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Mode">AI Mode</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Search Engines`, `#Regulation`, `#OpenAI`, `#Competition`

---