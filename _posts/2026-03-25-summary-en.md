---
layout: default
title: "Horizon Summary: 2026-03-25 (EN)"
date: 2026-03-25
lang: en
---

> From 34 items, 15 important content pieces were selected

---

1. [LiteLLM PyPI packages 1.82.7 and 1.82.8 found compromised](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.82.8 PyPI package compromised with credential stealer](#item-2) ⭐️ 9.0/10
3. [Streaming experts technique enables trillion-parameter models on consumer hardware](#item-3) ⭐️ 8.0/10
4. [Nvidia accused of leveraging financial power to lock AI startups into its ecosystem](#item-4) ⭐️ 8.0/10
5. [Alibaba DAMO releases Xuantie C950 RISC-V CPU, claims record performance](#item-5) ⭐️ 8.0/10
6. [DarkSword Safari Exploit Chain Disclosed, Affecting iOS 18.4-18.7](#item-6) ⭐️ 8.0/10
7. [Google launches Gemini dark web intelligence AI agent in preview](#item-7) ⭐️ 8.0/10
8. [OpenAI to discontinue Sora, shut API, end Disney deal](#item-8) ⭐️ 8.0/10
9. [OpenAI Shuts Down Sora Video App](#item-9) ⭐️ 7.0/10
10. [Claude Code Introduces Auto Mode with Safeguards](#item-10) ⭐️ 7.0/10
11. [Package Managers Adopt Dependency Cooldowns to Combat Supply Chain Attacks](#item-11) ⭐️ 7.0/10
12. [China's daily AI token usage surges over 1,000x, hits 140 trillion in March 2025](#item-12) ⭐️ 7.0/10
13. [EU's age verification app may block non-Google Android systems](#item-13) ⭐️ 7.0/10
14. [Microsoft releases 7 Rust training books covering beginner to expert topics](#item-14) ⭐️ 7.0/10
15. [Claude Code Launches Auto Mode with Built-in Safety Checks](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM PyPI packages 1.82.7 and 1.82.8 found compromised](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

Versions 1.82.7 and 1.82.8 of LiteLLM on PyPI were found to contain malicious base64-encoded code in proxy_server.py that triggered a forkbomb attack, exhausting system memory. The maintainers have quarantined the package on PyPI and are investigating the breach. This is a critical supply chain attack affecting a popular LLM integration library used by many AI developers, potentially compromising thousands of systems. It highlights ongoing security risks in open-source package ecosystems and the need for better dependency verification. The attack involved a base64 payload that decoded and executed malicious code, exhibiting characteristics of the TeamPCP hacking group's recent campaign. Docker users were unaffected as versions are pinned in requirements.txt.

hackernews · dot_treo · Mar 24, 12:06

**Background**: LiteLLM is an open-source library providing a unified interface for 100+ LLM APIs including OpenAI and Anthropic. PyPI is Python's official package repository, recently targeted in supply chain attacks. A forkbomb is a denial-of-service attack where processes rapidly replicate to exhaust system resources.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm">GitHub - BerriAI/litellm: Python SDK, Proxy Server (AI ... litellm - PyPI LiteLLM on PyPI Was Compromised, What the Attack Changed and ... Popular LiteLLM PyPI package compromised in TeamPCP supply ... litellm | Python SDK, Proxy Server (AI Gateway) to call 100 ... LiteLLM - Getting Started GitHub - BerriAI/ litellm : Python SDK, Proxy Server (AI Gateway) to call A gentle introduction to LiteLLM - Medium litellm · PyPI A gentle introduction to LiteLLM. Unify LLM APIs across ... Top Stories</a></li>
<li><a href="https://pypi.org/project/litellm/">litellm - PyPI</a></li>
<li><a href="https://www.imperva.com/learn/ddos/fork-bomb/">What is a Fork Bomb (Rabbit Virus) | DDoS Attack Glossary ... What Is Fork Bomb Malware and How Does It Work? What Is Fork Bomb Attack? — Definition by ThreatDotMedia What Is a Fork Bomb? Prevention & Linux Fix | SupportPro Fork bomb definition – Glossary | NordVPN</a></li>

</ul>
</details>

**Discussion**: Maintainers confirmed the breach originated from a compromised CI/CD tool (Trivy), while security experts linked it to TeamPCP's campaign. Discussions highlighted the need for better sandboxing in development environments, with suggestions ranging from canary tokens to VM-level isolation.

**Tags**: `#security`, `#pypi`, `#supply-chain`, `#malware`, `#devops`

---

<a id="item-2"></a>
## [LiteLLM v1.82.8 PyPI package compromised with credential stealer](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

The LiteLLM v1.82.8 package on PyPI was compromised with a credential stealer hidden in a base64-encoded litellm_init.pth file, which activates upon installation without requiring the package to be imported. PyPI has quarantined the package, limiting the exposure window to a few hours. This is a critical supply chain attack affecting a widely-used Python package, potentially compromising sensitive credentials across multiple systems and services. The attack highlights the growing risk of malicious actors exploiting trusted distribution channels like PyPI. The credential stealer targets a wide range of sensitive files, including SSH keys, cloud service credentials, and cryptocurrency wallets. The attack originated from compromised PyPI credentials likely stolen via a prior exploit of the Trivy security scanner.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is a popular Python library for interacting with large language models (LLMs). PyPI (Python Package Index) is the official repository for Python packages, making it a high-value target for supply chain attacks. .pth files in Python are special files that can execute code when the Python interpreter starts.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm _ init . pth in litellm...</a></li>
<li><a href="https://simonwillison.net/2026/Mar/24/malicious-litellm/">Malicious litellm _ init . pth in litellm 1.82.8 — credential stealer</a></li>
<li><a href="https://devblogs.co/posts/malicious-litellm-initpth-in-litellm-1828-credential-stealer">Malicious litellm _ init . pth in litellm 1.82.8 — credential stealer</a></li>

</ul>
</details>

**Tags**: `#security`, `#python`, `#pypi`, `#vulnerability`, `#supply-chain`

---

<a id="item-3"></a>
## [Streaming experts technique enables trillion-parameter models on consumer hardware](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Researchers demonstrated running trillion-parameter Mixture-of-Experts models like Kimi K2.5 on consumer devices (MacBook Pro, iPhone) by streaming expert weights from SSD instead of loading full models into RAM. The technique achieved 1.7 tokens/sec on a 128GB M4 Max Mac and 0.6 tokens/sec on an iPhone. This breakthrough democratizes access to massive AI models by enabling them to run on affordable consumer hardware instead of requiring expensive server-grade GPUs with terabytes of memory. It could accelerate on-device AI applications while maintaining model capabilities. The approach leverages MoE models' sparse activation (only ~32B weights active at once) and fast SSD speeds (~17GB/s). Current limitations include slow token generation speeds (0.6-1.7 tokens/sec) due to SSD latency being the bottleneck.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) models divide neural networks into specialized sub-models ('experts'), with a gating mechanism activating only relevant experts per input. This allows huge parameter counts (e.g. 1T) while keeping computational costs manageable since most weights remain inactive. Traditional implementations require loading all experts into memory.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@shubhamku2022/mixture-of-experts-models-for-efficient-ai-3f754759ef19">Mixture of Experts Models for Efficient AI | by Shubhamku | Medium</a></li>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#Hardware`, `#Optimization`

---

<a id="item-4"></a>
## [Nvidia accused of leveraging financial power to lock AI startups into its ecosystem](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

Nvidia has invested billions since 2022 in AI startups like OpenAI, CoreWeave, and Reflection, acting as both supplier and investor to effectively lock them into its ecosystem. The company also reportedly uses high-value acquisitions like its $20B deal with Groq to acquire talent while avoiding antitrust scrutiny. This strategy could stifle competition in the AI hardware market by making it financially difficult for startups to adopt alternatives like AMD, potentially violating antitrust principles. US senators have already raised concerns about Nvidia's tactics to dominate the AI infrastructure landscape. CoreWeave operates Nvidia's 'fastest AI supercomputer' in Texas, while Reflection AI focuses on autonomous coding agents. Groq's LPU chip was specifically designed for AI inference tasks, making its acquisition strategically valuable.

telegram · zaihuapd · Mar 24, 03:02

**Background**: Nvidia's GPUs have become the gold standard for AI training due to their CUDA architecture and software ecosystem. Startups like CoreWeave provide cloud-based GPU infrastructure, while Groq developed alternative AI chips to compete with Nvidia's dominance. Reflection AI represents the next wave of AI startups working on autonomous systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://groq.com/">Groq is fast, low cost inference.</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Nvidia`, `#Antitrust`, `#Semiconductors`, `#Market-Competition`

---

<a id="item-5"></a>
## [Alibaba DAMO releases Xuantie C950 RISC-V CPU, claims record performance](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

Alibaba DAMO Academy unveiled its flagship Xuantie C950 RISC-V CPU on March 24 at the 2026 Xuantie RISC-V Ecosystem Conference in Shanghai. The processor achieved over 70 points in the Specint2006 single-core test, setting a new performance record for publicly available RISC-V chips. This breakthrough demonstrates RISC-V's growing capability in high-performance computing and AI applications, potentially challenging ARM and x86 dominance in cloud and edge computing. The native support for billion-parameter AI models like Qwen3 and DeepSeek V3 positions it as a contender for next-gen AI workloads. The chip integrates DAMO's proprietary AI acceleration engine and specifically targets cloud computing, generative AI, high-end robotics, and edge computing scenarios. However, independent verification of its performance claims and detailed architectural specifications are not yet publicly available.

telegram · zaihuapd · Mar 24, 06:01

**Background**: RISC-V is an open standard instruction set architecture that has gained traction as an alternative to proprietary architectures like ARM and x86. The Specint2006 benchmark measures integer computation performance and is widely used for CPU comparisons. Qwen3 is Alibaba's large language model family with variants ranging from 0.6B to 235B parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#AI Hardware`, `#Cloud Computing`, `#Edge Computing`, `#Semiconductors`

---

<a id="item-6"></a>
## [DarkSword Safari Exploit Chain Disclosed, Affecting iOS 18.4-18.7](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

The DarkSword exploit chain, active since November 2025, was disclosed, affecting iOS 18.4 to 18.7 and allowing infection via malicious web pages in Safari. The chain combines six vulnerabilities, including CVE-2025-43529, to deploy payloads like GHOSTBLADE, with patches available in later iOS versions. This is significant because DarkSword was used in targeted attacks across Saudi Arabia, Turkey, Malaysia, and Ukraine, demonstrating a high-risk exploit chain capable of remote code execution. The disclosure highlights ongoing security challenges in iOS, especially for users delaying updates. The exploit chain includes 3 zero-day vulnerabilities and is primarily written in JavaScript, enabling easy deployment. Patches were rolled out incrementally, with CVE-2025-43529 fixed in iOS 18.7.3 and later versions.

telegram · zaihuapd · Mar 24, 11:45

**Background**: DarkSword is a full-chain iOS exploit kit leveraging WebKit vulnerabilities in Safari. WebKit is the browser engine powering Safari and all web content handling in Apple's ecosystem. GHOSTBLADE is a crypto-stealing malware recently flagged by Google Threat Intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword: iOS Exploit Chain Adopted by ...</a></li>
<li><a href="https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html">DarkSword iOS Exploit Kit Uses 6 Flaws, 3 Zero-Days for Full ...</a></li>
<li><a href="https://www.linkedin.com/posts/cointelegraph_google-threat-intel-flags-ghostblade-crypto-stealing-activity-7441660499534131200-Gpmh">Google Threat Intel flags ' Ghostblade ' crypto-stealing malware</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#ios`, `#vulnerability`, `#safari`, `#zero-day`

---

<a id="item-7"></a>
## [Google launches Gemini dark web intelligence AI agent in preview](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

Google has launched a preview of Gemini, an AI-powered dark web intelligence agent integrated with Google Threat Intelligence. The system analyzes 8-10 million dark web posts daily to identify risks like initial access broker activities, data leaks, and insider threats with 98% accuracy in internal tests. This addresses critical cybersecurity needs by automating dark web monitoring at scale, helping organizations proactively detect threats before they escalate. The integration with Google's threat intelligence ecosystem makes enterprise security teams more efficient against evolving cybercrime tactics. Gemini autonomously builds organizational profiles and adjusts them dynamically based on business operations. It specifically targets initial access brokers who sell network access to ransomware groups, a growing segment of cybercrime-as-a-service.

telegram · zaihuapd · Mar 24, 13:15

**Background**: The dark web hosts illicit marketplaces where cybercriminals trade stolen data and network access. Initial access brokers (IABs) specialize in compromising systems and selling access to ransomware operators. Google Threat Intelligence combines Mandiant's frontline expertise with Google's visibility across billions of devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://cloud.google.com/blog/products/identity-security/bringing-dark-web-intelligence-into-the-ai-era">Bringing dark web intelligence into the AI era | Google Cloud Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Initial_access_broker">Initial access broker - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Cybersecurity`, `#Dark Web`, `#Google`, `#Threat Intelligence`

---

<a id="item-8"></a>
## [OpenAI to discontinue Sora, shut API, end Disney deal](https://www.bloomberg.com/news/articles/2026-03-24/openai-plans-to-discontinue-support-for-sora-ai-video-generator?srnd=phx-technology) ⭐️ 8.0/10

OpenAI plans to discontinue its AI video generator Sora just six months after launch, shutting down its standalone app and developer API, while also winding down its partnership with Disney. This marks a significant strategic shift for OpenAI as it reallocates resources toward AI agents and a new model called Spud, signaling a move away from consumer-facing video generation products. The discontinuation comes alongside organizational changes to integrate safety teams more closely with development processes, suggesting a refocus on core model development rather than application layers.

telegram · zaihuapd · Mar 25, 00:30

**Background**: Sora was OpenAI's text-to-video generation model that could create short video clips from prompts and extend existing videos. The model gained attention for its ability to generate high-quality, imaginative video content from textual descriptions. OpenAI's new focus appears to be on Spud, a next-generation AI model currently in development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sora_(text-to-video_model)">Sora (text-to- video model) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI`, `#VideoGeneration`, `#APIs`, `#BusinessStrategy`

---

<a id="item-9"></a>
## [OpenAI Shuts Down Sora Video App](https://twitter.com/soraofficialapp/status/2036532795984715896) ⭐️ 7.0/10

OpenAI announced the shutdown of its AI video generation app Sora, just six months after its high-profile launch. The decision comes despite Sora's initial buzz for its ability to quickly produce AI-generated videos. This move signals OpenAI's strategic pivot away from consumer-facing AI video tools, potentially towards more lucrative automation opportunities. It also raises questions about product-market fit for standalone AI creativity apps in an ecosystem dominated by multipurpose platforms. The shutdown follows closely after OpenAI published safety guidelines for Sora, suggesting either abrupt decision-making or internal misalignment. Disney also terminated a $1 billion investment deal tied to Sora's development.

hackernews · mikeocool · Mar 24, 20:01

**Background**: Sora was OpenAI's standalone video generation app launched in 2024, capable of creating short AI-generated videos from text prompts. It competed in a crowded space of AI creativity tools, where many apps struggle to maintain user engagement beyond initial novelty.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/03/24/technology/openai-shutting-down-sora.html">OpenAI Is Shutting Down Sora, Its A.I. Video Generator OpenAI shutting down Sora video-creation app - NBC News That Was Fast. OpenAI to Shut Down Sora Video Generator App OpenAI is shutting down its Sora video generation app - Engadget Sora App Shut Down by OpenAI, Disney Deal Dead - IGN OpenAI Discontinues Sora App, Shuts Down Video Generation ... OpenAI to Shut Down Sora App - The Wrap</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/openai-shuttering-sora-video-generating-service-rcna264989">OpenAI shutting down Sora video-creation app - NBC News</a></li>
<li><a href="https://www.pcmag.com/news/that-was-fast-openai-to-shut-down-sora-video-generator-app">That Was Fast. OpenAI to Shut Down Sora Video Generator App</a></li>

</ul>
</details>

**Discussion**: Comments reveal mixed reactions: some users mourned the loss of creative possibilities, while others criticized Sora's fundamental product design as unsustainable. Several noted OpenAI's broader strategic shifts, including focus on developer tools and political lobbying.

**Tags**: `#AI`, `#OpenAI`, `#video-generation`, `#product-market-fit`, `#tech-news`

---

<a id="item-10"></a>
## [Claude Code Introduces Auto Mode with Safeguards](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code has launched auto mode, a new permissions mode where the AI makes decisions on behalf of users while employing safeguards that monitor actions before execution. These safeguards are implemented using Claude Sonnet 4.6 as a classifier model to review conversations and block inappropriate actions. This development provides a safer alternative to the '--dangerously-skip-permissions' flag, balancing automation with security in AI-assisted coding. It could significantly streamline developer workflows while reducing risks associated with unchecked AI actions in sensitive environments. The auto mode includes extensive default filters covering operations like local file management, Git commands, and package installations, with special attention to security risks. Users can also customize these rules, and the system maintains strict boundaries against scope escalation and irreversible destructive actions.

rss · Simon Willison · Mar 24, 23:57

**Background**: Claude is a series of large language models developed by Anthropic, using constitutional AI for improved ethical compliance. Claude Code is its application for software development, where permission modes control what actions the AI can perform. The '--dangerously-skip-permissions' flag previously allowed bypassing all safety checks, creating potential security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://code.claude.com/docs/en/permissions">Configure permissions - Claude Code Docs</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#code-assistance`, `#permissions`, `#automation`

---

<a id="item-11"></a>
## [Package Managers Adopt Dependency Cooldowns to Combat Supply Chain Attacks](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

Major package managers including pnpm, Yarn, Bun, Deno, uv, pip, and npm have recently implemented dependency cooldown features, which delay installing new package versions for a set period to allow security vetting. This trend was inspired by the March 2026 LiteLLM supply chain attack and builds on William Woodruff's 2025 proposal for dependency cooldowns. Dependency cooldowns provide a critical defense against supply chain attacks by creating a buffer period for the community to detect compromised packages before widespread adoption. With over 75% of modern applications relying on open-source dependencies, this practice could significantly reduce the impact of malicious package updates. Implementation details vary: pnpm and Bun use 'minimumReleaseAge', Yarn has 'npmMinimalAgeGate', Deno implements '--minimum-dependency-age', while pip currently only supports absolute timestamps with '--uploaded-prior-to'. Most tools allow exceptions for trusted packages through whitelisting mechanisms.

rss · Simon Willison · Mar 24, 21:11

**Background**: Supply chain attacks target software dependencies to infiltrate downstream systems, with attackers often publishing malicious updates to legitimate packages. Dependency cooldowns mitigate this by enforcing a waiting period (typically 24-72 hours) before new versions can be installed, allowing security tools and maintainers to detect anomalies.

<details><summary>References</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://pnpm.io/blog/releases/10.16">pnpm 10.16 | pnpm</a></li>
<li><a href="https://cybercyte.com/blog/software-supply-chain-attacks/">Software Supply Chain Attacks : How Malicious Libraries... - Cybercyte</a></li>

</ul>
</details>

**Tags**: `#package-management`, `#security`, `#supply-chain`, `#devops`

---

<a id="item-12"></a>
## [China's daily AI token usage surges over 1,000x, hits 140 trillion in March 2025](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

China's National Data Administration revealed that daily AI token usage exceeded 140 trillion in March 2025, marking a 1,000-fold increase from 100 billion in early 2024 to 100 trillion by end of 2025. This explosive growth signals rapid AI commercialization in China, with tokens becoming measurable, tradable units that form a new value system for AI services and data transactions. Tokens serve as the smallest processing units in large language models, with their pricing and settlement mechanisms enabling precise measurement of computing/data usage in AI services.

telegram · zaihuapd · Mar 24, 07:22

**Background**: Tokenization breaks text into smaller units for AI processing, with different methods impacting model performance. China's data element marketization reform has accelerated high-quality data supply chains, facilitating token-based AI commercialization. The surge also reflects China's competitive position in global AI token consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2403.00417">Rethinking Tokenization: Crafting Better Tokenizers for Large ...</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202603/24/WS69c21887a310d6866eb3f91f.html">Daily token surge heralds rapid commercialization of China's AI</a></li>
<li><a href="https://www.globaltimes.cn/page/202603/1357467.shtml">Chinese tokens going global - Global Times</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tokenization`, `#China-Tech`, `#Data-Economy`, `#Commercialization`

---

<a id="item-13"></a>
## [EU's age verification app may block non-Google Android systems](https://t.me/zaihuapd/40484) ⭐️ 7.0/10

The EU is developing an open-source age verification app that requires devices to pass Google's Play Integrity verification and be downloaded from the Play Store with a Google account, effectively blocking non-Google-authorized Android systems like GrapheneOS. This move raises concerns about digital sovereignty and deepens reliance on US tech giants, potentially limiting user choice and undermining open-source Android alternatives that prioritize privacy and security. The app will use Google's Play Integrity API (formerly SafetyNet) to verify device authenticity, which critics argue contradicts the EU's open-source and interoperability principles while creating barriers for privacy-focused Android forks.

telegram · zaihuapd · Mar 24, 12:22

**Background**: Play Integrity API is Google's security system that verifies app authenticity and device integrity. GrapheneOS is a privacy-focused Android fork that removes Google services, used by security-conscious users who avoid dependence on Google's ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Play_Integrity_API">Play Integrity API - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**Discussion**: Developers and privacy advocates on GitHub are opposing the requirement, arguing it contradicts digital sovereignty goals and creates unfair barriers for alternative Android implementations that don't rely on Google services.

**Tags**: `#EU policy`, `#Android`, `#digital sovereignty`, `#privacy`, `#open-source`

---

<a id="item-14"></a>
## [Microsoft releases 7 Rust training books covering beginner to expert topics](https://github.com/microsoft/RustTraining) ⭐️ 7.0/10

Microsoft has published a RustTraining repository on GitHub containing 7 Rust training books, covering topics from transitioning from other languages to advanced concepts like async programming, type-driven correctness, and engineering practices. This release is significant as it provides structured, official training materials from Microsoft for Rust, a language gaining popularity for its memory safety and performance, which will help accelerate adoption among developers. Each book contains 15-16 chapters with Mermaid diagrams, editable Rust Playgrounds, exercises, and full-text search. The materials are dual-licensed under MIT and CC-BY-4.0 and available as Markdown files or rendered via GitHub Pages.

telegram · zaihuapd · Mar 24, 23:57

**Background**: Rust is a systems programming language known for its memory safety guarantees without garbage collection. Async programming in Rust allows concurrent execution without OS involvement, managed by async runtimes. Type-driven correctness leverages Rust's strong type system to enforce correctness at compile time.

<details><summary>References</summary>
<ul>
<li><a href="https://rust-lang.github.io/async-book/">Introduction - Asynchronous Programming in Rust</a></li>
<li><a href="https://github.com/microsoft/RustTraining/blob/main/type-driven-correctness-book/src/SUMMARY.md">microsoft/RustTraining - type-driven-correctness-book - GitHub</a></li>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Microsoft`, `#Programming`, `#Education`, `#Open-Source`

---

<a id="item-15"></a>
## [Claude Code Launches Auto Mode with Built-in Safety Checks](https://claude.com/blog/auto-mode) ⭐️ 7.0/10

Claude Code has introduced Auto Mode, allowing AI to make autonomous decisions during task execution while implementing safety checks to prevent high-risk actions like mass file deletions or sensitive data leaks. The feature is currently available in research preview for Team plan users, with Enterprise and API support coming soon for Claude Sonnet 4.6 and Opus 4.6 models. This represents a significant step in balancing AI autonomy with security, reducing developer interruptions while maintaining safeguards against destructive commands. The feature addresses a critical pain point in AI-assisted development workflows where excessive permission prompts can hinder productivity. Developers can enable Auto Mode via command line (`claude --enable-auto-mode`) or through settings in Desktop/VS Code. While safer than the `--dangerously-skip-permissions` option, Anthropic warns it's not risk-free and recommends use in isolated environments, noting potential slight increases in token consumption and latency.

telegram · zaihuapd · Mar 25, 01:15

**Background**: Claude Sonnet 4.6 and Opus 4.6 are Anthropic's latest AI models with enhanced capabilities in coding, long-context reasoning, and agent planning. Auto Mode represents a middle ground between fully manual permission approval and completely skipping safety checks, using classifiers to evaluate tool usage in real-time.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zdnet.com/article/claude-code-auto-mode/">How Claude Code's new auto mode prevents AI coding ... - ZDNET</a></li>
<li><a href="https://www.anthropic.com/news/claude-sonnet-4-6">Introducing Claude Sonnet 4.6 - Anthropic</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-6">Introducing Claude Opus 4.6 - Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Automation`, `#Security`, `#Claude`, `#Developer Tools`

---