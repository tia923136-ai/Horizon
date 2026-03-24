---
layout: default
title: "Horizon Summary: 2026-03-24 (ZH)"
date: 2026-03-24
lang: zh
---

> From 32 items, 13 important content pieces were selected

---

1. [专家权重流式加载技术让消费级设备运行万亿参数模型成为可能](#item-1) ⭐️ 8.0/10
2. [英伟达被指利用资金优势捆绑 AI 客户](#item-2) ⭐️ 8.0/10
3. [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](#item-3) ⭐️ 8.0/10
4. [DarkSword 漏洞链通过恶意网页攻击 Safari 用户](#item-4) ⭐️ 8.0/10
5. [谷歌推出 Gemini 暗网威胁情报 AI 代理，现已开放预览](#item-5) ⭐️ 8.0/10
6. [微软 Windows 11 的'修复'方案引发用户强烈不满](#item-6) ⭐️ 7.0/10
7. [DIY 教程：将公寓对讲系统接入 Apple Home](#item-7) ⭐️ 7.0/10
8. [FastAPI 底层框架 Starlette 1.0 正式发布](#item-8) ⭐️ 7.0/10
9. [PC Gamer 文章因自动播放广告导致体积达 37MB](#item-9) ⭐️ 7.0/10
10. [JavaScript 沙盒技术全面对比](#item-10) ⭐️ 7.0/10
11. [CRDT 版本控制的交互式合并状态可视化工具](#item-11) ⭐️ 7.0/10
12. [美国 FCC 以安全风险为由全面禁止外国制造的路由器](#item-12) ⭐️ 7.0/10
13. [我国日均词元调用量两年增超千倍，今年 3 月突破 140 万亿](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [专家权重流式加载技术让消费级设备运行万亿参数模型成为可能](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

研究人员通过从 SSD 流式加载专家权重而非完整加载模型的技术，成功在 96GB 内存的 MacBook Pro 上运行了万亿参数的 Kimi K2.5 模型，并在 iPhone 上以 0.6 token/秒的速度运行 Qwen3.5-397B-A17B 模型。 这一突破大幅降低了运行尖端 AI 模型的硬件需求，有望在个人设备上实现不依赖云端的先进 LLM 能力，可能重塑本地 AI 应用的格局。 该技术从 1T 参数的 Kimi K2.5 模型中每次仅激活 320 亿权重，而 Qwen3.5-397B-A17B 仅需 48GB 内存。移动设备上的性能仍有限制（iPhone 上 0.6 token/秒）。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家(MoE)模型使用针对不同输入选择性激活的专用子网络(专家)，可以在较低活跃计算量的情况下实现更大总参数量。传统 MoE 实现需要将所有专家加载到内存中，而这种新的流式方法可以动态从存储中加载所需的专家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 开发者对快速进展感到兴奋，有人认为这将催生新型本地 AI 应用。也有人提醒当前移动设备上的性能对大多数实际用例仍不实用。

**标签**: `#LLM`, `#Mixture-of-Experts`, `#hardware-optimization`, `#AI`, `#streaming`

---

<a id="item-2"></a>
## [英伟达被指利用资金优势捆绑 AI 客户](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

自 2022 年以来，英伟达已向 OpenAI、CoreWeave 和 Reflection 等 AI 初创公司投入数十亿美元，通过供应商兼投资者的双重身份将客户锁定在其生态系统中。该公司还因与芯片初创公司 Groq 达成的 200 亿美元交易面临审查，被质疑旨在规避反垄断监管。 英伟达的策略可能通过限制客户转向 AMD 等竞争对手的能力来抑制 AI 市场竞争。这已引起美国立法者的关注，他们担忧潜在的反垄断违规行为以及对市场多样性的长期影响。 英伟达的投资对象包括云 GPU 提供商 CoreWeave 和自主编码初创公司 Reflection。与 Groq 的交易通过授权协议而非完全收购来规避监管障碍，同时获取其核心团队。

telegram · zaihuapd · Mar 24, 03:02

**背景**: 英伟达凭借其 GPU 在 AI 芯片市场占据主导地位，这些芯片对训练大语言模型至关重要。CoreWeave 专注于为 AI 提供 GPU 云基础设施，Groq 开发 AI 加速器芯片，而 Reflection AI 则致力于通过自主编码代理实现超级智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#Nvidia`, `#antitrust`, `#semiconductors`, `#investment`

---

<a id="item-3"></a>
## [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

3 月 24 日，阿里巴巴达摩院在上海举办的 2026 玄铁 RISC-V 生态大会上发布了新一代旗舰 CPU 玄铁 C950，该产品在 Specint2006 单核测试中得分超过 70 分，创下当前公开 RISC-V 处理器的最高性能纪录。 这一突破表明 RISC-V 在高性能计算领域的竞争力日益增强，可能打破 ARM 和 x86 在云 AI 和边缘计算市场的主导地位，特别是该芯片原生支持 Qwen3 和 DeepSeek V3 等千亿参数级模型。 该芯片集成了达摩院自研的 AI 加速引擎，面向云计算、生成式 AI、高端机器人和边缘计算领域。其 Specint2006 测试 70+的分数显著超越了之前的 RISC-V 处理器实现。

telegram · zaihuapd · Mar 24, 06:01

**背景**: RISC-V 是一种开放标准的指令集架构，正逐渐成为 ARM 和 x86 等专有架构的替代选择。Specint2006 是衡量 CPU 整数性能的标准基准测试。Qwen3 和 DeepSeek V3 是阿里巴巴开发的千亿参数级别大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/models/comparisons/qwen3-max-vs-deepseek-v3">Qwen3 Max vs DeepSeek V3 (Dec '24): Model Comparison</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#AI Hardware`, `#Cloud Computing`, `#Semiconductors`, `#Edge Computing`

---

<a id="item-4"></a>
## [DarkSword 漏洞链通过恶意网页攻击 Safari 用户](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

自 2025 年 11 月起活跃的 DarkSword 漏洞链通过恶意网页感染 Safari 用户，影响 iOS 18.4 至 18.7 版本，并投放 GHOSTBLADE 等恶意载荷。相关漏洞已在 iOS 26.3 中全部修补，部分漏洞如 CVE-2025-43529 更早就在 iOS 18.7.3 和 26.2 中修复。 这一漏洞链因其复杂性（串联了 6 个漏洞，包括 3 个零日漏洞）和跨国针对性攻击而备受关注。GHOSTBLADE 载荷能窃取敏感数据，如通讯记录、照片和加密货币交易所凭证，对受影响用户构成严重威胁。 该漏洞链完全由 JavaScript 编写，可在未打补丁的 iPhone 上实现一键设备接管。它专门针对 iOS 18.4-18.7 版本，并已在沙特、土耳其、马来西亚和乌克兰的攻击中被使用。

telegram · zaihuapd · Mar 24, 11:45

**背景**: DarkSword 是近期披露的 iOS 漏洞链，利用多个零日漏洞完全控制 iOS 设备。GHOSTBLADE 是一种已知的恶意软件家族，会系统性地扫描受感染设备中的敏感数据，包括加密货币交易所应用和个人通讯记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword: iOS Exploit Chain Adopted by ...</a></li>
<li><a href="https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html">DarkSword iOS Exploit Kit Uses 6 Flaws, 3 Zero-Days for Full ...</a></li>
<li><a href="https://cybersecsentinel.com/darksword-ios-exploit-chains-six-vulnerabilities-for-silent-device-takeover/">DarkSword iOS Exploit Chains Six Vulnerabilities for Silent ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#ios`, `#safari`, `#zero-day`, `#malware`

---

<a id="item-5"></a>
## [谷歌推出 Gemini 暗网威胁情报 AI 代理，现已开放预览](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

谷歌将基于 Gemini 的 AI 代理集成至 Google Threat Intelligence 服务，并开放公开预览。该系统每天分析约 800 万至 1000 万条暗网帖子，以 98%的准确率识别初始访问中介活动、数据泄露和内部威胁等组织风险。 这标志着暗网监控自动化的重大进步，使企业能够以前所未有的规模主动检测网络威胁。其高准确率可显著降低威胁情报运营中的误报情况。 该 AI 会先建立组织画像再扫描暗网内容，特别针对初始访问中介（IABs）——即向其他网络犯罪分子出售网络访问权限的黑客。98%的准确率数据来自谷歌内部测试。

telegram · zaihuapd · Mar 24, 13:15

**背景**: 初始访问中介（IABs）是专门入侵网络并向勒索软件组织出售访问权限的网络犯罪分子。暗网中存在进行此类非法交易的论坛。Google Threat Intelligence 是谷歌云安全套件的一部分，而 Gemini 是谷歌的旗舰 AI 模型系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cybersecuritynews.com/google-gemini-ai-dark-web/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to...</a></li>
<li><a href="https://www.cisecurity.org/insights/blog/initial-access-brokers-how-theyre-changing-cybercrime">Initial Access Brokers How They’re Changing Cybercrime - CIS A Deep-Dive Into Initial Access Brokers: Trends, Statistics ... M-Trends 2026: Initial Access Handoff Shrinks From Hours to ... Researchers Uncover Data Leak Site Linked To Active Initial ... They hack to sell: corporate access traded in shadows | Cybernews New Data Leak Site Uncovered Linked to Active Initial Access ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#Dark Web`, `#Google`, `#Threat Intelligence`

---

<a id="item-6"></a>
## [微软 Windows 11 的'修复'方案引发用户强烈不满](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/) ⭐️ 7.0/10

微软解决 Windows 11 用户体验问题的方式被批评为敷衍且对用户不友好，引发了关于企业软件实践的广泛讨论。 此事影响重大，因为全球数百万用户使用 Windows 11，微软处理更新和强制功能的方式为科技巨头如何平衡商业利益与用户需求树立了先例。 具体投诉包括被禁用的 Microsoft Start 新闻反复出现、强制推送不受欢迎的内容，以及缺乏防止问题再次发生的系统性改变。

hackernews · h0ek · Mar 24, 09:36

**背景**: Windows 11 是微软 2021 年发布的最新操作系统，接替 Windows 10。微软一直因其激进的更新策略、预装应用和用户难以永久禁用的功能而受到批评。

**社区讨论**: 评论显示出对微软做法的深度不满，有人将其与历史上的反竞争行为相提并论。用户对 Microsoft Start 的顽固存在和内容质量特别愤怒，同时有人讨论政府采用是否纵容了糟糕的用户体验。

**标签**: `#Microsoft`, `#Windows11`, `#UserExperience`, `#CorporateCriticism`, `#Software`

---

<a id="item-7"></a>
## [DIY 教程：将公寓对讲系统接入 Apple Home](https://www.jackhogan.me/blog/box-of-secrets/) ⭐️ 7.0/10

一份详细的 DIY 指南展示了如何隐蔽地改造公寓对讲系统，使其接入 Apple Home，从而通过 HomeKit 实现远程开门功能。该方案涉及硬件破解，并尝试避免被房东或物业发现。 这解决了传统对讲系统缺乏智能家居兼容性的城市生活痛点，同时也引发了关于改造共享建筑基础设施的合法性和伦理问题。该方案可能推动这个服务不足的市场出现更符合伦理的商业替代方案。 该改造需要截取并模拟对讲系统的电信号，同时保留原有功能。一些评论者提到地区性替代方案，如罗马尼亚的预制适配板(30 欧元)或更简单的基于语音信箱的解决方案。

hackernews · jackhogan11 · Mar 23, 12:42

**背景**: Apple HomeKit 是苹果的智能家居平台，可通过 iOS 控制兼容设备。许多公寓对讲系统使用模拟系统，缺乏现代连接选项，因此产生了对接入解决方案的需求。此类系统的硬件破解通常涉及逆向工程专有协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.home-assistant.io/integrations/homekit/">Instructions on how to set up the HomeKit Bridge integration in Home...</a></li>
<li><a href="https://jdmcd.io/blog/hacking-my-apartment-intercom/">Hacking My Apartment Intercom – Jimmy McDermott –</a></li>
<li><a href="https://hackaday.io/project/186880/instructions">HOW I HACKED MY INTERCOM SO I CAN BE MORE LAZY - Hackaday.io</a></li>

</ul>
</details>

**社区讨论**: 评论显示了对改造共享基础设施的伦理担忧，一些用户称其'在法律上可疑'。用户分享了替代解决方案，包括商业适配器和语音信箱破解。许多人指出对讲技术现状不佳，市场缺乏简单安全的解决方案。

**标签**: `#DIY`, `#Home Automation`, `#Apple HomeKit`, `#Intercom`, `#Hardware Hacking`

---

<a id="item-8"></a>
## [FastAPI 底层框架 Starlette 1.0 正式发布](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

经过多年开发，FastAPI 的底层 ASGI 框架 Starlette 1.0 正式发布，引入了包括基于异步上下文管理器的生命周期机制在内的重大变更。 此次发布意义重大，因为 Starlette 是 Python 最受欢迎的 Web 框架 FastAPI 的底层支撑，1.0 版本标志着 ASGI 生态系统获得了稳定的 API 基础。 最显著的变更是用异步上下文管理器的生命周期机制替代了原有的 on_startup/on_shutdown 参数，同时保持了 Starlette 类似 Flask 的单文件简洁特性，这对大语言模型生成代码特别友好。

rss · Simon Willison · Mar 22, 23:57

**背景**: Starlette 是用于构建异步 Web 服务的轻量级 ASGI 框架。ASGI（异步服务器网关接口）是 WSGI 的异步继任者，使 Python 框架能高效处理并发连接。FastAPI 在 Starlette 基础上构建，增加了自动生成 OpenAPI 文档等特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>
<li><a href="https://fastapi.tiangolo.com/benchmarks/">Benchmarks - FastAPI</a></li>

</ul>
</details>

**标签**: `#Python`, `#ASGI`, `#Web Frameworks`, `#Starlette`, `#FastAPI`

---

<a id="item-9"></a>
## [PC Gamer 文章因自动播放广告导致体积达 37MB](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

技术审计发现一篇 PC Gamer 文章因自动播放视频广告膨胀至 37MB，该分析使用了 Rodney 命令行工具。调查显示这些广告会导致持续下载数百 MB 的额外数据。 这展现了严重影响用户体验和可访问性的网页膨胀问题，尤其对带宽有限的用户。它证明了广告密集型设计如何损害媒体网站的内容交付。 该分析使用了用于网页交互和性能测试的命令行工具 Rodney。37MB 的大小尚未包含自动播放广告在后台持续加载的后续下载。

rss · Simon Willison · Mar 22, 22:49

**背景**: 网页膨胀指由过大媒体文件、冗余代码和过多脚本导致的不必要页面体积。Rodney 是 Simon Willison 开发的开源命令行工具，用于网页自动化和性能分析，常与 AI 代理配合使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/rodney">GitHub - simonw/rodney: CLI tool for interacting with the web</a></li>
<li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">Introducing Showboat and Rodney, so agents can demo what they ...</a></li>
<li><a href="https://www.speedcurve.com/blog/page-bloat-web-performance/">SpeedCurve | What is page bloat? And how is it hurting your business, your search rank, and your users?</a></li>

</ul>
</details>

**标签**: `#web-performance`, `#web-bloat`, `#rodney`, `#analysis`, `#web-development`

---

<a id="item-10"></a>
## [JavaScript 沙盒技术全面对比](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

一项详细研究对比了六种 JavaScript 沙盒技术：isolated-vm、vm2、quickjs-emscripten、QuickJS-NG、ShadowRealm 和 Deno Workers，该研究灵感来源于对 Node.js 工作线程的探索。 这项研究很重要，因为沙盒技术对于安全执行不受信任的 JavaScript 代码至关重要，应用场景包括插件系统、在线 IDE 和无服务器函数等，这些场景中的安全漏洞可能造成严重后果。 研究指出尽管 vm2 很受欢迎但存在安全漏洞，而 isolated-vm 虽然隔离性更强但面临维护挑战。QuickJS 变体提供了轻量级替代方案，但各有取舍。

rss · Simon Willison · Mar 22, 19:53

**背景**: JavaScript 沙盒技术通过隔离不受信任的代码执行来防止访问敏感系统资源。传统方法包括 iframe（用于浏览器）和 VM 模块（用于 Node.js），但每种方法在安全性或性能上都有局限。ShadowRealm 等新提案和 Deno 等运行时提供了现代替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://healeycodes.com/sandboxing-javascript-code">Sandboxing JavaScript Code — Andrew Healey</a></li>
<li><a href="https://dev.to/leapcell/a-deep-dive-into-javascript-sandboxing-97b">A Deep Dive into JavaScript Sandboxing - DEV Community</a></li>
<li><a href="https://zendesk.engineering/sandboxing-javascript-e4def55e855e?gi=b5419a96afd3">Sandboxing JavaScript. tl;dr iframes are likely your best bet… | by Daniel Ribeiro | Zendesk Engineering</a></li>

</ul>
</details>

**标签**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-11"></a>
## [CRDT 版本控制的交互式合并状态可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 Pyodide 创建了一个交互式合并状态可视化工具，用于演示 Bram Cohen 基于 CRDT 的版本控制概念，并借助 Claude AI 生成解释说明。 该工具为理解基于 CRDT 的高级版本控制系统提供了实用途径，相比现有工具可能为分布式环境中的复杂合并冲突提供更好的解决方案。 该可视化工具基于 Bram Cohen 用 470 行 Python 代码实现的'manyana'概念，通过 Pyodide 完全在浏览器中运行，无需服务器端处理。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（无冲突复制数据类型）是一种数据结构，允许分布式系统无需协调即可同步。Pyodide 是通过 WebAssembly 在浏览器中运行的 Python 发行版。BitTorrent 的创建者 Bram Cohen 提出将 CRDT 作为版本控制系统的未来，认为它比当前方法能更好地处理复杂合并场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bramcohen.com/p/manyana">A Coherent Vision for the Future of Version Control</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 0.29.3</a></li>

</ul>
</details>

**标签**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#visualization`

---

<a id="item-12"></a>
## [美国 FCC 以安全风险为由全面禁止外国制造的路由器](https://www.bloomberg.com/news/articles/2026-03-23/fcc-bans-all-foreign-made-routers-citing-security-risks?embedded-checkout=true) ⭐️ 7.0/10

美国联邦通信委员会（FCC）正式宣布，出于网络安全和供应链漏洞的担忧，全面禁止所有外国制造的消费级路由器进入美国市场，并将其列入'受管辖实体名单'。新型号若想获得豁免，必须向美国国防部等机构申请批准。 这一决定可能严重扰乱全球供应链并影响主要网络设备制造商，同时也反映出对源自外国制造硬件的网络安全威胁日益增长的担忧。 该禁令遵循'新老划断'原则，已获批准的现有型号可继续使用和销售，但新型号必须获得认证。豁免需要多个美国政府机构的批准。

telegram · zaihuapd · Mar 24, 01:17

**背景**: FCC 的'受管辖实体名单'包含被视为国家安全风险的公司，主要是华为、中兴等中国企业。供应链攻击已成为主要担忧，类似 SolarWinds 事件中，被入侵的硬件/软件更新被用来渗透系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1937155538233320578">FCC 新规核心条款+过渡期强制时间表 - 知乎</a></li>
<li><a href="https://gma.caict.ac.cn/update/66/138">美国: FCC 禁止对涵盖清单涉及公司的通信设备进行授权| FCC认证更新</a></li>
<li><a href="https://cn-sec.com/archives/5120429.html">800万次请求后，我们发现了一个让SolarWinds... | CN-SEC 中文网</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#regulation`, `#networking`, `#supply-chain`, `#FCC`

---

<a id="item-13"></a>
## [我国日均词元调用量两年增超千倍，今年 3 月突破 140 万亿](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

国家数据局披露，我国日均词元调用量在今年 3 月突破 140 万亿，相比 2024 年初的 1000 亿增长超千倍。 这一爆发式增长反映了人工智能产业快速商业化进程，以及在中国数据要素市场化改革推动下，围绕词元调用、定价和交易的新价值体系正在形成。 词元是大模型处理信息的最小单元，具有可计量、可交易特性。140 万亿的里程碑表明中国 AI 应用和数据供应链建设正在加速。

telegram · zaihuapd · Mar 24, 07:22

**背景**: 在 AI 系统中，词元代表模型处理的文本分段单元，可以是单个字符或完整词语。中国自 2020 年启动的数据要素市场化改革建立了数据交易和估值的制度机制，使基于词元的 AI 服务商业化成为可能。目前主流平台按词元计费，输出词元成本通常是输入的 3-5 倍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them">What are tokens and how to count them? - OpenAI Help Center</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1059056026002649">The Marketization of Data Elements, Facilitation of Cross ...</a></li>
<li><a href="https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/">Tokens Explained: The Currency of Generative AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tokenization`, `#Data Market`, `#China Tech`, `#Commercialization`

---