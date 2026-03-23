---
layout: default
title: "Horizon Summary: 2026-03-23 (ZH)"
date: 2026-03-23
lang: zh
---

> From 29 items, 9 important content pieces were selected

---

1. [POSSE（自主发布、跨平台分发）模式获内容创作者关注](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 正式发布，引入生命周期新机制](#item-2) ⭐️ 7.0/10
3. [JavaScript 沙盒技术的对比分析](#item-3) ⭐️ 7.0/10
4. [基于 Pyodide 的 CRDT 版本控制交互式可视化工具](#item-4) ⭐️ 7.0/10
5. [将 Git 与 AI 编程代理结合以优化工作流](#item-5) ⭐️ 7.0/10
6. [MiniMax 升级 Coding Plan 支持全模态模型并实施高峰限流](#item-6) ⭐️ 7.0/10
7. [活鱼运输非法添加麻醉剂调查引发多地市场监管核查](#item-7) ⭐️ 7.0/10
8. [中国发现世界第二大轻稀土矿](#item-8) ⭐️ 7.0/10
9. [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [POSSE（自主发布、跨平台分发）模式获内容创作者关注](https://indieweb.org/POSSE) ⭐️ 7.0/10

POSSE（自主发布、跨平台分发）模式近期引发热议，该策略主张在个人网站首发内容后再同步至社交平台。社区讨论既认可其符合 IndieWeb 的自主精神，也指出了实际运营中的技术难题。 该模式通过让创作者保留内容所有权的同时触达广泛受众，动摇了封闭平台的垄断地位，与创作者经济中日益兴起的去中心化和数字主权运动相呼应。 实际操作常需手动跨平台分发且缺乏统一的评论系统，部分创作者选择完全关闭评论以避免讨论碎片化。联邦宇宙（Fediverse）集成被视为聚合回复的潜在解决方案。

hackernews · tosh · Mar 23, 08:29

**背景**: POSSE 是 IndieWeb 运动的核心原则，该运动主张将自建网站作为主要网络身份。与 PESOS（他处发布、自主站同步）模式不同，POSSE 要求内容首发于个人站点。IndieWeb 技术如 Webmention 可在保持所有权的同时实现站间互动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://indieweb.org/POSSE?ref=upstract.com">POSSE - IndieWeb</a></li>
<li><a href="https://en.wikipedia.org/wiki/IndieWeb">IndieWeb - Wikipedia</a></li>
<li><a href="https://www.insanityworks.org/randomtangent/2024/11/3/the-posse-approach-to-your-online-presence">The POSSE approach to your online presence — Insanity Works</a></li>

</ul>
</details>

**社区讨论**: 支持者强调内容自主权优势，批评者则指出需手动操作且流量增长有限。部分成员认为联邦宇宙集成能优化该模式，另一些人则接受平台内容易逝性并专注 RSS 分发。

**标签**: `#indieweb`, `#content-syndication`, `#blogging`, `#decentralization`, `#hugo`

---

<a id="item-2"></a>
## [Starlette 1.0 正式发布，引入生命周期新机制](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

作为 FastAPI 底层框架的 Starlette 1.0 经过多年开发后正式发布，采用了基于异步上下文管理器的新生命周期机制，取代了原有的 on_startup/on_shutdown 参数。 Starlette 作为 FastAPI 的底层框架支撑着众多现代 Python Web 应用，1.0 版本的发布标志着其进入稳定阶段，同时引入的异步资源管理新模式将影响未来 Web 开发。 最重要的变更是采用 Python 异步上下文管理器实现的全新生命周期系统，使启动/关闭处理更加清晰。该项目所有权也已转移给长期维护者 Marcelo Trylesinski。

rss · Simon Willison · Mar 22, 23:57

**背景**: Starlette 是用于构建异步 Web 服务的轻量级 ASGI 框架。ASGI(异步服务器网关接口)是 WSGI 的异步继任者，使 Python Web 框架能够高效处理并发连接。Python 最流行的 Web 框架之一 FastAPI 就是基于 Starlette 构建的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asgi.readthedocs.io/en/latest/specs/main.html">ASGI (Asynchronous Server Gateway Interface) Specification — ASGI ...</a></li>
<li><a href="https://www.starlette.io/">Introduction - Starlette</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/ starlette : The little ASGI framework that shines.</a></li>

</ul>
</details>

**标签**: `#Python`, `#Web Development`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-3"></a>
## [JavaScript 沙盒技术的对比分析](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison 对 JavaScript 沙盒技术进行了研究比较，评估了 isolated-vm、vm2、QuickJS 变体、ShadowRealm 和 Deno Workers 等技术，灵感来自于对 Node.js 工作线程的讨论。 这项研究对于需要安全执行不受信任 JavaScript 代码的开发者非常重要，提供了当前沙盒选项及其在 Node.js 和 Deno 等替代环境中的权衡的清晰比较。 研究强调了技术差异，如 isolated-vm 使用 V8 引擎隔离、vm2 的同一进程沙盒化、QuickJS-NG 的轻量级可嵌入引擎，以及新兴标准如 ShadowRealm。

rss · Simon Willison · Mar 22, 19:53

**背景**: JavaScript 沙盒技术对于安全运行不受信任的代码至关重要，防止访问敏感系统资源。技术范围包括进程隔离（isolated-vm）、同一进程上下文分离（vm2）和替代引擎（QuickJS）。新兴标准如 ShadowRealm 旨在提供原生浏览器沙盒能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>
<li><a href="https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/">Research: JavaScript Sandboxing Research</a></li>
<li><a href="https://dev.to/leapcell/a-deep-dive-into-javascript-sandboxing-97b">A Deep Dive into JavaScript Sandboxing - DEV Community</a></li>

</ul>
</details>

**标签**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-4"></a>
## [基于 Pyodide 的 CRDT 版本控制交互式可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 利用 Pyodide 和 Claude 的代码解释功能，为 Bram Cohen 基于 CRDT 的版本控制概念创建了一个交互式可视化工具。该工具通过基于浏览器的界面，使 Cohen 用 470 行 Python 代码实现的'Manyana'版本控制愿景更易于理解。 这展示了 CRDT 和 Pyodide 等新兴技术如何使复杂的分布式系统概念更易于理解，可能影响未来版本控制系统的设计。在当前行业探索替代传统 Git 工作流以实现实时协作的场景下尤为重要。 该可视化工具是通过将 Cohen 的 Python 代码（不含注释）输入 Claude 进行解释，然后使用 Pyodide 构建交互式 UI 而创建的。Pyodide 通过 WebAssembly 实现在浏览器中运行 Python，使得该工具无需本地安装即可立即使用。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（无冲突复制数据类型）是一种可以在多台计算机上复制并独立更新的数据结构，无需协调即可自动解决冲突。Pyodide 是通过 WebAssembly 在浏览器中运行的 Python 发行版，无需服务器端处理即可实现交互式 Python 应用。BitTorrent 的创建者 Bram Cohen 提出了'Manyana'作为传统版本控制系统的基于 CRDT 的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.loro.dev/">Loro – Reimagine state management with CRDTs – Loro</a></li>
<li><a href="https://conzit.com/post/envisioning-the-future-of-version-control-with-manyana">Envisioning the Future of Version Control with Manyana</a></li>
<li><a href="https://pyodide.com/what-is-pyodide/">What is Pyodide? - pyodide</a></li>

</ul>
</details>

**标签**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-5"></a>
## [将 Git 与 AI 编程代理结合以优化工作流](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything) ⭐️ 7.0/10

文章展示了 AI 编程代理如何通过自然语言指令充分利用 Git 的全部功能，包括仓库管理、提交记录和分支合并等操作。 这种集成使开发者能将复杂的 Git 操作交给 AI 代理处理，同时保持版本控制的最佳实践，有望加速开发周期并减少人为错误。 文章列举了编程代理可执行的具体 Git 命令（如 git init、git commit），并强调代理如何利用 git log 上下文理解项目的近期变更。

rss · Simon Willison · Mar 21, 22:08

**背景**: Git 是软件开发中广泛使用的分布式版本控制系统。AI 编程代理是能自主编写、测试和修改代码的智能系统。代理工程学（Agentic Engineering）指设计和协调这类 AI 代理完成复杂任务的学科。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.glideapps.com/blog/what-is-agentic-engineering">What is agentic engineering? How AI engineering has evolved ...</a></li>

</ul>
</details>

**标签**: `#Git`, `#AI Coding Agents`, `#Agentic Engineering`, `#Version Control`, `#Software Development`

---

<a id="item-6"></a>
## [MiniMax 升级 Coding Plan 支持全模态模型并实施高峰限流](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax 将其 Coding Plan 升级为 Token Plan，Plus 及以上套餐用户在保留原编程模型用量的基础上，额外获赠视频、语音、音乐、图像等多模态模型调用额度。同时宣布 MiniMax 2.7 开源权重将在约两周内发布。 此次升级显著扩展了 MiniMax 超越语言模型的能力，使开发者能够构建更具创意的应用。即将发布的开源版本可能会加速 AI 社区的采用和创新。 平台将在工作日下午高峰时间（15:00–17:30）实施动态限流，单周调用上限为原编程模型 5 小时用量的 10 倍。MiniMax 2.7 在 OpenClaw 基准测试上表现明显提升。

telegram · zaihuapd · Mar 23, 02:09

**背景**: 多模态模型可以处理和生成多种类型的数据（文本、图像、音频等），从而实现更复杂的 AI 应用。OpenClaw 是专门用于评估编码代理的基准测试系统，PinchBench 是其特定场景的评估框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.minimax.io/docs/token-plan/intro">Token Plan Overview - MiniMax API Docs</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding agents. Made with 🦀 by the humans at https://kilo.ai</a></li>
<li><a href="https://help.apiyi.com/en/openclaw-pinchbench-ai-agent-benchmark-guide-en.html">OpenClaw + PinchBench: Understand the 5 key dimensions of AI agent evaluation benchmarks - Apiyi.com Blog</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal-models`, `#open-source`, `#rate-limiting`, `#MiniMax`

---

<a id="item-7"></a>
## [活鱼运输非法添加麻醉剂调查引发多地市场监管核查](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=13441552639759293847) ⭐️ 7.0/10

《财经调查》暗访发现重庆、山东临沂、安徽宿州等地活鱼运输环节非法使用丁香酚、MS-222 等麻醉剂，多地市场监管部门已启动核查处置。 涉事麻醉剂未被批准用于食用活鱼，其使用剂量、残留限量及检测标准均存在空白，可能对全国消费者健康构成潜在威胁。 厂家称丁香酚在鱼体内完全代谢需 48 小时以上；MS-222 虽是 FDA 唯一批准的活鱼麻醉剂，但在国内商业运输中缺乏规范监管。

telegram · zaihuapd · Mar 23, 06:45

**背景**: 丁香酚最初作为牙科麻醉剂，20 世纪 80 年代因其镇静效果被转用于水产麻醉。MS-222（间氨基苯甲酸乙酯甲磺酸盐）是美国 FDA 批准的唯一活鱼运输麻醉剂，但需严格剂量控制。目前二者均未列入我国食用活鱼允许使用名单。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/ms-222/4872783">ms-222_百度百科</a></li>
<li><a href="https://blog.sina.com.cn/s/blog_e136a7da0101c7gw.html">丁香酚 适合长途运输、无水运输，提供长年免费技术咨询，20元/瓶_水产保活剂_新浪博客</a></li>

</ul>
</details>

**标签**: `#food-safety`, `#public-health`, `#regulatory-compliance`, `#investigative-journalism`, `#China`

---

<a id="item-8"></a>
## [中国发现世界第二大轻稀土矿](https://www.stdaily.com/web/gdxw/2026-03/23/content_491087.html) ⭐️ 7.0/10

中国自然资源部宣布在四川牦牛坪矿区探明 966.56 万吨稀土氧化物，使其成为仅次于内蒙古白云鄂博矿的世界第二大在产轻稀土矿。 这一发现巩固了中国在稀土供应链中的主导地位，稀土对新能源、航空航天和先进材料制造等高科技产业至关重要。 该矿床含有轻稀土元素(LREE)，通常比重稀土更丰富且成本更低，主要用于永磁体、催化剂和抛光粉。

telegram · zaihuapd · Mar 23, 13:59

**背景**: 轻稀土元素包括镧、铈、镨、钕和钐。中国目前占全球稀土产量的 95%以上，大多数矿床位于中国南部。稀土氧化物是电子产品、清洁能源技术和国防系统的重要组成部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element - Wikipedia</a></li>
<li><a href="https://www.bastillepost.com/global/article/5709722-china-reports-major-rare-earth-reserves-in-sichuan">China reports major rare earth reserves in Sichuan</a></li>

</ul>
</details>

**标签**: `#mining`, `#rare-earth`, `#china`, `#resources`, `#supply-chain`

---

<a id="item-9"></a>
## [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 7.0/10

OpenAI 在 3 月 6 日向英国竞争与市场管理局（CMA）提交的公开咨询意见中建议，Google 搜索选择页应纳入具备搜索功能的 AI 聊天机器人，使用户能在 Android 设备和 Chrome 等入口将其设为默认搜索服务。 该提议可能通过将 AI 聊天机器人认可为传统搜索引擎的合法替代方案来重塑搜索引擎竞争格局，既加速 AI 在日常信息检索中的普及，又确保新兴技术获得公平的市场准入。 OpenAI 指出 ChatGPT 的对话式/多模态能力与 Google 的 AI Overviews 相当，建议采用基于流行度的动态入选标准，并将选择页覆盖范围扩展至语音/视觉搜索等入口。

telegram · zaihuapd · Mar 23, 14:50

**背景**: Google 搜索选择页允许用户在 Android/Chrome 上选择默认搜索引擎。CMA 正在调查 Google 的搜索垄断问题。AI Overviews 是 Google 于 2023 年推出的 AI 生成搜索摘要功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/websearch/answer/464?hl=zh-Hans">将 Google 设为您的默认搜索引擎 - Google 搜索帮助</a></li>
<li><a href="https://readhub.cn/topic/8g8qdc3OBL5">英 国 反垄断监 管 机构将对谷歌展开调查，评估其搜索服务对 市 场 的影响</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Search Engines`, `#Regulation`, `#OpenAI`, `#Google`

---