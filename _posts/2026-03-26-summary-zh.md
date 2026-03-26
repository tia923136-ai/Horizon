---
layout: default
title: "Horizon Summary: 2026-03-26 (ZH)"
date: 2026-03-26
lang: zh
---

> From 42 items, 22 important content pieces were selected

---

1. [LiteLLM v1.82.8 PyPI 软件包被植入窃取凭证的恶意代码](#item-1) ⭐️ 9.0/10
2. [Swift 6.3 正式发布：支持原生 Android 开发](#item-2) ⭐️ 9.0/10
3. [使用事故车零件在桌面上运行特斯拉 Model 3 电脑](#item-3) ⭐️ 8.0/10
4. [ARC-AGI-3 基准测试引发 AGI 衡量标准争议](#item-4) ⭐️ 8.0/10
5. [欧盟拟推动对私人信息的全面监控](#item-5) ⭐️ 8.0/10
6. [LiteLLM PyPI 软件包遭攻击影响 4.7 万次下载](#item-6) ⭐️ 8.0/10
7. [专家权重流式传输技术让万亿参数模型可在消费级设备上运行](#item-7) ⭐️ 8.0/10
8. [Arm 将首次销售自研 AI 芯片，Meta 成首个主要客户，台积电代工](#item-8) ⭐️ 8.0/10
9. [NASA 暂停月球轨道空间站，转向 2029 年前建立月球基地](#item-9) ⭐️ 8.0/10
10. [谷歌研究院推出 TurboQuant，将大模型 KV 缓存压缩至 3 比特](#item-10) ⭐️ 8.0/10
11. [Apifox 桌面端遭供应链投毒攻击：CDN 脚本被篡改窃取敏感数据](#item-11) ⭐️ 8.0/10
12. [苹果与谷歌达成合作，Gemini AI 将为 Siri 提供支持](#item-12) ⭐️ 8.0/10
13. [美国最高法院裁定 ISP 无需为用户版权侵权行为负责](#item-13) ⭐️ 7.0/10
14. [对 AI 驱动编码速度与质量权衡的批判](#item-14) ⭐️ 7.0/10
15. [Claude Code 推出带安全保护的自动模式](#item-15) ⭐️ 7.0/10
16. [包管理器纷纷引入依赖冷却机制](#item-16) ⭐️ 7.0/10
17. [Claude Code 推出自动模式：AI 自主决策权限，内置安全审查](#item-17) ⭐️ 7.0/10
18. [腾讯撤销 AI Lab 并引入字节 Seed 骨干推进混元升级](#item-18) ⭐️ 7.0/10
19. [拼多多官宣‘新拼姆’：三年投入 1000 亿元转型品牌自营](#item-19) ⭐️ 7.0/10
20. [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿，呼吁抵制](#item-20) ⭐️ 7.0/10
21. [英特尔和 AMD 通知中国客户：服务器 CPU 交付周期将延长](#item-21) ⭐️ 7.0/10
22. [GitHub 更新 Copilot 数据政策：免费与个人付费版默认纳入 AI 训练，可手动退出](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM v1.82.8 PyPI 软件包被植入窃取凭证的恶意代码](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

PyPI 上的 LiteLLM v1.82.8 软件包被发现包含一个恶意的 litellm_init.pth 文件，该文件在安装时自动执行窃取凭证的脚本，无需导入该软件包。此次攻击源于 PyPI 凭证被盗，可能是通过之前对 Trivy 安全扫描器的漏洞利用实现的。 这是一次影响广泛使用的 Python 软件包的关键供应链攻击，可能窃取包括 SSH 密钥、云服务凭证和加密货币钱包在内的敏感凭证。安装时自动执行的特性使其特别危险，因为用户无需主动使用该软件包就会受到攻击。 该恶意软件使用多层 base64 混淆，针对各种系统中的超过 25 种凭证文件。PyPI 迅速隔离了该软件包，将暴露窗口限制在几小时内。版本 1.82.7 也有类似漏洞，但需要导入软件包才会激活。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是一个用于与大型语言模型交互的热门 Python 库。.pth 文件是特殊的 Python 路径配置文件，会在 Python 启动时执行。PyPI 是 Python 的官方第三方软件包仓库，使其成为供应链攻击的主要目标。此次攻击似乎与 LiteLLM CI 管道中使用的安全扫描器 Trivy 最近被入侵有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 — credential stealer · Issue #24512 · BerriAI/litellm</a></li>
<li><a href="https://www.stepsecurity.io/blog/litellm-credential-stealer-hidden-in-pypi-wheel">litellm: Credential Stealer Hidden in PyPI Wheel - StepSecurity</a></li>
<li><a href="https://www.ox.security/blog/litellm-malware-malicious-pypi-versions-steal-cloud-and-crypto-credentials/">Malicious LiteLLM Packages Steal AWS & Crypto Keys</a></li>

</ul>
</details>

**社区讨论**: GitHub 问题讨论显示开发者对这种复杂攻击手段和目标广泛的凭证窃取行为深感担忧。许多人呼吁改进 PyPI 发布流程的安全措施，并加强对软件包变更的监控。

**标签**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#malware`

---

<a id="item-2"></a>
## [Swift 6.3 正式发布：支持原生 Android 开发](https://swift.org/blog/swift-6.3-released/) ⭐️ 9.0/10

Swift 6.3 于 2026 年 3 月 25 日正式发布，首次推出官方 Swift SDK for Android，开发者可使用 Swift 编写原生 Android 应用，或通过 Swift Java 插件将代码集成到现有的 Kotlin/Java 应用中。 这是跨平台开发的重大突破，移动开发团队现在可以使用 Swift 同时开发 iOS 和 Android 应用，减少对独立代码库的需求，并简化开发流程。 Swift Java 插件简化了 JNI 代码的编写和从 Swift 调用 Java 的过程，而 Swift SDK for Android 是 Swift.org 官方项目的一部分，由苹果开源团队支持。

telegram · zaihuapd · Mar 25, 03:45

**背景**: Swift 是苹果公司为 iOS、macOS 和其他苹果平台开发的编程语言。在此之前，Android 应用通常使用 Kotlin 或 Java 开发，而 iOS 应用使用 Swift，导致跨平台开发需要维护独立的代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/tomholmes96_announcing-the-swift-sdk-for-android-activity-7388557917077008384-9DEO">Announcing the Swift SDK for Android | Tom Holmes</a></li>
<li><a href="https://levelup.gitconnected.com/swift-on-android-how-the-new-swift-sdk-unlocks-real-cross-platform-mobile-development-0b4b79d476aa">Swift on Android : How the New Swift SDK Unlocks... | Level Up Coding</a></li>
<li><a href="https://github.com/swiftlang/swift-java">GitHub - swiftlang/swift-java: Java interopability support ...</a></li>

</ul>
</details>

**标签**: `#Swift`, `#Android`, `#Cross-platform`, `#Mobile Development`, `#Programming Languages`

---

<a id="item-3"></a>
## [使用事故车零件在桌面上运行特斯拉 Model 3 电脑](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 8.0/10

一名黑客成功使用事故车零件在桌面上运行特斯拉 Model 3 的电脑系统，并揭示了特斯拉的 root 访问计划——该计划向符合条件的安全研究人员提供永久 SSH 证书。 该项目展示了汽车计算系统日益增长的研究可及性，并突显了特斯拉通过 root 访问漏洞赏金计划推动安全研究的独特方式，这可能加速漏洞发现。 该项目揭示了特斯拉车辆使用捆扎线束而非单独线缆的细节，且 root 访问计划要求研究人员必须先发现有效的 root 漏洞才能获得对自己车辆的永久 SSH 访问权限。

hackernews · driesdep · Mar 25, 21:11

**背景**: 特斯拉的全自动驾驶(FSD)计算机(Hardware 3)自 2019 年起使用内部开发定制 AI 芯片，取代了之前的 NVIDIA 硬件。该系统通过神经网络处理摄像头、雷达和传感器数据来驱动所有自动驾驶功能。特斯拉的 root 访问计划类似苹果的安全研究设备计划，但具有车辆特定的资格要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Model_3">Tesla Model 3 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware">Tesla Autopilot hardware - Wikipedia</a></li>
<li><a href="https://www.autopilotreview.com/tesla-custom-ai-chips-hardware-3/">Tesla Hardware 3 (Full Self-Driving Computer) Detailed - AutoPilot Review</a></li>
<li><a href="https://hackaday.com/2024/01/05/getting-root-access-on-a-telsa/">Getting Root Access On A Tesla | Hackaday</a></li>

</ul>
</details>

**社区讨论**: 评论显示人们对线束发现的惊讶，与汽车开发测试台的比较，以及关于特斯拉 root 访问计划类似苹果安全研究计划的讨论。有人指出 LVDS 线缆在笔记本电脑中很常见却被称作'汽车专用'的讽刺。

**标签**: `#hardware-hacking`, `#automotive`, `#reverse-engineering`, `#tesla`, `#security`

---

<a id="item-4"></a>
## [ARC-AGI-3 基准测试引发 AGI 衡量标准争议](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

ARC-AGI-3 技术报告发布了一个新的交互式推理基准测试，包含 150 多个环境中的 1000 多个关卡，将 AI 表现与人类解谜能力进行对比。其采用独特的评分系统，将人类基准定义为按操作次数计算的第二优首次尝试人类表现。 这代表了创建标准化 AGI 衡量框架的最雄心勃勃的尝试之一，可能重塑我们评估 AI 向人类水平发展的进程。其方法论引发了关于什么真正构成人工通用智能的重要讨论。 该基准测试专注于需要在多样化环境中进行探索、学习、规划和适应的代理智能。批评者指出人类对比方法可能存在问题，因为它不使用平均人类表现作为基准。

hackernews · lairv · Mar 25, 18:16

**背景**: ARC(对齐研究中心)是一个专注于 AI 安全和对齐研究的非营利组织。AGI(人工通用智能)指能够执行人类任何智力任务的 AI 系统。由于缺乏对正确测量方法的共识，AGI 进展的基准测试仍然存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3/">ARC-AGI-3</a></li>
<li><a href="https://www.lumenova.ai/blog/artificial-general-intelligence-measuring-agi/">The Path to AGI : How Do We Know When We’re There? | Lumenova AI</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-general-intelligence">What is Artificial General Intelligence ( AGI )? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，一些人称赞基准测试的严谨性，而另一些人则批评其人类对比方法。值得注意的辩论包括是否应该将专业 AI 表现与人类通用智能进行比较，经常提到飞机与鸟类的类比。

**标签**: `#AGI`, `#AI-benchmarking`, `#human-comparison`, `#research-methodology`, `#cognitive-tasks`

---

<a id="item-5"></a>
## [欧盟拟推动对私人信息的全面监控](https://fightchatcontrol.eu/?foo=bar) ⭐️ 8.0/10

尽管欧洲议会于 3 月 11 日投票决定用针对嫌疑人的定向监控取代全面监控，欧盟仍试图延长允许自愿扫描私人通信的'聊天控制 1.0'法规。 这对欧洲的数字隐私权构成重大威胁，可能在安全名义下使全面监控常态化，影响所有欧盟公民的基本权利。 拟议的延期将延续自 2021 年起实施的(EU) 2021/1232 号法规，该法规允许自愿扫描私人通信。由于人权担忧和缺乏有效性证据，该措施面临反对。

hackernews · MrBruh · Mar 25, 20:27

**背景**: 自移民危机和恐怖袭击以来，欧盟一直在安全与隐私之间寻求平衡。'聊天控制'措施源于对网络儿童剥削的担忧，但已扩展到更广泛的监控。欧盟此前曾通过倡导以人为本方法的数字权利原则，使得此次监控推动尤为争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://repository.gchumanrights.org/items/515f3276-e4b2-4398-9c6c-904f17e95b33">From sleepwalking into surveillance societies to drifting into...</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-principles">European Digital Rights and Principles - Shaping Europe’s ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0267364923000560">The transformative nature of the EU Declaration on Digital ...</a></li>

</ul>
</details>

**社区讨论**: 评论显示强烈反对意见，Fight Chat Control 的创建者称情况'令人震惊'。有人建议起草保护私人通信的反向立法，也有人批评欧盟日益增长的控制欲。一位用户指出匈牙利的支持是该提案的负面指标。

**标签**: `#privacy`, `#EU`, `#surveillance`, `#digital-rights`, `#policy`

---

<a id="item-6"></a>
## [LiteLLM PyPI 软件包遭攻击影响 4.7 万次下载](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 8.0/10

分析显示，在 46 分钟窗口期内，被入侵的 LiteLLM PyPI 软件包（版本 1.82.7 和 1.82.8）被下载了 46,996 次，其中 88%的依赖包未采用安全的版本锁定机制。 该事件暴露了 Python 软件供应链中的关键漏洞，特别是依赖管理方面的问题，影响了数千个依赖 LiteLLM 进行大语言模型交互的 AI 应用。 攻击者通过入侵 LiteLLM 的 CI/CD 管道中的 Trivy 安全扫描器获取了维护者凭证，随后发布了包含凭证窃取程序的恶意版本。

rss · Simon Willison · Mar 25, 17:21

**背景**: LiteLLM 是一个流行的 Python 包，为多种大语言模型提供商（OpenAI、Anthropic、Google）提供统一接口。PyPI 是 Python 官方的第三方软件仓库。版本锁定机制可确保依赖项使用经过验证的特定版本，防止意外更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/litellm/">litellm · PyPI</a></li>
<li><a href="https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/">How a Poisoned Security Scanner Became the Key to Backdooring LiteLLM | Snyk</a></li>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential Stealer</a></li>

</ul>
</details>

**标签**: `#security`, `#pypi`, `#supply-chain`, `#python`, `#packaging`

---

<a id="item-7"></a>
## [专家权重流式传输技术让万亿参数模型可在消费级设备上运行](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

研究人员通过从 SSD 流式传输专家权重而非将完整模型加载到内存的方式，成功在 MacBook 和 iPhone 等消费级设备上运行了 Qwen3.5-397B-A17B 和 Kimi K2.5 等万亿参数规模的混合专家模型。其中具有 1 万亿参数、320 亿活跃权重的 Kimi K2.5 模型可在 96GB 内存的 M2 Max MacBook Pro 上运行，而 Qwen3.5-397B-A17B 在 iPhone 上达到了 0.6 token/秒的速度。 这一突破性进展大幅降低了运行先进 AI 模型的硬件门槛，使个人设备无需昂贵云基础设施或专业硬件即可具备高级 AI 能力。这标志着向普及尖端 AI 技术迈出了重要一步。 该技术通过仅从 SSD 加载每个 token 所需的专家权重，大幅降低了内存需求。性能因设备而异，目前 iPhone 实现速度限制在 0.6 token/秒，而 M4 Max MacBook 运行 Kimi K2.5 可达约 1.7 token/秒。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家(MoE)模型是一种使用专门子网络(专家)处理不同输入的神经网络，每个 token 只激活总参数的一小部分，使其在大规模时比密集模型更高效。Qwen3.5-397B-A17B 是阿里巴巴开发的 3970 亿参数 MoE 模型，活跃参数 170 亿；Kimi K2.5 则是更新的 1 万亿参数模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Mar/24/streaming-experts/">Streaming experts | Simon Willison’s Weblog</a></li>
<li><a href="https://www.linkedin.com/pulse/mixture-of-experts-moe-models-scalable-path-smarter-ai-vinay-saini-6p7fc?tl=en">Mixture - of - Experts (MoE) Models : The Scalable Path for Smarter AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区正在积极尝试这项技术，多位研究人员报告了在不同硬件配置上的成功实现。人们特别期待通过持续的'自动研究循环'进行进一步优化以提升性能。

**标签**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#Hardware`, `#Optimization`

---

<a id="item-8"></a>
## [Arm 将首次销售自研 AI 芯片，Meta 成首个主要客户，台积电代工](https://www.bloomberg.com/news/articles/2026-03-24/arm-to-sell-its-own-chips-for-first-time-in-bid-for-ai-revenue) ⭐️ 8.0/10

Arm Holdings 宣布将首次销售自研 AI 芯片 'AGI CPU'，Meta 成为首个主要客户。这款芯片最高配备 136 核，功耗 300 瓦，由台积电代工，设计用于与英伟达等公司的加速器芯片协同工作。 这标志着 Arm 正式进入竞争激烈的 AI 芯片市场，可能对英特尔和 AMD 等传统 CPU 厂商构成挑战。随着 Meta、OpenAI 和 SK Telecom 等科技巨头采用该芯片，或将重塑 AI 硬件生态格局。 该 AGI CPU 号称能效优于传统设计，广达和超微已推出基于该芯片的现成系统。Arm 预计将在 2026 年下半年扩大生产规模。

telegram · zaihuapd · Mar 25, 02:45

**背景**: Arm 以设计芯片架构闻名，其技术被苹果和高通等公司授权使用，但此前从未销售自研芯片。AGI CPU 专为数据中心 AI 工作负载优化，标志着 Arm 进军由英伟达主导的利润丰厚的 AI 硬件市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsroom.arm.com/blog/introducing-arm-agi-cpu">Announcing Arm AGI CPU: The silicon foundation for the agentic AI cloud era - Arm Newsroom</a></li>
<li><a href="https://www.arm.com/products/cloud-datacenter/arm-agi-cpu">Arm AGI CPU</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#AI-hardware`, `#Arm`, `#Meta`, `#TSMC`

---

<a id="item-9"></a>
## [NASA 暂停月球轨道空间站，转向 2029 年前建立月球基地](https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/) ⭐️ 8.0/10

NASA 宣布暂停 Gateway 月球轨道站项目，将重点转向 2029 年前建立永久月球基地，计划每年实施至少一次月面着陆，并加速核动力火星任务。 这一战略调整标志着月球表面作业和太空探索商业化的重大加速，同时推进对未来火星任务至关重要的核推进技术。 Artemis V 任务后，NASA 计划引入更多商业采购和可重复使用硬件，目标是每 6 个月执行一次载人登月任务。核动力飞船 Space Reactor-1 Freedom 火星任务计划于 2028 年发射。

telegram · zaihuapd · Mar 25, 04:30

**背景**: Gateway 项目原本是作为支持 Artemis 任务的月球轨道站。Artemis V 最初计划是在月球着陆前安装 Gateway 组件。此前太空核推进仅限于放射性同位素系统，尚未有裂变反应堆用于地球轨道以外的推进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbeta.com.tw/articles/science/1444756.htm">NASA正测试其" Gateway ..." - cnBeta.COM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artemis_V">Artemis V</a></li>
<li><a href="https://www.space.com/astronomy/mars/nasas-1st-nuclear-powered-interplanetary-spacecraft-will-send-skyfall-helicopters-to-mars-in-2028">NASA's '1st nuclear powered interplanetary spacecraft' will ...</a></li>

</ul>
</details>

**标签**: `#NASA`, `#space-exploration`, `#moon-base`, `#Mars-mission`, `#nuclear-propulsion`

---

<a id="item-10"></a>
## [谷歌研究院推出 TurboQuant，将大模型 KV 缓存压缩至 3 比特](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) ⭐️ 8.0/10

谷歌研究院推出了向量量化算法 TurboQuant，无需训练或微调即可将大语言模型的 KV 缓存压缩至 3 比特。实验结果显示，该方法在长上下文任务中实现了 6 倍内存占用压缩和 8 倍计算速度提升，同时保持下游任务结果不变。 这一突破性进展显著缓解了大语言模型推理中的内存瓶颈，使具备长上下文能力的大模型部署更加高效。3 比特压缩且零精度损失代表了 AI 效率的重大进步，有望降低 AI 服务的成本和能耗。 TurboQuant 将在 ICLR 2026 上展示，配套方法 QJL 和 PolarQuant 将在 AISTATS 2026 亮相。4 比特版本在高维向量搜索任务中的召回率优于 PQ 和 RabbiQ 方法。

telegram · zaihuapd · Mar 25, 05:15

**背景**: KV 缓存是 Transformer 架构大语言模型中的关键优化技术，通过存储先前计算的注意力键值对来避免文本生成时的冗余计算。向量量化是通过用更少比特表示高维向量来减少内存使用的方法，但传统方法通常会牺牲精度或需要额外开销比特。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>
<li><a href="https://arxiv.org/pdf/2603.20397">KV Cache Optimization Strategies for Scalable and Efficient ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Quantization`, `#Efficiency`, `#Google-Research`

---

<a id="item-11"></a>
## [Apifox 桌面端遭供应链投毒攻击：CDN 脚本被篡改窃取敏感数据](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 8.0/10

Apifox 桌面端遭遇供应链攻击，攻击者篡改其 CDN 上的统计脚本并注入恶意代码，窃取 SSH 密钥、Git 凭证、Shell 历史记录及进程列表等敏感信息。该攻击自 3 月 4 日起活跃，影响 Windows、macOS 和 Linux 三平台用户。 此次事件暴露了软件供应链的重大风险，作为 Postman/Swagger 的替代方案，Apifox 被入侵可能导致开发者凭证泄露，进而引发基础设施入侵。SSH 密钥和 Git 凭证的窃取将严重威胁企业代码安全与系统访问权限。 安全研究人员 phith0n 已逆向分析出恶意载荷，其通信域名包括 apifox.it.com 和 cdn.openroute.dev。缓解措施包括检查 Network Persistent State 文件是否含有这些域名并通过防火墙/DNS 屏蔽。最新版客户端已不再请求恶意域名。

telegram · zaihuapd · Mar 25, 11:10

**背景**: Apifox 是集成了 Postman 调试、Swagger 文档和 JMeter 测试的 API 协作平台。近期 CDN 供应链攻击激增（如 Polyfill.io 事件），攻击者通过篡改第三方依赖向广泛分发的软件注入恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huntscreens.com/en/products/apifox">Apifox: All-in-One API Platform for Enhanced Collaboration ...</a></li>
<li><a href="https://dev.to/snyk/polyfill-supply-chain-attack-embeds-malware-in-javascript-cdn-assets-55d6">Polyfill supply chain attack embeds malware in JavaScript CDN ...</a></li>
<li><a href="https://byteiota.com/trivy-compromised-twice-github-actions-attack-hits-again/">Trivy Compromised Twice: GitHub Actions Attack Hits Again</a></li>

</ul>
</details>

**标签**: `#security`, `#supply-chain-attack`, `#apifox`, `#malware`, `#devops`

---

<a id="item-12"></a>
## [苹果与谷歌达成合作，Gemini AI 将为 Siri 提供支持](https://t.me/zaihuapd/40506) ⭐️ 8.0/10

苹果与谷歌宣布达成多年合作协议，谷歌的 Gemini AI 模型将为下一代 Apple Foundation Models 提供技术支持，增强 Siri 功能的同时保持设备端和私有云处理以保护隐私。 这一合作可能在保持苹果隐私标准的同时显著提升 Siri 的智能水平，通过将苹果硬件生态与谷歌先进 AI 模型结合，有望重塑 AI 助手领域的格局。 整合将采用在设备端和私有云计算上运行的 Gemini 模型，苹果强调将继续遵守其隐私标准。增强版 Siri 功能预计将于今年晚些时候推出。

telegram · zaihuapd · Mar 25, 16:32

**背景**: Gemini 是谷歌的多模态大语言模型系列，是 LaMDA 和 PaLM 2 的继任者，包含 Gemini Pro 和 Gemini Flash 等多个版本。Apple Foundation Models 是苹果的设备端 AI 框架，支撑如 Apple Intelligence 等功能，使用苹果的 AXLearn 框架进行训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://machinelearning.apple.com/research/introducing-apple-foundation-models">Introducing Apple ’s On-Device and Server Foundation Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#Apple`, `#Google`, `#Siri`, `#Gemini`

---

<a id="item-13"></a>
## [美国最高法院裁定 ISP 无需为用户版权侵权行为负责](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html) ⭐️ 7.0/10

美国最高法院在版权侵权案件中支持 Cox Communications，裁定互联网服务提供商(ISP)无需为用户分享盗版内容的行为负责，除非 ISP 主动鼓励侵权行为。 这一裁决为限制 ISP 在版权法下的责任确立了重要先例，可能减少 ISP 监控用户活动的动机，并影响未来的版权执法策略。 法院援引 1984 年'Betamax 案'先例，强调责任认定需要证明存在促进侵权的意图。该裁决在明确限制的同时，保持了 DMCA 安全港条款的保护。

hackernews · oj2828 · Mar 25, 15:02

**背景**: 《数字千年版权法案》(DMCA)提供'安全港'保护，如果在线服务提供商遵循特定的程序(如回应删除通知)，可免除其对用户生成内容的责任。此案测试了这些保护的边界，音乐公司认为 Cox 从侵权用户中获得了经济利益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyber.harvard.edu/property/liability/ispliab.html">ISP Liability for Copyright Infringement</a></li>
<li><a href="https://copyrightalliance.org/education/copyright-law-explained/the-digital-millennium-copyright-act-dmca/dmca-safe-harbor/">DMCA Safe Harbor | Copyright Alliance</a></li>
<li><a href="https://www.congress.gov/crs_external_products/IF/PDF/IF11478/IF11478.1.pdf">Digital Millennium Copyright Act (DMCA) Safe Harbor ...</a></li>

</ul>
</details>

**社区讨论**: 评论显示不同反应，有人庆祝减少 ISP 监控，也有人批评版权期限过长。一位用户将案件类比为制造商对产品滥用的责任，引发了关于意图标准的辩论。

**标签**: `#copyright`, `#legal`, `#isp`, `#privacy`, `#supreme-court`

---

<a id="item-14"></a>
## [对 AI 驱动编码速度与质量权衡的批判](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Pi agent 框架创建者 Mario Zechner 批评了 AI 驱动代码生成的失控速度，警告称在没有适当人工监督的情况下会导致不可持续的复杂性积累。 这凸显了现代软件开发中的关键矛盾：AI 加速可能导致产生无法管理的'认知债务'和超出人类理解能力的系统。 Pi 框架创建者特别警告 AI 代理每天生成超过 2 万行未经检查的代码，建议架构决策采用手动编码并设置严格的每日生成限制。

rss · Simon Willison · Mar 25, 21:47

**背景**: 代理工程(agentic engineering)指能自主规划和执行编码任务的 AI 系统。Pi 框架是构建此类 AI 代理的开源工具，具有持久化存储和 SQLite 集成等功能。认知债务(cognitive debt)描述了维护过度复杂系统带来的心智负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pchaganti/gx-pi-mono">pchaganti/gx- pi -mono: Monorepo for pi packages: TUI library, agent ...</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#Software Engineering`, `#Productivity`, `#Code Quality`

---

<a id="item-15"></a>
## [Claude Code 推出带安全保护的自动模式](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code 推出了'自动模式'，这是一种新的权限模式，AI 可在内置安全保护下代表用户做出决策。该模式使用 Claude Sonnet 4.6 作为分类器模型，在执行前审查并阻止潜在危险操作。 这代表了 AI 辅助编码的重大进步，在手动批准每个操作和完全不受限制的执行之间提供了中间地带。它可以显著提高开发人员的工作效率，同时保持自动化编码工作流程中的安全标准。 自动模式包含广泛的默认过滤器，涵盖本地文件管理、软件包安装和 git 操作等。用户还可以自定义这些过滤器，系统严格禁止范围扩展和潜在破坏性操作。

rss · Simon Willison · Mar 24, 23:57

**背景**: Claude Code 是由 Anthropic 开发的 AI 编程助手。'--dangerously-skip-permissions'标志以前允许用户绕过所有安全检查，而自动模式现在提供了更安全的替代方案。Claude Sonnet 4.6 是 Anthropic 语言模型的专门版本，针对多步骤工作流程和条件逻辑进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://grokipedia.com/page/Claude_Sonnet_46">Claude Sonnet 4.6</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding`, `#permissions`, `#automation`, `#developer-tools`

---

<a id="item-16"></a>
## [包管理器纷纷引入依赖冷却机制](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

包括 pnpm、Yarn、Bun、Deno、uv、pip 和 npm 在内的主流包管理器近期均引入了依赖冷却功能，这些功能会延迟安装新发布的包更新一段时间，以便检测潜在的供应链攻击。 这一行业性转变是针对日益增长的供应链攻击（如最近的 LiteLLM 事件）的应对措施，在恶意更新被检测到之前可能快速传播。冷却期为社区审查新版本提供了关键时间窗口。 具体实现各有不同：pnpm 使用 `minimumReleaseAge`，Yarn 采用分钟为单位的 `npmMinimalAgeGate`，Bun 通过 `bunfig.toml` 配置，而 pip 目前仅支持绝对时间戳（已有基于 cron 的变通方案）。

rss · Simon Willison · Mar 24, 21:11

**背景**: 依赖冷却是一种安全实践，包管理器会有意延迟安装新发布的更新。这为社区留出时间检测软件包是否在供应链攻击中遭到破坏（攻击者劫持合法软件包分发恶意软件）。在 2026 年 3 月影响 AI 框架的 LiteLLM 攻击等重大事件后，这一方法变得尤为紧迫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns - blog.yossarian.net</a></li>
<li><a href="https://cybernews.com/security/critical-litellm-supply-chain-attack-sends-shockwaves/">Critical supply chain attack hits LiteLLM, exposing AI ...</a></li>

</ul>
</details>

**标签**: `#package-managers`, `#security`, `#supply-chain`, `#devops`, `#dependencies`

---

<a id="item-17"></a>
## [Claude Code 推出自动模式：AI 自主决策权限，内置安全审查](https://claude.com/blog/auto-mode) ⭐️ 7.0/10

Claude Code 发布自动模式（Auto Mode），允许 AI 在任务执行中自主决定权限，通过分类器在每次工具调用前审查操作，自动放行安全动作并拦截高风险行为（如批量删文件或敏感数据外泄）。 该功能在 AI 辅助开发领域迈出了重要一步，通过平衡自主性与安全性，减少人工审批需求的同时规避无监管 AI 操作的风险，将影响开发者效率和企业的 AI 采用。 该功能目前以研究预览形式向 Team 计划用户开放，即将覆盖 Enterprise 及 API 用户，支持 Claude Sonnet 4.6 与 Opus 4.6 模型。虽比 '--dangerously-skip-permissions' 参数更安全，但可能轻微增加 Token 消耗与延迟。

telegram · zaihuapd · Mar 25, 01:15

**背景**: Claude Code 是 Anthropic 开发的 AI 辅助编程工具。传统方案要么需要人工审批每个操作（降低效率），要么完全跳过权限（带来安全风险）。自动模式通过动态评估操作的安全分类器实现了折中方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/claude-code-auto-mode">Claude Code auto mode: a safer way to skip permissions</a></li>
<li><a href="https://smartscope.blog/en/generative-ai/claude/claude-code-auto-mode-guide/">Claude Code Auto Mode Complete Guide — How the Classifier ...</a></li>
<li><a href="https://institute.sfeir.com/en/articles/claude-code-auto-mode-permissions-autonomy/">Claude Code Auto Mode: Complete Guide to Autonomous Mode ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#developer-tools`, `#safety`, `#automation`, `#Claude`

---

<a id="item-18"></a>
## [腾讯撤销 AI Lab 并引入字节 Seed 骨干推进混元升级](https://mp.weixin.qq.com/s/24ZWs8JFP6seQSSIhU6mOw) ⭐️ 7.0/10

腾讯近期撤销了 AI Lab 并重组大模型研发体系，同时从字节跳动 Seed 团队引入了多位技术骨干，包括原 Seed 视觉 AI 平台负责人肖学锋和训练 Infra 组负责人黄启。公司计划于 2026 年 4 月发布新一代混元大模型。 此举显示了腾讯在 AI 研发战略上的重大调整，通过引入字节 Seed 团队的核心技术人才来强化大模型竞争力，可能加速混元模型的发展以对抗 DeepSeek 等竞争对手。 重组后，原字节 Seed 成员担任要职：肖学锋任 AI Infra 部助理负责人，黄启负责训练 Infra 组。腾讯的 Hunyuan Turbo S 模型已宣称比 DeepSeek 的 R1 系统响应速度更快。

telegram · zaihuapd · Mar 25, 03:00

**背景**: 腾讯混元是中国 AI 市场竞争中的大语言模型，其 Hunyuan-Large 版本在性能基准测试中表现优异。字节跳动的 Seed 团队成立于 2023 年，专注于 LLM、视觉和基础设施等前沿 AI 研究。AI Infra 指的是支撑 AI 模型开发和部署的基础系统和工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Tencent-Hunyuan-Large">tencent / Tencent - Hunyuan -Large · Hugging Face</a></li>
<li><a href="https://seed.bytedance.com/en/">ByteDance Seed</a></li>
<li><a href="https://github.com/bytedance-seed">ByteDance-Seed · GitHub</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tencent`, `#LLM`, `#Corporate Restructuring`, `#ByteDance`

---

<a id="item-19"></a>
## [拼多多官宣‘新拼姆’：三年投入 1000 亿元转型品牌自营](https://m.tmtpost.com/nictation/7929040.html) ⭐️ 7.0/10

拼多多集团正式宣布‘新拼姆’项目，计划未来三年投入 1000 亿元现金，从平台化运营转向品牌自营，首期已注资 150 亿元。该项目将整合拼多多和 Temu 的供应链资源，系统性孵化面向全球市场的自营品牌。 这一战略转型可能重塑拼多多的商业模式，并加剧与亚马逊、阿里巴巴等对手的全球电商竞争。千亿级投入体现了中国企业通过垂直整合掌控供应链、建立直接消费者关系的趋势。 该项目已在上海成立专项公司，将按品类和市场差异化孵化品牌。这是赵佳臻 2023 年 12 月出任联席 CEO 后落地的首个重大战略。

telegram · zaihuapd · Mar 25, 12:37

**背景**: 拼多多最初是农产品团购平台，Temu 是其主打跨境低价商品的国际版。品牌自营模式让电商企业直接控制产品质量、定价和供应链，不同于传统连接第三方卖家和买家的平台模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Temu">Temu - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1366554522003283">How does manufacturer’s self-operating channel interact with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vertical_integration">Vertical integration - Wikipedia</a></li>

</ul>
</details>

**标签**: `#e-commerce`, `#supply-chain`, `#business-strategy`, `#china-tech`, `#retail`

---

<a id="item-20"></a>
## [中国计算机学会反对 NeurIPS 限制受美制裁机构投稿，呼吁抵制](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 7.0/10

中国计算机学会(CCF)发表声明，强烈反对 NeurIPS 2026 会议禁止受美国制裁机构投稿的政策，并呼吁中国学者抵制该会议。CCF 表示若 NeurIPS 不及时改正，将考虑将其移出《中国计算机学会推荐国际学术会议和期刊目录》。 这一争议凸显了 AI 研究领域学术自由与地缘政治限制之间日益紧张的关系，可能破坏该领域传统的开放交流与国际合作。CCF 的立场代表了中国学术界对科学讨论政治化的强烈反对。 NeurIPS 2026 将于 2026 年 12 月 6-12 日在悉尼举行。CCF 的推荐会议目录在中国计算机学界具有重要影响力，直接影响研究人员的发表策略和职业评估。

telegram · zaihuapd · Mar 25, 14:07

**背景**: NeurIPS(神经信息处理系统大会)成立于 1987 年，是全球最具声望的 AI 会议之一。中国计算机学会(CCF)成立于 1962 年，是中国计算机领域主要的学术组织，其维护的《推荐国际学术会议和期刊目录》在学界具有重要影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neurips.cc/">NeurIPS - 2026 Conference</a></li>
<li><a href="https://www.ccf.org.cn/Academic_Evaluation/By_category/">CCF推荐国际学术刊物目录-中国计算机学会</a></li>
<li><a href="https://www.ccf.org.cn/en/About_CCF/Media_Center/">The Latest Edition of "List of International Academic ...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#academic freedom`, `#NeurIPS`, `#China-US relations`, `#research policy`

---

<a id="item-21"></a>
## [英特尔和 AMD 通知中国客户：服务器 CPU 交付周期将延长](https://t.me/zaihuapd/40507) ⭐️ 7.0/10

英特尔和 AMD 已通知中国客户服务器 CPU 供应紧张，英特尔部分至强处理器交付周期最长达 6 个月，AMD 部分产品则延长至 8-10 周。受此影响，英特尔服务器产品在中国整体涨价超过 10%。 这一供应紧张可能严重影响中国的服务器基础设施建设和 AI 应用，因为这些 CPU 对数据中心和 AI 工作负载至关重要。价格上涨和交付延迟可能会延缓该地区企业和云计算的发展。 英特尔正在中国限量供应第四、第五代至强处理器，预计 2026 年一季度库存水平最低，二季度开始改善。公司将短缺归因于 AI 应用对'传统计算'资源的需求激增。

telegram · zaihuapd · Mar 26, 00:03

**背景**: 至强处理器是英特尔面向数据中心高要求工作负载的服务器级 CPU 产品线。当前供应问题出现时，正值全球 AI 服务器需求激增，预计到 2027 年 AI 服务器将占总服务器出货量的 19%。由于 AI 驱动的需求变化，服务器内存价格也面临上涨压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xeon">Xeon - Wikipedia</a></li>
<li><a href="https://files.futurememorystorage.com/proceedings/2024/20240808_BMKT-301-1_KUNG.pdf">See Generative AI's Impact on the AI Server Market to 2025</a></li>
<li><a href="https://www.reuters.com/world/china/ai-frenzy-is-driving-new-global-supply-chain-crisis-2025-12-03/">The AI frenzy is driving a memory chip supply crisis | Reuters</a></li>

</ul>
</details>

**标签**: `#supply-chain`, `#semiconductors`, `#servers`, `#AI`, `#China`

---

<a id="item-22"></a>
## [GitHub 更新 Copilot 数据政策：免费与个人付费版默认纳入 AI 训练，可手动退出](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) ⭐️ 7.0/10

GitHub 宣布自 4 月 24 日起，Copilot Free、Pro 和 Pro+用户的交互数据（包括输入、输出及代码片段）将默认用于 AI 模型训练，用户可在隐私设置中选择退出。此次调整不涉及 Copilot Business 和 Enterprise 用户，且已关闭数据收集选项的用户偏好将保留。 这一政策变更通过纳入数百万开发者的编码模式，大幅扩展了 GitHub 的 AI 训练数据集，可能提升 Copilot 的建议质量，但也引发隐私考量。这反映了行业利用真实用户交互优化 AI 模型的趋势，同时通过退出机制保持透明度。 训练数据包含光标附近代码上下文、注释、文件名、仓库结构、导航模式及建议反馈。数据可能与微软关联公司共享，但不会提供给第三方 AI 供应商。企业代码库仍不纳入此数据收集范围。

telegram · zaihuapd · Mar 26, 00:47

**背景**: GitHub Copilot 是由 OpenAI 模型驱动的 AI 编程助手，可自动建议代码补全。AI 模型通常通过多样化数据集（包括用户交互）的训练来改进。当前技术趋势强调从实时用户行为中动态学习，而不仅依赖静态数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/">Updates to GitHub Copilot interaction data usage policy</a></li>
<li><a href="https://www.howtogeek.com/githubs-copilot-will-use-you-as-ai-training-data-but-you-can-opt-out/">GitHub’s Copilot will use you as AI training data, but you ...</a></li>
<li><a href="https://roboin.io/article/en/2026/03/26/github-to-use-copilot-data-for-ai-training/">GitHub to use Copilot data for AI training from April 24; how ...</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Copilot`, `#AI`, `#Privacy`, `#Data Policy`

---