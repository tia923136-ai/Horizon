---
layout: default
title: "Horizon Summary: 2026-03-23 (EN)"
date: 2026-03-23
lang: en
---

> From 31 items, 9 important content pieces were selected

---

1. [Optimization secrets of RollerCoaster Tycoon revealed](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 Released with Key ASGI Framework Updates](#item-2) ⭐️ 7.0/10
3. [PC Gamer's Web Performance Audit Reveals Extreme Bloat](#item-3) ⭐️ 7.0/10
4. [Comparative Study of JavaScript Sandboxing Techniques](#item-4) ⭐️ 7.0/10
5. [Interactive CRDT Version Control Visualizer Built with Claude AI](#item-5) ⭐️ 7.0/10
6. [Profiling Hacker News users via comment analysis with Algolia API and ChatGPT](#item-6) ⭐️ 7.0/10
7. [MiniMax upgrades Coding Plan to Token Plan, announces MiniMax 2.7 open-source weights release](#item-7) ⭐️ 7.0/10
8. [China's market regulator summons Alibaba, Tencent and 5 other platform companies](#item-8) ⭐️ 7.0/10
9. [China discovers world's second-largest light rare earth deposit](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Optimization secrets of RollerCoaster Tycoon revealed](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/) ⭐️ 7.0/10

A technical analysis reveals how RollerCoaster Tycoon achieved exceptional performance through assembly language optimization and power-of-two arithmetic tricks, as demonstrated by the OpenRCT2 reimplementation project. This showcases timeless optimization principles that remain relevant today, demonstrating how hardware-aware programming can overcome performance limitations even on 1990s-era computers. The game used bit-shifting operations instead of division for power-of-two calculations, and OpenRCT2 confirms these optimizations were preserved despite modern compilers theoretically being able to handle such conversions automatically.

hackernews · mariuz · Mar 22, 19:02

**Background**: RollerCoaster Tycoon was famously written almost entirely in x86 assembly language by Chris Sawyer, allowing extreme hardware optimization. The OpenRCT2 project is a complete reimplementation that maintains compatibility with original game assets while providing modern insights into its code structure.

<details><summary>References</summary>
<ul>
<li><a href="https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/">The gold standard of optimization: A look under the hood of RollerCoaster Tycoon – Larst Of Us</a></li>
<li><a href="https://www.pcgamesn.com/rollercoaster-tycoon/code-chris-sawyer">RollerCoaster Tycoon: the best-optimised game of all time?</a></li>
<li><a href="https://github.com/orgs/community/discussions/73498">What are the cons of coding a game engine in Assembly? · community · Discussion #73498</a></li>

</ul>
</details>

**Discussion**: Developers debate whether such low-level optimizations remain necessary today, with some noting modern compilers handle arithmetic tricks automatically while others emphasize cache efficiency still requires manual attention. Several commenters draw parallels to optimization techniques in Blizzard's early RTS games.

**Tags**: `#optimization`, `#game-development`, `#performance`, `#assembly`, `#history`

---

<a id="item-2"></a>
## [Starlette 1.0 Released with Key ASGI Framework Updates](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

Starlette 1.0, the foundational ASGI framework behind FastAPI, has been officially released with breaking changes including a new lifespan async context manager system for startup/shutdown events, replacing the previous on_startup/on_shutdown parameters. This release matters because Starlette powers FastAPI (one of Python's most popular web frameworks), and the 1.0 milestone signals API stability while introducing modern async patterns that could influence the broader Python web ecosystem. The new lifespan system uses Python's contextlib.asynccontextmanager for cleaner resource management. The framework maintains its Flask-like simplicity (single-file apps possible) while being async-native, making it particularly LLM-friendly for code generation.

rss · Simon Willison · Mar 22, 23:57

**Background**: Starlette is a lightweight ASGI framework for building async web services in Python. ASGI (Asynchronous Server Gateway Interface) is the async successor to WSGI, enabling Python web frameworks to handle concurrent connections efficiently. FastAPI builds upon Starlette to add API-specific features like data validation.

<details><summary>References</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://dev.to/ceb10n/understanding-fastapi-how-starlette-works-43i1">Understanding FastAPI: How Starlette works - DEV Community</a></li>
<li><a href="https://www.libhunt.com/compare-fastapi-vs-starlette">fastapi vs starlette - compare differences and reviews? | LibHunt</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Web Development`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-3"></a>
## [PC Gamer's Web Performance Audit Reveals Extreme Bloat](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

A technical audit of PC Gamer's website revealed extreme performance issues, with a single article consuming 37MB due to auto-playing video ads and inefficient resource loading. The analysis was conducted using Rodney, a custom web performance tool developed by Simon Willison. This case study highlights how ad-heavy designs and auto-playing media significantly degrade user experience and waste bandwidth, serving as a cautionary example for web publishers prioritizing monetization over performance. The audit found the page continued downloading hundreds of additional MBs in the background. Rodney tool provided detailed network waterfall analysis showing problematic resource loading patterns.

rss · Simon Willison · Mar 22, 22:49

**Background**: Web performance optimization focuses on improving page load times and reducing resource consumption. Tools like Rodney and WebPageTest help developers analyze and fix performance bottlenecks. Auto-playing video ads are known to significantly impact page weight and user experience.

<details><summary>References</summary>
<ul>
<li><a href="https://www.webpagetest.org/">webpagetest.org</a></li>
<li><a href="https://fatlabwebsupport.com/blog/preventing-common-web-design-mistakes-a-consultants-perspective/">Preventing Common Web Design Mistakes... | FatLab Web Support</a></li>

</ul>
</details>

**Tags**: `#web-performance`, `#web-bloat`, `#rodney`, `#audit`, `#optimization`

---

<a id="item-4"></a>
## [Comparative Study of JavaScript Sandboxing Techniques](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison published a detailed comparison of JavaScript sandboxing approaches, evaluating isolated-vm, vm2, QuickJS, ShadowRealm, and Deno Workers. The research was inspired by Aaron Harper's work on Node.js worker threads and expanded by Claude Code's analysis. This research is crucial for developers needing secure execution of untrusted JavaScript code, particularly in SaaS platforms, serverless environments, and plugin systems. The findings help navigate trade-offs between security, performance, and compatibility in modern JavaScript runtimes. The comparison highlights isolated-vm's true process isolation using V8 Isolates, vm2's transformation-based approach, and Deno Workers' built-in security model. Notably, isolated-vm requires Node.js 16+ with --no-node-snapshot flag for versions ≥20.

rss · Simon Willison · Mar 22, 19:53

**Background**: JavaScript sandboxing refers to techniques for safely executing untrusted code by restricting access to system resources. Common approaches include process isolation (isolated-vm), code transformation (vm2), lightweight interpreters (QuickJS), and runtime-enforced boundaries (Deno Workers). The TC39 ShadowRealm proposal aims to standardize sandboxing in browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/laverdet/isolated-vm">GitHub - laverdet/isolated-vm: Secure & isolated JS ... isolated-vm - npm research/javascript-sandboxing-research at main - GitHub The Anatomy of an Isolate Cloud | Deno Sandboxing JavaScript Code — Andrew Healey Riza: a modern alternative to isolated-vm and vm2 | Riza</a></li>
<li><a href="https://deno.com/blog/anatomy-isolate-cloud">The Anatomy of an Isolate Cloud | Deno</a></li>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>

</ul>
</details>

**Tags**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-5"></a>
## [Interactive CRDT Version Control Visualizer Built with Claude AI](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison created an interactive Merge State Visualizer tool that demonstrates Bram Cohen's CRDT-based version control concepts, using Claude AI to explain the Python code and Pyodide to build the browser-based interface. This tool makes advanced distributed version control concepts accessible through visualization, which could help developers better understand CRDTs' potential for conflict-free collaboration in version control systems. The visualization is based on Cohen's 470-line Python implementation of Manyana version control concepts, with Claude AI providing the explanation and Pyodide enabling browser-based Python execution.

rss · Simon Willison · Mar 22, 18:57

**Background**: CRDTs (Conflict-Free Replicated Data Types) are data structures that can be replicated across multiple computers and updated independently without coordination, while guaranteeing eventual consistency. Pyodide is a Python distribution that runs in the browser via WebAssembly, enabling interactive Python applications without server-side processing. Bram Cohen, creator of BitTorrent, has proposed using CRDTs for next-generation version control systems to enable seamless distributed collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>
<li><a href="https://shambhavishandilya.medium.com/understanding-real-time-collaboration-with-crdts-e764eb65024e">Understanding real-time collaboration with CRDTs | by Shambhavi Shandilya | Medium</a></li>

</ul>
</details>

**Tags**: `#vcs`, `#crdt`, `#pyodide`, `#version-control`, `#ai`

---

<a id="item-6"></a>
## [Profiling Hacker News users via comment analysis with Algolia API and ChatGPT](https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything) ⭐️ 7.0/10

Simon Willison demonstrated how to profile Hacker News users by fetching their last 1,000 comments via Algolia's API and analyzing them with ChatGPT/Claude, creating surprisingly accurate user profiles. This technique reveals how publicly available comment data can be leveraged for personal profiling, raising important questions about online privacy and the power of LLMs in analyzing digital footprints. The method uses Algolia's open CORS API to fetch comment history and processes it with Claude Opus 4.6, capable of identifying professional identities, technical interests, and even working habits from comment patterns.

rss · Simon Willison · Mar 21, 23:59

**Background**: The Algolia Hacker News API provides programmatic access to HN comments with author tagging. CORS headers allow cross-origin requests from any webpage. Modern LLMs like ChatGPT can effectively analyze large text corpora to extract patterns and insights about individuals.

<details><summary>References</summary>
<ul>
<li><a href="https://hn.algolia.com/api">HN Search API | HN Search powered by Algolia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS">Cross-Origin Resource Sharing ( CORS ) - HTTP | MDN</a></li>
<li><a href="https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt">Data analysis with ChatGPT - OpenAI Help Center</a></li>

</ul>
</details>

**Tags**: `#data-analysis`, `#hacker-news`, `#api`, `#chatgpt`, `#privacy`

---

<a id="item-7"></a>
## [MiniMax upgrades Coding Plan to Token Plan, announces MiniMax 2.7 open-source weights release](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax has upgraded its Coding Plan to Token Plan, offering Plus and higher-tier users additional quotas for multimodal models including video, audio, music, and images. The company also announced that MiniMax 2.7 open-source weights will be released in approximately two weeks. This upgrade significantly expands MiniMax's capabilities by supporting multimodal models, making it more versatile for diverse AI applications. The upcoming open-source release of MiniMax 2.7 weights will enable broader community access and potential improvements to the model. The platform will implement dynamic rate limiting during peak hours (3:00-5:30 PM on weekdays), with a weekly call limit set at 10 times the original programming model's 5-hour usage. MiniMax 2.7 has shown significant improvements in OpenClaw benchmark tests.

telegram · zaihuapd · Mar 23, 02:09

**Background**: MiniMax is an AI company specializing in efficient models for coding and agentic workflows. The Token Plan provides access to various MiniMax models, while the OpenClaw benchmark evaluates how well AI models perform as agents in real-world tasks like scheduling and coding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.verdent.ai/guides/minimax-m2-5-pricing">MiniMax M2.5 Pricing (2026): Token Costs, Coding Plan vs ...</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking ...</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M2">MiniMaxAI/MiniMax-M2 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#multimodal-models`, `#open-source`, `#MiniMax`, `#machine-learning`

---

<a id="item-8"></a>
## [China's market regulator summons Alibaba, Tencent and 5 other platform companies](https://t.me/zaihuapd/40458) ⭐️ 7.0/10

On February 13, 2026, China's State Administration for Market Regulation summoned seven major platform companies including Alibaba, ByteDance (TikTok's parent), Baidu, Tencent, JD.com, Meituan, and Taobao Flash Sales to enforce compliance with competition and consumer protection laws. This regulatory action signals China's continued crackdown on anti-competitive practices in the tech sector, aiming to create a fairer market environment and protect consumer rights in the platform economy. The regulator specifically demanded companies eliminate 'involution-style' competition (excessive internal competition that leads to market distortion) and standardize promotional activities in compliance with multiple laws including the Anti-Unfair Competition Law and E-Commerce Law.

telegram · zaihuapd · Mar 23, 09:40

**Background**: China has been strengthening regulation of its tech giants since 2020, with the Anti-Unfair Competition Law revised in 2025 to address new forms of digital market manipulation. 'Involution-style competition' refers to destructive business practices where companies engage in excessive internal competition that ultimately harms market health and innovation.

<details><summary>References</summary>
<ul>
<li><a href="https://scjgj.sh.gov.cn/1582/20251014/2c984a7299dbc4280199e13cb8d71716.html">《中华人民共和国反不正当竞争法（2025年修订）》全文</a></li>
<li><a href="https://baike.baidu.com/item/内卷式竞争/65316511">内卷式竞争_百度百科</a></li>
<li><a href="http://www.csrc.gov.cn/beijing/c105536/c7431842/content.shtml">中华人民共和国反不正当竞争法 (2019修正)_北京监管局</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#tech-giants`, `#china`, `#market-competition`, `#compliance`

---

<a id="item-9"></a>
## [China discovers world's second-largest light rare earth deposit](https://www.stdaily.com/web/gdxw/2026-03/23/content_491087.html) ⭐️ 7.0/10

China's Ministry of Natural Resources announced the discovery of 9.6656 million tons of rare earth oxides at the Maoniuping mining area in Sichuan, making it the world's second-largest active light rare earth deposit after Bayan Obo in Inner Mongolia. This discovery strengthens China's rare earth resource security and supports strategic emerging industries like new energy, advanced materials, and aerospace that depend on these critical minerals. The deposit primarily contains light rare earth elements like lanthanum, cerium, and neodymium, which are crucial for permanent magnets, power batteries, and wind turbines. It ranks second only to Inner Mongolia's Bayan Obo deposit in scale.

telegram · zaihuapd · Mar 23, 13:59

**Background**: Light rare earth elements are essential for high-tech and green energy technologies. China dominates global rare earth production, with Bayan Obo being the world's largest light rare earth deposit. These elements are used in electronics, lasers, magnets, and industrial applications.

<details><summary>References</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/5930752">Discussion on the Rare earth resources and its... | IEEE Xplore</a></li>
<li><a href="https://min.news/en/news/9beb66a52d750bb059ee1e548e5840f1.html">President Tokayev presented a great gift by finalizing a rare earth ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#rare_earth`, `#mining`, `#china`, `#resources`, `#energy`

---