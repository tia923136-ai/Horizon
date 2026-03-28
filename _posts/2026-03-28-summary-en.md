---
layout: default
title: "Horizon Summary: 2026-03-28 (EN)"
date: 2026-03-28
lang: en
---

> From 27 items, 10 important content pieces were selected

---

1. [LiteLLM PyPI package compromised in malware attack](#item-1) ⭐️ 8.0/10
2. [Interactive deep dive on LLM quantization and floating-point representation](#item-2) ⭐️ 8.0/10
3. [China Computer Federation opposes NeurIPS 2026's policy restricting submissions from US-sanctioned institutions](#item-3) ⭐️ 8.0/10
4. [Huawei launches Atlas 350 AI accelerator with Ascend 950PR, 2.87x H20 performance](#item-4) ⭐️ 8.0/10
5. [AI Rewrites JSONata in Go, Saves $500K Annually](#item-5) ⭐️ 7.0/10
6. [IOC restricts women's Olympic events to biological females from 2028](#item-6) ⭐️ 7.0/10
7. [Google adds system-level VPN split-tunneling in Android 17 Beta 3](#item-7) ⭐️ 7.0/10
8. [ByteDance's Seedance 2.0 AI Model Launches Internationally via Dreamina with Enhanced Copyright Protection](#item-8) ⭐️ 7.0/10
9. [Apple provides FBI with real user data behind anonymous iCloud email](#item-9) ⭐️ 7.0/10
10. [China launches trade barriers investigation against US practices](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM PyPI package compromised in malware attack](https://simonwillison.net/2026/Mar/26/response-to-the-litellm-malware-attack/#atom-everything) ⭐️ 8.0/10

Versions 1.82.7 and 1.82.8 of the LiteLLM package on PyPI were found to contain malware that steals credentials and sensitive data, with the attack traced to a compromised maintainer account via a prior Trivy security scanner breach. This incident highlights critical supply chain risks in AI infrastructure, as LiteLLM is widely used to interface with major LLM providers like OpenAI and Anthropic, potentially exposing API keys and cloud credentials across numerous applications. The malware uses AES-256-CBC + RSA-4096 encryption to exfiltrate stolen data to models.litellm.cloud, targeting SSH keys, cloud credentials, crypto wallets, and CI/CD configurations. Analysis was conducted in an isolated Docker container confirming live infection.

rss · Simon Willison · Mar 26, 23:58

**Background**: LiteLLM provides a unified API for interacting with multiple LLM providers. PyPI is Python's official package repository where developers publish and share libraries. Supply chain attacks have increased as attackers target widely used dependencies to maximize impact.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sonatype.com/blog/compromised-litellm-pypi-package-delivers-multi-stage-credential-stealer">Compromised litellm PyPI Package Delivers Multi-Stage Credential Stealer</a></li>
<li><a href="https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/">How a Poisoned Security Scanner Became the Key to Backdooring LiteLLM | Snyk</a></li>
<li><a href="https://github.com/BerriAI/litellm/issues/24518">[Security]: litellm PyPI package (v1.82.7 + v1.82.8) compromised — full timeline and status · Issue #24518 · BerriAI/litellm</a></li>

</ul>
</details>

**Tags**: `#security`, `#PyPI`, `#malware`, `#incident-response`, `#AI`

---

<a id="item-2"></a>
## [Interactive deep dive on LLM quantization and floating-point representation](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose published an interactive essay explaining quantization in Large Language Models, featuring an innovative visual breakdown of floating-point number representation and analysis of outlier values' impact on model quality. This provides crucial technical insights for ML practitioners implementing model compression, showing how 8-bit quantization maintains ~90% accuracy while significantly reducing computational requirements. The essay reveals that preserving 'super weights' (critical outlier values) is essential to prevent model degradation, and demonstrates quantization effects using llama.cpp's perplexity tool on Qwen 3.5 9B model.

rss · Simon Willison · Mar 26, 16:21

**Background**: Quantization reduces model size by converting high-precision numbers (like 32-bit floats) to lower precision (like 8-bit integers). Floating-point numbers use binary representation with sign, exponent and significand components. LLMs often contain rare but critical weight values that require special handling during quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@lmpo/understanding-model-quantization-for-llms-1573490d44ad">Understanding Quantization for LLMs | by LM Po | Medium</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/model-quantization-large-language-models">Understanding Model Quantization in Large Language ... | DigitalOcean</a></li>
<li><a href="https://en.wikipedia.org/wiki/Floating-point_arithmetic">Floating-point arithmetic - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#quantization`, `#llms`, `#floating-point`, `#technical-deep-dive`

---

<a id="item-3"></a>
## [China Computer Federation opposes NeurIPS 2026's policy restricting submissions from US-sanctioned institutions](https://t.me/zaihuapd/40549) ⭐️ 8.0/10

The China Computer Federation (CCF) has issued a statement opposing NeurIPS 2026's policy that restricts submissions from institutions on the US sanctions list, calling it a politicization of academic exchange and urging Chinese scholars to boycott the conference. This controversy highlights the growing politicization of academic conferences and could significantly impact international collaboration in AI research, potentially leading to a divide in the global academic community. NeurIPS 2026 explicitly prohibits submissions from 'certain organizations on the US sanctions list,' which has sparked widespread debate. The CCF emphasizes that open, inclusive, and equal collaboration is a core value of academic exchange.

telegram · zaihuapd · Mar 27, 11:00

**Background**: NeurIPS (Conference on Neural Information Processing Systems) is one of the most prestigious AI conferences globally, known for its interdisciplinary approach and high ethical standards. The US sanctions against certain Chinese institutions have been a point of contention in academic and technological exchanges between the two countries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conference_on_Neural_Information_Processing_Systems">Conference on Neural Information Processing Systems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_sanctions_against_China">United States sanctions against China - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Ethics`, `#Academic Freedom`, `#NeurIPS`, `#International Collaboration`, `#Research Policy`

---

<a id="item-4"></a>
## [Huawei launches Atlas 350 AI accelerator with Ascend 950PR, 2.87x H20 performance](https://t.me/zaihuapd/40556) ⭐️ 8.0/10

Huawei unveiled the Atlas 350 AI accelerator card at its China Partners Conference 2026, featuring the new Ascend 950PR processor with 112GB HBM memory and FP4 low-precision inference support, delivering 2.87x the performance of Nvidia's H20 accelerator. This represents a major advancement in domestic AI hardware capabilities, reducing reliance on foreign chips while offering superior performance for large language model inference with lower latency and cost. The Atlas 350 supports single-card loading of 70B parameter models and features significant improvements in vector computing, interconnect bandwidth, and self-developed HBM technology compared to previous generations.

telegram · zaihuapd · Mar 27, 15:30

**Background**: FP4 is a 4-bit floating point format gaining adoption in cutting-edge AI architectures for efficient low-precision inference. HBM (High Bandwidth Memory) is a 3D-stacked memory technology crucial for AI accelerators, offering much higher bandwidth than traditional memory solutions. The Ascend 950PR is Huawei's latest AI processor featuring a monolithic compute die design.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/">Ascend 950PR AI Chip: Everything you need to know - Huawei Central</a></li>
<li><a href="https://convequity.substack.com/p/huawei-ascend-ai-chip-roadmap-and">Huawei Ascend AI Chip Roadmap & System level performance data</a></li>
<li><a href="https://www.trendforce.com/news/2026/03/23/news-huawei-debuts-atlas-350-on-ascend-950pr-with-in-house-hbm-touting-2-8x-h20-performance/">[News] Huawei Debuts Atlas 350 on Ascend 950PR with In-house HBM, Touting 2.8X H20 Performance</a></li>

</ul>
</details>

**Tags**: `#AI Hardware`, `#Accelerators`, `#Huawei`, `#Deep Learning`, `#FP4 Inference`

---

<a id="item-5"></a>
## [AI Rewrites JSONata in Go, Saves $500K Annually](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

The Reco team used AI to rewrite JSONata, a JSON query language, in Go within 7 hours using $400 worth of tokens, then validated it through shadow deployment against the original implementation. This demonstrates how AI-assisted 'vibe porting' can dramatically reduce development costs and time while maintaining accuracy through existing test suites and validation techniques. The project leveraged JSONata's comprehensive test suite for rapid validation, and used shadow deployment to run both implementations in parallel for a week to ensure behavioral parity.

rss · Simon Willison · Mar 27, 00:35

**Background**: JSONata is a lightweight query and transformation language for JSON data, similar to jq but with richer expression capabilities. Shadow deployment is a testing technique where new implementations process real traffic invisibly alongside production systems. 'Vibe porting' refers to using AI to quickly adapt software to new environments while preserving its core functionality.

<details><summary>References</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata : A declarative open-source query and transformation...</a></li>
<li><a href="https://devops.com/what-is-a-shadow-deployment/">What is a Shadow Deployment? - DevOps.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#go`, `#json`, `#ai`, `#automation`, `#cost-optimization`

---

<a id="item-6"></a>
## [IOC restricts women's Olympic events to biological females from 2028](https://www.bbc.com/sport/olympics/articles/cdj7dgvlj0no?at_medium=RSS&amp;at_campaign=rss) ⭐️ 7.0/10

The International Olympic Committee announced that starting from the 2028 Los Angeles Olympics, women's events will be restricted to biological females, with eligibility determined by a one-time SRY gene test. Transgender women who have undergone male puberty and most DSD athletes will be excluded from women's categories but can compete in men's, open, or mixed-gender events. This policy represents a major shift in Olympic gender eligibility rules, potentially reshaping competitive fairness debates in women's sports. It aligns with similar moves by World Athletics and could set a precedent for other international sporting bodies. The SRY gene test detects the presence of the Y-chromosome's sex-determining region. DSD (Differences of Sex Development) athletes with certain conditions like 46,XY DSD will be most affected by this ruling.

telegram · zaihuapd · Mar 27, 05:15

**Background**: The SRY gene is the sex-determining region on the Y chromosome that triggers male development. DSD refers to congenital conditions where chromosomal, gonadal or anatomical sex develops atypically. Sports organizations have struggled to balance inclusion with competitive fairness in women's categories.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sex-determining_region_Y_protein">Sex-determining region Y protein - Wikipedia</a></li>
<li><a href="https://scienceinsights.org/what-is-a-dsd-athlete-meaning-and-rules-explained/">What Is a DSD Athlete? Meaning and Rules Explained</a></li>
<li><a href="https://www.olympics.com/en/news/semenya-niyonsaba-wambui-what-is-dsd-iaaf-regulations">DSD athletes: What does it mean to be DSD and how gender and ...</a></li>

</ul>
</details>

**Tags**: `#sports`, `#gender`, `#policy`, `#olympics`, `#biology`

---

<a id="item-7"></a>
## [Google adds system-level VPN split-tunneling in Android 17 Beta 3](https://www.androidauthority.com/android-17-vpn-split-tunneling-3652497/) ⭐️ 7.0/10

Google introduced system-level VPN split-tunneling in Android 17 Beta 3, allowing users to exclude specific apps from VPN connections. The feature replaces fragmented implementations by individual VPN apps with a unified settings page. This standardization improves VPN usability and security by addressing common issues with banking and streaming apps that often malfunction under VPN connections. It also reduces dependency on individual VPN providers' implementations. The feature currently targets developers and requires VPN app integration to function. Changes can take effect immediately during active VPN connections or upon next connection.

telegram · zaihuapd · Mar 27, 05:57

**Background**: VPN split-tunneling allows selective routing of network traffic, where some apps use the VPN while others connect directly through the ISP. Prior to Android 17, implementations varied widely across VPN apps, often leading to inconsistent user experiences.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/android-17-vpn-split-tunneling-3652497/">Android 17 could finally fix one of the most annoying VPN problems</a></li>
<li><a href="https://grokipedia.com/page/Split_Tunneling">Split Tunneling</a></li>

</ul>
</details>

**Tags**: `#Android`, `#VPN`, `#Networking`, `#Beta`, `#Security`

---

<a id="item-8"></a>
## [ByteDance's Seedance 2.0 AI Model Launches Internationally via Dreamina with Enhanced Copyright Protection](https://dreamina.capcut.com/tools/seedance-2-0) ⭐️ 7.0/10

ByteDance's Seedance 2.0 AI model is now available internationally through Dreamina, featuring improved copyright protection via visible watermarks and embedded C2PA content credentials. The model integrates images, videos, audio, and text into AI-generated videos with enhanced consistency control for characters, shots, and visual styles. This marks ByteDance's strategic expansion in AI video generation tools, addressing growing industry concerns about content authenticity and intellectual property protection. The C2PA integration positions Dreamina as a platform prioritizing media provenance in an era of rampant AI-generated content. The model outputs 720p-1080p videos lasting 5-12 seconds, with strict IP protection measures including platform-level blocking of unauthorized content. Seedance 2.0 specifically solves common AI video issues like character drift and style inconsistency through its multi-modal architecture.

telegram · zaihuapd · Mar 27, 06:43

**Background**: Seedance is ByteDance's proprietary AI video generation model, with version 2.0 introducing cinematic-quality multi-modal capabilities. C2PA (Coalition for Content Provenance and Authenticity) is an open standard for content attribution metadata, used by over 500 companies to combat misinformation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.seedance20.com/">Generate Cinematic Videos with Seedance 2 . 0 Model | Seedio</a></li>
<li><a href="https://seedance2.ai/">Seedance 2 . 0</a></li>
<li><a href="https://en.wikipedia.org/wiki/C2PA_signatures">Content Credentials - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#video-generation`, `#copyright-protection`, `#ByteDance`, `#C2PA`

---

<a id="item-9"></a>
## [Apple provides FBI with real user data behind anonymous iCloud email](https://www.404media.co/apple-gives-fbi-a-users-real-name-hidden-behind-hide-my-email-feature/) ⭐️ 7.0/10

Apple provided the FBI with the real iCloud account details linked to an anonymous 'Hide My Email' address used to send threats. The user, Alden Ruml, had generated 134 anonymous email addresses and later confessed to sending threatening emails. This case reveals that Apple's privacy-focused 'Hide My Email' feature can still be traced back to real accounts during law enforcement investigations, raising questions about the balance between user privacy and corporate cooperation with government agencies. The 'Hide My Email' feature is part of iCloud+ subscription service, allowing users to create random forwarding email aliases. Despite being marketed as privacy-protecting, Apple retains the ability to link these aliases to real accounts.

telegram · zaihuapd · Mar 27, 13:09

**Background**: Apple's 'Hide My Email' is a feature for iCloud+ subscribers that generates random email aliases to protect users' real email addresses when signing up for services online. While marketed as enhancing privacy, the feature doesn't provide complete anonymity as Apple can still associate aliases with the original iCloud account.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/guide/icloud/what-you-can-do-with-icloud-and-hide-my-email-mme38e1602db/icloud">Create unique, random email addresses with Hide My Email and ...</a></li>
<li><a href="https://www.techspot.com/news/111851-apple-hide-email-isnt-anonymous-sounds.html">Apple's "Hide My Email" isn't as anonymous as it sounds</a></li>
<li><a href="https://www.404media.co/apple-gives-fbi-a-users-real-name-hidden-behind-hide-my-email-feature/">Apple Gives FBI a User’s Real Name Hidden Behind ’Hide My Email ...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#law-enforcement`, `#Apple`, `#cybersecurity`, `#data-privacy`

---

<a id="item-10"></a>
## [China launches trade barriers investigation against US practices](https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_a87743853da94b22ace113ee98591fa5.html) ⭐️ 7.0/10

China's Ministry of Commerce announced on March 27, 2026, that it has initiated a trade barriers investigation into US practices affecting global supply chains, including restrictions on Chinese products, high-tech exports, and bilateral investments. This investigation could escalate trade tensions between the world's two largest economies and potentially lead to WTO disputes, affecting global supply chains and international trade rules. The investigation will use questionnaires, hearings, and on-site inspections, and must conclude within 6 months (extendable by 3 months). Stakeholders must submit written comments within 20 days of the announcement.

telegram · zaihuapd · Mar 27, 14:23

**Background**: Trade barrier investigations are WTO-authorized procedures to examine whether a country's trade practices violate international rules. The Technical Barriers to Trade Agreement aims to prevent unnecessary obstacles to trade while allowing legitimate policy objectives.

<details><summary>References</summary>
<ul>
<li><a href="https://www.trade.gov/technical-regulatory-trade-barriers">Technical Regulatory Trade Barriers - International Trade Administration</a></li>
<li><a href="https://www.wto-ilibrary.org/content/theme/wto-technical-barriers-to-trade">Technical barriers to trade - WTO iLibrary</a></li>

</ul>
</details>

**Tags**: `#trade`, `#China-US relations`, `#supply chain`, `#WTO`, `#commerce`

---