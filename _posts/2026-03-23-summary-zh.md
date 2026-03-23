---
layout: default
title: "Horizon Summary: 2026-03-23 (ZH)"
date: 2026-03-23
lang: zh
---

> From 31 items, 10 important content pieces were selected

---

1. [GitHub 面临 99.9%可用性困境，引发广泛批评](#item-1) ⭐️ 7.0/10
2. [Starlette 1.0 发布：ASGI 框架重大升级](#item-2) ⭐️ 7.0/10
3. [PC Gamer 37MB 文章暴露网页臃肿问题](#item-3) ⭐️ 7.0/10
4. [JavaScript 沙箱解决方案对比研究](#item-4) ⭐️ 7.0/10
5. [基于 Pyodide 的 CRDT 版本控制交互式可视化工具](#item-5) ⭐️ 7.0/10
6. [Simon Willison 通过评论分析对 Hacker News 用户进行画像](#item-6) ⭐️ 7.0/10
7. [在 AI 编程助手开发中高效使用 Git](#item-7) ⭐️ 7.0/10
8. [MiniMax 升级 Coding Plan 支持全模态模型并宣布 MiniMax 2.7 开源权重](#item-8) ⭐️ 7.0/10
9. [千问上线打车能力，支持自然语言预约和个性化需求筛选](#item-9) ⭐️ 7.0/10
10. [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GitHub 面临 99.9%可用性困境，引发广泛批评](https://www.theregister.com/2026/02/10/github_outages/) ⭐️ 7.0/10

GitHub 近期可用性表现不佳，仅达到三个 9（99.9%）的水平，同时其 GitHub Actions 功能存在安全漏洞，导致了类似 Aqua Security 被入侵的严重事件。 作为全球最大的代码托管平台，GitHub 的可靠性和安全问题直接影响数百万依赖它进行日常开发的程序员和组织，可能导致软件开发流程的大范围中断。 三个 9 的可用性意味着每年约 8.76 小时的停机时间，批评者指出 GitHub 仍在 Actions 中使用社区长期警告的可变引用，以及其有争议的 Azure 基础设施迁移。

hackernews · richtr · Mar 23, 10:39

**背景**: 高可用性通常用'几个 9'来衡量，三个 9（99.9%）被视为关键业务系统的基本可靠性标准。GitHub 的基础设施决策，包括迁移到微软 Azure 云平台的决定，自 2025 年放弃独立数据中心以来一直备受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_availability">High availability - Wikipedia</a></li>
<li><a href="https://github.blog/engineering/infrastructure/">How GitHub approaches infrastructure - The GitHub Blog</a></li>
<li><a href="https://wellarchitected.github.com/library/overview/">Overview – GitHub Well-Architected</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧，有人为 GitHub 在云迁移中面临的挑战辩护，也有人批评其优先发展 AI 功能而忽视核心可靠性。多位评论者特别提到 GitHub Actions 中已知多年的安全漏洞仍未解决。

**标签**: `#github`, `#reliability`, `#security`, `#devops`, `#cloud`

---

<a id="item-2"></a>
## [Starlette 1.0 发布：ASGI 框架重大升级](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

作为 FastAPI 底层基础的 Python ASGI 框架 Starlette 正式发布 1.0 版本，包含重大变更如用生命周期机制替代原有的启动/关闭处理器。该项目在 Kim Christie 多年开发后，于 2025 年移交给了 Marcelo Trylesinski 维护。 该版本标志着这个通过 FastAPI 默默支撑 Python 现代异步网络生态的框架进入稳定阶段，其引入的更清晰的异步资源管理模式可能影响未来 ASGI 发展。 新的生命周期系统采用 Python 异步上下文管理器处理资源，提供更清晰的启动/关闭顺序。但这一破坏性变更可能影响 AI 生成代码的兼容性，因为模型训练基于 1.0 之前的版本。

rss · Simon Willison · Mar 22, 23:57

**背景**: Starlette 是一个轻量级 ASGI 框架，专为构建 Python 异步网络服务设计，是 FastAPI 的基础。ASGI(异步服务器网关接口)是 Python 的异步网络服务器和应用标准，支持 WebSocket 等异步协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://asgi.readthedocs.io/en/latest/specs/main.html">ASGI (Asynchronous Server Gateway Interface) Specification — ASGI ...</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/starlette: The little ASGI framework that shines. 🌟</a></li>

</ul>
</details>

**标签**: `#Python`, `#ASGI`, `#Starlette`, `#FastAPI`, `#Web Development`

---

<a id="item-3"></a>
## [PC Gamer 37MB 文章暴露网页臃肿问题](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

对 PC Gamer 网页性能的分析显示，一篇 37MB 的文章因自动播放视频广告持续下载数百 MB 数据，调查中使用了 Rodney 工具。 这凸显了网页臃肿对用户体验和数据使用的严重影响，尤其是自动播放广告，影响了主要出版物及其读者。 调查使用了轻量级 Chrome 自动化 CLI 工具 Rodney，发现页面存在资源加载效率低下和过度消耗数据的问题。

rss · Simon Willison · Mar 22, 22:49

**背景**: 网页臃肿指的是过度且低效地使用脚本、广告和媒体等资源，导致页面加载缓慢。自动播放视频广告是这一问题的常见原因，通常会在未经用户同意的情况下消耗大量带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lobehub.com/skills/maragudk-skills-rodney">rodney | Skills Marketplace - LobeHub</a></li>
<li><a href="https://www.digitalcitizen.life/how-to-stop-videos-from-playing-automatically-on-websites/">How to Stop Videos from Playing Automatically on Websites</a></li>

</ul>
</details>

**标签**: `#web-performance`, `#web-bloat`, `#analysis`, `#rodney`, `#optimization`

---

<a id="item-4"></a>
## [JavaScript 沙箱解决方案对比研究](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一份关于 JavaScript 沙箱技术的对比研究，涵盖了 isolated-vm、vm2、QuickJS、ShadowRealm 和 Deno Workers 等多种方案，该研究受到 Node.js 工作线程研究的启发。 该研究对需要安全执行不可信 JavaScript 代码的开发者至关重要，因为它评估了 JavaScript 生态中不同沙箱方案的隔离能力和安全权衡。 对比研究既包含 Node.js 专用方案（isolated-vm、vm2），也涵盖了替代引擎（QuickJS），以及新兴标准如 ShadowRealm 和提供更强隔离保证的 Deno Workers 实现。

rss · Simon Willison · Mar 22, 19:53

**背景**: JavaScript 沙箱技术指在隔离环境中运行不可信代码以防止访问敏感系统资源的方法。传统方案如 Node.js 的 vm 模块存在已知安全缺陷，促使开发者寻求更健壮的解决方案。ShadowRealm 是 TC39 提出的创建隔离 JavaScript 执行上下文的新提案，而 Deno Workers 则提供类似 Web Workers 的进程级隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/patriksimek/vm2">GitHub - patriksimek/vm2: Advanced vm/sandbox for Node.js · GitHub</a></li>
<li><a href="https://medium.com/@asierr/javascripts-new-shadowrealm-secure-and-isolated-javascript-execution-f620350750ed">JavaScript ’s New ShadowRealm : Secure and Isolated... | Medium</a></li>
<li><a href="https://docs.deno.com/api/node/worker_threads/">worker_threads - Node documentation</a></li>

</ul>
</details>

**标签**: `#javascript`, `#sandboxing`, `#security`, `#runtime`, `#nodejs`

---

<a id="item-5"></a>
## [基于 Pyodide 的 CRDT 版本控制交互式可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一个交互式工具，用于可视化 Bram Cohen 基于 CRDT 的版本控制系统 Manyana，该工具使用 Pyodide 在浏览器中运行 Python，并整合了 Claude AI 对 470 行 Python 代码实现的解释。 这展示了一种使用无冲突复制数据类型(CRDT)的版本控制新方法，相比 Git 等传统系统可能实现更无缝的协作和冲突解决，同时通过可视化使复杂概念更易于理解。 该可视化聚焦 Manyana 的核心算法(仍是一个演示版，存在如无法挑选提交/本地撤销等限制)，并利用基于 WebAssembly 的 Pyodide Python 运行时实现浏览器内的交互式探索。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT(无冲突复制数据类型)是可跨多设备复制并能独立更新而无需协调的数据结构，保证最终一致性。Pyodide 是将 Python 编译为 WebAssembly 的发行版，使 Python 代码能在浏览器中运行。BitTorrent 创造者 Bram Cohen 提出 Manyana 作为基于 CRDT 的 Git 合并冲突替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bramcohen.com/p/manyana">A Coherent Vision for the Future of Version Control</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>
<li><a href="https://pyodide.com/what-is-pyodide/">What is Pyodide? - pyodide</a></li>

</ul>
</details>

**标签**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-6"></a>
## [Simon Willison 通过评论分析对 Hacker News 用户进行画像](https://simonwillison.net/2026/Mar/21/profiling-hacker-news-users/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一种方法，通过使用 Algolia API 和 ChatGPT/Claude Opus 分析用户最近的 1000 条评论，对 Hacker News 用户进行画像，并以自己的画像为例展示了其效果。 这项技术展示了 LLM 在行为分析方面日益增长的能力，引发了关于公开评论空间隐私问题的思考，同时为理解社区动态提供了一个实用工具。 该方法利用 Algolia 的开放 CORS API 获取评论历史，并使用 Claude Opus 4.6 等高级 LLM 进行分析。Willison 指出结果'惊人地有效'，但可能具有侵入性。

rss · Simon Willison · Mar 21, 23:59

**背景**: Algolia Hacker News API 提供了对 Hacker News 数据（包括评论）的程序化访问，其开放的 CORS 头允许客户端 JavaScript 访问。CORS（跨源资源共享）是一种安全机制，允许网页从第一个资源服务域之外的另一个域请求受限资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hn.algolia.com/api">Hacker News Search powered by Algolia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cross-origin_resource_sharing">Cross-origin resource sharing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Hacker News`, `#API`, `#Data Analysis`, `#ChatGPT`, `#User Profiling`

---

<a id="item-7"></a>
## [在 AI 编程助手开发中高效使用 Git](https://simonwillison.net/guides/agentic-engineering-patterns/using-git-with-coding-agents/#atom-everything) ⭐️ 7.0/10

文章展示了 AI 编程助手如何通过特定命令提示充分利用 Git 的全部功能进行版本控制，包括仓库管理、提交跟踪和分支操作。 这很重要，因为它使开发者能够将复杂的 Git 操作委托给 AI 助手，在 AI 辅助开发工作流程中提高生产力，同时保持稳健的版本控制实践。 文章提供了 AI 编程助手能理解的具体 Git 命令示例，如'git init'、'git commit'和'git log'，并解释了如何通过自然语言提示触发这些操作。

rss · Simon Willison · Mar 21, 22:08

**背景**: 编程助手是协助软件开发任务的 AI 系统。Git 是一个分布式版本控制系统，用于跟踪开发过程中的源代码变更。代理工程学指的是在开发工作流程中有效使用 AI 助手的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/">Agentic Engineering Patterns - Simon Willison's Weblog</a></li>
<li><a href="https://medium.com/@analyticsinsight/ai-coding-agents-transforming-software-development-e75e098e4603">AI Coding Agents : Transforming Software Development | Medium</a></li>

</ul>
</details>

**标签**: `#Git`, `#AI-assisted-development`, `#version-control`, `#agentic-engineering`, `#software-engineering`

---

<a id="item-8"></a>
## [MiniMax 升级 Coding Plan 支持全模态模型并宣布 MiniMax 2.7 开源权重](https://mp.weixin.qq.com/s/o4KGGgtp32vRMecOYCbVmA) ⭐️ 7.0/10

MiniMax 将其 Coding Plan 升级为 Token Plan，为 Plus 及以上套餐用户提供视频、语音、音乐和图像等多模态模型的额外调用额度。同时宣布 MiniMax 2.7 开源权重将在约两周内发布。 此次升级使开发者能够在一个计划下访问全面的多模态 AI 工具，显著提升生产力和创意可能性。即将发布的 MiniMax 2.7 开源权重将为研究人员和开发者提供宝贵的 AI 模型开发和实验资源。 平台将在工作日下午高峰时段（15:00-17:30）实施动态限流，单周调用上限为原编程模型 5 小时用量的 10 倍。MiniMax 2.7 在 OpenClaw 基准测试中表现明显提升。

telegram · zaihuapd · Mar 23, 02:09

**背景**: MiniMax 成立于 2021 年 12 月，是中国领先的 AI 公司，专注于多模态和万亿参数的 MoE 大模型。该公司开发了海螺 AI、星野等原生应用，并为企业及开发者提供构建 AI 应用的 API 服务。OpenClaw 是专门用于评估 LLM 模型作为编程代理的基准测试系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.minimaxi.com/subscribe/coding-plan">Token Plan - MiniMax API 平台</a></li>
<li><a href="https://www.aibase.com/news/26453">MiniMax Launches Token Plan: The World's First All-Modal ...</a></li>
<li><a href="https://github.com/pinchbench/skill">GitHub - pinchbench/skill: PinchBench is a benchmarking system for evaluating LLM models as OpenClaw coding agents. Made with 🦀 by the humans at https://kilo.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#multimodal-models`, `#open-source`, `#rate-limiting`, `#MiniMax`

---

<a id="item-9"></a>
## [千问上线打车能力，支持自然语言预约和个性化需求筛选](http://www.ce.cn/cysc/newmain/yc/jsxw/202603/t20260323_2849214.shtml) ⭐️ 7.0/10

3 月 23 日，千问正式接入打车服务，用户可通过自然语言完成车型选择、途经点添加、预约时间及支付等全流程操作。系统支持“价格不超过 30 元”“驾驶平稳”“空气清新”等个性化需求指令，并能根据人数自动匹配车型。 这一功能将 AI 自然语言处理与日常服务相结合，提升了打车服务的便捷性和个性化水平。同时，它强化了阿里巴巴的生态系统，将打车与酒店预订、外卖等服务无缝衔接，为用户提供更流畅的体验。 该功能支持行程结束后通过“支付宝 AI 付”结算，并能记忆家庭与公司地址、预约特定时间用车。此外，它还可与订酒店、点外卖等生态服务串联执行连续指令。

telegram · zaihuapd · Mar 23, 02:50

**背景**: 千问是阿里巴巴的 AI 平台，利用自然语言处理技术提供多种数字生活服务。“支付宝 AI 付”是 2025 年推出的智能支付服务，用户可通过语音指令完成交易，无需跳转多个页面。此次上线的打车功能进一步将 AI 融入日常生活场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dn.com/en-us/news/detail-4202.html">Alibaba's Qianwen platform launched its AI-powered ride ...</a></li>
<li><a href="https://news.aibase.com/news/26451">Qwen Launches AI Ride-Hailing Service, Supports Alipay AI Payment</a></li>
<li><a href="https://www.oschina.net/news/371606">支付宝推出国内首个 AI 付 - OSCHINA - 中文开源技术交流社区</a></li>

</ul>
</details>

**标签**: `#AI`, `#ride-hailing`, `#natural-language-processing`, `#personalization`, `#mobile-payments`

---

<a id="item-10"></a>
## [OpenAI 建议英国将 AI 聊天机器人纳入 Google 搜索选择页](https://assets.publishing.service.gov.uk/media/69b970dcc06ba9576435ab5a/OpenAI.pdf) ⭐️ 7.0/10

OpenAI 在 3 月 6 日提交给英国竞争与市场管理局（CMA）的公开咨询意见中建议，Google 搜索选择页的资格标准应明确纳入具备搜索功能的 AI 聊天机器人，让这类服务也能在 Android 设备和 Chrome 等入口被用户选为默认搜索服务。 这一提议可能通过将标准现代化以纳入 AI 驱动服务，重塑搜索引擎竞争格局，确保传统搜索引擎与新兴的对话式 AI 工具（如 ChatGPT）之间的公平竞争。 OpenAI 认为 ChatGPT 的对话式和多模态功能与 Google 的 AI Overviews 和 AI Mode 在功能上相近，并建议采用透明、动态的流行度标准决定入选服务，同时将选择页扩展到语音、视觉和 AI 辅助搜索等入口。

telegram · zaihuapd · Mar 23, 14:50

**背景**: Google 搜索选择页允许用户在 Android 设备和浏览器上选择默认搜索引擎。AI Overviews 和 AI Mode 是 Google 自家的 AI 驱动搜索功能，可提供摘要式答案并处理复杂查询。OpenAI 的提议旨在让第三方 AI 聊天机器人在这一生态中获得同等地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/websearch/answer/464?hl=zh-Hans">将 Google 设为您的默认搜索引擎</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Mode">AI Mode</a></li>

</ul>
</details>

**标签**: `#AI`, `#Search Engines`, `#Regulation`, `#OpenAI`, `#Competition`

---