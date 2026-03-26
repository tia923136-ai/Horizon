---
layout: default
title: "Horizon Summary: 2026-03-26 (EN)"
date: 2026-03-26
lang: en
---

> From 42 items, 14 important content pieces were selected

---

1. [LiteLLM v1.82.8 on PyPI compromised with credential-stealing exploit](#item-1) ⭐️ 9.0/10
2. [Tesla Model 3 computer repurposed from salvaged parts](#item-2) ⭐️ 8.0/10
3. [ARC-AGI-3 Launches as New Benchmark for AGI Evaluation](#item-3) ⭐️ 8.0/10
4. [EU pushes for mass scanning of private messages despite privacy concerns](#item-4) ⭐️ 8.0/10
5. [Package Managers Adopt Dependency Cooldowns to Combat Supply Chain Attacks](#item-5) ⭐️ 8.0/10
6. [Streaming Experts Technique Enables Large MoE Models on Constrained Hardware](#item-6) ⭐️ 8.0/10
7. [Apifox desktop client compromised in supply chain attack stealing SSH keys](#item-7) ⭐️ 8.0/10
8. [China Computer Federation opposes NeurIPS' US-sanctioned institution submission ban](#item-8) ⭐️ 8.0/10
9. [Apple and Google partner to integrate Gemini AI into Siri](#item-9) ⭐️ 8.0/10
10. [Critique of Speed Over Quality in AI-Driven Development](#item-10) ⭐️ 7.0/10
11. [LiteLLM PyPI Hack Affected 47,000 Downloads](#item-11) ⭐️ 7.0/10
12. [Claude Code introduces auto mode with safeguards](#item-12) ⭐️ 7.0/10
13. [Pinduoduo Launches 'New Pinmu' with 100B RMB Investment for Brand Self-Operation](#item-13) ⭐️ 7.0/10
14. [GitHub updates Copilot data policy: free and paid individual users' interactions now included in AI training by default, with opt-out option](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM v1.82.8 on PyPI compromised with credential-stealing exploit](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

The LiteLLM v1.82.8 package on PyPI was compromised with a credential-stealing exploit hidden in a litellm_init.pth file, which automatically executes upon package installation without requiring the package to be imported. PyPI has quarantined the package, limiting the exposure window to a few hours. This is a serious supply chain attack affecting a widely-used Python package, demonstrating how malicious actors can exploit trusted distribution channels like PyPI to steal sensitive credentials. The attack's automatic execution upon installation makes it particularly dangerous, as users may be compromised without any explicit action. The exploit was hidden in base64 within litellm_init.pth and could steal credentials from numerous sensitive files including SSH keys, cloud service configurations, and cryptocurrency wallets. The attack appears to have originated from compromised PyPI credentials stolen via an earlier exploit of the Trivy security scanner.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is a popular Python library for interacting with large language models. PyPI (.pth) files are special Python path configuration files that can execute arbitrary code when the Python interpreter starts. Supply chain attacks target software distribution channels to inject malicious code into legitimate packages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.banandre.com/blog/pypi-silent-killer-pth-file-secrets-theft">PyPI’s Silent Killer: How a . pth File Stole Your Secrets... - Banandre</a></li>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm _ init . pth in litellm...</a></li>
<li><a href="https://dev.to/diverdale/litellm-pypi-supply-chain-compromise-how-a-popular-llm-proxy-became-a-credential-stealing-backdoor-noa">LiteLLM PyPI Supply Chain Compromise: How... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#vulnerability`

---

<a id="item-2"></a>
## [Tesla Model 3 computer repurposed from salvaged parts](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 8.0/10

A developer successfully ran a Tesla Model 3's computer on a desktop setup using salvaged parts from crashed vehicles, demonstrating the feasibility of repurposing Tesla's hardware outside of a car. The project also highlights Tesla's 'Root access program' which grants researchers SSH certificates for qualifying security vulnerabilities. This demonstrates the accessibility of Tesla's proprietary hardware for research and reverse engineering, which could lead to new discoveries in automotive computing and security. It also sheds light on Tesla's unique approach to security research incentives compared to other tech companies. The project faced challenges with mechanical connectors, particularly a 6-pin connector, despite having wiring schematics. Tesla's Hardware 3 computer, used in this project, features custom Tesla-designed FSD chips that replaced NVIDIA hardware in 2019.

hackernews · driesdep · Mar 25, 21:11

**Background**: Tesla's Autopilot hardware evolved from using NVIDIA's Drive PX 2 platform to custom-designed FSD chips starting in 2019. The company offers a security research program that rewards qualifying researchers with permanent root access to their own vehicles, similar to Apple's Security Research Device Program.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware">Tesla Autopilot hardware - Wikipedia</a></li>
<li><a href="https://www.autopilotreview.com/tesla-custom-ai-chips-hardware-3/">Tesla Hardware 3 (Full Self-Driving Computer) Detailed</a></li>
<li><a href="https://applyingai.com/2025/07/decoding-teslas-core-ai-and-hardware-architecture-a-ceos-perspective/">Decoding Tesla’s Core AI and Hardware Architecture: A CEO’s ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted similarities between Tesla's root access program and Apple's security research initiatives. Some discussed technical challenges with automotive connectors, while others pointed out the general-purpose nature of LVDS cables beyond automotive applications. There was also discussion about potential 3D-printed solutions for mechanical connector issues.

**Tags**: `#automotive`, `#reverse-engineering`, `#tesla`, `#embedded-systems`, `#hardware-hacking`

---

<a id="item-3"></a>
## [ARC-AGI-3 Launches as New Benchmark for AGI Evaluation](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

The ARC-AGI-3 benchmark was announced on March 25, 2026, featuring 1,000+ levels across 150+ environments designed to test AI's ability to explore, learn, plan, and adapt through interactive reasoning tasks. This benchmark represents a significant shift in AGI evaluation by focusing on novel problem-solving rather than pattern recognition, potentially exposing current AI systems' fundamental limitations in achieving human-like intelligence. The benchmark uses universally accessible cognitive primitives as input and compares AI performance against human baselines, though its scoring methodology (using second-best human performance as reference) has drawn criticism.

hackernews · lairv · Mar 25, 18:16

**Background**: AGI (Artificial General Intelligence) refers to AI systems that can understand, learn, and apply knowledge across diverse domains like humans. Traditional AI benchmarks often measure narrow capabilities, while ARC-AGI-3 aims to assess more general cognitive abilities. The benchmark was developed by François Chollet and the ARC Prize Foundation to address limitations in current AI evaluation methods.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3/">ARC-AGI-3</a></li>
<li><a href="https://www.fastcompany.com/91515360/arc-prize-foundation-new-ai-benchmark">Exclusive: This new benchmark could expose AI’s biggest weakness - Fast Company</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with some praising the benchmark's focus on genuine problem-solving while others criticize its human baseline methodology. Notable debates include whether AI needs to replicate human learning mechanisms to achieve AGI, with comparisons made to airplanes not needing to flap wings like birds.

**Tags**: `#AGI`, `#AI-benchmarks`, `#machine-learning`, `#research`, `#cognitive-science`

---

<a id="item-4"></a>
## [EU pushes for mass scanning of private messages despite privacy concerns](https://fightchatcontrol.eu/?foo=bar) ⭐️ 8.0/10

The EU is attempting to extend Regulation (EU) 2021/1232, which allows voluntary scanning of private communications, despite Parliament's March 11 vote favoring targeted monitoring with judicial oversight instead of blanket surveillance. This threatens fundamental digital rights for 450 million EU citizens by enabling mass surveillance of private communications without sufficient safeguards, setting a dangerous precedent for government overreach in the digital sphere. The proposed extension would maintain 'voluntary' scanning provisions first introduced in 2021, while Parliament's alternative proposal requiring judicial involvement for targeted monitoring was rejected by the Council, leading to legislative deadlock.

hackernews · MrBruh · Mar 25, 20:27

**Background**: Mass surveillance in the EU has been controversial since 2013 revelations about US spying programs. The current 'Chat Control 1.0' measures were implemented temporarily in 2021 following debates about balancing security needs with privacy rights under the European Convention on Human Rights. Previous EU court rulings have struck down similar mass data retention laws as disproportionate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mass_surveillance">Mass surveillance - Wikipedia</a></li>
<li><a href="https://www.statewatch.org/news/2024/june/policing-by-design-the-latest-eu-surveillance-plan/">Statewatch | Policing by design: the latest EU surveillance plan</a></li>
<li><a href="https://fra.europa.eu/en/news/2025/mass-surveillance-case-law-factsheet">Mass surveillance case law factsheet | European Union Agency for Fundamental Rights</a></li>

</ul>
</details>

**Discussion**: Comments reveal deep concerns about privacy erosion, with some noting Hungary's support as a 'red flag'. Others question why pro-privacy legislation isn't being advanced instead, while technical contributors clarify this extends existing temporary measures rather than creating new powers.

**Tags**: `#privacy`, `#EU-regulation`, `#digital-rights`, `#surveillance`, `#legislation`

---

<a id="item-5"></a>
## [Package Managers Adopt Dependency Cooldowns to Combat Supply Chain Attacks](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 8.0/10

Major package managers including pnpm, Yarn, Bun, Deno, uv, pip, and npm have recently implemented dependency cooldown features, which delay installation of newly published packages to allow time for security vetting. This follows recent high-profile supply chain attacks like the malicious LiteLLM package on PyPI. Dependency cooldowns provide a crucial defense against supply chain attacks by creating a buffer period to detect compromised packages before they're widely installed. This addresses a critical vulnerability in modern software development where immediate dependency updates can propagate malicious code rapidly. Implementation details vary: pnpm uses minimumReleaseAge (in minutes), Yarn has npmMinimalAgeGate, Bun configures via bunfig.toml, while pip currently only supports absolute timestamps. Most solutions allow exemptions for trusted packages through allowlists like minimumReleaseAgeExclude in pnpm.

rss · Simon Willison · Mar 24, 21:11

**Background**: Dependency cooldowns refer to intentionally delaying installation of newly published package versions to allow time for community scrutiny. The concept gained urgency after multiple high-profile supply chain attacks where compromised maintainer accounts were used to push malicious updates to widely-used packages. Package managers are now building this security measure directly into their tools.

<details><summary>References</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://pnpm.io/blog/releases/10.16">pnpm 10.16 | pnpm</a></li>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI - FutureSearch</a></li>

</ul>
</details>

**Tags**: `#package-managers`, `#security`, `#supply-chain`, `#devops`, `#dependencies`

---

<a id="item-6"></a>
## [Streaming Experts Technique Enables Large MoE Models on Constrained Hardware](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Researchers have successfully implemented the streaming experts technique to run massive Mixture-of-Experts models like Qwen3.5-397B-A17B and Kimi K2.5 on devices with limited RAM, including a MacBook Pro (96GB RAM) and even an iPhone (0.6 tokens/second). The approach involves streaming expert weights from SSD as needed during token processing. This breakthrough significantly lowers the hardware barrier for running state-of-the-art AI models, making powerful MoE architectures accessible on consumer devices. It could democratize advanced AI capabilities and enable new edge computing applications where cloud connectivity is limited. The Qwen3.5-397B-A17B model was initially run in 48GB RAM, while the 1-trillion-parameter Kimi K2.5 (with 32B active weights) was demonstrated on a 96GB M2 Max MacBook Pro. Performance varies from 0.6 tokens/second on iPhone to ~1.7 tokens/second on a 128GB M4 Max.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) models are AI architectures that use specialized sub-networks ('experts') for different inputs, activating only relevant experts per token to improve efficiency. Traditional MoE implementations require all expert weights to be loaded in memory, making large models impractical for devices with limited RAM. The streaming experts approach dynamically loads only the needed expert weights from storage during inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/mixture-of-experts/">What Is Mixture of Experts (MoE) and How It Works? | NVIDIA Glossary</a></li>
<li><a href="https://openreview.net/forum?id=stXtBqyTWX&noteId=p7ADDxdU8g">Toward Efficient Inference for Mixture of Experts | OpenReview</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#hardware-optimization`, `#streaming`

---

<a id="item-7"></a>
## [Apifox desktop client compromised in supply chain attack stealing SSH keys](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 8.0/10

The Apifox desktop client was compromised via a supply chain attack where attackers modified its CDN-hosted analytics script to inject malicious code that steals SSH keys, Git credentials, shell history, and process lists. The attack has been active since March 4th, affecting Windows, macOS, and Linux users. This is a high-severity security incident affecting a widely-used API development tool, potentially compromising developers' sensitive credentials and enabling further lateral attacks. Supply chain attacks on devtools can have cascading effects across software ecosystems. Security researcher phith0n has reverse-engineered the malicious payload. Users can check for compromise by examining Network Persistent State files for 'apifox.it.com' or LevelDB entries with 'rl_mc'/'rl_headers' keys. Official mitigation includes blocking malicious domains and reinstalling the latest version.

telegram · zaihuapd · Mar 25, 11:10

**Background**: Apifox is a popular all-in-one API platform combining documentation, debugging, and testing features. LevelDB is a key-value storage library used by Chromium-based applications for persistent data. Supply chain attacks target software distribution channels to infect downstream users.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.apifox.com/download">下载 Apifox - Windows macOS Linux 桌面版下载</a></li>
<li><a href="https://en.wikipedia.org/wiki/LevelDB">LevelDB - Wikipedia</a></li>
<li><a href="https://phoenix.security/teampcp-supply-chain-attack-trivy-checkmarx-github-actions-npm-canisterworm/">TeamPCP Supply Chain Attack: Trivy to Checkmarx to npm (2026)</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain-attack`, `#devtools`, `#api`, `#vulnerability`

---

<a id="item-8"></a>
## [China Computer Federation opposes NeurIPS' US-sanctioned institution submission ban](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 8.0/10

The China Computer Federation (CCF) issued a statement opposing NeurIPS 2026's policy prohibiting submissions from US-sanctioned institutions and called for Chinese researchers to boycott the conference. CCF threatened to remove NeurIPS from its recommended international academic conference list if the policy isn't revoked. This confrontation highlights growing tensions between academic freedom and geopolitical restrictions in AI research, potentially reshaping international collaboration patterns. As NeurIPS is a premier AI conference, this standoff could significantly impact global research dissemination and China's participation in top-tier academic forums. NeurIPS 2026 explicitly banned submissions from certain US-sanctioned organizations in its submission guidelines. CCF's recommended conference list carries significant weight in China's academic evaluation system, making its potential removal of NeurIPS a substantial threat.

telegram · zaihuapd · Mar 25, 14:07

**Background**: NeurIPS (Conference on Neural Information Processing Systems) is one of the world's most prestigious AI conferences, first held in 1987. The China Computer Federation's recommended conference list serves as an official benchmark for academic evaluation in China's computer science community, influencing researchers' publication strategies and career advancement.

<details><summary>References</summary>
<ul>
<li><a href="https://neurips.cc/">NeurIPS - 2026 Conference</a></li>
<li><a href="https://ccf.atom.im/">中国计算机学会推荐国际学术会议和期刊目录（2026） 中国计算机学会推荐国际学术会议和期刊目录CCF-A（2025年使用） 重磅更新！CCF 第七版国际学术会议 / 期刊目录（2026.3）发布，收藏备... 中国计算机学会推荐国际学术会议和期刊目录 （2026年）-辽宁工程技术... 刚刚！2026年中国计算机学会 (CCF) 推荐A-B-C类期刊目录公示！_调整_... 科学网-重磅更新！CCF 第七版国际学术会议 / 期刊目录（2026.3）发布...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#NeurIPS`, `#Academic Freedom`, `#Politics`, `#Research Ethics`

---

<a id="item-9"></a>
## [Apple and Google partner to integrate Gemini AI into Siri](https://t.me/zaihuapd/40506) ⭐️ 8.0/10

Apple and Google announced a multi-year partnership where Google's Gemini AI models will power the next generation of Apple Foundation Models, enhancing Siri's capabilities while maintaining on-device and private cloud processing for privacy. The collaboration will support new Apple intelligence features launching this year. This partnership combines Apple's privacy-focused ecosystem with Google's advanced Gemini AI, potentially creating the most powerful yet privacy-conscious AI assistant. It could reshape the competitive landscape against other AI assistants like Amazon Alexa and Microsoft Copilot. The integration will use multiple Gemini model variants (Pro, Deep Think, Flash) while maintaining Apple's privacy standards through on-device processing and private cloud compute. Apple emphasizes this won't compromise existing privacy protections.

telegram · zaihuapd · Mar 25, 16:32

**Background**: Gemini is Google's family of multimodal LLMs that succeed LaMDA and PaLM 2, capable of processing text, images, audio and video. Apple Foundation Models are on-device LLMs that power Apple Intelligence features while maintaining privacy by processing data locally rather than in the cloud.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://developer.apple.com/documentation/foundationmodels">Foundation Models | Apple Developer Documentation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Apple`, `#Google`, `#Siri`, `#Gemini`

---

<a id="item-10"></a>
## [Critique of Speed Over Quality in AI-Driven Development](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Mario Zechner, creator of the Pi agent framework, critiques the unchecked speed of AI-driven software development, warning of accumulating 'cognitive debt' from rapid agent-generated code. He advocates for deliberate slowdowns and human oversight in architectural decisions. This highlights a critical tension in agentic engineering: while AI agents dramatically accelerate coding, their unchecked use risks creating unmaintainable systems. The critique resonates as organizations increasingly adopt AI coding assistants without established guardrails. The Pi framework (used by OpenClaw) supports 30+ agent types but emphasizes scoped memory and SQLite-based state tracking. Zechner specifically warns against automating architecture/API decisions, suggesting daily code generation limits aligned with review capacity.

rss · Simon Willison · Mar 25, 21:47

**Background**: Agentic engineering refers to systems where AI agents autonomously plan and execute tasks with minimal human oversight. The Pi framework is an open-source tool for building such agents, featuring persistent memory and context management. Cognitive debt describes the mental overhead from rapidly accumulated technical decisions without proper evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/24601/agent-deep-research">GitHub - 24601/ agent -deep-research: Deep research (CLI and agent ...)</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://addyosmani.com/blog/agentic-engineering/">Agentic Engineering - AddyOsmani.com</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software-engineering`, `#ethics`, `#automation`, `#productivity`

---

<a id="item-11"></a>
## [LiteLLM PyPI Hack Affected 47,000 Downloads](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 7.0/10

Analysis reveals 46,996 downloads of compromised LiteLLM PyPI packages (versions 1.82.7 and 1.82.8) during their 46-minute availability, with 88% of dependent projects failing to implement proper version pinning that could have prevented the exploit. This incident highlights critical vulnerabilities in Python's package supply chain, demonstrating how quickly malicious packages can spread and the widespread failure of dependency management practices that could mitigate such risks. The attack involved multi-stage credential stealing through .pth files for persistence, with TeamPCP identified as the threat actor. The BigQuery PyPI dataset was instrumental in quantifying the impact.

rss · Simon Willison · Mar 25, 17:21

**Background**: LiteLLM is a popular Python package that provides a unified interface for various large language models (LLMs). PyPI (Python Package Index) is the official repository for Python packages, where version pinning refers to explicitly specifying package versions in requirements to prevent automatic updates to potentially vulnerable versions.

<details><summary>References</summary>
<ul>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI</a></li>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential Stealer</a></li>
<li><a href="https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign">LiteLLM TeamPCP Supply Chain Attack: Malicious PyPI Packages | Wiz Blog</a></li>

</ul>
</details>

**Tags**: `#security`, `#pypi`, `#supply-chain`, `#python`, `#packaging`

---

<a id="item-12"></a>
## [Claude Code introduces auto mode with safeguards](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code has launched auto mode, a new permissions mode where Claude makes decisions on your behalf while using Claude Sonnet 4.6 as a classifier to monitor and block unsafe actions before execution. This provides a safer alternative to the dangerous --dangerously-skip-permissions flag, enabling more automated workflows while maintaining security through built-in safeguards and customizable rules. The auto mode uses Claude Sonnet 4.6 as a separate classifier model to review conversations before execution, blocking actions that escalate beyond task scope or target untrusted infrastructure. It includes extensive default filters covering areas like test artifacts, local operations, and read-only operations.

rss · Simon Willison · Mar 24, 23:57

**Background**: Claude Code is a software development tool powered by Anthropic's Claude AI models. The --dangerously-skip-permissions flag was previously used to bypass all permission checks but posed significant security risks. Claude Sonnet 4.6 is a large language model optimized for multi-step workflows and conditional logic.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude</a></li>
<li><a href="https://www.anthropic.com/claude/sonnet">Claude Sonnet 4.6 \ Anthropic</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#code-safety`, `#permissions`, `#Claude`

---

<a id="item-13"></a>
## [Pinduoduo Launches 'New Pinmu' with 100B RMB Investment for Brand Self-Operation](https://m.tmtpost.com/nictation/7929040.html) ⭐️ 7.0/10

Pinduoduo announced its 'New Pinmu' initiative, pledging to invest 100 billion RMB over three years to transition from platform operations to brand self-operation, starting with an initial cash injection of 15 billion RMB. The project aims to integrate supply chain resources from Pinduoduo and Temu to build and incubate self-operated brands for global markets. This marks a strategic shift for Pinduoduo, potentially reshaping its role in global e-commerce by directly controlling brands and supply chains, which could enhance profitability and market competitiveness. The move also signals intensifying competition in cross-border e-commerce, particularly against rivals like Amazon and Shein. The initiative includes establishing a dedicated company in Shanghai, focusing on category-specific brands for diverse markets. It follows Zhao Jiazhen's appointment as co-chairman in December 2023, reflecting leadership-driven strategy execution.

telegram · zaihuapd · Mar 25, 12:37

**Background**: Pinduoduo is a major Chinese e-commerce platform known for its group-buying model, while Temu is its international sister site offering discounted goods globally. Brand self-operation models allow platforms to bypass third-party sellers, gaining higher margins and quality control—a trend seen in Amazon's 'Basics' line and Alibaba's Tmall Supermarket.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Temu">Temu - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1366554522003283">How does manufacturer’s self-operating channel interact with ...</a></li>

</ul>
</details>

**Tags**: `#e-commerce`, `#supply-chain`, `#business-strategy`, `#china-tech`, `#retail`

---

<a id="item-14"></a>
## [GitHub updates Copilot data policy: free and paid individual users' interactions now included in AI training by default, with opt-out option](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) ⭐️ 7.0/10

GitHub announced updates to Copilot's data usage policy starting April 24, where interactions from Copilot Free, Pro, and Pro+ users (including inputs, outputs, code snippets, and context) will be used to train AI models by default, with an opt-out option in Privacy settings. Enterprise users and private codebases are exempt from this change. This change significantly expands the training data pool for GitHub's AI models, potentially improving Copilot's performance but raising privacy concerns for individual developers. It reflects the growing industry trend of leveraging user interactions to refine AI tools, balancing innovation with user control. Training data includes nearby code context, comments, filenames, repo structures, navigation patterns, and feedback on suggestions. Data may be shared with Microsoft but not third-party AI providers. Previously disabled data collection preferences remain unaffected.

telegram · zaihuapd · Mar 26, 00:47

**Background**: GitHub Copilot is an AI-powered code completion tool developed by GitHub and OpenAI. Many AI systems improve through machine learning on user interactions, but this often requires balancing model improvement with privacy considerations. The opt-out mechanism follows similar approaches by other AI services like Anthropic's Claude.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/">Updates to GitHub Copilot interaction data usage policy</a></li>
<li><a href="https://www.windowscentral.com/software-apps/microsofts-github-is-going-to-start-using-copilot-interactions-to-train-ai-models-and-its-starting-soon">GitHub is going to use Copilot interactions to train its AI</a></li>
<li><a href="https://magazine.mindplex.ai/post/anthropic-will-include-user-interactions-in-claudes-training-data">Anthropic will include user interactions in Claude's training ... | Mindplex</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#AI`, `#Privacy`, `#Copilot`, `#DataPolicy`

---