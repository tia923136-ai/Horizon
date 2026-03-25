---
layout: default
title: "Horizon Summary: 2026-03-25 (ZH)"
date: 2026-03-25
lang: zh
---

> From 34 items, 15 important content pieces were selected

---

1. [LiteLLM PyPI 软件包 1.82.7 和 1.82.8 版本被发现存在恶意代码](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.82.8 PyPI 软件包被植入凭证窃取程序](#item-2) ⭐️ 9.0/10
3. [流式专家技术让消费级硬件可运行万亿参数模型](#item-3) ⭐️ 8.0/10
4. [英伟达被指利用资金优势捆绑 AI 初创公司，巩固生态霸权](#item-4) ⭐️ 8.0/10
5. [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](#item-5) ⭐️ 8.0/10
6. [DarkSword 漏洞链曝光：影响 iOS 18.4-18.7 的 Safari 漏洞](#item-6) ⭐️ 8.0/10
7. [谷歌推出 Gemini 暗网情报 AI 代理，现已开放预览](#item-7) ⭐️ 8.0/10
8. [OpenAI 拟停用 Sora 视频生成器，关闭 API 并终止迪士尼合作](#item-8) ⭐️ 8.0/10
9. [OpenAI 关闭 Sora 视频生成应用](#item-9) ⭐️ 7.0/10
10. [Claude Code 推出带安全保护的自动模式](#item-10) ⭐️ 7.0/10
11. [包管理器引入依赖冷却机制应对供应链攻击](#item-11) ⭐️ 7.0/10
12. [我国日均词元调用量两年增超千倍，今年 3 月突破 140 万亿](#item-12) ⭐️ 7.0/10
13. [欧盟年龄验证 App 或限制非谷歌授权安卓系统使用](#item-13) ⭐️ 7.0/10
14. [微软发布 7 本 Rust 培训教材，覆盖从入门到专家级](#item-14) ⭐️ 7.0/10
15. [Claude Code 推出自动模式，内置安全审查](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM PyPI 软件包 1.82.7 和 1.82.8 版本被发现存在恶意代码](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

PyPI 上的 LiteLLM 1.82.7 和 1.82.8 版本被发现包含恶意 base64 编码代码，位于 proxy_server.py 中，会触发 forkbomb 攻击耗尽系统内存。维护者已将该包在 PyPI 上隔离并正在调查入侵事件。 这是一次影响广泛的供应链攻击，波及众多 AI 开发者使用的流行 LLM 集成库，可能导致数千系统被入侵。该事件凸显了开源软件包生态系统的持续安全风险，以及加强依赖验证的必要性。 攻击包含一个 base64 负载，会解码并执行恶意代码，具有 TeamPCP 黑客组织近期活动的特征。Docker 用户未受影响，因为 requirements.txt 中锁定了版本。

hackernews · dot_treo · Mar 24, 12:06

**背景**: LiteLLM 是一个开源库，为包括 OpenAI 和 Anthropic 在内的 100 多个 LLM API 提供统一接口。PyPI 是 Python 官方软件包仓库，近期成为供应链攻击目标。Forkbomb 是一种拒绝服务攻击，通过进程快速复制耗尽系统资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI ... litellm - PyPI LiteLLM on PyPI Was Compromised, What the Attack Changed and ... Popular LiteLLM PyPI package compromised in TeamPCP supply ... litellm | Python SDK, Proxy Server (AI Gateway) to call 100 ... LiteLLM - Getting Started GitHub - BerriAI/ litellm : Python SDK, Proxy Server (AI Gateway) to call A gentle introduction to LiteLLM - Medium litellm · PyPI A gentle introduction to LiteLLM. Unify LLM APIs across ... Top Stories</a></li>
<li><a href="https://pypi.org/project/litellm/">litellm - PyPI</a></li>
<li><a href="https://www.imperva.com/learn/ddos/fork-bomb/">What is a Fork Bomb (Rabbit Virus) | DDoS Attack Glossary ... What Is Fork Bomb Malware and How Does It Work? What Is Fork Bomb Attack? — Definition by ThreatDotMedia What Is a Fork Bomb? Prevention & Linux Fix | SupportPro Fork bomb definition – Glossary | NordVPN</a></li>

</ul>
</details>

**社区讨论**: 维护者确认漏洞源自被入侵的 CI/CD 工具(Trivy)，安全专家将其与 TeamPCP 黑客组织活动关联。讨论强调了开发环境需要更好的沙箱保护，建议方案从蜜罐令牌到虚拟机级隔离不等。

**标签**: `#security`, `#pypi`, `#supply-chain`, `#malware`, `#devops`

---

<a id="item-2"></a>
## [LiteLLM v1.82.8 PyPI 软件包被植入凭证窃取程序](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

PyPI 上的 LiteLLM v1.82.8 软件包被植入了一个隐藏在 base64 编码的 litellm_init.pth 文件中的凭证窃取程序，该程序在安装时即激活，无需导入包即可运行。PyPI 已将该软件包隔离，将暴露时间窗口限制在几小时内。 这是一次针对广泛使用的 Python 软件包的严重供应链攻击，可能危及多个系统和服务的敏感凭证。此次攻击凸显了恶意行为者利用 PyPI 等受信任分发渠道的风险正在增加。 该凭证窃取程序针对多种敏感文件，包括 SSH 密钥、云服务凭证和加密货币钱包。攻击源于 PyPI 凭证被盗，这些凭证可能是通过之前对 Trivy 安全扫描器的漏洞利用窃取的。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一个用于与大型语言模型（LLM）交互的热门 Python 库。PyPI（Python 包索引）是 Python 软件包的官方存储库，因此成为供应链攻击的高价值目标。Python 中的 .pth 文件是一种特殊文件，可以在 Python 解释器启动时执行代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm _ init . pth in litellm...</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/malicious-litellm/">Malicious litellm _ init . pth in litellm 1.82.8 — credential stealer</a></li>
<li><a href="https://devblogs.co/posts/malicious-litellm-initpth-in-litellm-1828-credential-stealer">Malicious litellm _ init . pth in litellm 1.82.8 — credential stealer</a></li>

</ul>
</details>

**标签**: `#security`, `#python`, `#pypi`, `#vulnerability`, `#supply-chain`

---

<a id="item-3"></a>
## [流式专家技术让消费级硬件可运行万亿参数模型](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

研究人员通过从 SSD 流式加载专家权重而非完整模型，成功在消费级设备（MacBook Pro、iPhone）上运行了 Kimi K2.5 等万亿参数的混合专家模型。该技术在 128GB M4 Max Mac 上达到 1.7 token/秒，在 iPhone 上实现 0.6 token/秒。 这一突破通过让大模型在平价消费级硬件上运行（而非需要配备 TB 级内存的昂贵服务器 GPU），实现了大规模 AI 模型的平民化。既能保持模型能力，又可加速设备端 AI 应用发展。 该方法利用了 MoE 模型的稀疏激活特性（每次仅激活约 320 亿参数）和 SSD 的高速读写（约 17GB/秒）。当前主要限制是 SSD 延迟导致的生成速度较慢（0.6-1.7 token/秒）。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家（MoE）模型将神经网络划分为多个专用子模型（'专家'），通过门控机制为每个输入仅激活相关专家。这种架构可在保持计算成本可控的同时实现超大参数量（如 1 万亿），因为多数权重处于未激活状态。传统实现需要将所有专家权重加载到内存中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@shubhamku2022/mixture-of-experts-models-for-efficient-ai-3f754759ef19">Mixture of Experts Models for Efficient AI | by Shubhamku | Medium</a></li>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#Hardware`, `#Optimization`

---

<a id="item-4"></a>
## [英伟达被指利用资金优势捆绑 AI 初创公司，巩固生态霸权](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

自 2022 年起，英伟达已向 OpenAI、CoreWeave 和 Reflection 等 AI 初创公司投资数十亿美元，通过‘供应商兼投资者’的双重身份将其锁定在自身生态中。该公司还通过 200 亿美元收购芯片初创公司 Groq 等交易获取核心技术团队，同时规避反垄断审查。 该策略可能通过财务手段阻止初创公司采用 AMD 等竞争对手产品，从而压制 AI 硬件市场竞争，涉嫌违反反垄断原则。美国参议员已对英伟达主导 AI 基础设施的战术表示担忧。 CoreWeave 在德克萨斯州运营着英伟达‘全球最快 AI 超算’，而 Reflection AI 专注于自主编程代理开发。Groq 的 LPU 芯片专为 AI 推理任务设计，使其收购具有战略价值。

telegram · zaihuapd · Mar 24, 03:02

**背景**: 英伟达 GPU 因 CUDA 架构和软件生态成为 AI 训练的金标准。CoreWeave 等公司提供基于 GPU 的云基础设施，而 Groq 开发了替代性 AI 芯片挑战英伟达。Reflection AI 则代表致力于自主系统的下一代 AI 初创企业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://groq.com/">Groq is fast, low cost inference.</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#Nvidia`, `#Antitrust`, `#Semiconductors`, `#Market-Competition`

---

<a id="item-5"></a>
## [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

3 月 24 日，阿里巴巴达摩院在上海举办的 2026 玄铁 RISC-V 生态大会上发布了旗舰 CPU 玄铁 C950。该芯片在 Specint2006 单核测试中得分超过 70 分，创下公开 RISC-V 处理器的性能新高。 这一突破展示了 RISC-V 在高性能计算和 AI 应用中的潜力，可能挑战 ARM 和 x86 在云计算及边缘计算领域的主导地位。其原生支持千亿参数级 AI 模型的能力，使其成为下一代 AI 工作负载的有力竞争者。 该芯片集成了达摩院自研 AI 加速引擎，专门面向云计算、生成式 AI、高端机器人和边缘计算场景。但截至目前，其性能宣称尚未经过第三方验证，详细架构规格也未完全公开。

telegram · zaihuapd · Mar 24, 06:01

**背景**: RISC-V 是一种开源指令集架构，正逐步成为 ARM 和 x86 等专有架构的替代选择。Specint2006 是衡量 CPU 整数计算性能的基准测试工具。Qwen3 是阿里云开发的大语言模型系列，参数规模从 6 亿到 2350 亿不等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#AI Hardware`, `#Cloud Computing`, `#Edge Computing`, `#Semiconductors`

---

<a id="item-6"></a>
## [DarkSword 漏洞链曝光：影响 iOS 18.4-18.7 的 Safari 漏洞](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

DarkSword 漏洞链自 2025 年 11 月起被披露，影响 iOS 18.4 至 18.7 版本，用户仅需通过 Safari 打开恶意网页即可被感染。该漏洞链串联了 6 个漏洞（包括 CVE-2025-43529），可投放 GHOSTBLADE 等恶意载荷，相关漏洞已在 iOS 26.3 等后续版本中修复。 这一漏洞链曾在沙特、土耳其、马来西亚和乌克兰等地被用于针对性攻击，能够实现远程代码执行，风险极高。此次披露凸显了 iOS 用户（尤其是延迟更新的用户）面临的安全挑战。 该漏洞链包含 3 个零日漏洞，主要采用 JavaScript 编写，易于部署。相关修复补丁已分批推出，例如 CVE-2025-43529 在 iOS 18.7.3 及后续版本中修复。

telegram · zaihuapd · Mar 24, 11:45

**背景**: DarkSword 是一个针对 iOS 的完整漏洞利用工具包，利用了 Safari 中 WebKit 引擎的漏洞。WebKit 是 Safari 及苹果生态中所有网页内容处理的核心引擎。GHOSTBLADE 是谷歌威胁情报团队近期发现的一种窃取加密货币的恶意软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword: iOS Exploit Chain Adopted by ...</a></li>
<li><a href="https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html">DarkSword iOS Exploit Kit Uses 6 Flaws, 3 Zero-Days for Full ...</a></li>
<li><a href="https://www.linkedin.com/posts/cointelegraph_google-threat-intel-flags-ghostblade-crypto-stealing-activity-7441660499534131200-Gpmh">Google Threat Intel flags ' Ghostblade ' crypto-stealing malware</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#ios`, `#vulnerability`, `#safari`, `#zero-day`

---

<a id="item-7"></a>
## [谷歌推出 Gemini 暗网情报 AI 代理，现已开放预览](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

谷歌推出了集成 Google Threat Intelligence 的 Gemini 暗网情报 AI 代理预览版。该系统每天分析约 800 万至 1000 万条暗网帖子，识别初始访问中介活动、数据泄露和内部威胁等风险，内部测试显示准确率达 98%。 该产品通过规模化自动监控暗网，帮助企业在威胁升级前主动发现风险，满足了关键网络安全需求。与谷歌威胁情报生态的集成使企业安全团队能更高效应对不断演变的网络犯罪手段。 Gemini 可自主构建组织画像并根据业务运营动态调整。它特别针对向勒索软件组织出售网络访问权限的初始访问中介，这是网络犯罪即服务中日益增长的领域。

telegram · zaihuapd · Mar 24, 13:15

**背景**: 暗网是网络犯罪分子交易被盗数据和网络访问权限的非法市场。初始访问中介（IAB）专门入侵系统并向勒索软件运营商出售访问权限。Google Threat Intelligence 结合了 Mandiant 的前线专业知识和谷歌跨数十亿设备的可见性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era">Bringing dark web intelligence into the AI era | Google Cloud Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Initial_access_broker">Initial access broker - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#Dark Web`, `#Google`, `#Threat Intelligence`

---

<a id="item-8"></a>
## [OpenAI 拟停用 Sora 视频生成器，关闭 API 并终止迪士尼合作](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 8.0/10

OpenAI 计划停用 AI 视频生成产品 Sora，该应用上线仅约 6 个月后就将关闭，同时停止开发者 API 服务，与迪士尼的合作也在逐步收尾。 这标志着 OpenAI 的重大战略调整，公司将资源转向 AI agents 和名为 Spud 的新模型，意味着其正在远离面向消费者的视频生成产品。 此次停用伴随着组织架构调整，公司计划将安全团队更紧密地纳入开发流程，显示出 OpenAI 正重新聚焦于核心模型开发而非应用层产品。

telegram · zaihuapd · Mar 25, 00:30

**背景**: Sora 是 OpenAI 的文本生成视频模型，能够根据提示词生成短视频片段或延长现有视频。该模型因能从文本描述生成高质量创意视频内容而备受关注。OpenAI 的新焦点似乎是正在开发的下一代 AI 模型 Spud。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to- video model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI`, `#VideoGeneration`, `#APIs`, `#BusinessStrategy`

---

<a id="item-9"></a>
## [OpenAI 关闭 Sora 视频生成应用](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 7.0/10

OpenAI 宣布关闭其 AI 视频生成应用 Sora，距离其高调发布仅六个月。这一决定尽管 Sora 最初因其快速生成 AI 视频的能力而备受关注。 这一举动标志着 OpenAI 从面向消费者的 AI 视频工具转向可能更有利可图的自动化机会的战略转变。这也引发了关于在由多功能平台主导的生态系统中，独立 AI 创意应用的产品市场适应性问题。 在 OpenAI 发布 Sora 安全指南后不久即宣布关闭，这表明决策过程突然或内部存在分歧。迪士尼也终止了与 Sora 开发相关的 10 亿美元投资协议。

hackernews · mikeocool · Mar 24, 20:01

**背景**: Sora 是 OpenAI 于 2024 年推出的独立视频生成应用，能够根据文本提示创建 AI 生成的短视频。它在一个拥挤的 AI 创意工具空间中竞争，许多应用难以在最初的新鲜感过后保持用户参与度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/03/24/technology/openai-shutting-down-sora.html">OpenAI Is Shutting Down Sora, Its A.I. Video Generator OpenAI shutting down Sora video-creation app - NBC News That Was Fast. OpenAI to Shut Down Sora Video Generator App OpenAI is shutting down its Sora video generation app - Engadget Sora App Shut Down by OpenAI, Disney Deal Dead - IGN OpenAI Discontinues Sora App, Shuts Down Video Generation ... OpenAI to Shut Down Sora App - The Wrap</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/openai-shuttering-sora-video-generating-service-rcna264989">OpenAI shutting down Sora video-creation app - NBC News</a></li>
<li><a href="https://www.pcmag.com/news/that-was-fast-openai-to-shut-down-sora-video-generator-app">That Was Fast. OpenAI to Shut Down Sora Video Generator App</a></li>

</ul>
</details>

**社区讨论**: 评论显示反应不一：一些用户对失去创意可能性表示遗憾，而其他人则批评 Sora 的基本产品设计不可持续。有几位用户注意到 OpenAI 更广泛的战略转变，包括专注于开发者工具和政治游说。

**标签**: `#AI`, `#OpenAI`, `#video-generation`, `#product-market-fit`, `#tech-news`

---

<a id="item-10"></a>
## [Claude Code 推出带安全保护的自动模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code 推出了自动模式，这是一种新的权限模式，AI 代表用户做出决策，同时采用安全保护措施在执行前监控操作。这些保护措施通过 Claude Sonnet 4.6 作为分类器模型实现，用于审查对话并阻止不适当的操作。 这一发展为'--dangerously-skip-permissions'标志提供了更安全的替代方案，在 AI 辅助编程中实现了自动化与安全性的平衡。它可以显著简化开发人员的工作流程，同时降低在敏感环境中未经检查的 AI 操作带来的风险。 自动模式包含全面的默认过滤器，涵盖本地文件管理、Git 命令和软件包安装等操作，特别关注安全风险。用户还可以自定义这些规则，系统会严格防止范围扩大和不可逆的破坏性操作。

rss · Simon Willison · Mar 24, 23:57

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，使用宪法 AI 来提高伦理合规性。Claude Code 是其面向软件开发的应用，其中权限模式控制 AI 可以执行的操作。之前'--dangerously-skip-permissions'标志允许绕过所有安全检查，存在潜在安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://code.claude.com/docs/en/permissions">Configure permissions - Claude Code Docs</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**标签**: `#AI`, `#code-assistance`, `#permissions`, `#automation`

---

<a id="item-11"></a>
## [包管理器引入依赖冷却机制应对供应链攻击](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

包括 pnpm、Yarn、Bun、Deno、uv、pip 和 npm 在内的主流包管理器近期纷纷推出依赖冷却功能，通过延迟安装新发布的包版本以便进行安全检查。这一趋势源于 2026 年 3 月的 LiteLLM 供应链攻击事件，并延续了 William Woodruff 在 2025 年提出的依赖冷却理念。 依赖冷却机制通过建立缓冲期让社区能够检测问题包，为防范供应链攻击提供了关键防线。现代应用中超过 75%依赖开源组件，该实践将大幅降低恶意包更新的影响范围。 具体实现各有不同：pnpm 和 Bun 采用'minimumReleaseAge'参数，Yarn 使用'npmMinimalAgeGate'，Deno 实现'--minimum-dependency-age'选项，而 pip 目前仅支持'--uploaded-prior-to'绝对时间戳。多数工具都提供可信包的白名单豁免机制。

rss · Simon Willison · Mar 24, 21:11

**背景**: 供应链攻击通过污染软件依赖包入侵下游系统，攻击者常向合法包发布恶意更新。依赖冷却机制强制新版本发布后需等待 24-72 小时才能安装，为安全工具和维护者留出检测异常的时间窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://pnpm.io/blog/releases/10.16">pnpm 10.16 | pnpm</a></li>
<li><a href="https://cybercyte.com/blog/software-supply-chain-attacks/">Software Supply Chain Attacks : How Malicious Libraries... - Cybercyte</a></li>

</ul>
</details>

**标签**: `#package-management`, `#security`, `#supply-chain`, `#devops`

---

<a id="item-12"></a>
## [我国日均词元调用量两年增超千倍，今年 3 月突破 140 万亿](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

国家数据局披露，我国日均词元（Token）调用量已在 2025 年 3 月突破 140 万亿，从 2024 年初的 1000 亿增至 2025 年底的 100 万亿，两年增长超千倍。 这一爆发式增长标志着中国 AI 商业化加速，词元作为可计量、可交易的信息单元，正形成 AI 服务和数据交易的新价值体系。 词元是大模型处理信息的最小单元，其定价和结算机制实现了 AI 服务中计算与数据使用的精准计量。

telegram · zaihuapd · Mar 24, 07:22

**背景**: 词元化（Tokenization）将文本分解为 AI 可处理的单元，不同方法影响模型性能。我国数据要素市场化改革加速了高质量数据供应链建设，推动基于词元的 AI 商业化。这一增长也反映了中国在全球 AI 词元消耗中的竞争优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2403.00417">Rethinking Tokenization: Crafting Better Tokenizers for Large ...</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202603/24/WS69c21887a310d6866eb3f91f.html">Daily token surge heralds rapid commercialization of China's AI</a></li>
<li><a href="https://www.globaltimes.cn/page/202603/1357467.shtml">Chinese tokens going global - Global Times</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tokenization`, `#China-Tech`, `#Data-Economy`, `#Commercialization`

---

<a id="item-13"></a>
## [欧盟年龄验证 App 或限制非谷歌授权安卓系统使用](https://t.me/zaihuapd/40484) ⭐️ 7.0/10

欧盟正在开发一款开源年龄验证 App，要求设备通过谷歌 Play Integrity 验证且必须从 Play 商店下载并登录谷歌账号，这将导致 GrapheneOS 等非谷歌授权安卓系统无法使用。 这一举措引发了对数字主权的担忧，加深了对美国科技巨头的依赖，可能限制用户选择并损害注重隐私安全的开源安卓替代系统。 该 App 将使用谷歌 Play Integrity API（原 SafetyNet）验证设备真实性，批评者认为这违背了欧盟的开源和互操作性原则，并为注重隐私的安卓分支系统设置了障碍。

telegram · zaihuapd · Mar 24, 12:22

**背景**: Play Integrity API 是谷歌用于验证应用真实性和设备完整性的安全系统。GrapheneOS 是一个注重隐私的安卓分支系统，移除了谷歌服务，被那些希望避免依赖谷歌生态的安全意识用户使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Play_Integrity_API">Play Integrity API - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**社区讨论**: GitHub 上的开发者和隐私倡导者反对这一要求，认为其违背数字主权目标，并为不依赖谷歌服务的替代安卓实现设置了不公平障碍。

**标签**: `#EU policy`, `#Android`, `#digital sovereignty`, `#privacy`, `#open-source`

---

<a id="item-14"></a>
## [微软发布 7 本 Rust 培训教材，覆盖从入门到专家级](https://github.com/microsoft/RustTraining) ⭐️ 7.0/10

微软在 GitHub 上发布了 RustTraining 培训材料仓库，包含 7 本 Rust 教材，涵盖从其他语言转向 Rust 的过渡课程，以及异步编程、类型驱动正确性和工程实践等高级主题。 这一发布具有重要意义，因为微软提供了结构化的官方 Rust 培训材料，Rust 语言因其内存安全和性能优势日益流行，这将有助于加速开发者的学习与采用。 每本教材包含 15 至 16 章，配有 Mermaid 图、可编辑的 Rust Playground、练习和全文搜索功能。项目采用 MIT 与 CC-BY-4.0 双许可证发布，可在 GitHub 上直接阅读 Markdown 源文件或通过 GitHub Pages 浏览渲染站点。

telegram · zaihuapd · Mar 24, 23:57

**背景**: Rust 是一种系统编程语言，以其无需垃圾回收的内存安全保证而闻名。Rust 中的异步编程允许在没有操作系统参与的情况下实现并发执行，由异步运行时管理。类型驱动正确性利用 Rust 强大的类型系统在编译时强制执行正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rust-lang.github.io/async-book/">Introduction - Asynchronous Programming in Rust</a></li>
<li><a href="https://github.com/microsoft/RustTraining/blob/main/type-driven-correctness-book/src/SUMMARY.md">microsoft/RustTraining - type-driven-correctness-book - GitHub</a></li>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Microsoft`, `#Programming`, `#Education`, `#Open-Source`

---

<a id="item-15"></a>
## [Claude Code 推出自动模式，内置安全审查](https://claude.com/blog/auto-mode) ⭐️ 7.0/10

Claude Code 发布自动模式（Auto Mode），允许 AI 在任务执行中自主决定权限，同时通过内置分类器审查操作，自动拦截批量删文件、敏感数据外泄等高危行为。该功能目前以研究预览形式向 Team 计划用户开放，未来数日将覆盖 Enterprise 及 API 用户，支持 Claude Sonnet 4.6 与 Opus 4.6 模型。 该功能在 AI 自主性与安全性之间取得平衡，既减少人工审批打断，又规避完全跳过权限的安全隐患。它解决了 AI 辅助开发中的关键痛点——过多的权限提示会阻碍工作效率。 开发者可通过命令行执行 `claude --enable-auto-mode` 启用，Desktop 与 VS Code 用户可在设置中开启。官方提示该模式虽比 `--dangerously-skip-permissions` 参数更安全，但并非零风险，建议在隔离环境使用，且可能轻微增加 Token 消耗与延迟。

telegram · zaihuapd · Mar 25, 01:15

**背景**: Claude Sonnet 4.6 和 Opus 4.6 是 Anthropic 最新的 AI 模型，在编程、长上下文推理和智能体规划方面能力增强。自动模式介于完全手动审批权限和完全跳过安全检查之间，通过实时分类器评估工具使用情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zdnet.com/article/claude-code-auto-mode/">How Claude Code's new auto mode prevents AI coding ... - ZDNET</a></li>
<li><a href="https://www.anthropic.com/news/claude-sonnet-4-6">Introducing Claude Sonnet 4.6 - Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-6">Introducing Claude Opus 4.6 - Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Automation`, `#Security`, `#Claude`, `#Developer Tools`

---