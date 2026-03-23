---
layout: default
title: "Horizon Summary: 2026-03-23 (EN)"
date: 2026-03-23
lang: en
---

> From 29 items, 9 important content pieces were selected

---

1. [POSSE Approach Gains Traction for Content Ownership](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 released with lifespan changes](#item-2) ⭐️ 7.0/10
3. [Comparative Analysis of JavaScript Sandboxing Techniques](#item-3) ⭐️ 7.0/10
4. [Interactive CRDT Version Control Visualizer Built with Pyodide](#item-4) ⭐️ 7.0/10
5. [Using Git with AI coding agents for enhanced workflows](#item-5) ⭐️ 7.0/10
6. [MiniMax upgrades Coding Plan to support multimodal models and implements peak rate limiting](#item-6) ⭐️ 7.0/10
7. [Regulatory checks launched after investigation reveals illegal anesthetics in live fish transport](#item-7) ⭐️ 7.0/10
8. [China discovers world's second-largest light rare earth deposit](#item-8) ⭐️ 7.0/10
9. [OpenAI proposes UK include AI chatbots in Google search selection](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [POSSE Approach Gains Traction for Content Ownership](https://indieweb.org/POSSE) ⭐️ 7.0/10

The POSSE (Publish on your Own Site, Syndicate Elsewhere) approach is being actively discussed as a strategy for maintaining content ownership while distributing to social platforms. Recent community debates highlight both its philosophical alignment with IndieWeb principles and practical challenges in implementation. This challenges the dominance of walled garden platforms by empowering creators to retain control over their content while still reaching broad audiences. It aligns with growing movements toward decentralization and digital ownership in the creator economy. Implementation often requires manual cross-posting and lacks unified comment systems, with some creators opting to disable comments entirely to avoid fragmentation. Fediverse integration is seen as a potential solution for reply aggregation.

hackernews · tosh · Mar 23, 08:29

**Background**: POSSE is a core principle of the IndieWeb movement, which advocates for self-hosted personal websites as primary online identities. The approach contrasts with PESOS (Publish Elsewhere, Syndicate to your Own Site), where content originates on third-party platforms. IndieWeb technologies like Webmention enable cross-site interactions while maintaining ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://indieweb.org/POSSE?ref=upstract.com">POSSE - IndieWeb</a></li>
<li><a href="https://en.wikipedia.org/wiki/IndieWeb">IndieWeb - Wikipedia</a></li>
<li><a href="https://www.insanityworks.org/randomtangent/2024/11/3/the-posse-approach-to-your-online-presence">The POSSE approach to your online presence — Insanity Works</a></li>

</ul>
</details>

**Discussion**: Supporters emphasize content ownership benefits, while critics note the manual effort required and limited traffic gains. Some suggest Fediverse integration improves the model, whereas others accept platform ephemerality and focus on RSS syndication.

**Tags**: `#indieweb`, `#content-syndication`, `#blogging`, `#decentralization`, `#hugo`

---

<a id="item-2"></a>
## [Starlette 1.0 released with lifespan changes](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

Starlette 1.0, the foundational ASGI framework used by FastAPI, has been released after years of development, featuring a new lifespan mechanism using async context managers instead of the previous on_startup/on_shutdown parameters. This matters because Starlette powers many modern Python web applications through FastAPI, and the 1.0 release signals stability while introducing improved patterns for async resource management that will influence future web development. The most significant change is the lifespan system which uses Python's async context managers for cleaner startup/shutdown handling. The release also marks a project ownership transfer to Marcelo Trylesinski after years of maintenance contributions.

rss · Simon Willison · Mar 22, 23:57

**Background**: Starlette is a lightweight ASGI framework for building async web services in Python. ASGI (Asynchronous Server Gateway Interface) is the async successor to WSGI, enabling Python web frameworks to handle concurrent connections efficiently. FastAPI, one of Python's most popular web frameworks, is built on top of Starlette.

<details><summary>References</summary>
<ul>
<li><a href="https://asgi.readthedocs.io/en/latest/specs/main.html">ASGI (Asynchronous Server Gateway Interface) Specification — ASGI ...</a></li>
<li><a href="https://www.starlette.io/">Introduction - Starlette</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/ starlette : The little ASGI framework that shines.</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Web Development`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-3"></a>
## [Comparative Analysis of JavaScript Sandboxing Techniques](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison conducted a research comparison of JavaScript sandboxing techniques, evaluating isolated-vm, vm2, QuickJS variants, ShadowRealm, and Deno Workers, inspired by a discussion on Node.js worker threads. This research is significant for developers needing to securely execute untrusted JavaScript code, providing a clear comparison of current sandboxing options and their trade-offs in Node.js and alternative environments like Deno. The research highlights technical differences such as isolated-vm's use of V8 engine isolation, vm2's same-process sandboxing, and QuickJS-NG's lightweight embeddable engine, along with emerging standards like ShadowRealm.

rss · Simon Willison · Mar 22, 19:53

**Background**: JavaScript sandboxing is crucial for safely running untrusted code, preventing access to sensitive system resources. Techniques range from process isolation (isolated-vm) to same-process context separation (vm2) and alternative engines (QuickJS). Emerging standards like ShadowRealm aim to provide native browser sandboxing capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>
<li><a href="https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/">Research: JavaScript Sandboxing Research</a></li>
<li><a href="https://dev.to/leapcell/a-deep-dive-into-javascript-sandboxing-97b">A Deep Dive into JavaScript Sandboxing - DEV Community</a></li>

</ul>
</details>

**Tags**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-4"></a>
## [Interactive CRDT Version Control Visualizer Built with Pyodide](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison created an interactive visualization tool for Bram Cohen's CRDT-based version control concepts using Pyodide and Claude's code explanation capabilities. The tool makes Cohen's 470-line Python implementation of his 'Manyana' version control vision more accessible through a browser-based interface. This demonstrates how emerging technologies like CRDTs and Pyodide can make complex distributed systems concepts more accessible, potentially influencing future version control system designs. It's particularly relevant as the industry explores alternatives to traditional Git-based workflows for real-time collaboration scenarios. The visualization was created by feeding Cohen's Python code (minus comments) into Claude for explanation, then using Pyodide to build the interactive UI. Pyodide enables running Python in the browser via WebAssembly, making the tool immediately accessible without local installation.

rss · Simon Willison · Mar 22, 18:57

**Background**: CRDTs (Conflict-Free Replicated Data Types) are data structures that can be replicated across multiple computers and updated independently without coordination, resolving conflicts automatically. Pyodide is a Python distribution that runs in the browser via WebAssembly, enabling interactive Python applications without server-side processing. Bram Cohen, creator of BitTorrent, has proposed 'Manyana' as a CRDT-based alternative to traditional version control systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.loro.dev/">Loro – Reimagine state management with CRDTs – Loro</a></li>
<li><a href="https://conzit.com/post/envisioning-the-future-of-version-control-with-manyana">Envisioning the Future of Version Control with Manyana</a></li>
<li><a href="https://pyodide.com/what-is-pyodide/">What is Pyodide? - pyodide</a></li>

</ul>
</details>

**Tags**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-5"></a>
## [Using Git with AI coding agents for enhanced workflows](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything) ⭐️ 7.0/10

The article demonstrates how AI coding agents can leverage Git's full capabilities, including repository management, commit tracking, and branch merging, through natural language prompts. This integration allows developers to offload complex Git operations to AI agents while maintaining version control best practices, potentially accelerating development cycles and reducing human error. The article provides specific Git commands (like git init, git commit) that coding agents can execute, and highlights how agents can use git log to contextually understand recent changes in a project.

rss · Simon Willison · Mar 21, 22:08

**Background**: Git is a distributed version control system widely used in software development. AI coding agents are autonomous systems that can write, test and modify code with minimal human intervention. Agentic engineering refers to the discipline of designing and coordinating such AI agents to complete complex tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>

</ul>
</details>

**Tags**: `#Git`, `#AI Coding Agents`, `#Agentic Engineering`, `#Version Control`, `#Software Development`

---

<a id="item-6"></a>
## [MiniMax upgrades Coding Plan to support multimodal models and implements peak rate limiting](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax has upgraded its Coding Plan to Token Plan, providing Plus and higher-tier users with additional multimodal model call quotas for video, audio, music, and images while maintaining original programming model usage. The company also announced that MiniMax 2.7 open-source weights will be released in about two weeks. This upgrade significantly expands MiniMax's capabilities beyond language models, enabling developers to build more creative applications. The upcoming open-source release could accelerate adoption and innovation in the AI community. Peak-hour rate limiting (15:00-17:30 on weekdays) will be implemented with a weekly cap of 10 times the original programming model's 5-hour usage. The MiniMax 2.7 model showed significant improvement in OpenClaw benchmark tests.

telegram · zaihuapd · Mar 23, 02:09

**Background**: Multimodal models can process and generate multiple types of data (text, images, audio, etc.), enabling more complex AI applications. OpenClaw is a specialized benchmarking system for evaluating coding agents, with PinchBench being its scenario-specific evaluation framework.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.minimax.io/docs/token-plan/intro">Token Plan Overview - MiniMax API Docs</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding agents. Made with 🦀 by the humans at https://kilo.ai</a></li>
<li><a href="https://help.apiyi.com/en/openclaw-pinchbench-ai-agent-benchmark-guide-en.html">OpenClaw + PinchBench: Understand the 5 key dimensions of AI agent evaluation benchmarks - Apiyi.com Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal-models`, `#open-source`, `#rate-limiting`, `#MiniMax`

---

<a id="item-7"></a>
## [Regulatory checks launched after investigation reveals illegal anesthetics in live fish transport](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=13441552639759293847) ⭐️ 7.0/10

An undercover investigation by Caijing Survey exposed the illegal use of anesthetics like eugenol and MS-222 in live fish transportation across Chongqing, Shandong Linyi, and Anhui Suzhou, prompting regulatory checks in multiple regions. This poses significant public health risks as these substances are unapproved for aquatic food products, with unknown dosage limits and residue effects, potentially affecting consumer safety nationwide. Eugenol takes at least 48 hours to fully metabolize in fish; MS-222 is the only FDA-approved fish anesthetic but its commercial use in China lacks proper oversight.

telegram · zaihuapd · Mar 23, 06:45

**Background**: Eugenol, originally a dental anesthetic, was repurposed for aquaculture in the 1980s due to its sedative effects. MS-222 (methanesulfonate) is water-soluble and FDA-approved for fish transport but requires strict dosage control. Neither substance is currently listed as permitted for food fish in China.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/ms-222/4872783">ms-222_百度百科</a></li>
<li><a href="https://blog.sina.com.cn/s/blog_e136a7da0101c7gw.html">丁香酚 适合长途运输、无水运输，提供长年免费技术咨询，20元/瓶_水产保活剂_新浪博客</a></li>

</ul>
</details>

**Tags**: `#food-safety`, `#public-health`, `#regulatory-compliance`, `#investigative-journalism`, `#China`

---

<a id="item-8"></a>
## [China discovers world's second-largest light rare earth deposit](https://www.stdaily.com/web/gdxw/2026-03/23/content_491087.html) ⭐️ 7.0/10

China's Ministry of Natural Resources announced the discovery of 9.6656 million tons of rare earth oxides in the Maoniuping mining area in Sichuan, making it the world's second-largest producing light rare earth deposit after Bayan Obo in Inner Mongolia. This discovery strengthens China's dominance in rare earth supply chains, which are critical for high-tech industries like renewable energy, aerospace, and advanced materials manufacturing. The deposit contains light rare earth elements (LREE), which are generally more abundant and less expensive than heavy rare earths, and are primarily used in permanent magnets, catalysts, and polishing powders.

telegram · zaihuapd · Mar 23, 13:59

**Background**: Light rare earth elements include lanthanum, cerium, praseodymium, neodymium, and samarium. China currently dominates over 95% of global rare earth production, with most deposits located in southern China. Rare earth oxides are essential components in electronics, clean energy technologies, and defense systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element - Wikipedia</a></li>
<li><a href="https://www.bastillepost.com/global/article/5709722-china-reports-major-rare-earth-reserves-in-sichuan">China reports major rare earth reserves in Sichuan</a></li>

</ul>
</details>

**Tags**: `#mining`, `#rare-earth`, `#china`, `#resources`, `#supply-chain`

---

<a id="item-9"></a>
## [OpenAI proposes UK include AI chatbots in Google search selection](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 7.0/10

On March 6, OpenAI submitted a proposal to the UK Competition and Markets Authority (CMA) suggesting that AI chatbots like ChatGPT should be included in Google's search selection page, allowing users to set them as default search services on Android and Chrome. This could reshape search engine competition by recognizing AI chatbots as legitimate alternatives to traditional search engines, potentially accelerating AI adoption in everyday information retrieval while ensuring fair market access for emerging technologies. OpenAI argues ChatGPT's conversational/multimodal capabilities parallel Google's AI Overviews, and proposes dynamic popularity-based inclusion criteria. The suggestion also extends to voice/visual search interfaces.

telegram · zaihuapd · Mar 23, 14:50

**Background**: Google's search selection page lets users choose default search engines on Android/Chrome. The CMA is currently investigating Google's search dominance. AI Overviews is Google's AI-generated search summary feature launched in 2023.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/websearch/answer/464?hl=zh-Hans">将 Google 设为您的默认搜索引擎 - Google 搜索帮助</a></li>
<li><a href="https://readhub.cn/topic/8g8qdc3OBL5">英 国 反垄断监 管 机构将对谷歌展开调查，评估其搜索服务对 市 场 的影响</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Search Engines`, `#Regulation`, `#OpenAI`, `#Google`

---