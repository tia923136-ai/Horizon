---
layout: default
title: "Horizon Summary: 2026-03-24 (ZH)"
date: 2026-03-24
lang: zh
---

> From 34 items, 16 important content pieces were selected

---

1. [LiteLLM Python 包遭受供应链攻击](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.82.8 被植入窃取凭证的恶意.pth 文件](#item-2) ⭐️ 9.0/10
3. [Ripgrep 在速度上超越 grep 及其他搜索工具](#item-3) ⭐️ 8.0/10
4. [专家权重流式加载技术突破：消费级硬件可运行超大规模 MoE 模型](#item-4) ⭐️ 8.0/10
5. [美国 FCC 以安全风险为由全面禁止外国制造的路由器](#item-5) ⭐️ 8.0/10
6. [英伟达通过大规模投资巩固 AI 霸权，被指利用资金优势捆绑客户](#item-6) ⭐️ 8.0/10
7. [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](#item-7) ⭐️ 8.0/10
8. [DarkSword 漏洞链通过 Safari 攻击多国用户](#item-8) ⭐️ 8.0/10
9. [谷歌推出基于 Gemini 的暗网情报 AI 代理，助力安全运营](#item-9) ⭐️ 8.0/10
10. [微软对 Windows 11 的'修复'引发批评](#item-10) ⭐️ 7.0/10
11. [Starlette 1.0 正式发布，带来 ASGI 框架重大更新](#item-11) ⭐️ 7.0/10
12. [PC Gamer 网站性能审计揭露严重资源臃肿问题](#item-12) ⭐️ 7.0/10
13. [JavaScript 沙盒技术对比研究](#item-13) ⭐️ 7.0/10
14. [基于 CRDT 的版本控制交互式可视化工具](#item-14) ⭐️ 7.0/10
15. [我国日均 AI 词元调用量两年增长超千倍](#item-15) ⭐️ 7.0/10
16. [欧盟拟推年龄验证 App 或限制非谷歌授权安卓系统](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM Python 包遭受供应链攻击](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

LiteLLM Python 包遭受供应链攻击，导致 PyPI 将该包隔离并移除了受影响的 1.82.7 和 1.82.8 版本。攻击似乎源于使用了 Trivy 安全扫描器的 CI/CD 管道被入侵。 这一事件凸显了针对开源依赖项的供应链攻击风险日益增长，可能影响数千个下游项目。同时也强调了 Python 生态系统中需要更强的 CI/CD 安全实践。 该包在 PyPI 上被暂时隔离，阻止了所有下载，但在移除受影响的版本后已恢复。使用代理 Docker 镜像的用户未受影响，因为版本已在 requirements.txt 中被固定。

hackernews · theanonymousone · Mar 24, 12:36

**背景**: LiteLLM 是一个流行的 Python SDK 和代理服务器，用于与各种 LLM API 交互。PyPI 的隔离功能是一种安全措施，在怀疑存在恶意软件时暂时阻止包下载。供应链攻击针对软件分发渠道，向合法包中注入恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://litellm.vercel.app/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://blog.pypi.org/posts/2024-12-30-quarantine/">Project Quarantine - The Python Package Index Blog</a></li>
<li><a href="https://www.wiz.io/academy/application-security/ci-cd-security-best-practices">CI/CD Pipeline Security Best Practices: The Ultimate Guide | Wiz</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 CI/CD 安全性表示担忧，提出了从更好的沙箱到将包发布与公共仓库分离等各种建议。一些人将此事件与更广泛的 TeamPCP 活动联系起来，而维护者则持续提供情况更新。

**标签**: `#security`, `#supply-chain`, `#python`, `#devops`, `#ci-cd`

---

<a id="item-2"></a>
## [LiteLLM v1.82.8 被植入窃取凭证的恶意.pth 文件](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

PyPI 上的 LiteLLM v1.82.8 软件包被植入恶意 litellm_init.pth 文件，内含 base64 编码的凭证窃取程序，安装时即自动执行且无需导入代码。 这次供应链攻击针对广泛使用的 Python 库，可能泄露开发者的 SSH 密钥、云凭证和加密货币钱包，暴露出 PyPI 对恶意上传的脆弱性。 恶意程序针对 25+种凭证类型，包括 AWS、Kubernetes、Docker 和区块链钱包。PyPI 在数小时内隔离了该软件包，将风险窗口限制在 2026 年 3 月 24 日的短暂时间段内。

rss · Simon Willison · Mar 24, 15:07

**背景**: LiteLLM 是统一 LLM API 的热门开源库。.pth 文件是 Python 解释器启动时执行的路径配置文件。PyPI 是 Python 的主要软件包仓库，管理着超过 50 万个软件包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1 ...</a></li>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI - futuresearch.ai</a></li>

</ul>
</details>

**标签**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#vulnerability`

---

<a id="item-3"></a>
## [Ripgrep 在速度上超越 grep 及其他搜索工具](https://burntsushi.net/ripgrep/) ⭐️ 8.0/10

2016 年，ripgrep（rg）通过详细的技术对比和优化，被证明在速度上显著优于 grep、ag、git grep、ucg、pt 和 sift 等工具。分析特别强调了其性能优势，如使用 SIMD 和多线程技术。 这很重要，因为更快的搜索工具能提高开发者的生产力，尤其是在大型代码库中。Ripgrep 的优化为文本搜索性能设立了新标准，影响了后续工具和工作流程。 Ripgrep 通过 Rust 语言的性能、SIMD 优化和并行处理实现高速搜索。相比竞争对手，它还能更高效地处理忽略规则和仓库规模的搜索。

hackernews · jxmorris12 · Mar 24, 06:31

**背景**: Grep 是经典的 Unix 命令行工具，用于搜索纯文本数据集。Ripgrep 是用 Rust 编写的现代替代品，旨在保持与 grep 核心功能兼容的同时，提供更快的速度和更好的用户体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://burntsushi.net/ripgrep/">ripgrep is faster than { grep , ag, git grep , ucg, pt, sift} - Andrew...</a></li>
<li><a href="https://www.codeant.ai/blogs/ripgrep-vs-grep-performance">Ripgrep vs Grep Performance : Why rg Is 10x Faster for Modern...</a></li>

</ul>
</details>

**社区讨论**: 社区称赞这篇文章是技术深度分析的典范，开发者们在自己的工具中采用了 ripgrep 的优化。值得注意的是，即使在 300MHz 的 Octane 系统等老旧硬件上，ripgrep 仍能保持性能优势。

**标签**: `#ripgrep`, `#performance`, `#search-tools`, `#optimization`, `#systems-programming`

---

<a id="item-4"></a>
## [专家权重流式加载技术突破：消费级硬件可运行超大规模 MoE 模型](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

研究人员通过在存储设备中流式加载专家权重而非完整模型，成功在消费级设备（96GB 内存的 M2 Max MacBook Pro）上运行了万亿参数规模的 Kimi K2.5 等 MoE 模型，甚至在 iPhone 上实现了 0.6 token/秒的推理速度。 该技术突破大幅降低了运行尖端 AI 模型的硬件门槛，使得边缘设备也能部署复杂 LLM 应用，推动前沿 AI 能力的普惠化发展。 Qwen3.5-397B-A17B 模型（3970 亿总参数/170 亿激活参数）已通过 flash-moe 项目在 iPhone 运行，而 Kimi K2.5（1 万亿参数/320 亿激活参数）可在 MacBook 上运作——两者均利用苹果 NVMe 存储带宽实现权重流式加载。

rss · Simon Willison · Mar 24, 05:09

**背景**: 混合专家（MoE）模型将神经网络划分为按条件激活的专用子网络（'专家'），能以有限计算开销支持超大规模参数。传统实现需将所有专家加载到内存，而流式专家技术则根据每个 token 的需求从存储动态获取权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 开发者在 Twitter 和 GitHub 上积极分享优化技术，自研循环取得显著进展。iOS 版 0.6 token/秒的速度引发了关于技术可行性与实际可用性的讨论。

**标签**: `#LLM`, `#Mixture-of-Experts`, `#Edge AI`, `#Model Optimization`, `#Hardware Efficiency`

---

<a id="item-5"></a>
## [美国 FCC 以安全风险为由全面禁止外国制造的路由器](https://www.bloomberg.com/news/articles/2026-03-23/fcc-bans-all-foreign-made-routers-citing-security-risks?embedded-checkout=true) ⭐️ 8.0/10

美国联邦通信委员会（FCC）正式宣布，出于对网络安全和供应链漏洞的担忧，全面禁止所有在外国制造的新型消费级路由器进口至美国市场，并将这些设备列入'受管辖实体名单'。已获批准的现有型号不受影响。 这一举措可能严重扰乱全球科技供应链并影响国际贸易，同时也为消费级网络设备制定更严格的网络安全监管开创先例。这反映出人们越来越担心外国制造的设备可能通过漏洞或后门危害国家安全。 该禁令仅适用于寻求认证的新型路由器，已获批准的现有型号仍可继续进口和销售。制造商可通过美国国防部等机构申请豁免。

telegram · zaihuapd · Mar 24, 01:17

**背景**: FCC（美国联邦通信委员会）是一个独立的美国政府机构，负责监管无线电、电视、有线、卫星和电缆通信。长期以来，由于制造商为降低成本而采取的措施（包括缺乏固件更新和安全功能不足），消费级路由器的安全漏洞一直受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/联邦通信委员会">联邦通信委员会 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.secrss.com/articles/1373">研究：消费级路由器固件木马分析及防护建议 - 安全内参 | 决策者的网络安全知识库</a></li>
<li><a href="https://www.boringcompliance.com/post/untitled-144">美国FCC更新Covered List 将所有外国生产路由器列入国家安全风险清单</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#regulations`, `#networking`, `#trade-policy`, `#FCC`

---

<a id="item-6"></a>
## [英伟达通过大规模投资巩固 AI 霸权，被指利用资金优势捆绑客户](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

自 2022 年以来，英伟达已向 OpenAI、CoreWeave 和 Reflection 等 AI 初创公司投资数十亿美元，通过“供应商兼投资者”的双重身份将客户锁定在其生态系统中。该公司还因 200 亿美元收购芯片初创公司 Groq 核心团队等行为面临反垄断审查。 英伟达的策略可能通过限制客户转向 AMD 等竞争对手来抑制 AI 行业竞争。该公司在资金上的主导地位和激进策略已引发监管关注，可能影响 AI 创新的未来和市场公平性。 CoreWeave 专注于为 AI 提供 GPU 云基础设施，而 Reflection 则致力于开发自主编码代理。英伟达与 Groq 达成的 200 亿美元协议包括技术授权和核心团队收购，引发了反垄断担忧。

telegram · zaihuapd · Mar 24, 03:02

**背景**: 英伟达通过其 GPU 在 AI 领域占据主导地位，这些 GPU 对训练和运行 AI 模型至关重要。CoreWeave 和 Reflection 等初创公司依赖英伟达的硬件，使其容易受到其资金影响。Groq 以其 AI 加速器芯片闻名，与英伟达的产品形成竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Nvidia`, `#Antitrust`, `#Investment`, `#Market Competition`

---

<a id="item-7"></a>
## [阿里达摩院发布玄铁 C950 RISC-V CPU，刷新全球性能纪录](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

2026 年 3 月 24 日，阿里巴巴达摩院在上海发布新一代旗舰 CPU 玄铁 C950，该产品基于开源 RISC-V 架构，在 Specint2006 单核测试中得分超过 70 分。芯片集成了自研 AI 加速引擎，可原生运行千亿参数级大模型如 Qwen3 和 DeepSeek V3。 这是 RISC-V 架构在高性能计算领域的重要突破，可能动摇 ARM 和 x86 在云/AI 应用中的主导地位。原生支持大模型运行使其成为中国下一代 AI 基础设施的有力竞争者。 玄铁 C950 面向云计算、生成式 AI、高端机器人和边缘计算领域，目前性能处于公开 RISC-V 处理器的领先水平。但具体架构细节和第三方基准测试验证尚未公布。

telegram · zaihuapd · Mar 24, 06:01

**背景**: RISC-V 是一种开源指令集架构，正逐步挑战 ARM 和 x86 的垄断地位。Specint2006 是测量整数处理性能的标准基准。Qwen3 和 DeepSeek V3 是参数规模堪比 GPT-4 的中文开源大模型，近期已登陆 AWS Bedrock 平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://www.aboutamazon.com/news/aws/alibaba-qwen3-deepseek-v3-amazon-bedrock">Qwen3 and DeepSeek-V3.1 models now available fully ...</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#AI-Hardware`, `#Cloud-Computing`, `#Edge-Computing`, `#Semiconductors`

---

<a id="item-8"></a>
## [DarkSword 漏洞链通过 Safari 攻击多国用户](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

自 2025 年 11 月起，名为 DarkSword 的高级漏洞利用链通过 Safari 浏览器感染 iPhone，主要针对沙特阿拉伯、土耳其、马来西亚和乌克兰的用户。该攻击链结合了六个漏洞来投放 GHOSTBLADE 等恶意载荷，影响 iOS 18.4 至 18.7 版本，最终在 iOS 26.3 中得到修复。 这一漏洞披露揭示了一种只需访问恶意网站即可入侵 iPhone 的多阶段攻击方式，展现了移动威胁的复杂化趋势。其跨国攻击特征和载荷投放能力表明漏洞利用链正被武器化用于跨境实际攻击。 攻击链中的关键漏洞 CVE-2025-43529 是 WebKit 内存释放后重用漏洞，已在 iOS 18.7.3 中提前修复。该漏洞利用链采用模块化设计，使得不同攻击者能将其适配于不同目的，谷歌已追踪到多个不同组织使用该技术。

telegram · zaihuapd · Mar 24, 11:45

**背景**: DarkSword 是一种结合多个漏洞绕过安全防护的高级 iOS 漏洞利用链。此类攻击链通常从浏览器或渲染引擎漏洞（如 Safari 的 WebKit）开始，然后通过后续漏洞提升权限。GHOSTBLADE 似乎是自定义的载荷名称，而非网络搜索结果中提到的《上古卷轴》游戏道具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword : iOS Exploit Chain Adopted by...</a></li>
<li><a href="https://www.malwarebytes.com/blog/mobile/2026/03/a-darksword-hangs-over-unpatched-iphones">A DarkSword hangs over unpatched iPhones | Malwarebytes</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-43529">NVD - CVE-2025-43529</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#ios`, `#safari`, `#zero-day`, `#vulnerability`

---

<a id="item-9"></a>
## [谷歌推出基于 Gemini 的暗网情报 AI 代理，助力安全运营](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

谷歌正式推出基于 Gemini 的暗网情报服务公开预览版，该服务集成至 Google Threat Intelligence 平台，每日可分析 800 万至 1000 万条暗网帖子，内部测试显示其识别组织相关风险的准确率达 98%。 该技术通过自动化大规模暗网监控实现了威胁检测的重大突破，有望扰乱初始访问中介市场，在数据泄露发生前及时预警，对网络安全防御体系具有革新意义。 该服务会先为客户建立组织画像，重点识别初始访问中介活动、数据泄露和内部威胁等风险。目前主要分析英文暗网论坛内容，未来可能支持更多语言。

telegram · zaihuapd · Mar 24, 13:15

**背景**: 初始访问中介（IABs）是专门向勒索软件组织出售网络入侵权限的网络犯罪分子。暗网中存在大量交易此类权限和被盗数据的地下市场。Google Threat Intelligence 是整合了谷歌基础设施和 VirusTotal 威胁数据的安全平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://teamwin.in/google-says-gemini-ai-agents-are-crawling-the-dark-web-posts-to-detect-threats/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to...</a></li>
<li><a href="https://cloud.google.com/security/products/threat-intelligence">Google Threat Intelligence - know who's targeting you</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#threat-intelligence`, `#dark-web`, `#Google`

---

<a id="item-10"></a>
## [微软对 Windows 11 的'修复'引发批评](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/) ⭐️ 7.0/10

微软处理 Windows 11 问题的方式被用户批评为'煤气灯效应'，包括强制更新和像 Microsoft Start 新闻这样的侵入性功能，该功能在被禁用后会自动重新启用。 这凸显了用户对 Windows 11 中微软敌对用户做法日益增长的不满，如果不妥善解决，可能会削弱信任并推动用户转向其他操作系统。 具体投诉包括 Microsoft Start 新闻显示不需要的内容、强制更新，以及与苹果在 macOS 更新和 iCloud 推广中类似侵入性做法的比较。

hackernews · h0ek · Mar 24, 09:36

**背景**: Windows 11 自推出以来就因其用户界面变化、系统要求和各种内置广告而受到批评。微软有着推送不需要功能的历史，可以追溯到 1990 年代的 Internet Explorer-Netscape 浏览器大战。该公司在政府和企业领域的主导市场地位历史上保护了其免受糟糕用户体验决策的影响。

**社区讨论**: 评论显示用户对微软做法普遍感到沮丧，有人将其比作家暴（尽管有些人认为这种比较不合适），注意到用户虐待的历史模式，并与苹果日益侵入的做法相提并论。一些人建议唯一的解决方案是政府组织放弃微软产品。

**标签**: `#Microsoft`, `#Windows 11`, `#User Experience`, `#Tech Criticism`, `#Software Ethics`

---

<a id="item-11"></a>
## [Starlette 1.0 正式发布，带来 ASGI 框架重大更新](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

作为 FastAPI 基础架构的 Python ASGI 框架 Starlette 1.0 经过八年开发后正式发布，引入了重大变更，包括全新的 lifespan 机制来处理启动/关闭事件。 该版本标志着这个支撑 FastAPI(日下载量超 1000 万次)的框架进入生产就绪阶段，虽然兼容性变化可能影响现有 AI 生成的代码，但为 LLM 辅助开发提供了更好支持。 新版用异步上下文管理器替代了原有的 on_startup/on_shutdown 参数，同时保留了如 httpx(测试)和 Jinja2(模板)等可选依赖，项目已移交 Marcelo Trylesinski 的 GitHub 账号维护。

rss · Simon Willison · Mar 22, 23:57

**背景**: Starlette 是专为异步 Web 服务设计的轻量级 ASGI 框架，提供 WebSocket 支持和后台任务处理。它是 FastAPI 的基础架构但提供更底层的控制。ASGI(异步服务器网关接口)是 Python 用于异步 Web 服务器和应用的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/starlette: The little ASGI framework that ...</a></li>
<li><a href="https://pypi.org/project/starlette/">starlette · PyPI Starlette: A Modern Python ASGI Framework - CodeRivers Python - Starlette - GeeksforGeeks Starlette 1.0.0: Eight Years on Zero-Ver and Finally a Stable ... Starlette</a></li>

</ul>
</details>

**标签**: `#Python`, `#Web Frameworks`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-12"></a>
## [PC Gamer 网站性能审计揭露严重资源臃肿问题](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

对 PC Gamer 网站的审计发现严重性能问题，由于自动播放视频广告和低效资源加载，单篇文章消耗了 37MB 流量。该分析使用 Claude Code 和 Rodney CLI 工具来调查页面结构和加载行为。 这凸显了影响用户体验的网页臃肿问题日益严重，特别是自动播放广告的影响，对优化现代网站的 Web 开发人员和性能工程师具有重要意义。使用 Claude Code 和 Rodney 等 AI 辅助工具的新方法展示了性能审计的新途径。 审计发现由于自动播放视频广告，页面在初始加载后继续下载数百 MB 数据。分析过程中使用 Rodney 按照其推荐的最佳实践，先分析页面的无障碍树结构再创建选择器。

rss · Simon Willison · Mar 22, 22:49

**背景**: Rodney 是 Simon Willison 最近开发的用于与网页交互和分析的 CLI 工具。Claude Code 是 Anthropic 的基于云的编码工具，可通过 Web 界面执行任务、编写代码和运行测试。网页臃肿指的是现代网页因广告、追踪器和不必要的 JavaScript 导致的过大体积和复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/rodney">GitHub - simonw/rodney: CLI tool for interacting with the web</a></li>
<li><a href="https://code.claude.com/docs/en/claude-code-on-the-web">Claude Code on the web - Claude Code Docs</a></li>
<li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">Introducing Showboat and Rodney, so agents can demo what they ...</a></li>

</ul>
</details>

**标签**: `#web-performance`, `#web-bloat`, `#rodney`, `#claude-code`, `#audit`

---

<a id="item-13"></a>
## [JavaScript 沙盒技术对比研究](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了一份详细的 JavaScript 沙盒技术对比研究，涵盖了 isolated-vm、vm2、QuickJS 变体、ShadowRealm 和 Deno Workers 等技术，扩展了 Aaron Harper 最初对 Node.js 工作线程的探索。 这项研究为需要安全运行不受信任 JavaScript 代码的开发人员提供了宝贵见解，解决了 Web 应用和服务器端 JavaScript 环境中的一个关键安全挑战。 对比突出了隔离性与性能之间的权衡：原生 V8 隔离(如 isolated-vm)速度更快，而基于 WebAssembly 的解决方案(如 QuickJS)提供更强的隔离性，但性能较低且功能受限。

rss · Simon Willison · Mar 22, 19:53

**背景**: JavaScript 沙盒是一种安全机制，用于隔离并安全执行不受信任的代码。常见方法包括 V8 隔离、WebAssembly 运行时以及 ShadowRealm 等语言级提案。Node.js 和 Deno 通过工作线程和权限模型提供了不同的内置沙盒功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybercorsairs.com/sandboxing-javascript-a-side-by-side-look-at-your-options/">JavaScript Sandboxing: Running Untrusted Code Safely</a></li>
<li><a href="https://letsdatascience.com/news/javascript-sandboxing-research-compares-nodejs-options-6f16be0b">JavaScript Sandboxing Research Compares Node.js Options</a></li>

</ul>
</details>

**标签**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-14"></a>
## [基于 CRDT 的版本控制交互式可视化工具](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison 开发了一个交互式可视化工具，用于展示 Bram Cohen 基于 CRDT 的版本控制系统 Manyana，该工具使用 Pyodide 在浏览器中运行 Python，并借助 Claude AI 生成解释说明。 该工具为理解版本控制系统中的 CRDT 提供了直观方式，可能通过实现无需集中协调的无冲突合并，彻底改变协作编辑方式。 可视化基于 Cohen 的 470 行 Python 实现，UI 使用 Pyodide 构建，后者通过 WebAssembly 允许 Python 直接在浏览器中运行。

rss · Simon Willison · Mar 22, 18:57

**背景**: CRDT（无冲突复制数据类型）是能自动解决分布式系统中冲突的数据结构。Pyodide 是通过 WebAssembly 在浏览器中运行的 Python 发行版，可实现无需服务器处理的交互式 Python 应用。Bram Cohen 是 BitTorrent 的创造者，一直致力于开发下一代版本控制系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/r-language/what-is-crdt-in-distributed-systems/">What is CRDT in Distributed Systems? - GeeksforGeeks</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 0.29.3</a></li>

</ul>
</details>

**标签**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-15"></a>
## [我国日均 AI 词元调用量两年增长超千倍](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

国家数据局披露，我国日均 AI 词元调用量从 2024 年初的 1000 亿飙升至 2025 年 3 月的 140 万亿，两年间增长超千倍。 这一爆发式增长标志着中国 AI 技术商业化进程加速，围绕词元调用、分发与结算的新价值体系正在形成，成为人工智能产业商业化的重要路径。 词元作为大模型处理的最小信息单元（约 1000 词元≈750 个英文单词），具有可计量、可定价、可交易的特征，为 AI 服务创造了新的经济模型。

telegram · zaihuapd · Mar 24, 07:22

**背景**: 词元化技术将文本/图像转化为 AI 模型可处理的数字表示。我国自 2020 年推进的数据要素市场化配置改革加速了基于词元的 AI 生态发展，这一增长与国家将数据作为新型生产要素的政策方向一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/">Tokens Explained: The Currency of Generative AI</a></li>
<li><a href="https://ideas.repec.org/a/eee/finana/v104y2025ipas1057521925004168.html">Data element marketization and corporate investment efficiency...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Tokenization`, `#China`, `#Data Economy`, `#Commercialization`

---

<a id="item-16"></a>
## [欧盟拟推年龄验证 App 或限制非谷歌授权安卓系统](https://t.me/zaihuapd/40484) ⭐️ 7.0/10

欧盟正在开发一款开源年龄验证 App，要求设备通过谷歌 Play Integrity 验证并从 Play 商店下载且需谷歌账号，这将导致未获谷歌授权的安卓系统（如 GrapheneOS）无法使用。 此举可能加深对美国科技巨头谷歌的依赖，违背欧盟数字主权目标，同时引发隐私担忧，因为将排除注重隐私的安卓分支系统。 该 App 将使用谷歌 Play Integrity API（前身为 SafetyNet）验证设备真实性，要求设备安装谷歌服务，这将排除那些刻意避免谷歌服务的安全增强型安卓变体。

telegram · zaihuapd · Mar 24, 12:22

**背景**: Play Integrity API 是谷歌用于验证应用真实性和设备完整性的系统。GrapheneOS 是一个注重隐私的安卓分支系统，其设计刻意移除了谷歌服务。欧盟一直在推动数字主权计划以减少对非欧盟科技公司的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Play_Integrity_API">Play Integrity API - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**社区讨论**: 开发者和隐私倡导者在 GitHub 等平台强烈反对这一举措，认为其违背开源原则，增加了对谷歌的依赖，同时排除了注重隐私的用户群体。

**标签**: `#EU Regulation`, `#Android`, `#Digital Sovereignty`, `#Privacy`, `#Open Source`

---