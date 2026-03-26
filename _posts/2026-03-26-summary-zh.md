---
layout: default
title: "Horizon Summary: 2026-03-26 (ZH)"
date: 2026-03-26
lang: zh
---

> From 42 items, 13 important content pieces were selected

---

1. [LiteLLM 1.82.8 中的恶意 litellm_init.pth 文件窃取凭证](#item-1) ⭐️ 9.0/10
2. [Apifox 桌面端遭供应链投毒攻击](#item-2) ⭐️ 9.0/10
3. [黑客利用报废零件在桌面上运行特斯拉 Model 3 车载电脑](#item-3) ⭐️ 8.0/10
4. [ARC-AGI-3 发布新的人工通用智能基准测试](#item-4) ⭐️ 8.0/10
5. [欧盟不顾反对继续推进私密信息扫描计划](#item-5) ⭐️ 8.0/10
6. [LiteLLM PyPI 漏洞影响 47000 次下载](#item-6) ⭐️ 8.0/10
7. [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿](#item-7) ⭐️ 8.0/10
8. [苹果与谷歌达成合作，Gemini AI 将为 Siri 提供支持](#item-8) ⭐️ 8.0/10
9. [一篇被广泛引用的商学院论文因虚假声明遭批评](#item-9) ⭐️ 7.0/10
10. [对 AI 辅助编码无节制速度的批判](#item-10) ⭐️ 7.0/10
11. [Claude Code 推出带安全保护的自动模式](#item-11) ⭐️ 7.0/10
12. [包管理器引入依赖冷却机制应对供应链攻击](#item-12) ⭐️ 7.0/10
13. [GitHub 更新 Copilot 数据政策：免费与个人付费用户数据默认纳入 AI 训练，可手动退出](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM 1.82.8 中的恶意 litellm_init.pth 文件窃取凭证](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

PyPI 上的 LiteLLM v1.82.8 包被植入了一个隐藏在 litellm_init.pth 文件中的凭证窃取程序，安装时即会激活，无需导入包。PyPI 已将该包隔离，将暴露时间限制在几小时内。 这一事件凸显了针对广泛使用的 Python 包的严重供应链攻击，可能危及多个平台和服务的敏感凭证。攻击的复杂性和广泛影响凸显了开源软件分发中日益增长的风险。 恶意负载采用 base64 编码，针对包括 SSH 密钥、云服务配置和加密货币钱包在内的多种凭证。攻击可能源自通过之前对 Trivy 安全扫描器的漏洞利用窃取的 PyPI 凭证。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一个用于与大型语言模型（LLM）交互的流行 Python 库。Python 中的 .pth 文件是特殊的文件，在 Python 启动时执行代码，通常用于路径配置，但可能被滥用于恶意目的。PyPI 的隔离功能是一种安全措施，用于临时限制对潜在有害包的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Mar/24/malicious-litellm/">Malicious litellm_init.pth in litellm 1.82.8 — credential stealer</a></li>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI - FutureSearch</a></li>
<li><a href="https://www.upwind.io/feed/litellm-pypi-supply-chain-attack-malicious-release">LiteLLM Supply Chain Breakdown - Upwind Security</a></li>

</ul>
</details>

**标签**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#vulnerability`

---

<a id="item-2"></a>
## [Apifox 桌面端遭供应链投毒攻击](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 9.0/10

Apifox 桌面端遭到供应链攻击，攻击者篡改了其 CDN 上的事件统计脚本并注入恶意代码，窃取受害主机的 SSH 密钥、Git 凭证、Shell 历史记录及进程列表等敏感信息。该攻击自 3 月 4 日起活跃，Windows、macOS 和 Linux 用户均受影响。 此次攻击影响重大，因为 Apifox 是广泛使用的 API 开发工具，被窃取的凭证可能导致攻击者对开发者系统和基础设施发起进一步的横向攻击。针对开发工具的供应链攻击已变得越来越普遍且危险。 安全研究员 phith0n 已独立分析并公开了恶意载荷的细节。用户可通过检查 Apifox 数据目录中的 LevelDB 条目或 Network Persistent State 文件来确认是否受影响。官方缓解措施包括封禁恶意域名并重新安装最新版本。

telegram · zaihuapd · Mar 25, 11:10

**背景**: Apifox 是一个集成了 Postman、Swagger 和 JMeter 功能的 API 开发平台。针对 CDN 托管脚本的供应链攻击已成为重大安全隐患，近期 Polyfill.io 事件就是典型案例。LevelDB 是许多应用用于本地数据存储的键值数据库库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://censys.com/blog/july-2-polyfill-io-supply-chain-attack-digging-into-the-web-of-compromised-domains/">July 2: Polyfill.io Supply Chain Attack - Digging into the Web of Compromised Domains - Censys</a></li>
<li><a href="https://github.com/google/leveldb">GitHub - google/leveldb: LevelDB is a fast key-value storage library written at Google that provides an ordered mapping from string keys to string values. · GitHub</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain-attack`, `#api-tools`, `#devops`, `#malware`

---

<a id="item-3"></a>
## [黑客利用报废零件在桌面上运行特斯拉 Model 3 车载电脑](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 8.0/10

一名研究人员利用事故车辆的零部件成功逆向工程并启动了特斯拉 Model 3 的车载电脑，揭示了特斯拉专有硬件和软件架构的细节。 这一突破为特斯拉封闭的车载计算系统提供了罕见的研究视角，既促进了安全研究和第三方开发，也凸显了现代车辆的可维修性挑战。 该项目涉及与特斯拉定制 FSD 芯片（硬件 3.0 版本）和 LVDS 显示接口的交互，特斯拉漏洞赏金计划还通过其安全研究项目为合格研究人员提供 root 访问权限。

hackernews · driesdep · Mar 25, 21:11

**背景**: 特斯拉硬件 3.0 是与 Mobileye 分道扬镳后自主研发的 AI 加速芯片，采用双神经网络处理器支持自动驾驶功能。现代车辆越来越多采用将多个 ECU 整合的高性能域控制器架构，这使得逆向工程更复杂但对安全研究更具价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware">Tesla Autopilot hardware - Wikipedia</a></li>
<li><a href="https://www.autopilotreview.com/tesla-custom-ai-chips-hardware-3/">Tesla Hardware 3 (Full Self-Driving Computer) Detailed</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reverse_engineering">Reverse engineering - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这与苹果安全研究设备计划的相似性，分享了汽车诊断工具的使用经验，并讨论了 LVDS 线缆在笔记本和车辆中的双重用途。有用户详细描述了为特斯拉加装第三方配件时改造电气系统的经历。

**标签**: `#automotive`, `#reverse-engineering`, `#tesla`, `#embedded-systems`, `#security`

---

<a id="item-4"></a>
## [ARC-AGI-3 发布新的人工通用智能基准测试](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

ARC-AGI-3 推出了一种新的交互式推理基准测试，旨在测量 AI 的人类级别智能，将于 2026 年 3 月 25 日推出，包含 150 多个环境中的 1000 多个级别。 这一基准测试通过关注 AI 在新情境中探索、学习、规划和适应的能力，超越了传统的基于准确性的指标，代表了测量真正 AGI 的重要一步。 该基准测试将 AI 表现与人类基准进行比较，具体是以操作次数为标准的次优首次尝试人类表现，并要求具备视觉推理、路径规划和屏幕交互能力。

hackernews · lairv · Mar 25, 18:16

**背景**: AGI（人工通用智能）指的是能在多个领域达到人类水平理解、学习和应用知识的 AI 系统。AGI 基准测试具有挑战性，因为它需要测量通用问题解决能力而非特定任务表现。ARC Prize 组织一直在开发越来越复杂的基准测试来测量真正的通用智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3/">ARC - AGI - 3</a></li>
<li><a href="https://medium.com/predict/benchmarks-the-elusive-measure-of-agi-d8e3a8f2dd38">Benchmarks & the Elusive Measure of AGI | Medium</a></li>
<li><a href="https://spectrum.ieee.org/agi-benchmark">AGI Benchmarks : Tracking Progress Toward AGI ... - IEEE Spectrum</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，一些人赞扬该基准测试对人类级别智能的关注，而另一些人则批评其方法，特别是人类基准的定义。支持者认为这是测量真正智能的好方法，而批评者则将其与历史上存在缺陷的 AI 基准测试相提并论。

**标签**: `#AGI`, `#benchmarking`, `#AI-research`, `#human-comparison`, `#evaluation`

---

<a id="item-5"></a>
## [欧盟不顾反对继续推进私密信息扫描计划](https://fightchatcontrol.eu/?foo=bar) ⭐️ 8.0/10

尽管欧洲议会于 3 月 11 日投票决定用针对嫌疑人的定向监控取代大规模监控，欧盟仍试图延长允许自愿扫描私人通信的(EU) 2021/1232 号法规。拟议的'聊天控制 1.0'政策将强制要求扫描整个欧洲的加密信息。 该政策对数字隐私权和加密技术构成根本性威胁，可能建立一个可能被滥用的监控基础设施。其结果将为民主国家如何在数字时代平衡安全关切与公民自由开创先例。 当前的自愿扫描法规自 2021 年起生效，主要针对儿童性虐待材料检测。技术专家普遍警告，客户端扫描(CSS)技术会破坏端到端加密并制造安全漏洞。

hackernews · MrBruh · Mar 25, 20:27

**背景**: 聊天控制指的是欧盟要求服务提供商扫描私人通信以查找非法内容(主要针对儿童性虐待材料)的提案。这场辩论使儿童保护倡导者与隐私专家对立，后者认为这些措施实际上会破坏端到端加密并实现大规模监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.heise.de/en/news/EU-agreement-fails-Voluntary-chat-control-ends-11213083.html">EU agreement fails: "Voluntary chat control" ends - heise online</a></li>
<li><a href="https://www.eff.org/deeplinks/2025/12/after-years-controversy-eus-chat-control-nears-its-final-hurdle-what-know">After Years of Controversy, the EU’s Chat Control Nears Its ...</a></li>
<li><a href="https://www.webpronews.com/inside-the-eus-encryption-war-how-chat-control-became-europes-most-dangerous-surveillance-proposal/">Inside the EU's Encryption War: How 'Chat Control' Became ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对政策的延续表示不满，'反对聊天控制'的创建者指出议会试图限制监控。其他人质疑为何不提出支持隐私的立法，而有些人则澄清这只是延长现有的自愿扫描而非实施新的强制措施。

**标签**: `#privacy`, `#EU-policy`, `#surveillance`, `#digital-rights`, `#chat-control`

---

<a id="item-6"></a>
## [LiteLLM PyPI 漏洞影响 47000 次下载](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 8.0/10

分析显示，在 PyPI 上 46 分钟的漏洞利用窗口期内，恶意 LiteLLM 包（版本 1.82.7 和 1.82.8）被下载了 46,996 次，其中 88%的依赖包未能正确实施版本锁定。 该事件暴露了 Python 包管理中的供应链安全漏洞，未锁定的依赖项会自动拉取恶意版本，可能导致数千个项目感染窃取凭证的恶意软件。 LiteLLM 作为连接 OpenAI、Anthropic 等主流 LLM 的统一接口，其漏洞危害性极大。研究人员通过 PyPI 的 BigQuery 数据集精确追踪了下载量和依赖关系模式。

rss · Simon Willison · Mar 25, 17:21

**背景**: LiteLLM 是一个流行的 Python SDK，提供调用多种大语言模型 API 的统一接口。Python 中的版本锁定（指定精确依赖版本）是防止自动更新到潜在恶意包的安全最佳实践。PyPI 的公开 BigQuery 数据集支持对包下载统计的详细分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/litellm/">litellm · PyPI</a></li>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/ litellm : Python SDK, Proxy Server (AI Gateway) to call...</a></li>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential...</a></li>
<li><a href="https://nvie.com/posts/pin-your-packages/">Pin Your Packages - nvie.com</a></li>

</ul>
</details>

**标签**: `#security`, `#pypi`, `#supply-chain`, `#python`, `#packaging`

---

<a id="item-7"></a>
## [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 8.0/10

中国计算机学会（CCF）发表声明，反对 NeurIPS 2026 在其投稿指南中禁止受美国制裁机构投稿的政策，称此举是将学术交流政治化，并呼吁中国学者抵制该会议。 CCF 作为中国重要的学术组织，其立场可能对全球 AI 研究合作和会议政策产生重大影响，因为 NeurIPS 是顶级 AI 会议，而 CCF 的推荐会议目录对中国研究者的投稿选择具有指导作用。 CCF 威胁称，如果 NeurIPS 不修改政策，将考虑将其移出《中国计算机学会推荐国际学术会议和期刊目录》，这会减少中国学者在这一知名会议上的参与。该禁令专门针对美国制裁名单上的机构。

telegram · zaihuapd · Mar 25, 14:07

**背景**: NeurIPS（神经信息处理系统大会）是全球最具声望的 AI 研究会议之一。中国计算机学会是中国计算机科学领域的主要专业组织，拥有超过 10 万名会员。其推荐的会议目录对中国研究者选择投稿的会议具有重要影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems">Conference on Neural Information Processing Systems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/China_Computer_Federation">China Computer Federation - Wikipedia</a></li>
<li><a href="https://www.ccf.org.cn/en/About_CCF/About_CCF/">China Computer Federation -About CCF -中国计算机学会</a></li>

</ul>
</details>

**标签**: `#AI Ethics`, `#Academic Freedom`, `#NeurIPS`, `#Research Policy`, `#China-US Relations`

---

<a id="item-8"></a>
## [苹果与谷歌达成合作，Gemini AI 将为 Siri 提供支持](https://t.me/zaihuapd/40506) ⭐️ 8.0/10

苹果与谷歌宣布达成多年合作协议，谷歌的 Gemini AI 模型将为下一代 Apple Foundation Models 提供技术支持，从而增强 Siri 的功能，同时保持设备端和私有云计算的隐私标准。 这一合作可能重新定义 AI 助手领域，将苹果注重隐私的方法与谷歌先进的 Gemini AI 相结合，有望为设备端 AI 性能和用户隐私设定新标准。 整合将利用 Gemini 的多模态能力，同时确保数据保留在设备端或私有云中，符合苹果严格的隐私标准。这一合作表明苹果可能正在改变之前依赖自有模型的策略。

telegram · zaihuapd · Mar 25, 16:32

**背景**: Gemini 是谷歌推出的多模态大语言模型系列，接替了 LaMDA 和 PaLM 2，能够处理文本、图像等多种数据类型。Apple Foundation Models 是苹果 2023 年推出的设备端 AI 框架，通过本地运行为 Apple Intelligence 等功能提供支持，同时保持用户隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://machinelearning.apple.com/research/introducing-apple-foundation-models">Introducing Apple ’s On-Device and Server Foundation Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#Apple`, `#Google`, `#Siri`, `#Gemini`

---

<a id="item-9"></a>
## [一篇被广泛引用的商学院论文因虚假声明遭批评](https://statmodeling.stat.columbia.edu/2026/03/24/false-claims-in-a-published-no-corrections-no-consequences-welcome-to-the-business-school/) ⭐️ 7.0/10

统计学家 Andrew Gelman 的博客文章揭露了一篇被广泛引用的商学院论文中存在虚假的方法论声明，尽管问题已被指出，但论文未做任何修正。该论文已被引用数千次，影响了许多学者的职业生涯。 这一事件凸显了学术出版中的系统性缺陷，尤其是在商学院领域，严谨性可能因追求影响力而受损。它引发了关于研究诚信、同行评审有效性以及有影响力论文中未纠正错误的长期后果的担忧。 批评特别指出，该论文描述了一种实际上并未在研究中使用的方法论。尽管发表在管理学期刊上，但该论文的主张已被学术界广泛采用。

hackernews · qsi · Mar 26, 00:46

**背景**: 商学院研究经常面临学术严谨性与实际相关性之间的紧张关系。学术界的'不发表就出局'文化，加上将引用指标作为成功标准，形成了可能损害研究诚信的激励机制。近年来，多个学科领域对可重复性危机的担忧日益增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://statmodeling.stat.columbia.edu/2026/03/24/false-claims-in-a-published-no-corrections-no-consequences-welcome-to-the-business-school/">False claims in a widely-cited paper. No corrections. No ...</a></li>
<li><a href="https://www.ft.com/content/7e81e1b6-eb08-43de-ab71-ab6c50181cc3">Business school and the pursuit of rigour, resonance and ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s40596-024-02021-6">Fraud: A Growing Threat to Academia’s Credibility | Academic ...</a></li>

</ul>
</details>

**社区讨论**: 评论显示出不同反应：有人为论文对职业生涯的影响辩护，有人预测 AI 生成论文会进一步降低研究质量，还有人质疑具体的指控。一个反复出现的主题是对管理研究质量的怀疑以及对有缺陷工作缺乏后果的沮丧。

**标签**: `#academic-integrity`, `#peer-review`, `#research-ethics`, `#reproducibility`, `#business-school`

---

<a id="item-10"></a>
## [对 AI 辅助编码无节制速度的批判](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

OpenClaw 使用的 Pi 代理框架创建者 Mario Zechner 批评了当前 AI 辅助编码中重速度轻质量的趋势，警告当缺乏人类监督时错误会快速累积。 这揭示了现代软件开发中的一个关键挑战：AI 编码代理生成代码的速度可能超过人类审查能力，导致代码库积累难以维护的'认知债务'。 Pi 框架是一个包含 pi-ai(LLM 通信)、pi-agent-core(代理循环)和 pi-coding-agent(带工具的完整编码代理)的单体仓库。Zechner 建议手动编写架构决策，并限制每日 AI 生成的代码量以匹配审查能力。

rss · Simon Willison · Mar 25, 21:47

**背景**: 代理工程是一门新兴学科，专注于开发能够自主规划和完成任务且只需最少人类监督的 AI 系统。使用 Pi 框架构建的编码代理可以快速生成数千行代码，但这种速度会带来错误和复杂性未被注意而累积的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lucumr.pocoo.org/2026/1/31/pi/">Pi: The Minimal Agent Within OpenClaw | Armin Ronacher's Thoughts and Writings</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#software development`, `#productivity`, `#code quality`

---

<a id="item-11"></a>
## [Claude Code 推出带安全保护的自动模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code 推出了自动模式，这是一种新的权限模式，Claude 可以代表用户做出决策，同时使用 Claude Sonnet 4.6 作为分类器在执行前监控并阻止不安全操作。 这为危险的--dangerously-skip-permissions 标志提供了一个更安全的替代方案，通过防止范围扩大、基础设施定位和恶意内容执行，在自动化和安全性之间取得平衡。 自动模式包含大量默认过滤器（如阻止 git 破坏性操作和外部代码执行）并允许自定义规则。无论主会话使用何种模型，分类器都运行在 Claude Sonnet 4.6 上。

rss · Simon Willison · Mar 24, 23:57

**背景**: Claude 是由 Anthropic 开发的 AI 助手，Claude Code 是其软件开发工具。--dangerously-skip-permissions 标志以前用于绕过所有权限检查，但风险很大。Claude Sonnet 4.6 是一个专为多步骤工作流和条件逻辑优化的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://grokipedia.com/page/Claude_Sonnet_46">Claude Sonnet 4.6</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**标签**: `#AI`, `#code-assistance`, `#permissions`, `#automation`

---

<a id="item-12"></a>
## [包管理器引入依赖冷却机制应对供应链攻击](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

包括 pnpm、Yarn、Bun、Deno、uv、pip 和 npm 在内的主流包管理器近期均引入了依赖冷却功能，通过延迟安装新发布的包版本以便社区审查。这些更新主要集中在 2025 年 9 月至 2026 年 2 月间发布，其中 pip 目前仍需通过变通方案实现相对日期支持。 这种全行业采用的冷却机制通过创建缓冲期来检测恶意更新，显著提升了软件供应链安全性，近期 LiteLLM 等攻击事件已验证其必要性。各工具的协调实施反映了现代软件开发中对依赖风险的日益重视。 具体实现各有不同：pnpm 和 Bun 使用 minimumReleaseAge 参数，Yarn 采用 npmMinimalAgeGate（以分钟计），Deno 通过--minimum-dependency-age 标志实现，而 pip 的--uploaded-prior-to 目前仅支持绝对时间戳。多数系统都支持通过白名单机制为可信包设置例外。

rss · Simon Willison · Mar 24, 21:11

**背景**: 依赖冷却指在软件包发布后故意延迟更新一段时间，为社区审查留出窗口期。该实践因多起供应链攻击事件而受到重视——在这些事件中，被入侵的维护者账户推送了恶意更新并被用户立即采用。现代包管理器正将这一安全措施直接集成到工具中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/">Package Managers Need to Cool Down</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns</a></li>

</ul>
</details>

**标签**: `#package-managers`, `#security`, `#supply-chain`, `#devops`, `#dependency-management`

---

<a id="item-13"></a>
## [GitHub 更新 Copilot 数据政策：免费与个人付费用户数据默认纳入 AI 训练，可手动退出](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) ⭐️ 7.0/10

GitHub 宣布自 4 月 24 日起更新 Copilot 数据使用政策，Copilot Free、Pro 和 Pro+用户的输入、输出及代码片段将默认用于 AI 模型训练和改进，用户可在隐私设置中选择退出。企业用户及自有代码库不受此调整影响。 这一变化显著影响个人开发者的隐私，并有助于 AI 模型训练，可能提升 Copilot 性能，但也引发数据使用担忧。它体现了 GitHub 利用用户交互增强 AI 的策略，同时保持对企业数据的保护。 收集的数据包括光标附近代码上下文、注释、文件名、仓库结构、导航模式及建议反馈，可能与微软等关联公司共享，但不会提供给第三方 AI 提供商。此前已关闭数据收集的用户偏好将保留。

telegram · zaihuapd · Mar 26, 00:47

**背景**: GitHub Copilot 是一款基于 AI 的编程助手，可根据上下文建议代码补全。它提供不同层级服务，包括面向个人的免费和付费计划（Free、Pro、Pro+），以及数据控制更严格的企业/商业计划。该服务由 OpenAI 模型驱动，并与微软生态系统集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/">Updates to GitHub Copilot interaction data usage policy - The GitHub Blog</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/do-more-with-ai/general-ai/right-copilot-plan-for-you">Which Copilot Plan Is Right for You? | Microsoft Copilot</a></li>
<li><a href="https://www.theregister.com/2026/03/26/github_ai_training_policy_changes/">GitHub: We going to train on your data after all - The Register</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI`, `#Privacy`, `#Copilot`, `#Data Policy`

---