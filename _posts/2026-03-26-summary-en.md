---
layout: default
title: "Horizon Summary: 2026-03-26 (EN)"
date: 2026-03-26
lang: en
---

> From 42 items, 22 important content pieces were selected

---

1. [LiteLLM v1.82.8 PyPI package compromised with credential-stealing malware](#item-1) ⭐️ 9.0/10
2. [Swift 6.3 Released with Official Android Support](#item-2) ⭐️ 9.0/10
3. [Running Tesla Model 3's computer on a desk using salvaged parts](#item-3) ⭐️ 8.0/10
4. [ARC-AGI-3 Benchmark Sparks AGI Measurement Debate](#item-4) ⭐️ 8.0/10
5. [EU pushes for mass surveillance of private messages](#item-5) ⭐️ 8.0/10
6. [LiteLLM PyPI Hack Affected 47,000 Downloads](#item-6) ⭐️ 8.0/10
7. [Streaming expert weights enable trillion-parameter models on consumer devices](#item-7) ⭐️ 8.0/10
8. [Arm to sell its own AI chips for the first time, with Meta as first major customer and TSMC as manufacturer](#item-8) ⭐️ 8.0/10
9. [NASA shifts focus from lunar orbit station to Moon base by 2029](#item-9) ⭐️ 8.0/10
10. [Google Research introduces TurboQuant, compressing LLM KV cache to 3 bits](#item-10) ⭐️ 8.0/10
11. [Apifox Desktop Client Hit by Supply Chain Attack via CDN Script Injection](#item-11) ⭐️ 8.0/10
12. [Apple and Google partner to integrate Gemini AI into Siri](#item-12) ⭐️ 8.0/10
13. [Supreme Court Rules ISPs Not Liable for User Copyright Infringement](#item-13) ⭐️ 7.0/10
14. [Critique of AI-driven coding speed and quality trade-offs](#item-14) ⭐️ 7.0/10
15. [Claude Code Introduces Auto Mode with Safeguards](#item-15) ⭐️ 7.0/10
16. [Package Managers Adopt Dependency Cooldown Mechanisms](#item-16) ⭐️ 7.0/10
17. [Claude Code Launches Auto Mode: AI Autonomous Decision-Making with Built-In Safety Reviews](#item-17) ⭐️ 7.0/10
18. [Tencent disbands AI Lab, hires ByteDance Seed leads to boost Hunyuan](#item-18) ⭐️ 7.0/10
19. [Pinduoduo announces 'New Pinmu' with 100B RMB investment for brand self-operation](#item-19) ⭐️ 7.0/10
20. [CCF opposes NeurIPS' ban on submissions from US-sanctioned institutions, calls for boycott](#item-20) ⭐️ 7.0/10
21. [Intel and AMD warn Chinese clients of extended server CPU delivery times](#item-21) ⭐️ 7.0/10
22. [GitHub updates Copilot data policy: Free and paid individual users now included in AI training by default, with opt-out option](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM v1.82.8 PyPI package compromised with credential-stealing malware](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

The LiteLLM v1.82.8 package on PyPI was found to contain a malicious litellm_init.pth file that automatically executes a credential-stealing script upon installation, without requiring the package to be imported. The attack originated from compromised PyPI credentials likely stolen through an earlier exploit of the Trivy security scanner. This is a critical supply chain attack affecting a widely-used Python package, with potential to steal sensitive credentials including SSH keys, cloud service credentials, and cryptocurrency wallets. The automatic execution upon installation makes it particularly dangerous as users don't need to actively use the package to be compromised. The malware uses multi-layer base64 obfuscation and targets over 25 types of credential files across various systems. PyPI quickly quarantined the package, limiting the exposure window to just a few hours. Version 1.82.7 had a similar exploit but required package import to activate.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is a popular Python library for interacting with large language models. .pth files are special Python path configuration files that execute when Python starts. PyPI is Python's official third-party package repository, making it a prime target for supply chain attacks. The attack appears linked to a recent compromise of Trivy, a security scanner used by LiteLLM's CI pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 — credential stealer · Issue #24512 · BerriAI/litellm</a></li>
<li><a href="https://www.stepsecurity.io/blog/litellm-credential-stealer-hidden-in-pypi-wheel">litellm: Credential Stealer Hidden in PyPI Wheel - StepSecurity</a></li>
<li><a href="https://www.ox.security/blog/litellm-malware-malicious-pypi-versions-steal-cloud-and-crypto-credentials/">Malicious LiteLLM Packages Steal AWS & Crypto Keys</a></li>

</ul>
</details>

**Discussion**: The GitHub issue threads reveal deep concern among developers about the sophistication of the attack and the broad range of credentials targeted. Many are calling for improved security measures in PyPI's publishing process and better monitoring of package changes.

**Tags**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#malware`

---

<a id="item-2"></a>
## [Swift 6.3 Released with Official Android Support](https://swift.org/blog/swift-6.3-released/) ⭐️ 9.0/10

Swift 6.3, released on March 25, 2026, introduces the official Swift SDK for Android, enabling developers to write native Android apps or integrate Swift code with existing Kotlin/Java applications using the Swift Java plugin. This marks a major cross-platform breakthrough, allowing mobile development teams to use Swift for both iOS and Android apps, reducing the need for separate codebases and streamlining the development process. The Swift Java plugin simplifies writing JNI code and calling Java from Swift, while the Swift SDK for Android is part of the official Swift.org project, supported by Apple's open-source team.

telegram · zaihuapd · Mar 25, 03:45

**Background**: Swift is a programming language developed by Apple for iOS, macOS, and other Apple platforms. Until now, Android apps typically required Kotlin or Java, while iOS apps used Swift, leading to separate codebases for cross-platform development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/tomholmes96_announcing-the-swift-sdk-for-android-activity-7388557917077008384-9DEO">Announcing the Swift SDK for Android | Tom Holmes</a></li>
<li><a href="https://levelup.gitconnected.com/swift-on-android-how-the-new-swift-sdk-unlocks-real-cross-platform-mobile-development-0b4b79d476aa">Swift on Android : How the New Swift SDK Unlocks... | Level Up Coding</a></li>
<li><a href="https://github.com/swiftlang/swift-java">GitHub - swiftlang/swift-java: Java interopability support ...</a></li>

</ul>
</details>

**Tags**: `#Swift`, `#Android`, `#Cross-platform`, `#Mobile Development`, `#Programming Languages`

---

<a id="item-3"></a>
## [Running Tesla Model 3's computer on a desk using salvaged parts](https://bugs.xdavidhu.me/tesla/2026/03/23/running-tesla-model-3s-computer-on-my-desk-using-parts-from-crashed-cars/) ⭐️ 8.0/10

A hacker successfully ran a Tesla Model 3's computer on a desk using parts from crashed cars, including insights into Tesla's root access program that grants permanent SSH certificates to qualifying security researchers. This demonstrates the growing accessibility of automotive computing systems for research and highlights Tesla's unique approach to security research through its root access bounty program, which could accelerate vulnerability discoveries. The project revealed Tesla vehicles use bundled cable 'looms' rather than individual wires, and the root access program requires researchers to first find a valid rooting vulnerability to qualify for permanent SSH access to their own vehicle.

hackernews · driesdep · Mar 25, 21:11

**Background**: Tesla's Full Self-Driving (FSD) Computer (Hardware 3) uses custom AI chips developed in-house since 2019, replacing previous NVIDIA hardware. The system powers all autonomous features through neural networks processing camera, radar and sensor data. Tesla's root access program resembles Apple's Security Research Device Program but with vehicle-specific qualifications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Model_3">Tesla Model 3 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Autopilot_hardware">Tesla Autopilot hardware - Wikipedia</a></li>
<li><a href="https://www.autopilotreview.com/tesla-custom-ai-chips-hardware-3/">Tesla Hardware 3 (Full Self-Driving Computer) Detailed - AutoPilot Review</a></li>
<li><a href="https://hackaday.com/2024/01/05/getting-root-access-on-a-telsa/">Getting Root Access On A Tesla | Hackaday</a></li>

</ul>
</details>

**Discussion**: Comments reveal surprise at the cable loom discovery, comparisons to automotive development benches, and discussions about Tesla's root access program being similar to Apple's security research initiative. Some noted the irony of LVDS cables being called 'automotive' when commonly used in laptops.

**Tags**: `#hardware-hacking`, `#automotive`, `#reverse-engineering`, `#tesla`, `#security`

---

<a id="item-4"></a>
## [ARC-AGI-3 Benchmark Sparks AGI Measurement Debate](https://arcprize.org/arc-agi/3) ⭐️ 8.0/10

The ARC-AGI-3 technical report introduces a new interactive reasoning benchmark with 1,000+ levels across 150+ environments, comparing AI performance against human puzzle-solving abilities. It uses a unique scoring system where the human baseline is defined as the second-best first-run human by action count. This represents one of the most ambitious attempts to create a standardized AGI measurement framework, potentially reshaping how we evaluate progress toward human-level AI. The methodology has sparked important discussions about what truly constitutes artificial general intelligence. The benchmark focuses on agentic intelligence requiring exploration, learning, planning and adaptation across diverse environments. Critics note the human comparison methodology may be problematic as it doesn't use average human performance.

hackernews · lairv · Mar 25, 18:16

**Background**: ARC (Alignment Research Center) is a non-profit focused on AI safety and alignment research. AGI (Artificial General Intelligence) refers to AI systems that can perform any intellectual task a human can. Benchmarking AGI progress remains controversial as there's no consensus on proper measurement methodologies.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3/">ARC-AGI-3</a></li>
<li><a href="https://www.lumenova.ai/blog/artificial-general-intelligence-measuring-agi/">The Path to AGI : How Do We Know When We’re There? | Lumenova AI</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-general-intelligence">What is Artificial General Intelligence ( AGI )? | IBM</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with some praising the benchmark's rigor while others criticize its human comparison methodology. Notable debates include whether specialized AI performance should be compared to human general intelligence, with analogies to airplanes vs. birds frequently mentioned.

**Tags**: `#AGI`, `#AI-benchmarking`, `#human-comparison`, `#research-methodology`, `#cognitive-tasks`

---

<a id="item-5"></a>
## [EU pushes for mass surveillance of private messages](https://fightchatcontrol.eu/?foo=bar) ⭐️ 8.0/10

The EU is attempting to extend its 'Chat Control 1.0' regulation that allows voluntary scanning of private communications, despite Parliament's March 11 vote to replace mass surveillance with targeted monitoring of suspects. This represents a significant threat to digital privacy rights across Europe, potentially normalizing mass surveillance under the guise of security, with implications for all EU citizens' fundamental rights. The proposed extension would continue Regulation (EU) 2021/1232, which has allowed voluntary scanning since 2021. The measure faces opposition due to human rights concerns and lack of evidence for effectiveness.

hackernews · MrBruh · Mar 25, 20:27

**Background**: The EU has been grappling with balancing security and privacy since the migration crisis and terrorist attacks. 'Chat Control' measures emerged from concerns about online child exploitation but have expanded to broader surveillance. The EU previously adopted digital rights principles promoting human-centric approaches, making this surveillance push particularly controversial.

<details><summary>References</summary>
<ul>
<li><a href="https://repository.gchumanrights.org/items/515f3276-e4b2-4398-9c6c-904f17e95b33">From sleepwalking into surveillance societies to drifting into...</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-principles">European Digital Rights and Principles - Shaping Europe’s ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0267364923000560">The transformative nature of the EU Declaration on Digital ...</a></li>

</ul>
</details>

**Discussion**: Comments reveal strong opposition, with creators of Fight Chat Control calling the situation 'dumbfounding'. Some suggest drafting counter-legislation to protect private communications, while others criticize the EU's increasing control. One user notes Hungary's support as a negative indicator for the proposal.

**Tags**: `#privacy`, `#EU`, `#surveillance`, `#digital-rights`, `#policy`

---

<a id="item-6"></a>
## [LiteLLM PyPI Hack Affected 47,000 Downloads](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything) ⭐️ 8.0/10

Analysis revealed 46,996 downloads of compromised LiteLLM PyPI packages (versions 1.82.7 and 1.82.8) during a 46-minute window, with 88% of dependent packages failing to securely pin versions. This incident highlights critical vulnerabilities in Python's software supply chain, particularly around dependency management, affecting thousands of AI applications that rely on LiteLLM for LLM interactions. The attack occurred when threat actors obtained maintainer credentials via a compromised Trivy security scanner in LiteLLM's CI/CD pipeline, publishing malicious versions that delivered credential stealers.

rss · Simon Willison · Mar 25, 17:21

**Background**: LiteLLM is a popular Python package providing a unified interface for interacting with multiple LLM providers (OpenAI, Anthropic, Google). PyPI is Python's official third-party software repository. Version pinning ensures dependencies use specific, vetted package versions to prevent unexpected updates.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/litellm/">litellm · PyPI</a></li>
<li><a href="https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/">How a Poisoned Security Scanner Became the Key to Backdooring LiteLLM | Snyk</a></li>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential Stealer</a></li>

</ul>
</details>

**Tags**: `#security`, `#pypi`, `#supply-chain`, `#python`, `#packaging`

---

<a id="item-7"></a>
## [Streaming expert weights enable trillion-parameter models on consumer devices](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Researchers demonstrated running trillion-parameter Mixture-of-Experts models like Qwen3.5-397B-A17B and Kimi K2.5 on consumer hardware including MacBooks and iPhones by streaming expert weights from SSD instead of loading full models into RAM. The Kimi K2.5 model with 1 trillion parameters and 32B active weights was successfully run on a 96GB M2 Max MacBook Pro, while Qwen3.5-397B-A17B achieved 0.6 tokens/sec on an iPhone. This breakthrough dramatically lowers the hardware barrier for running state-of-the-art AI models, enabling advanced AI capabilities on personal devices without requiring expensive cloud infrastructure or specialized hardware. It represents a significant step toward democratizing access to cutting-edge AI technology. The technique achieves this by only loading the necessary expert weights for each token from SSD, significantly reducing memory requirements. Performance varies by device, with the iPhone implementation currently limited to 0.6 tokens/sec, while an M4 Max MacBook achieved ~1.7 tokens/sec with Kimi K2.5.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) models are a type of neural network that uses specialized sub-networks (experts) for different inputs, activating only a fraction of the total parameters for each token. This makes them more efficient than dense models at scale. Qwen3.5-397B-A17B is a 397 billion parameter MoE model from Alibaba with 17B active parameters, while Kimi K2.5 is a newer 1 trillion parameter model.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Mar/24/streaming-experts/">Streaming experts | Simon Willison’s Weblog</a></li>
<li><a href="https://www.linkedin.com/pulse/mixture-of-experts-moe-models-scalable-path-smarter-ai-vinay-saini-6p7fc?tl=en">Mixture - of - Experts (MoE) Models : The Scalable Path for Smarter AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is actively experimenting with this technique, with multiple researchers reporting successful implementations on different hardware configurations. There's particular excitement about the potential for further optimizations through ongoing 'autoresearch loops' to improve performance.

**Tags**: `#AI`, `#Mixture-of-Experts`, `#LLM`, `#Hardware`, `#Optimization`

---

<a id="item-8"></a>
## [Arm to sell its own AI chips for the first time, with Meta as first major customer and TSMC as manufacturer](https://www.bloomberg.com/news/articles/2026-03-24/arm-to-sell-its-own-chips-for-first-time-in-bid-for-ai-revenue) ⭐️ 8.0/10

Arm Holdings announced it will begin selling its own AI-focused 'AGI CPU' chips for the first time, with Meta as the first major customer. The 136-core, 300W chips will be manufactured by TSMC and designed to work alongside accelerator chips from companies like Nvidia. This marks Arm's entry into the competitive AI chip market, potentially disrupting traditional CPU makers like Intel and AMD. The move could reshape AI hardware ecosystems as major tech firms like Meta, OpenAI and SK Telecom adopt these chips for their infrastructure. The AGI CPU claims superior energy efficiency compared to traditional designs, with systems already available from Quanta and Supermicro. Arm expects to scale production in second half of 2026.

telegram · zaihuapd · Mar 25, 02:45

**Background**: Arm is best known for designing chip architectures licensed by companies like Apple and Qualcomm, but has not previously sold its own chips. The AGI CPU is specifically optimized for AI workloads in data centers, representing Arm's push into the lucrative AI hardware market dominated by Nvidia.

<details><summary>References</summary>
<ul>
<li><a href="https://newsroom.arm.com/blog/introducing-arm-agi-cpu">Announcing Arm AGI CPU: The silicon foundation for the agentic AI cloud era - Arm Newsroom</a></li>
<li><a href="https://www.arm.com/products/cloud-datacenter/arm-agi-cpu">Arm AGI CPU</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#AI-hardware`, `#Arm`, `#Meta`, `#TSMC`

---

<a id="item-9"></a>
## [NASA shifts focus from lunar orbit station to Moon base by 2029](https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/) ⭐️ 8.0/10

NASA announced it will pause development of the Gateway lunar orbit station and instead prioritize establishing a permanent Moon base by 2029, with plans for annual lunar landings and accelerated nuclear-powered Mars missions. This strategic shift represents a major acceleration in lunar surface operations and commercialization of space exploration, while advancing nuclear propulsion technology crucial for future Mars missions. After Artemis V, NASA plans to introduce more commercial procurement and reusable hardware, aiming for crewed lunar missions every 6 months. The Space Reactor-1 Freedom nuclear-powered Mars mission is scheduled for 2028.

telegram · zaihuapd · Mar 25, 04:30

**Background**: The Gateway program was originally planned as a lunar orbit station to support Artemis missions. Artemis V was initially conceived as a mission to install Gateway elements before lunar landing. Nuclear propulsion in space has been limited to radioisotope systems previously, with no operational fission reactors used for propulsion beyond Earth orbit.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbeta.com.tw/articles/science/1444756.htm">NASA正测试其" Gateway ..." - cnBeta.COM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artemis_V">Artemis V</a></li>
<li><a href="https://www.space.com/astronomy/mars/nasas-1st-nuclear-powered-interplanetary-spacecraft-will-send-skyfall-helicopters-to-mars-in-2028">NASA's '1st nuclear powered interplanetary spacecraft' will ...</a></li>

</ul>
</details>

**Tags**: `#NASA`, `#space-exploration`, `#moon-base`, `#Mars-mission`, `#nuclear-propulsion`

---

<a id="item-10"></a>
## [Google Research introduces TurboQuant, compressing LLM KV cache to 3 bits](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) ⭐️ 8.0/10

Google Research has introduced TurboQuant, a vector quantization algorithm that compresses the key-value (KV) cache in large language models (LLMs) down to 3 bits without requiring retraining or fine-tuning. The method achieves a 6x reduction in memory usage and an 8x speedup in attention logits computation on H100 GPUs while maintaining accuracy. This breakthrough significantly reduces the memory bottleneck in LLM inference, enabling more efficient deployment of large models with long-context capabilities. The 3-bit compression with zero accuracy loss represents a major advancement in AI efficiency, potentially lowering costs and energy consumption for AI services. TurboQuant will be presented at ICLR 2026, while companion methods QJL and PolarQuant will debut at AISTATS 2026. The 4-bit version shows superior recall in high-dimensional vector search tasks compared to PQ and RabbiQ methods.

telegram · zaihuapd · Mar 25, 05:15

**Background**: KV cache is a critical optimization technique in Transformer-based LLMs that stores previously computed attention keys and values to avoid redundant computations during text generation. Vector quantization is a method to reduce memory usage by representing high-dimensional vectors with fewer bits, though traditional approaches often sacrifice accuracy or require additional overhead bits.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>
<li><a href="https://arxiv.org/pdf/2603.20397">KV Cache Optimization Strategies for Scalable and Efficient ...</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#Quantization`, `#Efficiency`, `#Google-Research`

---

<a id="item-11"></a>
## [Apifox Desktop Client Hit by Supply Chain Attack via CDN Script Injection](http://apifox.it.xn--comcdn-kr3e.openroute.xn--devupgrade-eh3i.feishu.it.com/) ⭐️ 8.0/10

Apifox's desktop client was compromised in a supply chain attack where attackers modified its CDN-hosted analytics script to inject malicious code that steals SSH keys, Git credentials, shell history, and process lists. The attack has been active since March 4, affecting Windows, macOS, and Linux users. This incident highlights critical risks in software supply chains, as a widely-used API development tool (positioned as a Postman/Swagger alternative) was compromised to harvest developer credentials that could lead to infrastructure breaches. The theft of SSH keys and Git credentials poses severe risks to organizations' code integrity and system access. Security researcher phith0n reverse-engineered the malware, which communicates with malicious domains (apifox.it.com, cdn.openroute.dev). Mitigation involves checking Network Persistent State files for these domains and blocking them via firewall/DNS. The official client no longer contacts the malicious domain in its latest version.

telegram · zaihuapd · Mar 25, 11:10

**Background**: Apifox is an all-in-one API collaboration platform combining Postman-like debugging with Swagger documentation and JMeter testing. Supply chain attacks via CDNs have surged recently, as seen in the Polyfill.io incident, where attackers compromise third-party dependencies to inject malware into widely-distributed software.

<details><summary>References</summary>
<ul>
<li><a href="https://huntscreens.com/en/products/apifox">Apifox: All-in-One API Platform for Enhanced Collaboration ...</a></li>
<li><a href="https://dev.to/snyk/polyfill-supply-chain-attack-embeds-malware-in-javascript-cdn-assets-55d6">Polyfill supply chain attack embeds malware in JavaScript CDN ...</a></li>
<li><a href="https://byteiota.com/trivy-compromised-twice-github-actions-attack-hits-again/">Trivy Compromised Twice: GitHub Actions Attack Hits Again</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain-attack`, `#apifox`, `#malware`, `#devops`

---

<a id="item-12"></a>
## [Apple and Google partner to integrate Gemini AI into Siri](https://t.me/zaihuapd/40506) ⭐️ 8.0/10

Apple and Google announced a multi-year partnership where Google's Gemini AI models will power the next generation of Apple Foundation Models, enhancing Siri's capabilities while maintaining on-device and private cloud processing for privacy. This partnership could significantly improve Siri's intelligence and capabilities while maintaining Apple's privacy standards, potentially reshaping the AI assistant landscape by combining Apple's hardware ecosystem with Google's advanced AI models. The integration will use Gemini models running on-device and through private cloud computing, with Apple emphasizing continued adherence to its privacy standards. The enhanced Siri features are expected to launch later this year.

telegram · zaihuapd · Mar 25, 16:32

**Background**: Gemini is Google's family of multimodal large language models, successor to LaMDA and PaLM 2, comprising several versions like Gemini Pro and Gemini Flash. Apple Foundation Models are Apple's on-device AI framework that powers features like Apple Intelligence, trained using Apple's AXLearn framework.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(AI_model)">Gemini (AI model)</a></li>
<li><a href="https://machinelearning.apple.com/research/introducing-apple-foundation-models">Introducing Apple ’s On-Device and Server Foundation Models</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Apple`, `#Google`, `#Siri`, `#Gemini`

---

<a id="item-13"></a>
## [Supreme Court Rules ISPs Not Liable for User Copyright Infringement](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html) ⭐️ 7.0/10

The US Supreme Court ruled in favor of Cox Communications in a copyright infringement case, determining that internet service providers (ISPs) are not liable for pirated content shared by their users unless they actively encourage infringement. This decision sets an important precedent limiting ISP liability under copyright law, potentially reducing incentives for ISPs to monitor user activity and impacting future copyright enforcement strategies. The Court cited the 1984 'Betamax case' precedent, emphasizing that liability requires proof of intent to facilitate infringement. The ruling maintains DMCA safe harbor protections while clarifying their limits.

hackernews · oj2828 · Mar 25, 15:02

**Background**: The Digital Millennium Copyright Act (DMCA) provides 'safe harbor' protections that shield online service providers from liability for user-generated content if they follow specific procedures like responding to takedown notices. This case tested the boundaries of those protections, with music labels arguing Cox benefited financially from infringing users.

<details><summary>References</summary>
<ul>
<li><a href="https://cyber.harvard.edu/property/liability/ispliab.html">ISP Liability for Copyright Infringement</a></li>
<li><a href="https://copyrightalliance.org/education/copyright-law-explained/the-digital-millennium-copyright-act-dmca/dmca-safe-harbor/">DMCA Safe Harbor | Copyright Alliance</a></li>
<li><a href="https://www.congress.gov/crs_external_products/IF/PDF/IF11478/IF11478.1.pdf">Digital Millennium Copyright Act (DMCA) Safe Harbor ...</a></li>

</ul>
</details>

**Discussion**: Comments show mixed reactions, with some celebrating reduced ISP surveillance while others criticize copyright duration. One user drew analogies to manufacturer liability for product misuse, sparking debate about intent standards.

**Tags**: `#copyright`, `#legal`, `#isp`, `#privacy`, `#supreme-court`

---

<a id="item-14"></a>
## [Critique of AI-driven coding speed and quality trade-offs](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Mario Zechner, creator of the Pi agent framework, critiques the unchecked speed of AI-driven code generation, warning that it leads to unsustainable complexity accumulation without proper human oversight. This highlights a critical tension in modern software development where AI acceleration risks creating unmanageable 'cognitive debt' and systems that outpace human comprehension. The Pi framework creator specifically warns about agents generating 20,000+ lines of unchecked code daily, recommending manual coding for architectural decisions and strict daily generation limits.

rss · Simon Willison · Mar 25, 21:47

**Background**: Agentic engineering refers to AI systems that autonomously plan and execute coding tasks. The Pi framework is an open-source tool for building such AI agents, with features like persistent memory and SQLite integration. Cognitive debt describes the mental overhead from maintaining overly complex systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pchaganti/gx-pi-mono">pchaganti/gx- pi -mono: Monorepo for pi packages: TUI library, agent ...</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Software Engineering`, `#Productivity`, `#Code Quality`

---

<a id="item-15"></a>
## [Claude Code Introduces Auto Mode with Safeguards](https://simonwillison.net/2026/Mar/24/auto-mode-for-claude-code/#atom-everything) ⭐️ 7.0/10

Claude Code has introduced 'auto mode', a new permissions mode where the AI makes decisions on behalf of users with built-in safeguards to prevent unsafe actions. This mode uses Claude Sonnet 4.6 as a classifier model to review and block potentially harmful operations before execution. This represents a significant advancement in AI-assisted coding by providing a middle ground between manual approval of every action and completely unrestricted execution. It could significantly improve developer productivity while maintaining safety standards in automated coding workflows. The auto mode includes extensive default filters covering operations like local file management, package installations, and git operations. Users can also customize these filters, and the system maintains strict rules against scope escalation and potentially destructive actions.

rss · Simon Willison · Mar 24, 23:57

**Background**: Claude Code is an AI-powered coding assistant developed by Anthropic. The '--dangerously-skip-permissions' flag previously allowed users to bypass all safety checks, while auto mode now provides a safer alternative. Claude Sonnet 4.6 is a specialized version of Anthropic's language model optimized for multi-step workflows and conditional logic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet_4">Claude Sonnet 4</a></li>
<li><a href="https://grokipedia.com/page/Claude_Sonnet_46">Claude Sonnet 4.6</a></li>
<li><a href="https://claudelog.com/mechanics/dangerous-skip-permissions/">Dangerous Skip Permissions | ClaudeLog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding`, `#permissions`, `#automation`, `#developer-tools`

---

<a id="item-16"></a>
## [Package Managers Adopt Dependency Cooldown Mechanisms](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/#atom-everything) ⭐️ 7.0/10

Major package managers including pnpm, Yarn, Bun, Deno, uv, pip, and npm have recently implemented dependency cooldown features, which delay installing new package updates for a set period to detect potential supply chain attacks. This industry-wide shift responds to growing supply chain attacks like the recent LiteLLM incident, where malicious updates can spread rapidly before detection. Cooldowns create a critical window for community vetting of new releases. Implementation details vary: pnpm uses `minimumReleaseAge`, Yarn has `npmMinimalAgeGate` in minutes, Bun configures via `bunfig.toml`, while pip currently only supports absolute timestamps with a cron-based workaround available.

rss · Simon Willison · Mar 24, 21:11

**Background**: Dependency cooldowns are a security practice where package managers intentionally delay installing newly published updates. This allows time for the community to detect if a package has been compromised in a supply chain attack, where attackers hijack legitimate packages to distribute malware. The approach gained urgency after high-profile incidents like the March 2026 LiteLLM attack affecting AI frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html">Package Managers Need to Cool Down | Andrew Nesbitt</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns - blog.yossarian.net</a></li>
<li><a href="https://cybernews.com/security/critical-litellm-supply-chain-attack-sends-shockwaves/">Critical supply chain attack hits LiteLLM, exposing AI ...</a></li>

</ul>
</details>

**Tags**: `#package-managers`, `#security`, `#supply-chain`, `#devops`, `#dependencies`

---

<a id="item-17"></a>
## [Claude Code Launches Auto Mode: AI Autonomous Decision-Making with Built-In Safety Reviews](https://claude.com/blog/auto-mode) ⭐️ 7.0/10

Claude Code has introduced Auto Mode, enabling AI to autonomously make decisions during task execution while using a classifier to review actions before each tool call, automatically approving safe operations and blocking high-risk behaviors like mass file deletion or sensitive data leaks. This feature represents a significant step in AI-assisted development by balancing autonomy with safety, reducing the need for manual approvals while mitigating the risks of unchecked AI actions, which could impact developer productivity and enterprise AI adoption. Currently available in research preview for Team plan users, Auto Mode will soon roll out to Enterprise and API users, supporting Claude Sonnet 4.6 and Opus 4.6 models. Though safer than the '--dangerously-skip-permissions' parameter, it may slightly increase token consumption and latency.

telegram · zaihuapd · Mar 25, 01:15

**Background**: Claude Code is an AI-powered developer tool by Anthropic that assists with coding tasks. Traditional approaches either require manual approval for every action (slowing workflows) or skip permissions entirely (creating security risks). Auto Mode introduces a middle path using safety classifiers to evaluate actions dynamically.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/claude-code-auto-mode">Claude Code auto mode: a safer way to skip permissions</a></li>
<li><a href="https://smartscope.blog/en/generative-ai/claude/claude-code-auto-mode-guide/">Claude Code Auto Mode Complete Guide — How the Classifier ...</a></li>
<li><a href="https://institute.sfeir.com/en/articles/claude-code-auto-mode-permissions-autonomy/">Claude Code Auto Mode: Complete Guide to Autonomous Mode ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer-tools`, `#safety`, `#automation`, `#Claude`

---

<a id="item-18"></a>
## [Tencent disbands AI Lab, hires ByteDance Seed leads to boost Hunyuan](https://mp.weixin.qq.com/s/24ZWs8JFP6seQSSIhU6mOw) ⭐️ 7.0/10

Tencent dissolved its AI Lab and restructured its LLM division, while recruiting multiple technical leads from ByteDance's Seed team including Xiao Xuefeng (former head of Seed's visual AI platform) and Huang Qi (training Infra lead). The company plans to release a new generation Hunyuan model in April 2026. This reflects Tencent's strategic shift in AI development focus, consolidating resources to compete in the LLM race by acquiring top talent from ByteDance's cutting-edge Seed team, potentially accelerating Hunyuan's capabilities against rivals like DeepSeek. The restructuring places former ByteDance Seed members in key positions: Xiao Xuefeng as assistant head of AI Infra department and Huang Qi leading training Infra. Tencent's Hunyuan Turbo S model already claims faster response speeds than DeepSeek's R1 system.

telegram · zaihuapd · Mar 25, 03:00

**Background**: Tencent's Hunyuan is a large language model competing in China's AI market, with versions like Hunyuan-Large achieving top performance benchmarks. ByteDance's Seed team, established in 2023, focuses on cutting-edge AI research including LLMs, vision, and infrastructure. AI Infra refers to the underlying systems and tools that support AI model development and deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Tencent-Hunyuan-Large">tencent / Tencent - Hunyuan -Large · Hugging Face</a></li>
<li><a href="https://seed.bytedance.com/en/">ByteDance Seed</a></li>
<li><a href="https://github.com/bytedance-seed">ByteDance-Seed · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tencent`, `#LLM`, `#Corporate Restructuring`, `#ByteDance`

---

<a id="item-19"></a>
## [Pinduoduo announces 'New Pinmu' with 100B RMB investment for brand self-operation](https://m.tmtpost.com/nictation/7929040.html) ⭐️ 7.0/10

Pinduoduo officially launched 'New Pinmu', pledging to invest 100 billion RMB over three years to shift from platform operations to brand self-operation, with an initial capital injection of 15 billion RMB. The initiative aims to integrate supply chain resources from Pinduoduo and Temu to build self-operated brands targeting global markets. This strategic shift could redefine Pinduoduo's business model and intensify competition in global e-commerce, particularly against rivals like Amazon and Alibaba. The massive investment signals China's growing emphasis on controlling supply chains and building direct consumer relationships through vertical integration. The project has established a dedicated company in Shanghai, focusing on category-specific brands for different markets. This marks the first major strategy implementation under co-CEO Zhao Jiazhen's leadership since December 2023.

telegram · zaihuapd · Mar 25, 12:37

**Background**: Pinduoduo originally operated as an agricultural-focused group-buying platform, while Temu is its international arm offering discounted goods shipped from China. Brand self-operation models allow e-commerce companies to control product quality, pricing, and supply chains directly, contrasting with traditional marketplace platforms that connect third-party sellers with buyers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Temu">Temu - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1366554522003283">How does manufacturer’s self-operating channel interact with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vertical_integration">Vertical integration - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#e-commerce`, `#supply-chain`, `#business-strategy`, `#china-tech`, `#retail`

---

<a id="item-20"></a>
## [CCF opposes NeurIPS' ban on submissions from US-sanctioned institutions, calls for boycott](https://www.ccf.org.cn/Focus/2026-03-25/865918.shtml) ⭐️ 7.0/10

The China Computer Federation (CCF) issued a statement strongly opposing NeurIPS 2026's policy banning submissions from US-sanctioned institutions and called for Chinese scholars to boycott the conference. CCF threatened to remove NeurIPS from its recommended international conference list if the policy isn't changed. This controversy highlights growing tensions between academic freedom and geopolitical restrictions in AI research, potentially fracturing international collaboration in a field that has traditionally valued open exchange. The CCF's stance represents a significant pushback from China's academic community against perceived politicization of scientific discourse. NeurIPS 2026 will be held in Sydney from December 6-12, 2026. CCF's recommended conference list is highly influential in China's computer science community, affecting researchers' publication strategies and career evaluations.

telegram · zaihuapd · Mar 25, 14:07

**Background**: NeurIPS (Conference on Neural Information Processing Systems) is one of the world's most prestigious AI conferences, founded in 1987. The China Computer Federation (CCF), established in 1962, is China's primary academic organization for computer science professionals and maintains an influential list of recommended international conferences and journals.

<details><summary>References</summary>
<ul>
<li><a href="https://neurips.cc/">NeurIPS - 2026 Conference</a></li>
<li><a href="https://www.ccf.org.cn/Academic_Evaluation/By_category/">CCF推荐国际学术刊物目录-中国计算机学会</a></li>
<li><a href="https://www.ccf.org.cn/en/About_CCF/Media_Center/">The Latest Edition of "List of International Academic ...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#academic freedom`, `#NeurIPS`, `#China-US relations`, `#research policy`

---

<a id="item-21"></a>
## [Intel and AMD warn Chinese clients of extended server CPU delivery times](https://t.me/zaihuapd/40507) ⭐️ 7.0/10

Intel and AMD have notified Chinese clients of server CPU supply constraints, with Intel's delivery times extending up to 6 months for some Xeon processors and AMD's up to 8-10 weeks. Prices for Intel server products in China have risen over 10% due to these shortages. This supply crunch could significantly impact China's server infrastructure and AI adoption, as these CPUs are critical for data centers and AI workloads. The price increases and delays may slow down enterprise and cloud computing expansions in the region. Intel is limiting supplies of its 4th and 5th Gen Xeon processors in China, with inventory levels expected to be lowest in Q1 2026 before improving in Q2. The company attributes the shortages to AI-driven demand for 'traditional computing' resources.

telegram · zaihuapd · Mar 26, 00:03

**Background**: Xeon processors are Intel's line of server-grade CPUs designed for demanding workloads in data centers. The current supply issues come amid a global AI server boom, with projections showing AI servers accounting for 19% of total server shipments by 2027. Server memory prices are also under pressure due to AI-driven demand shifts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xeon">Xeon - Wikipedia</a></li>
<li><a href="https://files.futurememorystorage.com/proceedings/2024/20240808_BMKT-301-1_KUNG.pdf">See Generative AI's Impact on the AI Server Market to 2025</a></li>
<li><a href="https://www.reuters.com/world/china/ai-frenzy-is-driving-new-global-supply-chain-crisis-2025-12-03/">The AI frenzy is driving a memory chip supply crisis | Reuters</a></li>

</ul>
</details>

**Tags**: `#supply-chain`, `#semiconductors`, `#servers`, `#AI`, `#China`

---

<a id="item-22"></a>
## [GitHub updates Copilot data policy: Free and paid individual users now included in AI training by default, with opt-out option](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) ⭐️ 7.0/10

GitHub announced changes to Copilot's data usage policy starting April 24, where interaction data from Copilot Free, Pro, and Pro+ users (including inputs, outputs, and code snippets) will be used by default to train AI models, with an opt-out option in Privacy settings. The policy excludes Copilot Business and Enterprise users, and previously set opt-out preferences will remain unchanged. This policy change significantly expands GitHub's AI training dataset by incorporating millions of individual developers' coding patterns, potentially improving Copilot's suggestions but raising privacy considerations. It reflects the industry trend of using real user interactions to refine AI models while balancing transparency through opt-out mechanisms. Training data includes adjacent code context, comments, filenames, repo structures, navigation patterns, and feedback on suggestions. Data may be shared with Microsoft affiliates but won't be provided to third-party AI vendors. Enterprise codebases remain excluded from this data collection.

telegram · zaihuapd · Mar 26, 00:47

**Background**: GitHub Copilot is an AI pair programmer that suggests code completions powered by OpenAI models. AI models typically improve through training on diverse datasets, including user interactions. Recent advances focus on dynamic learning from real-time user behavior beyond static datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/">Updates to GitHub Copilot interaction data usage policy</a></li>
<li><a href="https://www.howtogeek.com/githubs-copilot-will-use-you-as-ai-training-data-but-you-can-opt-out/">GitHub’s Copilot will use you as AI training data, but you ...</a></li>
<li><a href="https://roboin.io/article/en/2026/03/26/github-to-use-copilot-data-for-ai-training/">GitHub to use Copilot data for AI training from April 24; how ...</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#Copilot`, `#AI`, `#Privacy`, `#Data Policy`

---