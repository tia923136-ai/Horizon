---
layout: default
title: "Horizon Summary: 2026-03-27 (ZH)"
date: 2026-03-27
lang: zh
---

> From 36 items, 10 important content pieces were selected

---

1. [谷歌宣布在 Android 17 中引入后量子加密](#item-1) ⭐️ 9.0/10
2. [开发者分享应对 LiteLLM 恶意软件攻击的实时记录](#item-2) ⭐️ 8.0/10
3. [交互式指南揭秘大语言模型量化技术](#item-3) ⭐️ 8.0/10
4. [Apifox 桌面端遭供应链投毒攻击：CDN 脚本被篡改窃取敏感数据](#item-4) ⭐️ 8.0/10
5. [中科院发布香山 RISC-V 处理器和如意 OS，启动下一代芯片与系统联合研发](#item-5) ⭐️ 8.0/10
6. [日本第 58 代克隆小鼠次日死亡，或证实哺乳动物克隆存在极限](#item-6) ⭐️ 8.0/10
7. [谷歌发布 Gemini 3.1 Flash Live，实时多模态对话提速](#item-7) ⭐️ 8.0/10
8. [团队用 AI 一日内用 Go 重写 JSONata，年省 50 万美元](#item-8) ⭐️ 7.0/10
9. [对以速度为核心的 AI 辅助开发的批判](#item-9) ⭐️ 7.0/10
10. [研究显示父亲年龄增加会带来比此前认为更高的子代遗传病风险](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌宣布在 Android 17 中引入后量子加密](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) ⭐️ 9.0/10

谷歌宣布在 Android 17 中引入后量子加密（PQC）标准，升级引导加载程序以支持量子抗性数字签名，并将 Android 密钥库迁移至符合 PQC 标准的架构。 这一举措意义重大，因为它为 Android 设备应对未来量子计算威胁做好了准备，确保在量子时代设备启动过程和与外部服务器的通信仍能保持安全。 升级包括在引导加载程序中加入量子抗性数字签名以防止启动阶段被篡改，以及符合 PQC 标准的密钥库以确保安全的身份验证和数据传输。

telegram · zaihuapd · Mar 26, 07:09

**背景**: 后量子加密（PQC）指的是设计用于抵御量子计算机攻击的加密算法。NIST 于 2024 年发布了首批 PQC 标准，标志着为量子计算时代做准备的重要一步。传统的加密方法如 RSA 和 ECDSA 容易受到量子攻击，因此需要过渡到 PQC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography - Wikipedia</a></li>
<li><a href="https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html">Security for the Quantum Era: Implementing Post-Quantum ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#Quantum Cryptography`, `#Security`, `#Encryption`, `#Google`

---

<a id="item-2"></a>
## [开发者分享应对 LiteLLM 恶意软件攻击的实时记录](https://futuresearch.ai/blog/litellm-attack-transcript/) ⭐️ 8.0/10

一位开发者发布了逐分钟记录的详细过程，描述其发现并应对 PyPI 软件包 LiteLLM 1.82.7 和 1.82.8 版本中恶意软件攻击的经历，该软件包被篡改以植入窃取凭证的多阶段恶意程序。 该事件暴露了开源软件包生态系统的严重漏洞，展示了供应链攻击如何危害广泛使用的 AI 工具并威胁开发者系统安全。 攻击利用了 Python 的.pth 文件特性（该文件会在每次 Python 启动时执行，与 npm 的一次性 postinstall 钩子不同）。恶意软件专门设计用于窃取受感染系统的凭证和认证令牌。

hackernews · Fibonar · Mar 26, 15:48

**背景**: LiteLLM 是一个流行的 Python SDK，为调用各种大语言模型 API 提供统一接口。PyPI（Python 包索引）是 Python 软件包的官方仓库，类似于 JavaScript 的 npm。供应链攻击通过针对受信任的软件分发渠道来向下游用户传播恶意软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/litellm/">litellm · PyPI</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/supply-chain-attack/">What Is a Supply Chain Attack? - CrowdStrike</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXaDlyakVCR0F3M1ZIa2VnQW5pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - LiteLLM PyPI package hack - Overview</a></li>

</ul>
</details>

**社区讨论**: 开发者们讨论了改善软件包仓库监控的必要性，包括建议建立实时安全分析数据流。有人担忧 LLM 智能体可能执行恶意脚本，而关于 Python 的.pth 文件行为的技术细节引发了安全意识讨论。

**标签**: `#security`, `#malware`, `#pypi`, `#supply-chain`, `#ai`

---

<a id="item-3"></a>
## [交互式指南揭秘大语言模型量化技术](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose 发布了一篇带有突破性可视化效果的交互式文章，解释了大语言模型量化技术，包括 float32 二进制表示和异常值保留技术。文章使用 llama.cpp 的困惑度工具通过 Qwen 3.5 9B 模型测试展示了量化的影响。 该资源让从业者能够理解高级量化概念，这对在资源受限设备上部署大语言模型至关重要。理解异常值保留尤其有价值，因为这些'超级权重'会不成比例地影响模型性能。 可视化 float32 表示工具用颜色标注了符号位、指数位和有效数字位。测试显示 16 位到 8 位量化质量损失最小，而 16 位到 4 位量化保留了约 90%准确率。苹果的'超级权重'概念揭示单个异常值就能防止模型崩溃。

rss · Simon Willison · Mar 26, 16:21

**背景**: 量化通过将高精度数字(如 32 位浮点数)转换为低精度格式(如 8 位整数)来减少大语言模型的内存需求。IEEE 754 单精度(float32)使用 1 位符号位、8 位指数位和 23 位有效数字位。困惑度和 KL 散度是评估量化对模型质量影响的指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@lmpo/understanding-model-quantization-for-llms-1573490d44ad">Understanding Quantization for LLMs | by LM Po | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single-precision_floating-point_format">Single-precision floating - point format - Wikipedia</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#quantization`, `#llm`, `#floating-point`, `#interactive-learning`

---

<a id="item-4"></a>
## [Apifox 桌面端遭供应链投毒攻击：CDN 脚本被篡改窃取敏感数据](https://t.me/zaihuapd/40514) ⭐️ 8.0/10

Apifox 桌面端遭供应链投毒攻击，攻击者篡改其 CDN 上的事件统计脚本并注入恶意代码，自 3 月 4 日起窃取用户主机的 SSH 密钥、Git 凭证、Shell 历史记录及进程列表等敏感信息。安全研究者 phith0n 已独立还原恶意载荷，确认 Windows、macOS 和 Linux 三平台用户均受影响。 该事件暴露了主流开发工具的重大安全隐患——Apifox 集成了 Postman 和 Swagger 等功能，使其成为高价值攻击目标。泄露的 SSH/Git 凭证可能导致企业内网横向渗透及私有代码库未授权访问。 恶意代码被注入 Apifox 官方 CDN（cdn.apifox.com）托管的 apifox-app-event-tracking.min.js 文件，且经过高度混淆。由于脚本来自受信任源，该攻击方式能绕过传统安全检测。

telegram · zaihuapd · Mar 26, 04:19

**背景**: Apifox 是集成了 Postman、Swagger 和 JMeter 功能的流行 API 开发工具，广泛用于 API 文档、测试和持续集成。供应链攻击通过篡改 CDN 等软件分发渠道自动感染下游用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://slowmist.medium.com/security-alert-supply-chain-attack-on-apifox-desktop-client-via-compromised-official-cdn-script-bc3870992564">Security Alert: Supply Chain Attack on Apifox Desktop Client via Compromised Official CDN Script | by SlowMist | Mar, 2026 | Medium</a></li>
<li><a href="https://apifox.com/">Apifox - API 文档、调试、Mock...</a></li>
<li><a href="https://x.com/SlowMist_Team/status/2037024243112702075">SlowMist on X: "🚨 Security Alert: Supply Chain Attack on Apifox Desktop Client Yesterday, we detected a supply chain attack in which a front-end script file hosted on #Apifox’s official CDN was injected with heavily obfuscated malicious JavaScript code. ⚡ Impact on Apifox Desktop Client https://t.co/Z8Sl8FgFjQ" / X</a></li>

</ul>
</details>

**社区讨论**: 安全社区呼吁立即更换凭证，SlowMist 团队已确认 CDN 被入侵。用户反馈在本地 Apifox 数据中发现恶意痕迹，引发关于开发工具 CDN 安全实践的讨论。

**标签**: `#security`, `#supply-chain-attack`, `#apifox`, `#malware`, `#devops`

---

<a id="item-5"></a>
## [中科院发布香山 RISC-V 处理器和如意 OS，启动下一代芯片与系统联合研发](https://h.xinhuaxmt.com/vh512/share/13024070?docid=13024070) ⭐️ 8.0/10

3 月 26 日，中国科学院发布了开源高性能 RISC-V 处理器'香山'和原生操作系统'如意'，同时联合中国移动、阿里、腾讯等企业启动了下一代'昆明湖'架构与操作系统的协同开发。 这标志着中国在开源芯片和系统技术领域取得重大突破，香山处理器达到国际先进水平，如意 OS 率先全面支持国际标准，有望减少在关键半导体和操作系统领域对外依赖。 香山处理器包含全球首个开源片上互连网络 IP，基于该处理器的商用芯片已由进迭时空、蓝芯算力等企业推出。如意 SDK 支持多种 RISC-V 开发板，适用于物联网和智能设备开发。

telegram · zaihuapd · Mar 26, 10:08

**背景**: RISC-V 是一种开放标准指令集架构，正作为 ARM 等专有架构的替代方案获得全球关注。片上互连 IP 实现处理器核心间高效通信，原生操作系统指专为特定硬件架构设计而非从现有系统移植的操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/OpenXiangShan/XiangShan">GitHub - OpenXiangShan/ XiangShan : Open - source high-performance...</a></li>
<li><a href="https://ruyisdk.org/en/docs/intro/">Hello Ruyi | RuyiSDK</a></li>
<li><a href="https://www.design-reuse.com/ip/111-interconnect-d2d-c2c">Interconnect , D2D, C2C IP Core</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#open-source-hardware`, `#operating-systems`, `#semiconductors`, `#China-tech`

---

<a id="item-6"></a>
## [日本第 58 代克隆小鼠次日死亡，或证实哺乳动物克隆存在极限](https://www.nature.com/articles/s41467-026-69765-7) ⭐️ 8.0/10

日本研究团队历时 20 年对同一雌鼠进行连续 58 代克隆，共培育超过 1200 只克隆鼠，但到第 58 代时所有克隆鼠均在出生次日死亡，尽管外观无异常。 该研究首次通过长期实验证实哺乳动物克隆存在生物学极限，突变积累导致繁殖力最终归零，从基因组层面强化了有性生殖对维持遗传健康的核心作用。 克隆鼠突变发生率为自然繁殖后代的 3 倍，部分个体甚至丢失整条 X 染色体。从第 27 代起出现繁殖力下降、胎盘异常等问题，第 57 代存活率不足 1%。

telegram · zaihuapd · Mar 26, 16:46

**背景**: 克隆技术（如体细胞核移植）可创造遗传相同的生物体，但成功率通常低于 3%。此前研究表明，克隆过程表观遗传重编程错误常导致发育异常。多利羊诞生前曾经历 276 次失败尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/克隆">克隆 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.stdaily.com/web/gjxw/2026-03/25/content_492459.html">有性生殖为何重要？20年研究表明——哺乳动物克隆存在技术极限</a></li>

</ul>
</details>

**标签**: `#genetics`, `#cloning`, `#reproductive-science`, `#mammalian-biology`, `#mutations`

---

<a id="item-7"></a>
## [谷歌发布 Gemini 3.1 Flash Live，实时多模态对话提速](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/) ⭐️ 8.0/10

谷歌发布实时音频与语音模型 Gemini 3.1 Flash Live，支持 90 多种语言的实时多模态对话，强化了复杂指令遵循和声学细节识别能力，并将 Search Live 服务扩展至 200 多个国家和地区。该模型已接入 Gemini Live、企业客户体验解决方案及 Google AI Studio 的预览版 API。 此次升级大幅提升了全球用户的实时 AI 交互体验，使客服、搜索和开发者工具中的语音应用更加自然。扩展的语言支持和嘈杂环境下的语音处理能力，让谷歌多模态 AI 在全球范围内更具可用性。 该模型将移动端连续对话的上下文保持时间延长至 2 倍，并新增对音高/语速等声学细节的识别能力。技术文档显示其专为 Gemini Live API 预览版中的低延迟音频管道优化。

telegram · zaihuapd · Mar 26, 17:01

**背景**: Gemini 是谷歌的多模态 AI 模型系列，可同步处理文本、图像、音频和视频。多模态系统将不同输入类型转化为统一表征以实现上下文理解，支撑实时语音助手等应用（如结合语音识别与 Google Lens 视觉输入）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview">Gemini 3 . 1 Flash Live Preview | Gemini API | Google AI for Developers</a></li>
<li><a href="https://tblocks.com/guides/multi-modal-ai/">What Is Multimodal AI? Architecture, Use Cases, and Impact</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Multimodal`, `#Speech Recognition`, `#Real-time`

---

<a id="item-8"></a>
## [团队用 AI 一日内用 Go 重写 JSONata，年省 50 万美元](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

Reco 团队利用 AI 在 24 小时内用 Go 语言重写了 JSONata 查询语言，通过测试驱动开发和影子部署保持完全兼容性，实现年节省 50 万美元成本。 该案例证明了 AI 在加速高成本代码迁移同时保持可靠性的潜力，为 LLM 辅助的企业遗留系统现代化改造树立了范例。 迁移利用了 JSONata 现有测试套件进行验证，仅用 7 小时和 400 美元 AI 代币成本完成初始 Go 版本，并通过为期一周的影子部署进行行为验证。

rss · Simon Willison · Mar 27, 00:35

**背景**: JSONata 是类似 jq 的开源 JSON 查询语言，最初为 Node-RED 开发。影子部署通过复制生产流量测试新系统而不影响用户，而'vibe-porting'指利用现有测试套件作为护栏，通过 AI 辅助实现跨语言代码迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata : A declarative open-source query and transformation...</a></li>
<li><a href="https://codefresh.io/learn/software-deployment/shadow-deployments-benefits-process-and-4-tips-for-success/">Shadow Deployments : Benefits, Process, and 4 Tips for Success</a></li>

</ul>
</details>

**标签**: `#AI`, `#Go`, `#JSON`, `#code-migration`, `#cost-optimization`

---

<a id="item-9"></a>
## [对以速度为核心的 AI 辅助开发的批判](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Pi agent 框架创建者 Mario Zechner 批评了软件开发中 AI 代理的无节制使用，警告人们不要将速度置于质量之上，以及'认知债务'的积累。他主张有意识地放慢速度，并手动编写关键系统组件。 这一批判凸显了软件工程中日益增长的紧张关系：AI 工具虽然带来了前所未有的生产力，但也可能造成难以维护的系统。随着更多团队在没有适当防护措施的情况下采用代理工程方法，这一观点尤为重要。 提到的 Pi 框架是一个包含 LLM 通信组件、带有工具调用的代理循环以及具有会话持久性的编码代理的 monorepo。Zechner 特别警告了当多个代理在没有人工审查瓶颈的情况下运行时错误的复合效应。

rss · Simon Willison · Mar 25, 21:47

**背景**: 代理工程是一门新兴学科，专注于在最少人工监督下自主规划和执行任务的 AI 系统。Pi 框架是一个用于构建此类代理（特别是编码任务）的开源工具包。认知债务指的是理解和维护复杂系统所需的心理开销，类似于技术债务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/badlogic/pi-mono">GitHub - badlogic/pi-mono: AI agent toolkit: coding agent CLI ...</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#software development`, `#productivity`, `#technical debt`

---

<a id="item-10"></a>
## [研究显示父亲年龄增加会带来比此前认为更高的子代遗传病风险](https://t.me/zaihuapd/40521) ⭐️ 7.0/10

英国科学家通过对 81 份男性精子样本进行高精度测序，发现男性生殖细胞会在一生中持续积累突变，50 岁以上男性有 3-5%的精子携带可能导致疾病的突变。该研究共鉴定出 40 个存在显著正向选择的基因，其中 31 个为新发现。 这一发现挑战了关于父亲年龄影响的既有认知，对遗传咨询和生殖健康决策具有重要意义。研究结果表明高龄父亲可能传递比预估更多的致病突变，可能增加后代出现发育障碍和癌症易感性的风险。 研究采用高精度测序技术检测突变，发现的基因涉及多种与儿童发育障碍相关的细胞通路。50 岁以上男性精子 3-5%的突变率高于以往估计值。

telegram · zaihuapd · Mar 26, 12:47

**背景**: 种系突变是可遗传给后代的基因变化，人类大部分突变源自父亲。精子中的正向选择指那些在发育过程中赋予精子细胞生存优势的突变，即使这些突变可能对后代有害。父亲年龄与突变率的相关性早有认知，但其程度此前被低估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNA_sequencing">DNA sequencing - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12611766/">Sperm sequencing reveals extensive positive selection in the male...</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.1901259116">Overlooked roles of DNA damage and maternal age in... | PNAS</a></li>

</ul>
</details>

**标签**: `#genetics`, `#reproductive health`, `#mutations`, `#aging`, `#medical research`

---