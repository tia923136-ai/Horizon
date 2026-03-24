---
layout: default
title: "Horizon Summary: 2026-03-24 (EN)"
date: 2026-03-24
lang: en
---

> From 32 items, 13 important content pieces were selected

---

1. [Streaming experts enable trillion-parameter models on consumer devices](#item-1) ⭐️ 8.0/10
2. [Nvidia accused of leveraging financial power to lock AI customers into its ecosystem](#item-2) ⭐️ 8.0/10
3. [Alibaba DAMO Academy launches Xuantie C950 RISC-V CPU with record performance](#item-3) ⭐️ 8.0/10
4. [DarkSword Exploit Chain Targets Safari Users via Malicious Web Pages](#item-4) ⭐️ 8.0/10
5. [Google launches Gemini dark web threat intelligence AI agent in public preview](#item-5) ⭐️ 8.0/10
6. [Microsoft's Windows 11 'Fix' Faces Backlash](#item-6) ⭐️ 7.0/10
7. [DIY Apple Home Integration for Apartment Intercoms](#item-7) ⭐️ 7.0/10
8. [Starlette 1.0 Released as Foundation for FastAPI](#item-8) ⭐️ 7.0/10
9. [PC Gamer article found to be 37MB due to auto-playing ads](#item-9) ⭐️ 7.0/10
10. [JavaScript Sandboxing Techniques Compared](#item-10) ⭐️ 7.0/10
11. [Interactive Merge State Visualizer for CRDT Version Control](#item-11) ⭐️ 7.0/10
12. [FCC bans all foreign-made routers citing security risks](#item-12) ⭐️ 7.0/10
13. [China's daily token usage surges over 1000x, exceeding 140 trillion in March 2024](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Streaming experts enable trillion-parameter models on consumer devices](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Researchers have demonstrated running trillion-parameter Mixture-of-Experts models like Kimi K2.5 (1T params) on a MacBook Pro with 96GB RAM, and Qwen3.5-397B-A17B on an iPhone at 0.6 tokens/second, using a technique that streams expert weights from SSD instead of loading the full model into memory. This breakthrough dramatically lowers the hardware requirements for running state-of-the-art AI models, potentially enabling advanced LLM capabilities on personal devices without cloud dependency, which could reshape the landscape of local AI applications. The technique activates only 32B weights at a time from the 1T parameter Kimi K2.5 model, while Qwen3.5-397B-A17B runs on just 48GB RAM. Performance remains limited on mobile devices (0.6 tokens/sec on iPhone).

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) models use specialized sub-networks (experts) that are selectively activated per input, allowing larger total parameters with lower active compute. Traditional MoE implementations require loading all experts into memory, while this new streaming approach dynamically loads only the needed experts from storage.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Developers are excited about the rapid progress, with some noting this could enable new categories of local AI applications. Others caution that the current performance on mobile devices remains impractical for most real-world use cases.

**Tags**: `#LLM`, `#Mixture-of-Experts`, `#hardware-optimization`, `#AI`, `#streaming`

---

<a id="item-2"></a>
## [Nvidia accused of leveraging financial power to lock AI customers into its ecosystem](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

Nvidia has invested billions in AI startups like OpenAI, CoreWeave, and Reflection since 2022, acting as both supplier and investor to lock customers into its ecosystem. The company also faces scrutiny for its $20 billion deal with chip startup Groq, which some argue is designed to evade antitrust scrutiny. Nvidia's strategy could stifle competition in the AI market by making it difficult for customers to switch to competitors like AMD. This has drawn attention from US lawmakers concerned about potential antitrust violations and the long-term impact on market diversity. Nvidia's investments include cloud GPU provider CoreWeave and autonomous coding startup Reflection. The Groq deal involved acquiring key talent while avoiding full acquisition to dodge regulatory hurdles.

telegram · zaihuapd · Mar 24, 03:02

**Background**: Nvidia dominates the AI chip market with its GPUs being essential for training large language models. CoreWeave specializes in GPU cloud infrastructure for AI, while Groq develops AI accelerator chips. Reflection AI focuses on autonomous coding agents as a path to superintelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Nvidia`, `#antitrust`, `#semiconductors`, `#investment`

---

<a id="item-3"></a>
## [Alibaba DAMO Academy launches Xuantie C950 RISC-V CPU with record performance](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

Alibaba DAMO Academy unveiled its flagship Xuantie C950 RISC-V CPU on March 24 at the 2026 Xuantie RISC-V Ecosystem Conference in Shanghai, achieving over 70 points in the Specint2006 single-core benchmark, currently the highest publicly reported score for RISC-V processors. This breakthrough demonstrates RISC-V's growing competitiveness in high-performance computing, potentially disrupting ARM and x86 dominance in cloud AI and edge computing markets, especially with native support for billion-parameter models like Qwen3 and DeepSeek V3. The chip integrates DAMO's proprietary AI acceleration engine and targets cloud computing, generative AI, high-end robotics, and edge computing applications. Its Specint2006 score of 70+ significantly outperforms previous RISC-V implementations.

telegram · zaihuapd · Mar 24, 06:01

**Background**: RISC-V is an open-standard instruction set architecture gaining traction as an alternative to proprietary architectures like ARM and x86. Specint2006 is a standardized benchmark for measuring CPU integer performance. Qwen3 and DeepSeek V3 are Alibaba's large language models with hundreds of billions of parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/models/comparisons/qwen3-max-vs-deepseek-v3">Qwen3 Max vs DeepSeek V3 (Dec '24): Model Comparison</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#AI Hardware`, `#Cloud Computing`, `#Semiconductors`, `#Edge Computing`

---

<a id="item-4"></a>
## [DarkSword Exploit Chain Targets Safari Users via Malicious Web Pages](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

The DarkSword exploit chain, active since November 2025, targets Safari users by infecting devices when they visit malicious web pages, affecting iOS versions 18.4 to 18.7 and delivering GHOSTBLADE payloads. The vulnerabilities have been patched in iOS 26.3, with some fixes released earlier, such as CVE-2025-43529, which was addressed in iOS 18.7.3 and 26.2. This exploit chain is significant due to its sophistication, chaining six vulnerabilities (including three zero-days) to achieve silent device takeover, and its use in targeted attacks across multiple countries. The GHOSTBLADE payload can steal sensitive data, including communications, photos, and cryptocurrency exchange credentials, posing a severe threat to affected users. The exploit chain is entirely written in JavaScript and achieves one-click device takeover on unpatched iPhones. It specifically targets iOS 18.4-18.7 and has been used in attacks in Saudi Arabia, Turkey, Malaysia, and Ukraine.

telegram · zaihuapd · Mar 24, 11:45

**Background**: DarkSword is a newly disclosed iOS exploit chain that leverages multiple zero-day vulnerabilities to fully compromise iOS devices. GHOSTBLADE is a known malware family that systematically scans infected devices for sensitive data, including cryptocurrency exchange applications and personal communications.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword: iOS Exploit Chain Adopted by ...</a></li>
<li><a href="https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html">DarkSword iOS Exploit Kit Uses 6 Flaws, 3 Zero-Days for Full ...</a></li>
<li><a href="https://cybersecsentinel.com/darksword-ios-exploit-chains-six-vulnerabilities-for-silent-device-takeover/">DarkSword iOS Exploit Chains Six Vulnerabilities for Silent ...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#ios`, `#safari`, `#zero-day`, `#malware`

---

<a id="item-5"></a>
## [Google launches Gemini dark web threat intelligence AI agent in public preview](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

Google has integrated a Gemini-based AI agent into Google Threat Intelligence, now available in public preview. The service analyzes 8-10 million dark web posts daily with 98% accuracy to identify risks like initial access broker activities, data leaks, and insider threats for organizations. This represents a major advancement in automated dark web monitoring, enabling enterprises to proactively detect cyber threats at unprecedented scale. The high accuracy could significantly reduce false positives in threat intelligence operations. The AI first creates organizational profiles before scanning dark web content. It specifically targets initial access brokers (IABs) - hackers who sell network access to other cybercriminals. The 98% accuracy claim comes from Google's internal testing.

telegram · zaihuapd · Mar 24, 13:15

**Background**: Initial access brokers (IABs) are cybercriminals who specialize in breaching networks and selling access to ransomware groups. The dark web contains forums where such illegal transactions occur. Google Threat Intelligence is part of Google Cloud's security suite, while Gemini is Google's flagship AI model family.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cybersecuritynews.com/google-gemini-ai-dark-web/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to...</a></li>
<li><a href="https://www.cisecurity.org/insights/blog/initial-access-brokers-how-theyre-changing-cybercrime">Initial Access Brokers How They’re Changing Cybercrime - CIS A Deep-Dive Into Initial Access Brokers: Trends, Statistics ... M-Trends 2026: Initial Access Handoff Shrinks From Hours to ... Researchers Uncover Data Leak Site Linked To Active Initial ... They hack to sell: corporate access traded in shadows | Cybernews New Data Leak Site Uncovered Linked to Active Initial Access ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cybersecurity`, `#Dark Web`, `#Google`, `#Threat Intelligence`

---

<a id="item-6"></a>
## [Microsoft's Windows 11 'Fix' Faces Backlash](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/) ⭐️ 7.0/10

Microsoft's approach to addressing Windows 11 user experience issues has been criticized as inadequate and user-hostile, sparking widespread debate about corporate software practices. This matters because Windows 11 is used by millions globally, and Microsoft's handling of updates and forced features sets precedents for how tech giants balance business interests with user needs. Specific complaints include Microsoft Start news reappearing after being disabled, unwanted content delivery, and lack of meaningful system changes to prevent recurring issues.

hackernews · h0ek · Mar 24, 09:36

**Background**: Windows 11 is Microsoft's latest operating system released in 2021, succeeding Windows 10. Microsoft has faced ongoing criticism for aggressive update policies, pre-installed apps, and features that users find difficult to disable permanently.

**Discussion**: Comments reveal deep frustration with Microsoft's practices, comparing them to historical anti-competitive behavior. Users express particular anger about Microsoft Start's persistence and content quality, while some debate whether government adoption enables poor user experiences.

**Tags**: `#Microsoft`, `#Windows11`, `#UserExperience`, `#CorporateCriticism`, `#Software`

---

<a id="item-7"></a>
## [DIY Apple Home Integration for Apartment Intercoms](https://www.jackhogan.me/blog/box-of-secrets/) ⭐️ 7.0/10

A detailed DIY guide demonstrates how to discreetly modify an apartment intercom system to integrate with Apple Home, enabling remote door access via HomeKit. The solution involves hardware hacking while attempting to avoid detection by landlords or building management. This addresses a common urban living pain point where traditional intercoms lack smart home compatibility, while raising important questions about the legality and ethics of modifying shared building infrastructure. The solution could inspire more ethical commercial alternatives in this underserved market segment. The modification requires intercepting and simulating the intercom's electrical signals while maintaining the original functionality. Some commenters noted regional alternatives like pre-made adapter boards in Romania (€30) or simpler voicemail-based workarounds.

hackernews · jackhogan11 · Mar 23, 12:42

**Background**: Apple HomeKit is Apple's smart home platform that allows control of compatible devices through iOS. Many apartment intercoms use analog systems without modern connectivity options, creating demand for integration solutions. Hardware hacking of such systems typically involves reverse-engineering proprietary protocols.

<details><summary>References</summary>
<ul>
<li><a href="https://www.home-assistant.io/integrations/homekit/">Instructions on how to set up the HomeKit Bridge integration in Home...</a></li>
<li><a href="https://jdmcd.io/blog/hacking-my-apartment-intercom/">Hacking My Apartment Intercom – Jimmy McDermott –</a></li>
<li><a href="https://hackaday.io/project/186880/instructions">HOW I HACKED MY INTERCOM SO I CAN BE MORE LAZY - Hackaday.io</a></li>

</ul>
</details>

**Discussion**: Comments reveal ethical concerns about modifying shared infrastructure, with some users calling it 'legally dubious.' Alternative solutions were shared, including commercial adapters and voicemail hacks. Many noted the poor state of intercom technology and market gaps for simple, secure solutions.

**Tags**: `#DIY`, `#Home Automation`, `#Apple HomeKit`, `#Intercom`, `#Hardware Hacking`

---

<a id="item-8"></a>
## [Starlette 1.0 Released as Foundation for FastAPI](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

Starlette 1.0, the foundational ASGI framework for FastAPI, has been released after years of development, introducing breaking changes including a new lifespan mechanism using async context managers. This release is significant because Starlette powers FastAPI, one of Python's most popular web frameworks, and the 1.0 milestone signals API stability for the broader ASGI ecosystem. The most notable change replaces on_startup/on_shutdown parameters with a lifespan async context manager, while maintaining Starlette's signature Flask-like single-file simplicity that makes it LLM-friendly.

rss · Simon Willison · Mar 22, 23:57

**Background**: Starlette is a lightweight ASGI framework/toolkit for building async web services in Python. ASGI (Asynchronous Server Gateway Interface) is the async successor to WSGI, enabling Python frameworks to handle concurrent connections efficiently. FastAPI builds upon Starlette while adding features like automatic OpenAPI documentation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>
<li><a href="https://fastapi.tiangolo.com/benchmarks/">Benchmarks - FastAPI</a></li>

</ul>
</details>

**Tags**: `#Python`, `#ASGI`, `#Web Frameworks`, `#Starlette`, `#FastAPI`

---

<a id="item-9"></a>
## [PC Gamer article found to be 37MB due to auto-playing ads](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

A technical audit revealed a PC Gamer article bloated to 37MB due to auto-playing video ads, analyzed using the Rodney CLI tool. The investigation showed continuous downloading of hundreds more megabytes from these ads. This exemplifies severe web bloat that degrades user experience and accessibility, particularly for those with limited bandwidth. It demonstrates how ad-heavy designs can undermine content delivery in media websites. The analysis used Rodney, a CLI tool for web interaction and performance testing. The 37MB size doesn't include subsequent downloads from auto-playing ads that continue loading in the background.

rss · Simon Willison · Mar 22, 22:49

**Background**: Web bloat refers to unnecessary page weight from oversized media, redundant code, and excessive scripts. Rodney is an open-source CLI tool developed by Simon Willison for web automation and performance analysis, often used with AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/rodney">GitHub - simonw/rodney: CLI tool for interacting with the web</a></li>
<li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">Introducing Showboat and Rodney, so agents can demo what they ...</a></li>
<li><a href="https://www.speedcurve.com/blog/page-bloat-web-performance/">SpeedCurve | What is page bloat? And how is it hurting your business, your search rank, and your users?</a></li>

</ul>
</details>

**Tags**: `#web-performance`, `#web-bloat`, `#rodney`, `#analysis`, `#web-development`

---

<a id="item-10"></a>
## [JavaScript Sandboxing Techniques Compared](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

A detailed research comparison evaluates six JavaScript sandboxing approaches: isolated-vm, vm2, quickjs-emscripten, QuickJS-NG, ShadowRealm, and Deno Workers, inspired by Node.js worker threads exploration. This matters because sandboxing is critical for safely executing untrusted JavaScript code in applications like plugin systems, online IDEs, and serverless functions, where security breaches can have severe consequences. The research highlights vm2's security vulnerabilities despite its popularity, while noting isolated-vm's stronger isolation but maintenance challenges. QuickJS variants offer lightweight alternatives with different tradeoffs.

rss · Simon Willison · Mar 22, 19:53

**Background**: JavaScript sandboxing isolates untrusted code execution to prevent access to sensitive system resources. Traditional approaches include iframes (for browsers) and VM modules (for Node.js), but each has limitations in security or performance. New proposals like ShadowRealm and runtimes like Deno offer modern alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>
<li><a href="https://dev.to/leapcell/a-deep-dive-into-javascript-sandboxing-97b">A Deep Dive into JavaScript Sandboxing - DEV Community</a></li>
<li><a href="https://zendesk.engineering/sandboxing-javascript-e4def55e855e?gi=b5419a96afd3">Sandboxing JavaScript. tl;dr iframes are likely your best bet… | by Daniel Ribeiro | Zendesk Engineering</a></li>

</ul>
</details>

**Tags**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-11"></a>
## [Interactive Merge State Visualizer for CRDT Version Control](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison created an interactive Merge State Visualizer tool using Pyodide to demonstrate Bram Cohen's CRDT-based version control concepts, with AI-assisted explanations from Claude. This provides a practical way to understand advanced CRDT-based version control systems, which could potentially offer better solutions than current tools for handling complex merge conflicts in distributed environments. The visualizer is based on Bram Cohen's 470-line Python implementation of his 'manyana' concept, and runs entirely in the browser via Pyodide without requiring server-side processing.

rss · Simon Willison · Mar 22, 18:57

**Background**: CRDTs (Conflict-Free Replicated Data Types) are data structures that allow distributed systems to synchronize without coordination. Pyodide is a Python distribution that runs in the browser via WebAssembly. Bram Cohen, creator of BitTorrent, has proposed CRDTs as the future of version control systems to handle complex merge scenarios better than current approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://bramcohen.com/p/manyana">A Coherent Vision for the Future of Version Control</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 0.29.3</a></li>

</ul>
</details>

**Tags**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#visualization`

---

<a id="item-12"></a>
## [FCC bans all foreign-made routers citing security risks](https://www.bloomberg.com/news/articles/2026-03-23/fcc-bans-all-foreign-made-routers-citing-security-risks?embedded-checkout=true) ⭐️ 7.0/10

The FCC has officially banned all foreign-made consumer routers from the US market due to cybersecurity and supply chain concerns, placing them on the 'Covered List'. New models will require approval from US agencies like the Department of Defense for exemptions. This decision could significantly disrupt global supply chains and impact major networking equipment manufacturers, while also reflecting growing concerns about cybersecurity threats originating from foreign-made hardware. The ban follows a 'grandfathering' principle, allowing continued use and sale of previously approved models while blocking new uncertified devices. Exemptions require approval from multiple US government agencies.

telegram · zaihuapd · Mar 24, 01:17

**Background**: The FCC's Covered List includes companies deemed national security risks, primarily Chinese firms like Huawei and ZTE. Supply chain attacks have become a major concern following incidents like SolarWinds, where compromised hardware/software updates were used to infiltrate systems.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1937155538233320578">FCC 新规核心条款+过渡期强制时间表 - 知乎</a></li>
<li><a href="https://gma.caict.ac.cn/update/66/138">美国: FCC 禁止对涵盖清单涉及公司的通信设备进行授权| FCC认证更新</a></li>
<li><a href="https://cn-sec.com/archives/5120429.html">800万次请求后，我们发现了一个让SolarWinds... | CN-SEC 中文网</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#regulation`, `#networking`, `#supply-chain`, `#FCC`

---

<a id="item-13"></a>
## [China's daily token usage surges over 1000x, exceeding 140 trillion in March 2024](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

China's National Data Bureau revealed that daily token usage exceeded 140 trillion in March 2024, up from 100 billion at the start of 2024 and representing over 1000x growth in two years. This explosive growth reflects rapid AI industry commercialization and the formation of a new value system around token usage, pricing, and trading, driven by China's data market reforms. Tokens are the smallest units processed by AI models, with measurable, tradable characteristics. The 140 trillion milestone demonstrates China's accelerating AI adoption and data supply chain development.

telegram · zaihuapd · Mar 24, 07:22

**Background**: In AI systems, tokens represent segmented units of text that models process, ranging from single characters to full words. China's data element marketization reforms since 2020 have created institutional mechanisms for data trading and valuation, enabling token-based commercialization of AI services. Major platforms now bill per token, with output tokens typically costing 3-5× more than input tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them">What are tokens and how to count them? - OpenAI Help Center</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1059056026002649">The Marketization of Data Elements, Facilitation of Cross ...</a></li>
<li><a href="https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/">Tokens Explained: The Currency of Generative AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tokenization`, `#Data Market`, `#China Tech`, `#Commercialization`

---