---
layout: default
title: "Horizon Summary: 2026-03-26 (ZH)"
date: 2026-03-26
lang: zh
---

> From 42 items, 14 important content pieces were selected

---

1. [PyPI 上的 LiteLLM v1.82.8 版本被植入窃取凭证的恶意代码](#item-1) ⭐️ 9.0/10
2. [利用报废零件在桌面上运行特斯拉 Model 3 计算机](#item-2) ⭐️ 8.0/10
3. [ARC-AGI-3 发布，成为评估通用人工智能的新基准](#item-3) ⭐️ 8.0/10
4. [欧盟坚持推动扫描私人信息引发隐私争议](#item-4) ⭐️ 8.0/10
5. [包管理器引入依赖冷却机制应对供应链攻击](#item-5) ⭐️ 8.0/10
6. [流式专家技术让大型混合专家模型在受限硬件上运行成为可能](#item-6) ⭐️ 8.0/10
7. [Apifox 桌面端遭供应链投毒攻击，窃取 SSH 密钥与 Git 凭证](#item-7) ⭐️ 8.0/10
8. [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿](#item-8) ⭐️ 8.0/10
9. [苹果与谷歌达成合作，将 Gemini AI 整合至 Siri](#item-9) ⭐️ 8.0/10
10. [对 AI 驱动开发中速度优先于质量的批判](#item-10) ⭐️ 7.0/10
11. [LiteLLM PyPI 攻击事件影响 47000 次下载](#item-11) ⭐️ 7.0/10
12. [Claude Code 推出带安全保护的自动模式](#item-12) ⭐️ 7.0/10
13. [拼多多官宣‘新拼姆’：三年投入 1000 亿元转向品牌自营](#item-13) ⭐️ 7.0/10
14. [GitHub 更新 Copilot 数据政策：免费与个人付费版默认纳入 AI 模型训练，可手动退出](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [PyPI 上的 LiteLLM v1.82.8 版本被植入窃取凭证的恶意代码](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

PyPI 上的 LiteLLM v1.82.8 软件包被植入了一个隐藏在 litellm_init.pth 文件中的凭证窃取漏洞，该文件在安装软件包时自动执行，无需导入包即可触发。PyPI 已将该软件包隔离，将暴露时间窗口限制在几小时内。 这是一次针对广泛使用的 Python 软件包的严重供应链攻击，展示了恶意行为者如何利用 PyPI 等受信任的分发渠道窃取敏感凭证。该漏洞在安装时自动执行的特性使其特别危险，用户可能在未采取任何明确操作的情况下就被入侵。 该漏洞隐藏在 litellm_init.pth 文件的 base64 编码中，可以窃取 SSH 密钥、云服务配置和加密货币钱包等众多敏感文件中的凭证。此次攻击似乎源于通过早期 Trivy 安全扫描器漏洞窃取的 PyPI 凭证。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一个用于与大型语言模型交互的流行 Python 库。PyPI 的.pth 文件是特殊的 Python 路径配置文件，可以在 Python 解释器启动时执行任意代码。供应链攻击针对软件分发渠道，将恶意代码注入合法软件包中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.banandre.com/blog/pypi-silent-killer-pth-file-secrets-theft">PyPI’s Silent Killer: How a . pth File Stole Your Secrets... - Banandre</a></li>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm _ init . pth in litellm...</a></li>
<li><a href="https://dev.to/diverdale/litellm-pypi-supply-chain-compromise-how-a-popular-llm-proxy-became-a-credential-stealing-backdoor-noa">LiteLLM PyPI Supply Chain Compromise: How... - DEV Community</a></li>

</ul>
</details>

**标签**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#vulnerability`

---

<a id="item-2"></a>
## [利用报废零件在桌面上运行特斯拉 Model 3 计算机](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 8.0/10

一名开发者利用事故车辆的报废零件，成功在桌面环境下运行特斯拉 Model 3 的计算机系统，展示了特斯拉硬件在车辆外再利用的可行性。该项目还揭示了特斯拉的'Root 访问计划'，该计划为发现安全漏洞的研究人员提供 SSH 证书。 这展示了特斯拉专有硬件在研究和逆向工程中的可及性，可能为汽车计算和安全领域带来新发现。同时也揭示了特斯拉与其他科技公司相比在安全研究激励方面的独特做法。 该项目在机械连接器方面遇到挑战，特别是 6 针连接器，尽管拥有接线原理图。项目中使用的特斯拉 Hardware 3 计算机采用了 2019 年取代 NVIDIA 硬件的特斯拉定制 FSD 芯片。

hackernews · driesdep · Mar 25, 21:11

**背景**: 特斯拉的 Autopilot 硬件从使用 NVIDIA 的 Drive PX 2 平台发展到 2019 年开始采用定制设计的 FSD 芯片。该公司提供安全研究计划，为符合条件的研究人员提供对其车辆的永久 root 访问权限，类似于苹果的安全研究设备计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware">Tesla Autopilot hardware - Wikipedia</a></li>
<li><a href="https://www.autopilotreview.com/tesla-custom-ai-chips-hardware-3/">Tesla Hardware 3 (Full Self-Driving Computer) Detailed</a></li>
<li><a href="https://applyingai.com/2025/07/decoding-teslas-core-ai-and-hardware-architecture-a-ceos-perspective/">Decoding Tesla’s Core AI and Hardware Architecture: A CEO’s ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出特斯拉的 root 访问计划与苹果安全研究计划的相似之处。一些人讨论了汽车连接器的技术挑战，而另一些人则指出 LVDS 电缆在汽车应用之外的通用性。还有人讨论了机械连接器问题的潜在 3D 打印解决方案。

**标签**: `#automotive`, `#reverse-engineering`, `#tesla`, `#embedded-systems`, `#hardware-hacking`

---

<a id="item-3"></a>
## [ARC-AGI-3 发布，成为评估通用人工智能的新基准](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

ARC-AGI-3 基准测试于 2026 年 3 月 25 日发布，包含 150 多个环境中的 1000 多个关卡，旨在通过交互式推理任务测试 AI 的探索、学习、规划和适应能力。 该基准测试通过关注新颖问题解决而非模式识别，代表了 AGI 评估的重大转变，可能暴露当前 AI 系统在实现类人智能方面的根本局限。 该基准测试使用普遍可获取的认知基元作为输入，并将 AI 表现与人类基线进行比较，但其评分方法（使用次优人类表现作为参考）引发了争议。

hackernews · lairv · Mar 25, 18:16

**背景**: AGI（通用人工智能）指能像人类一样理解、学习并跨领域应用知识的 AI 系统。传统 AI 基准测试通常衡量狭窄能力，而 ARC-AGI-3 旨在评估更普遍的认知能力。该基准由 François Chollet 和 ARC Prize 基金会开发，以解决当前 AI 评估方法的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3/">ARC-AGI-3</a></li>
<li><a href="https://www.fastcompany.com/91515360/arc-prize-foundation-new-ai-benchmark">Exclusive: This new benchmark could expose AI’s biggest weakness - Fast Company</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一，有人赞赏基准测试对真实问题解决的关注，也有人批评其人类基线方法。显著争论包括 AI 是否需要复制人类学习机制来实现 AGI，并类比飞机不需要像鸟一样拍打翅膀。

**标签**: `#AGI`, `#AI-benchmarks`, `#machine-learning`, `#research`, `#cognitive-science`

---

<a id="item-4"></a>
## [欧盟坚持推动扫描私人信息引发隐私争议](https://fightchatcontrol.eu/?foo=bar) ⭐️ 8.0/10

尽管欧洲议会 3 月 11 日投票支持在司法监督下进行针对性监控而非全面监控，欧盟仍试图延长允许自愿扫描私人通信的(EU) 2021/1232 号法规。 该法规在缺乏充分保障的情况下允许对私人通信进行大规模监控，威胁 4.5 亿欧盟公民的数字基本权利，为政府在数字领域的过度干预开创危险先例。 拟议的延期将保留 2021 年首次引入的'自愿'扫描条款，而欧洲议会提出的要求司法介入进行针对性监控的替代方案遭到理事会拒绝，导致立法僵局。

hackernews · MrBruh · Mar 25, 20:27

**背景**: 自 2013 年美国监控计划曝光以来，欧盟的大规模监控一直存在争议。当前的'聊天控制 1.0'措施是 2021 年临时实施的，源于安全需求与《欧洲人权公约》隐私权保护之间的平衡争论。欧盟法院此前曾以不成比例为由否决过类似的大规模数据保留法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mass_surveillance">Mass surveillance - Wikipedia</a></li>
<li><a href="https://www.statewatch.org/news/2024/june/policing-by-design-the-latest-eu-surveillance-plan/">Statewatch | Policing by design: the latest EU surveillance plan</a></li>
<li><a href="https://fra.europa.eu/en/news/2025/mass-surveillance-case-law-factsheet">Mass surveillance case law factsheet | European Union Agency for Fundamental Rights</a></li>

</ul>
</details>

**社区讨论**: 评论显示出对隐私侵蚀的深切担忧，有人指出匈牙利的支持是'危险信号'。其他人质疑为何不推进支持隐私的立法，而技术贡献者则澄清这是延长现有临时措施而非创造新权力。

**标签**: `#privacy`, `#EU-regulation`, `#digital-rights`, `#surveillance`, `#legislation`

---

<a id="item-5"></a>
## [包管理器引入依赖冷却机制应对供应链攻击](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 8.0/10

包括 pnpm、Yarn、Bun、Deno、uv、pip 和 npm 在内的主流包管理器近期都实现了依赖冷却功能，延迟安装新发布的软件包以便进行安全检查。这一举措源于近期 PyPI 上 LiteLLM 恶意软件包等供应链攻击事件。 依赖冷却机制通过设置缓冲期来检测潜在的问题软件包，为防御供应链攻击提供了重要保障。这解决了现代软件开发中的一个关键漏洞——即时依赖更新可能快速传播恶意代码。 具体实现各有不同：pnpm 采用 minimumReleaseAge（分钟计）、Yarn 使用 npmMinimalAgeGate、Bun 通过 bunfig.toml 配置，而 pip 目前仅支持绝对时间戳。多数方案都允许通过白名单（如 pnpm 的 minimumReleaseAgeExclude）为受信任包设置例外。

rss · Simon Willison · Mar 24, 21:11

**背景**: 依赖冷却指有意延迟安装新发布的软件包版本，以便留出时间进行社区审查。这一概念在多次重大供应链攻击后变得紧迫，这些攻击中攻击者通过入侵维护者账户向流行软件包推送恶意更新。包管理器现在正将这一安全措施直接集成到工具中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://pnpm.io/blog/releases/10.16">pnpm 10.16 | pnpm</a></li>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI - FutureSearch</a></li>

</ul>
</details>

**标签**: `#package-managers`, `#security`, `#supply-chain`, `#devops`, `#dependencies`

---

<a id="item-6"></a>
## [流式专家技术让大型混合专家模型在受限硬件上运行成为可能](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

研究人员成功实现了流式专家技术，在内存受限的设备（包括 96GB 内存的 MacBook Pro 和 iPhone）上运行 Qwen3.5-397B-A17B 和 Kimi K2.5 等大型混合专家模型。该方法通过在处理每个 token 时从 SSD 流式加载所需的专家权重。 这一突破显著降低了运行先进 AI 模型的硬件门槛，使强大的混合专家架构能够在消费级设备上运行。这将有助于普及高级 AI 能力，并在云端连接受限的场景下实现新的边缘计算应用。 Qwen3.5-397B-A17B 模型最初在 48GB 内存中运行，而具有 1 万亿参数的 Kimi K2.5（同时激活 320 亿参数）则在 96GB 内存的 M2 Max MacBook Pro 上展示。性能从 iPhone 上的 0.6 token/秒到 128GB M4 Max 上的约 1.7 token/秒不等。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家(MoE)模型是一种 AI 架构，它使用专门的子网络（'专家'）处理不同输入，每个 token 只激活相关专家以提高效率。传统 MoE 实现需要将所有专家权重加载到内存中，这使得大型模型在内存受限的设备上不切实际。流式专家方法在推理过程中动态从存储中加载所需的专家权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://openreview.net/forum?id=stXtBqyTWX&noteId=p7ADDxdU8g">Toward Efficient Inference for Mixture of Experts | OpenReview</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#hardware-optimization`, `#streaming`

---

<a id="item-7"></a>
## [Apifox 桌面端遭供应链投毒攻击，窃取 SSH 密钥与 Git 凭证](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 8.0/10

Apifox 桌面端遭供应链投毒攻击，攻击者篡改其 CDN 上的统计脚本并注入恶意代码，窃取 SSH 密钥、Git 凭证、Shell 历史记录及进程列表等敏感信息。该攻击自 3 月 4 日起活跃，影响 Windows、macOS 和 Linux 三平台用户。 这是影响广泛使用的 API 开发工具的高危安全事件，可能泄露开发者敏感凭证并引发横向攻击。针对开发工具的供应链攻击可能对软件生态系统产生连锁反应。 安全研究员 phith0n 已逆向分析恶意载荷。用户可检查 Network Persistent State 文件中是否含'apifox.it.com'或在 LevelDB 中查找'rl_mc'/'rl_headers'键值确认是否受影响。官方建议封禁恶意域名并重新安装最新版本。

telegram · zaihuapd · Mar 25, 11:10

**背景**: Apifox 是集文档、调试和测试功能于一体的流行 API 平台。LevelDB 是 Chromium 系应用用于持久化数据的键值存储库。供应链攻击通过污染软件分发渠道感染下游用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.apifox.com/download">下载 Apifox - Windows macOS Linux 桌面版下载</a></li>
<li><a href="https://en.wikipedia.org/wiki/LevelDB">LevelDB - Wikipedia</a></li>
<li><a href="https://phoenix.security/teampcp-supply-chain-attack-trivy-checkmarx-github-actions-npm-canisterworm/">TeamPCP Supply Chain Attack: Trivy to Checkmarx to npm (2026)</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain-attack`, `#devtools`, `#api`, `#vulnerability`

---

<a id="item-8"></a>
## [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 8.0/10

中国计算机学会发表声明，反对 NeurIPS 2026 会议禁止受美国制裁机构投稿的政策，并呼吁中国学者抵制该会议。学会表示若不及时改正，将考虑把 NeurIPS 移出《中国计算机学会推荐国际学术会议和期刊目录》。 这一对峙凸显了 AI 研究领域学术自由与地缘政治限制间日益紧张的矛盾，可能重塑国际科研合作模式。作为顶级 AI 会议，这一冲突可能严重影响全球研究成果传播和中国学者参与顶尖学术论坛。 NeurIPS 2026 在投稿指南中明确禁止部分受美国制裁机构投稿。CCF 推荐目录在中国学术评价体系中具有重要影响力，其可能将 NeurIPS 除名的决定构成实质性威胁。

telegram · zaihuapd · Mar 25, 14:07

**背景**: NeurIPS（神经信息处理系统大会）是全球最具声望的 AI 会议之一，始于 1987 年。中国计算机学会推荐目录是中国计算机学界学术评价的官方基准，影响研究者的发表策略和职业发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neurips.cc/">NeurIPS - 2026 Conference</a></li>
<li><a href="https://ccf.atom.im/">中国计算机学会推荐国际学术会议和期刊目录（2026） 中国计算机学会推荐国际学术会议和期刊目录CCF-A（2025年使用） 重磅更新！CCF 第七版国际学术会议 / 期刊目录（2026.3）发布，收藏备... 中国计算机学会推荐国际学术会议和期刊目录 （2026年）-辽宁工程技术... 刚刚！2026年中国计算机学会 (CCF) 推荐A-B-C类期刊目录公示！_调整_... 科学网-重磅更新！CCF 第七版国际学术会议 / 期刊目录（2026.3）发布...</a></li>

</ul>
</details>

**标签**: `#AI`, `#NeurIPS`, `#Academic Freedom`, `#Politics`, `#Research Ethics`

---

<a id="item-9"></a>
## [苹果与谷歌达成合作，将 Gemini AI 整合至 Siri](https://t.me/zaihuapd/40506) ⭐️ 8.0/10

苹果与谷歌宣布达成多年合作协议，谷歌的 Gemini AI 模型将为下一代 Apple Foundation Models 提供技术支持，增强 Siri 的功能，同时保持设备端和私有云处理以保护隐私。该合作将支持苹果今年推出的新智能功能。 这一合作将苹果以隐私为核心的生态系统与谷歌先进的 Gemini AI 相结合，可能打造出功能强大且注重隐私的 AI 助手。这可能会重塑与亚马逊 Alexa 和微软 Copilot 等其他 AI 助手的竞争格局。 整合将使用多个 Gemini 模型变体（Pro、Deep Think、Flash），同时通过设备端处理和私有云计算保持苹果的隐私标准。苹果强调这不会影响现有的隐私保护措施。

telegram · zaihuapd · Mar 25, 16:32

**背景**: Gemini 是谷歌的多模态大语言模型系列，接替了 LaMDA 和 PaLM 2，能够处理文本、图像、音频和视频。Apple Foundation Models 是设备端的大语言模型，通过本地而非云端处理数据来保护隐私，为苹果智能功能提供支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Apple`, `#Google`, `#Siri`, `#Gemini`

---

<a id="item-10"></a>
## [对 AI 驱动开发中速度优先于质量的批判](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Pi agent 框架创建者 Mario Zechner 批评了 AI 驱动软件开发中不受控制的速度，警告快速生成的代理代码会积累'认知债务'。他主张在架构决策中刻意放慢速度并加强人工监督。 这揭示了智能体工程中的一个关键矛盾：虽然 AI 代理极大加速了编码，但不受控制的使用可能产生无法维护的系统。随着组织越来越多地采用没有防护措施的 AI 编码助手，这一批判引起了共鸣。 Pi 框架(被 OpenClaw 使用)支持 30 多种代理类型，但强调范围化内存和基于 SQLite 的状态跟踪。Zechner 特别警告不要自动化架构/API 决策，建议设置与审查能力相匹配的每日代码生成限制。

rss · Simon Willison · Mar 25, 21:47

**背景**: 智能体工程指 AI 代理在最少人工监督下自主规划和执行任务的系统。Pi 框架是构建此类代理的开源工具，具有持久化内存和上下文管理功能。认知债务描述了在没有适当评估的情况下快速积累技术决策所导致的心理负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/24601/agent-deep-research">GitHub - 24601/ agent -deep-research: Deep research (CLI and agent ...)</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://addyosmani.com/blog/agentic-engineering/">Agentic Engineering - AddyOsmani.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#software-engineering`, `#ethics`, `#automation`, `#productivity`

---

<a id="item-11"></a>
## [LiteLLM PyPI 攻击事件影响 47000 次下载](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 7.0/10

分析显示，被入侵的 LiteLLM PyPI 软件包（版本 1.82.7 和 1.82.8）在其可用的 46 分钟内被下载了 46,996 次，其中 88%的依赖项目未能正确实施版本锁定，本可避免这一漏洞利用。 该事件暴露了 Python 软件包供应链中的关键漏洞，展示了恶意软件包的快速传播能力，以及依赖管理实践的普遍失效——这些实践本可降低此类风险。 攻击通过.pth 文件实现持久化多阶段凭证窃取，威胁方被确认为 TeamPCP。BigQuery PyPI 数据集在量化影响范围方面发挥了关键作用。

rss · Simon Willison · Mar 25, 17:21

**背景**: LiteLLM 是一个流行的 Python 包，为各种大语言模型(LLM)提供统一接口。PyPI(Python 包索引)是 Python 软件包的官方仓库，版本锁定是指在 requirements 中明确指定软件包版本，以防止自动更新到可能存在漏洞的版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI</a></li>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential Stealer</a></li>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack: Malicious PyPI Packages | Wiz Blog</a></li>

</ul>
</details>

**标签**: `#security`, `#pypi`, `#supply-chain`, `#python`, `#packaging`

---

<a id="item-12"></a>
## [Claude Code 推出带安全保护的自动模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code 推出了自动模式，这是一种新的权限模式，在该模式下 Claude 可代表用户做出决策，同时使用 Claude Sonnet 4.6 作为分类器在执行前监控并阻止不安全操作。 这为危险的--dangerously-skip-permissions 标志提供了更安全的替代方案，在通过内置安全保护和可定制规则保持安全性的同时，实现了更自动化的工作流程。 自动模式使用 Claude Sonnet 4.6 作为独立的分类器模型在执行前审查对话，阻止超出任务范围或针对不受信任基础设施的操作。它包含涵盖测试工件、本地操作和只读操作等领域的广泛默认过滤器。

rss · Simon Willison · Mar 24, 23:57

**背景**: Claude Code 是由 Anthropic 的 Claude AI 模型驱动的软件开发工具。--dangerously-skip-permissions 标志之前用于绕过所有权限检查，但存在重大安全风险。Claude Sonnet 4.6 是一个针对多步骤工作流程和条件逻辑优化的大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet 4.6 \ Anthropic</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**标签**: `#AI`, `#code-safety`, `#permissions`, `#Claude`

---

<a id="item-13"></a>
## [拼多多官宣‘新拼姆’：三年投入 1000 亿元转向品牌自营](https://m.tmtpost.com/nictation/7929040.html) ⭐️ 7.0/10

拼多多宣布启动‘新拼姆’计划，未来三年将投入 1000 亿元现金，从平台化运营转向品牌自营，首期已注资 150 亿元。该项目旨在整合拼多多和 Temu 的供应链资源，系统性孵化面向全球市场的自营品牌。 这是拼多多的重大战略转型，通过直接掌控品牌和供应链，可能提升其盈利能力和全球市场竞争力。此举也预示着跨境电商业内竞争加剧，尤其是与亚马逊、Shein 等对手的角逐。 该项目已在上海成立专项公司，重点孵化针对不同市场和品类的自营品牌。这是赵佳臻 2023 年 12 月出任联席董事长后推动的首个重大战略落地。

telegram · zaihuapd · Mar 25, 12:37

**背景**: 拼多多是中国主流电商平台，以拼团模式闻名；Temu 是其国际站，主打全球低价商品。品牌自营模式让平台绕过第三方卖家，直接掌控利润和品控，类似亚马逊的‘Basics’和天猫超市的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Temu">Temu - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1366554522003283">How does manufacturer’s self-operating channel interact with ...</a></li>

</ul>
</details>

**标签**: `#e-commerce`, `#supply-chain`, `#business-strategy`, `#china-tech`, `#retail`

---

<a id="item-14"></a>
## [GitHub 更新 Copilot 数据政策：免费与个人付费版默认纳入 AI 模型训练，可手动退出](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) ⭐️ 7.0/10

GitHub 宣布自 4 月 24 日起更新 Copilot 数据使用政策：Copilot Free、Pro 和 Pro+用户的输入、输出、代码片段及相关上下文将默认用于 AI 模型训练，用户可在隐私设置中手动退出；企业版用户及自有代码库不受影响。 这一变更大幅扩展了 GitHub AI 模型的训练数据来源，可能提升 Copilot 性能，但也引发开发者隐私担忧。它体现了行业利用用户交互优化 AI 工具的趋势，需在创新与用户控制间取得平衡。 训练数据包含光标附近代码上下文、注释、文件名、仓库结构、导航模式及建议反馈。数据可能与微软共享但不会提供给第三方 AI 服务商。已关闭数据收集的用户设置将保持原状。

telegram · zaihuapd · Mar 26, 00:47

**背景**: GitHub Copilot 是由 GitHub 和 OpenAI 联合开发的 AI 代码补全工具。许多 AI 系统通过用户交互数据进行机器学习来改进性能，但需平衡模型优化与隐私保护。此次退出机制与 Anthropic 的 Claude 等 AI 服务的做法类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/">Updates to GitHub Copilot interaction data usage policy</a></li>
<li><a href="https://www.windowscentral.com/software-apps/microsofts-github-is-going-to-start-using-copilot-interactions-to-train-ai-models-and-its-starting-soon">GitHub is going to use Copilot interactions to train its AI</a></li>
<li><a href="https://magazine.mindplex.ai/post/anthropic-will-include-user-interactions-in-claudes-training-data">Anthropic will include user interactions in Claude's training ... | Mindplex</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI`, `#Privacy`, `#Copilot`, `#DataPolicy`

---