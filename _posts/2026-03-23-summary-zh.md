---
layout: default
title: "Horizon Summary: 2026-03-23 (ZH)"
date: 2026-03-23
lang: zh
---

> From 31 items, 9 important content pieces were selected

---

1. [《过山车大亨》的优化秘诀揭秘](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 发布：Python ASGI 框架重大更新](#item-2) ⭐️ 7.0/10
3. [PC Gamer 网站性能审计揭露严重资源臃肿问题](#item-3) ⭐️ 7.0/10
4. [JavaScript 沙箱技术对比研究](#item-4) ⭐️ 7.0/10
5. [基于 Claude AI 构建的 CRDT 版本控制交互式可视化工具](#item-5) ⭐️ 7.0/10
6. [通过 Algolia API 和 ChatGPT 分析 Hacker News 用户评论进行用户画像](#item-6) ⭐️ 7.0/10
7. [MiniMax 升级 Coding Plan 至 Token Plan，宣布即将开源 MiniMax 2.7 权重](#item-7) ⭐️ 7.0/10
8. [市场监管总局约谈阿里巴巴、腾讯等 7 家平台企业](#item-8) ⭐️ 7.0/10
9. [中国发现世界第二大轻稀土矿](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [《过山车大亨》的优化秘诀揭秘](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/) ⭐️ 7.0/10

技术分析揭示了《过山车大亨》如何通过汇编语言优化和二次方算术技巧实现卓越性能，OpenRCT2 重制项目对此进行了验证。 这展示了至今仍适用的经典优化原则，证明了即使在 1990 年代的计算机上，硬件感知编程也能突破性能限制。 游戏使用位移运算而非除法进行二次方计算，OpenRCT2 证实这些优化得以保留，尽管现代编译器理论上可以自动处理此类转换。

hackernews · mariuz · Mar 22, 19:02

**背景**: 《过山车大亨》因几乎完全由 Chris Sawyer 用 x86 汇编语言编写而闻名，实现了极致的硬件优化。OpenRCT2 项目是完全重制版，在保持与原版游戏资源兼容的同时，为代码结构提供了现代视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/">The gold standard of optimization: A look under the hood of RollerCoaster Tycoon – Larst Of Us</a></li>
<li><a href="https://www.pcgamesn.com/rollercoaster-tycoon/code-chris-sawyer">RollerCoaster Tycoon: the best-optimised game of all time?</a></li>
<li><a href="https://github.com/orgs/community/discussions/73498">What are the cons of coding a game engine in Assembly? · community · Discussion #73498</a></li>

</ul>
</details>

**社区讨论**: 开发者们争论这种底层优化在今天是否仍有必要，一些人指出现代编译器能自动处理算术技巧，而另一些人强调缓存效率仍需要人工关注。多位评论者将其与暴雪早期 RTS 游戏的优化技术相提并论。

**标签**: `#optimization`, `#game-development`, `#performance`, `#assembly`, `#history`

---

<a id="item-2"></a>
## [Starlette 1.0 发布：Python ASGI 框架重大更新](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

FastAPI 底层框架 Starlette 1.0 正式发布，引入了重大变更：采用基于异步上下文管理器的 lifespan 机制替代原有的 on_startup/on_shutdown 参数来处理启动/关闭事件。 此次发布意义重大，因为 Starlette 是 FastAPI（Python 最受欢迎的 web 框架之一）的底层框架。1.0 版本标志着 API 稳定性，同时引入了现代异步模式，可能影响整个 Python web 生态系统。 新的 lifespan 系统使用 Python 的 contextlib.asynccontextmanager 实现更清晰的资源管理。该框架保持了类 Flask 的简洁性（支持单文件应用）同时具备原生异步特性，使其特别适合 LLM 进行代码生成。

rss · Simon Willison · Mar 22, 23:57

**背景**: Starlette 是用于构建 Python 异步 web 服务的轻量级 ASGI 框架。ASGI（异步服务器网关接口）是 WSGI 的异步继任者，使 Python web 框架能高效处理并发连接。FastAPI 基于 Starlette 构建，添加了数据验证等 API 专用功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://dev.to/ceb10n/understanding-fastapi-how-starlette-works-43i1">Understanding FastAPI: How Starlette works - DEV Community</a></li>
<li><a href="https://www.libhunt.com/compare-fastapi-vs-starlette">fastapi vs starlette - compare differences and reviews? | LibHunt</a></li>

</ul>
</details>

**标签**: `#Python`, `#Web Development`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-3"></a>
## [PC Gamer 网站性能审计揭露严重资源臃肿问题](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

对 PC Gamer 网站的技术审计揭露了严重的性能问题，由于自动播放视频广告和低效资源加载，单篇文章消耗了 37MB 流量。该分析使用了 Simon Willison 开发的定制网页性能工具 Rodney。 该案例研究展示了广告密集型设计和自动播放媒体如何显著降低用户体验并浪费带宽，为那些优先考虑盈利而非性能的网页发布者敲响了警钟。 审计发现该页面在后台持续下载了数百 MB 额外数据。Rodney 工具提供了详细的网络瀑布流分析，显示了有问题的资源加载模式。

rss · Simon Willison · Mar 22, 22:49

**背景**: 网页性能优化专注于提高页面加载速度和减少资源消耗。像 Rodney 和 WebPageTest 这样的工具帮助开发者分析和修复性能瓶颈。众所周知，自动播放视频广告会显著增加页面重量并影响用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.webpagetest.org/">webpagetest.org</a></li>
<li><a href="https://fatlabwebsupport.com/blog/preventing-common-web-design-mistakes-a-consultants-perspective/">Preventing Common Web Design Mistakes... | FatLab Web Support</a></li>

</ul>
</details>

**标签**: `#web-performance`, `#web-bloat`, `#rodney`, `#audit`, `#optimization`

---

<a id="item-4"></a>
## [JavaScript 沙箱技术对比研究](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一份详细的 JavaScript 沙箱技术对比报告，评估了 isolated-vm、vm2、QuickJS、ShadowRealm 和 Deno Workers 等多种方案。这项研究受 Aaron Harper 关于 Node.js 工作线程的启发，并由 Claude Code 扩展完成。 该研究对需要安全执行不可信 JavaScript 代码的开发者至关重要，特别是在 SaaS 平台、无服务器环境和插件系统中。研究结果有助于权衡现代 JavaScript 运行时在安全性、性能和兼容性方面的取舍。 对比突显了 isolated-vm 基于 V8 Isolates 的进程级隔离、vm2 的代码转换方案以及 Deno Workers 的内置安全模型。值得注意的是，isolated-vm 需要 Node.js 16+环境，且 20 以上版本需使用--no-node-snapshot 参数。

rss · Simon Willison · Mar 22, 19:53

**背景**: JavaScript 沙箱技术指通过限制系统资源访问来安全执行不可信代码的方法，常见方案包括进程隔离（isolated-vm）、代码转换（vm2）、轻量级解释器（QuickJS）和运行时强制边界（Deno Workers）。TC39 的 ShadowRealm 提案旨在标准化浏览器端的沙箱实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/laverdet/isolated-vm">GitHub - laverdet/isolated-vm: Secure & isolated JS ... isolated-vm - npm research/javascript-sandboxing-research at main - GitHub The Anatomy of an Isolate Cloud | Deno Sandboxing JavaScript Code — Andrew Healey Riza: a modern alternative to isolated-vm and vm2 | Riza</a></li>
<li><a href="https://deno.com/blog/anatomy-isolate-cloud">The Anatomy of an Isolate Cloud | Deno</a></li>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>

</ul>
</details>

**标签**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-5"></a>
## [基于 Claude AI 构建的 CRDT 版本控制交互式可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一个交互式的合并状态可视化工具，展示了 Bram Cohen 基于 CRDT 的版本控制概念，该工具使用 Claude AI 解释 Python 代码，并通过 Pyodide 构建了基于浏览器的界面。 该工具通过可视化使先进的分布式版本控制概念更易理解，有助于开发者更好地认识 CRDT 在版本控制系统中实现无冲突协作的潜力。 该可视化基于 Cohen 用 470 行 Python 实现的 Manyana 版本控制概念，由 Claude AI 提供解释说明，并通过 Pyodide 实现了基于浏览器的 Python 运行环境。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（无冲突复制数据类型）是可以在多台计算机上复制并独立更新的数据结构，无需协调即可保证最终一致性。Pyodide 是通过 WebAssembly 在浏览器中运行的 Python 发行版，无需服务器端处理即可实现交互式 Python 应用。BitTorrent 的创建者 Bram Cohen 提出将 CRDT 用于下一代版本控制系统，以实现无缝的分布式协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type">Conflict-free replicated data type - Wikipedia</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>
<li><a href="https://shambhavishandilya.medium.com/understanding-real-time-collaboration-with-crdts-e764eb65024e">Understanding real-time collaboration with CRDTs | by Shambhavi Shandilya | Medium</a></li>

</ul>
</details>

**标签**: `#vcs`, `#crdt`, `#pyodide`, `#version-control`, `#ai`

---

<a id="item-6"></a>
## [通过 Algolia API 和 ChatGPT 分析 Hacker News 用户评论进行用户画像](https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything) ⭐️ 7.0/10

Simon Willison 展示了如何通过 Algolia API 获取用户最近的 1000 条评论，并使用 ChatGPT/Claude 进行分析，从而创建出惊人准确的 Hacker News 用户画像。 这项技术揭示了如何利用公开可用的评论数据进行个人画像分析，引发了关于网络隐私和 LLM 分析数字足迹能力的重要问题。 该方法使用 Algolia 的开放 CORS API 获取评论历史，并通过 Claude Opus 4.6 进行处理，能够从评论模式中识别出专业身份、技术兴趣甚至工作习惯。

rss · Simon Willison · Mar 21, 23:59

**背景**: Algolia Hacker News API 提供了对 HN 评论的程序化访问，并带有作者标记。CORS 头允许从任何网页进行跨域请求。像 ChatGPT 这样的现代 LLM 可以有效地分析大量文本语料，提取关于个人的模式和见解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hn.algolia.com/api">HN Search API | HN Search powered by Algolia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS">Cross-Origin Resource Sharing ( CORS ) - HTTP | MDN</a></li>
<li><a href="https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt">Data analysis with ChatGPT - OpenAI Help Center</a></li>

</ul>
</details>

**标签**: `#data-analysis`, `#hacker-news`, `#api`, `#chatgpt`, `#privacy`

---

<a id="item-7"></a>
## [MiniMax 升级 Coding Plan 至 Token Plan，宣布即将开源 MiniMax 2.7 权重](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax 将其 Coding Plan 升级为 Token Plan，Plus 及以上套餐用户将额外获得视频、语音、音乐、图像等多模态模型的调用额度。同时宣布 MiniMax 2.7 开源权重将在约两周内发布。 此次升级通过支持多模态模型显著扩展了 MiniMax 的能力，使其适用于更广泛的 AI 应用场景。即将开源的 MiniMax 2.7 权重将使更多开发者能够使用和改进该模型。 平台将在工作日下午高峰时间（15:00-17:30）实施动态限流，单周调用上限为原编程模型 5 小时用量的 10 倍。MiniMax 2.7 在 OpenClaw 基准测试中表现有明显提升。

telegram · zaihuapd · Mar 23, 02:09

**背景**: MiniMax 是一家专注于为编程和智能体工作流开发高效 AI 模型的公司。Token Plan 提供了多种 MiniMax 模型的访问权限，而 OpenClaw 基准测试则评估 AI 模型在日程安排、编码等实际任务中作为智能体的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.verdent.ai/guides/minimax-m2-5-pricing">MiniMax M2.5 Pricing (2026): Token Costs, Coding Plan vs ...</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking ...</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-M2">MiniMaxAI/MiniMax-M2 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal-models`, `#open-source`, `#MiniMax`, `#machine-learning`

---

<a id="item-8"></a>
## [市场监管总局约谈阿里巴巴、腾讯等 7 家平台企业](https://t.me/zaihuapd/40458) ⭐️ 7.0/10

2026 年 2 月 13 日，市场监管总局约谈阿里巴巴、抖音（字节跳动旗下）、百度、腾讯、京东、美团及淘宝闪购等 7 家平台企业，要求其严格遵守《反不正当竞争法》等法律法规。 此次约谈表明中国持续打击科技行业不正当竞争行为，旨在为平台经济创造更公平的市场环境并保护消费者权益。 总局特别要求企业杜绝'内卷式'竞争（导致市场扭曲的过度内部竞争），并按照《反不正当竞争法》《电子商务法》等规范促销行为。

telegram · zaihuapd · Mar 23, 09:40

**背景**: 自 2020 年以来中国持续加强科技巨头监管，《反不正当竞争法》于 2025 年修订以应对新型数字市场操纵行为。'内卷式竞争'指企业间过度内部竞争最终损害市场健康与创新的破坏性商业行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scjgj.sh.gov.cn/1582/20251014/2c984a7299dbc4280199e13cb8d71716.html">《中华人民共和国反不正当竞争法（2025年修订）》全文</a></li>
<li><a href="https://baike.baidu.com/item/内卷式竞争/65316511">内卷式竞争_百度百科</a></li>
<li><a href="http://www.csrc.gov.cn/beijing/c105536/c7431842/content.shtml">中华人民共和国反不正当竞争法 (2019修正)_北京监管局</a></li>

</ul>
</details>

**标签**: `#regulation`, `#tech-giants`, `#china`, `#market-competition`, `#compliance`

---

<a id="item-9"></a>
## [中国发现世界第二大轻稀土矿](https://www.stdaily.com/web/gdxw/2026-03/23/content_491087.html) ⭐️ 7.0/10

中国自然资源部公布在四川冕宁牦牛坪矿区探明 966.56 万吨稀土氧化物，使其成为仅次于内蒙古白云鄂博矿的世界第二大在产轻稀土矿。 这一发现增强了中国轻稀土资源保障能力，对新能源、新材料、航空航天等依赖稀土的战略性新兴产业发展具有重要支撑作用。 该矿床主要含有镧、铈、钕等轻稀土元素，这些是永磁材料、动力电池和风力发电设备的关键原料。其规模仅次于内蒙古白云鄂博矿床。

telegram · zaihuapd · Mar 23, 13:59

**背景**: 轻稀土元素对高科技和绿色能源技术至关重要。中国主导全球稀土生产，其中白云鄂博是世界最大轻稀土矿床。这些元素广泛应用于电子、激光、磁体和工业领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/5930752">Discussion on the Rare earth resources and its... | IEEE Xplore</a></li>
<li><a href="https://min.news/en/news/9beb66a52d750bb059ee1e548e5840f1.html">President Tokayev presented a great gift by finalizing a rare earth ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rare-earth_element">Rare-earth element - Wikipedia</a></li>

</ul>
</details>

**标签**: `#rare_earth`, `#mining`, `#china`, `#resources`, `#energy`

---