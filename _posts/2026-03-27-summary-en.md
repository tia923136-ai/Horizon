---
layout: default
title: "Horizon Summary: 2026-03-27 (EN)"
date: 2026-03-27
lang: en
---

> From 36 items, 10 important content pieces were selected

---

1. [Google announces post-quantum cryptography in Android 17](#item-1) ⭐️ 9.0/10
2. [Developer shares real-time transcript of LiteLLM malware attack response](#item-2) ⭐️ 8.0/10
3. [Interactive guide demystifies LLM quantization](#item-3) ⭐️ 8.0/10
4. [Apifox Desktop Client Hit by Supply-Chain Attack via CDN Script](#item-4) ⭐️ 8.0/10
5. [CAS releases Xiangshan RISC-V processor and Ruyi OS, launches next-gen chip/OS co-development](#item-5) ⭐️ 8.0/10
6. [58th-generation cloned mouse dies next day, suggesting mammalian cloning limits](#item-6) ⭐️ 8.0/10
7. [Google Launches Gemini 3.1 Flash Live with Faster Multimodal Conversations](#item-7) ⭐️ 8.0/10
8. [AI Rewrites JSONata in Go, Saves $500K Annually](#item-8) ⭐️ 7.0/10
9. [Critique of speed-focused AI-assisted development](#item-9) ⭐️ 7.0/10
10. [Study shows paternal age increases genetic disease risk more than previously thought](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google announces post-quantum cryptography in Android 17](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html) ⭐️ 9.0/10

Google announced the integration of post-quantum cryptography (PQC) standards in Android 17, upgrading the bootloader with quantum-resistant digital signatures and migrating the Android Keystore to PQC-compliant architecture. This is significant as it prepares Android devices for future quantum computing threats, ensuring continued security for device boot processes and communication with external servers in the quantum era. The upgrade includes quantum-resistant digital signatures in the bootloader to prevent tampering during the boot sequence, and a PQC-compliant Keystore for secure authentication and data transmission.

telegram · zaihuapd · Mar 26, 07:09

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to be secure against quantum computer attacks. NIST released the first PQC standards in 2024, marking a significant step in preparing for the quantum computing era. Traditional encryption methods like RSA and ECDSA are vulnerable to quantum attacks, necessitating the transition to PQC.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography - Wikipedia</a></li>
<li><a href="https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html">Security for the Quantum Era: Implementing Post-Quantum ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Quantum Cryptography`, `#Security`, `#Encryption`, `#Google`

---

<a id="item-2"></a>
## [Developer shares real-time transcript of LiteLLM malware attack response](https://futuresearch.ai/blog/litellm-attack-transcript/) ⭐️ 8.0/10

A developer published a minute-by-minute transcript detailing their discovery and response to a malware attack in versions 1.82.7 and 1.82.8 of the LiteLLM PyPI package, which was compromised to deliver a multi-stage credential stealer. This incident highlights critical vulnerabilities in open-source package ecosystems, demonstrating how supply chain attacks can compromise widely-used AI tools and put developers' systems at risk. The attack exploited Python's .pth files which execute on every Python startup, unlike npm's one-time postinstall hooks. The malware was designed to steal credentials and authentication tokens from infected systems.

hackernews · Fibonar · Mar 26, 15:48

**Background**: LiteLLM is a popular Python SDK that provides a unified interface to call various LLM APIs. PyPI (Python Package Index) is the official repository for Python packages, similar to npm for JavaScript. Supply chain attacks target trusted software distribution channels to spread malware to downstream users.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/litellm/">litellm · PyPI</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/supply-chain-attack/">What Is a Supply Chain Attack? - CrowdStrike</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lXaDlyakVCR0F3M1ZIa2VnQW5pZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - LiteLLM PyPI package hack - Overview</a></li>

</ul>
</details>

**Discussion**: Developers discussed the need for better package registry monitoring, with suggestions like real-time security analysis firehoses. Concerns were raised about LLM agents potentially executing malicious scripts, and technical details about Python's .pth file behavior sparked security awareness discussions.

**Tags**: `#security`, `#malware`, `#pypi`, `#supply-chain`, `#ai`

---

<a id="item-3"></a>
## [Interactive guide demystifies LLM quantization](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/#atom-everything) ⭐️ 8.0/10

Sam Rose published an interactive essay with groundbreaking visualizations explaining LLM quantization, including float32 binary representations and outlier value preservation techniques. The article demonstrates quantization's impact using Qwen 3.5 9B model tests with llama.cpp's perplexity tool. This resource makes advanced quantization concepts accessible to practitioners, crucial for deploying LLMs on resource-constrained devices. Understanding outlier preservation is particularly valuable as these 'super weights' disproportionately affect model performance. The visual float32 representation tool color-codes sign, exponent, and significand bits. Tests show 16-bit to 8-bit quantization has minimal quality loss, while 16-bit to 4-bit retains ~90% accuracy. Apple's 'super weight' concept reveals single outliers can prevent model collapse.

rss · Simon Willison · Mar 26, 16:21

**Background**: Quantization reduces LLM memory requirements by converting high-precision numbers (e.g., 32-bit floats) to lower-precision formats (e.g., 8-bit integers). IEEE 754 single-precision (float32) uses 1 sign bit, 8 exponent bits, and 23 significand bits. Perplexity and KL divergence are metrics for evaluating quantization's impact on model quality.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@lmpo/understanding-model-quantization-for-llms-1573490d44ad">Understanding Quantization for LLMs | by LM Po | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single-precision_floating-point_format">Single-precision floating - point format - Wikipedia</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#quantization`, `#llm`, `#floating-point`, `#interactive-learning`

---

<a id="item-4"></a>
## [Apifox Desktop Client Hit by Supply-Chain Attack via CDN Script](https://t.me/zaihuapd/40514) ⭐️ 8.0/10

Apifox's desktop client was compromised in a supply-chain attack where malicious code was injected into its CDN-hosted event tracking script, stealing SSH keys, Git credentials, shell history, and process lists since March 4. Security researcher phith0n independently analyzed the malicious payload, confirming cross-platform impact on Windows, macOS, and Linux users. This incident highlights critical risks in widely-used developer tools, as Apifox combines functionalities like Postman and Swagger, making it a high-value target. Compromised SSH/Git credentials could lead to lateral attacks in corporate networks and unauthorized access to private repositories. The obfuscated malicious JavaScript was injected into apifox-app-event-tracking.min.js hosted on Apifox's official CDN (cdn.apifox.com). The attack vector bypasses traditional security checks as the compromised script was served from a trusted source.

telegram · zaihuapd · Mar 26, 04:19

**Background**: Apifox is a popular API development tool combining features of Postman, Swagger, and JMeter, widely used for API documentation, testing, and CI/CD integration. Supply-chain attacks target software distribution channels like CDNs to infect downstream users automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://slowmist.medium.com/security-alert-supply-chain-attack-on-apifox-desktop-client-via-compromised-official-cdn-script-bc3870992564">Security Alert: Supply Chain Attack on Apifox Desktop Client via Compromised Official CDN Script | by SlowMist | Mar, 2026 | Medium</a></li>
<li><a href="https://apifox.com/">Apifox - API 文档、调试、Mock...</a></li>
<li><a href="https://x.com/SlowMist_Team/status/2037024243112702075">SlowMist on X: "🚨 Security Alert: Supply Chain Attack on Apifox Desktop Client Yesterday, we detected a supply chain attack in which a front-end script file hosted on #Apifox’s official CDN was injected with heavily obfuscated malicious JavaScript code. ⚡ Impact on Apifox Desktop Client https://t.co/Z8Sl8FgFjQ" / X</a></li>

</ul>
</details>

**Discussion**: Security communities emphasize urgent credential rotation, with SlowMist confirming the CDN compromise. Users report finding malicious artifacts in local Apifox data, sparking debates about CDN security practices in dev tools.

**Tags**: `#security`, `#supply-chain-attack`, `#apifox`, `#malware`, `#devops`

---

<a id="item-5"></a>
## [CAS releases Xiangshan RISC-V processor and Ruyi OS, launches next-gen chip/OS co-development](https://h.xinhuaxmt.com/vh512/share/13024070?docid=13024070) ⭐️ 8.0/10

The Chinese Academy of Sciences unveiled the open-source Xiangshan high-performance RISC-V processor and Ruyi native operating system on March 26, while initiating joint development of next-generation 'Kunming Lake' architecture and OS with industry partners including China Mobile, Alibaba, and Tencent. This marks China's major advancement in open-source chip and system technologies, with Xiangshan achieving international-level performance and Ruyi being the first to fully support global standards, potentially reducing foreign dependency in critical semiconductor and OS domains. Xiangshan includes the world's first open-source on-chip interconnect network IP, while commercial chips based on it have already been launched by companies like Ingenic and BlueCore. The Ruyi SDK supports multiple RISC-V development boards for IoT and smart devices.

telegram · zaihuapd · Mar 26, 10:08

**Background**: RISC-V is an open-standard instruction set architecture gaining global traction as an alternative to proprietary architectures like ARM. On-chip interconnect IP enables efficient communication between processor cores, while native OS refers to systems specifically designed for a particular hardware architecture rather than being ported from existing systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/OpenXiangShan/XiangShan">GitHub - OpenXiangShan/ XiangShan : Open - source high-performance...</a></li>
<li><a href="https://ruyisdk.org/en/docs/intro/">Hello Ruyi | RuyiSDK</a></li>
<li><a href="https://www.design-reuse.com/ip/111-interconnect-d2d-c2c">Interconnect , D2D, C2C IP Core</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#open-source-hardware`, `#operating-systems`, `#semiconductors`, `#China-tech`

---

<a id="item-6"></a>
## [58th-generation cloned mouse dies next day, suggesting mammalian cloning limits](https://www.nature.com/articles/s41467-026-69765-7) ⭐️ 8.0/10

A Japanese team cloned a female mouse through 58 successive generations over 20 years, producing over 1,200 cloned mice, but viability dropped to zero by the final generation with all 58th-generation clones dying within two days of birth despite no visible abnormalities. This provides concrete evidence that mammalian cloning has inherent biological limits due to accumulated genetic mutations, challenging the feasibility of indefinite cloning and highlighting the importance of sexual reproduction for maintaining genetic health. Mutation rates in cloned mice were 3× higher than naturally bred offspring, with some losing entire X chromosomes. Viability declined sharply after generation 25, with only 1% survival by generation 57.

telegram · zaihuapd · Mar 26, 16:46

**Background**: Cloning techniques like somatic cell nuclear transfer (used for Dolly the sheep) allow creating genetically identical organisms, but success rates remain low (typically <3%). Previous studies showed cloned animals often have developmental abnormalities due to epigenetic reprogramming errors during the cloning process.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-hans/克隆">克隆 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.stdaily.com/web/gjxw/2026-03/25/content_492459.html">有性生殖为何重要？20年研究表明——哺乳动物克隆存在技术极限</a></li>

</ul>
</details>

**Tags**: `#genetics`, `#cloning`, `#reproductive-science`, `#mammalian-biology`, `#mutations`

---

<a id="item-7"></a>
## [Google Launches Gemini 3.1 Flash Live with Faster Multimodal Conversations](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/) ⭐️ 8.0/10

Google released Gemini 3.1 Flash Live, a real-time audio and speech model that enhances multimodal conversations with faster responses, improved acoustic detail recognition, and expanded support for 90+ languages. The update also extends Search Live availability to 200+ countries and integrates with Gemini Live, Enterprise for Customer Experience, and Google AI Studio. This upgrade significantly improves real-time AI interactions for global users, enabling more natural voice-based applications in customer service, search, and developer tools. The expanded language support and noise robustness make Google's multimodal AI more accessible worldwide. The model doubles context retention for continuous conversations on mobile apps and introduces acoustic nuance detection for pitch/speed variations. Technical documentation confirms it's optimized for low-latency audio-to-audio pipelines in the Gemini Live API preview.

telegram · zaihuapd · Mar 26, 17:01

**Background**: Gemini is Google's family of multimodal AI models capable of processing text, images, audio, and video simultaneously. Multimodal systems translate different input types into shared representations for unified context understanding, enabling applications like real-time voice assistants that combine speech recognition with visual inputs (e.g., Google Lens).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview">Gemini 3 . 1 Flash Live Preview | Gemini API | Google AI for Developers</a></li>
<li><a href="https://tblocks.com/guides/multi-modal-ai/">What Is Multimodal AI? Architecture, Use Cases, and Impact</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Multimodal`, `#Speech Recognition`, `#Real-time`

---

<a id="item-8"></a>
## [AI Rewrites JSONata in Go, Saves $500K Annually](https://simonwillison.net/2026/Mar/27/vine-porting-jsonata/#atom-everything) ⭐️ 7.0/10

The Reco team used AI to rewrite the JSONata JSON query language in Go within 24 hours, achieving full compatibility through test-driven development and shadow deployment, resulting in $500K annual cost savings. This demonstrates AI's potential to accelerate costly code migrations while maintaining reliability, setting a precedent for LLM-assisted legacy system modernization in enterprise environments. The migration leveraged JSONata's existing test suite for validation, completed initial Go version in 7 hours with $400 AI token cost, and used week-long shadow deployment for behavioral verification.

rss · Simon Willison · Mar 27, 00:35

**Background**: JSONata is an open-source JSON query language similar to jq, originally developed for Node-RED. Shadow deployment duplicates production traffic to test new systems without affecting users, while 'vibe-porting' refers to AI-assisted code migration between languages using existing test suites as guardrails.

<details><summary>References</summary>
<ul>
<li><a href="https://jsonata.org/">JSONata : A declarative open-source query and transformation...</a></li>
<li><a href="https://codefresh.io/learn/software-deployment/shadow-deployments-benefits-process-and-4-tips-for-success/">Shadow Deployments : Benefits, Process, and 4 Tips for Success</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Go`, `#JSON`, `#code-migration`, `#cost-optimization`

---

<a id="item-9"></a>
## [Critique of speed-focused AI-assisted development](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything) ⭐️ 7.0/10

Mario Zechner, creator of the Pi agent framework, critiques the unchecked use of AI agents in software development, warning against prioritizing speed over quality and the accumulation of 'cognitive debt'. He advocates for deliberate slowdowns and manual coding of critical system components. This critique highlights a growing tension in software engineering as AI tools enable unprecedented productivity but risk creating unmaintainable systems. The perspective is particularly relevant as more teams adopt agentic engineering approaches without proper guardrails. The Pi framework mentioned is a monorepo including components for LLM communication, agent loops with tool calling, and coding agents with session persistence. Zechner specifically warns about the compounding effect of errors when multiple agents operate without human review bottlenecks.

rss · Simon Willison · Mar 25, 21:47

**Background**: Agentic engineering is an emerging discipline focused on AI systems that autonomously plan and execute tasks with minimal human oversight. The Pi framework is an open-source toolkit for building such agents, particularly for coding tasks. Cognitive debt refers to the mental overhead required to understand and maintain complex systems, analogous to technical debt.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/badlogic/pi-mono">GitHub - badlogic/pi-mono: AI agent toolkit: coding agent CLI ...</a></li>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#software development`, `#productivity`, `#technical debt`

---

<a id="item-10"></a>
## [Study shows paternal age increases genetic disease risk more than previously thought](https://t.me/zaihuapd/40521) ⭐️ 7.0/10

A UK study analyzing 81 sperm samples with high-precision sequencing found that male germ cells continuously accumulate mutations throughout life, with 3–5% of sperm from men over 50 carrying harmful mutations. The research identified 40 genes under positive selection in the male germline, 31 of which were newly discovered. This challenges previous assumptions about paternal age effects, with significant implications for genetic counseling and reproductive health decisions. The findings suggest older fathers may transmit more disease-causing mutations than estimated, potentially increasing risks for developmental disorders and cancer susceptibility in offspring. The study used high-precision sequencing to detect mutations and identified genes involved in various cellular pathways linked to childhood disorders. The 3–5% mutation rate in men over 50 represents a higher prevalence than earlier estimates.

telegram · zaihuapd · Mar 26, 12:47

**Background**: Germline mutations are genetic changes that can be passed to offspring, with most human mutations being paternal in origin. Positive selection in sperm refers to mutations that provide a survival advantage to sperm cells during development, even if harmful to offspring. Paternal age has long been known to correlate with mutation rates, but the extent was underestimated.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DNA_sequencing">DNA sequencing - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12611766/">Sperm sequencing reveals extensive positive selection in the male...</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.1901259116">Overlooked roles of DNA damage and maternal age in... | PNAS</a></li>

</ul>
</details>

**Tags**: `#genetics`, `#reproductive health`, `#mutations`, `#aging`, `#medical research`

---