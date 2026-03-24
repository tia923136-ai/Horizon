---
layout: default
title: "Horizon Summary: 2026-03-24 (EN)"
date: 2026-03-24
lang: en
---

> From 34 items, 16 important content pieces were selected

---

1. [LiteLLM Python package compromised in supply-chain attack](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.82.8 compromised with credential-stealing .pth file](#item-2) ⭐️ 9.0/10
3. [Ripgrep outperforms grep and other search tools in speed](#item-3) ⭐️ 8.0/10
4. [Breakthrough in Streaming Experts Enables Massive MoE Models on Consumer Hardware](#item-4) ⭐️ 8.0/10
5. [FCC bans all foreign-made routers citing security risks](#item-5) ⭐️ 8.0/10
6. [Nvidia uses massive investments to consolidate AI dominance, accused of locking in customers](#item-6) ⭐️ 8.0/10
7. [Alibaba DAMO unveils Xuantie C950 RISC-V CPU with record performance](#item-7) ⭐️ 8.0/10
8. [DarkSword exploit chain targets Safari users across multiple countries](#item-8) ⭐️ 8.0/10
9. [Google launches Gemini-powered dark web intelligence AI for security ops](#item-9) ⭐️ 8.0/10
10. [Microsoft's 'Fix' for Windows 11 Draws Criticism](#item-10) ⭐️ 7.0/10
11. [Starlette 1.0 Released with ASGI Framework Updates](#item-11) ⭐️ 7.0/10
12. [PC Gamer's Web Performance Audit Reveals Extreme Bloat](#item-12) ⭐️ 7.0/10
13. [JavaScript Sandboxing Techniques Compared](#item-13) ⭐️ 7.0/10
14. [Interactive CRDT-based Version Control Visualizer](#item-14) ⭐️ 7.0/10
15. [China's daily AI token usage surges over 1000x in two years](#item-15) ⭐️ 7.0/10
16. [EU's age verification app may block non-Google Android systems](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LiteLLM Python package compromised in supply-chain attack](https://github.com/BerriAI/litellm/issues/24512) ⭐️ 9.0/10

The LiteLLM Python package was compromised in a supply-chain attack, leading PyPI to quarantine the package and remove compromised versions 1.82.7 and 1.82.8. The attack appears to have originated from a compromised CI/CD pipeline using the Trivy security scanner. This incident highlights the growing risk of supply-chain attacks targeting open-source dependencies, which can affect thousands of downstream projects. It also underscores the need for stronger CI/CD security practices in the Python ecosystem. The package was temporarily quarantined on PyPI, blocking all downloads, but has since been restored after removing the compromised versions. Users of the proxy Docker image were not affected as versions were pinned in requirements.txt.

hackernews · theanonymousone · Mar 24, 12:36

**Background**: LiteLLM is a popular Python SDK and proxy server for interacting with various LLM APIs. PyPI's quarantine feature is a security measure to temporarily block package downloads when malware is suspected. Supply-chain attacks target software distribution channels to inject malicious code into legitimate packages.

<details><summary>References</summary>
<ul>
<li><a href="https://litellm.vercel.app/docs/">Getting Started | liteLLM</a></li>
<li><a href="https://blog.pypi.org/posts/2024-12-30-quarantine/">Project Quarantine - The Python Package Index Blog</a></li>
<li><a href="https://www.wiz.io/academy/application-security/ci-cd-security-best-practices">CI/CD Pipeline Security Best Practices: The Ultimate Guide | Wiz</a></li>

</ul>
</details>

**Discussion**: Community members expressed concerns about CI/CD security, with suggestions ranging from better sandboxing to separating package publishing from public repositories. Some linked this incident to broader TeamPCP activity, while maintainers provided ongoing updates about the situation.

**Tags**: `#security`, `#supply-chain`, `#python`, `#devops`, `#ci-cd`

---

<a id="item-2"></a>
## [LiteLLM v1.82.8 compromised with credential-stealing .pth file](https://simonwillison.net/2026/Mar/24/malicious-litellm/#atom-everything) ⭐️ 9.0/10

The LiteLLM v1.82.8 package on PyPI was compromised with a malicious litellm_init.pth file containing a base64-encoded credential stealer that executes automatically upon installation, without requiring any code import. This supply-chain attack affects a widely-used Python library, potentially exposing SSH keys, cloud credentials, and cryptocurrency wallets from developers' systems, highlighting PyPI's vulnerability to malicious uploads. The payload targeted 25+ credential types including AWS, Kubernetes, Docker, and blockchain wallets. PyPI quarantined the package within hours, limiting exposure to installations during a short window on March 24, 2026.

rss · Simon Willison · Mar 24, 15:07

**Background**: LiteLLM is a popular open-source library for unifying LLM APIs. .pth files are Python path configuration files that execute during interpreter startup. PyPI is Python's primary package repository, handling over 500,000 packages.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BerriAI/litellm/issues/24512">[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1 ...</a></li>
<li><a href="https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/">Supply Chain Attack in litellm 1.82.8 on PyPI - futuresearch.ai</a></li>

</ul>
</details>

**Tags**: `#security`, `#python`, `#pypi`, `#supply-chain`, `#vulnerability`

---

<a id="item-3"></a>
## [Ripgrep outperforms grep and other search tools in speed](https://burntsushi.net/ripgrep/) ⭐️ 8.0/10

In 2016, ripgrep (rg) was demonstrated to be significantly faster than grep, ag, git grep, ucg, pt, and sift through detailed technical comparisons and optimizations. The analysis highlighted specific performance advantages like SIMD usage and threading. This matters because faster search tools improve developer productivity, especially in large codebases. Ripgrep's optimizations set a new standard for text search performance, influencing subsequent tools and workflows. Ripgrep achieves speed through Rust's performance, SIMD optimizations, and parallel processing. It also intelligently handles ignore rules and repository-scale searches more efficiently than competitors.

hackernews · jxmorris12 · Mar 24, 06:31

**Background**: Grep is a classic Unix command-line tool for searching plain-text data sets. Ripgrep is a modern alternative written in Rust, designed to be faster and more user-friendly while maintaining compatibility with grep's core functionality.

<details><summary>References</summary>
<ul>
<li><a href="https://burntsushi.net/ripgrep/">ripgrep is faster than { grep , ag, git grep , ucg, pt, sift} - Andrew...</a></li>
<li><a href="https://www.codeant.ai/blogs/ripgrep-vs-grep-performance">Ripgrep vs Grep Performance : Why rg Is 10x Faster for Modern...</a></li>

</ul>
</details>

**Discussion**: The community praises the post as an exemplary technical deep dive, with developers adopting ripgrep's optimizations in their own tools. Notably, ripgrep's performance advantages hold even on older hardware like a 300MHz Octane system.

**Tags**: `#ripgrep`, `#performance`, `#search-tools`, `#optimization`, `#systems-programming`

---

<a id="item-4"></a>
## [Breakthrough in Streaming Experts Enables Massive MoE Models on Consumer Hardware](https://simonwillison.net/2026/Mar/24/streaming-experts/#atom-everything) ⭐️ 8.0/10

Researchers have demonstrated running trillion-parameter Mixture-of-Experts models like Kimi K2.5 on consumer devices (96GB RAM M2 Max MacBook Pro) and even an iPhone (0.6 tokens/sec) by streaming expert weights from storage instead of loading full models into memory. This breakthrough dramatically lowers the hardware barrier for running state-of-the-art AI models, enabling complex LLM applications on edge devices and democratizing access to cutting-edge AI capabilities. The Qwen3.5-397B-A17B model (397B total params, 17B active) now runs on iPhones via flash-moe iOS implementation, while Kimi K2.5 (1T params, 32B active) operates on MacBooks - both leveraging Apple's NVMe storage bandwidth for weight streaming.

rss · Simon Willison · Mar 24, 05:09

**Background**: Mixture-of-Experts (MoE) models partition neural networks into specialized sub-networks ('experts') that activate conditionally, allowing massive parameter counts with limited computational overhead. Traditional implementations require loading all experts into memory, whereas streaming experts dynamically fetch weights from storage per token.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.tweaktown.com/news/110610/the-iphone-17-pro-can-run-a-400b-parameter-large-language-model-on-device-by-streaming-weights-from-the-ssd/index.html">The iPhone 17 Pro can run a 400B parameter Large Language Model on-device by streaming weights from the SSD</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.5-397B-A17B">Qwen/Qwen3.5-397B-A17B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Developers are actively sharing optimization techniques on Twitter and GitHub, with notable progress in autoresearch loops. The iOS implementation's 0.6 token/sec speed sparks discussions about practical usability versus technical feasibility.

**Tags**: `#LLM`, `#Mixture-of-Experts`, `#Edge AI`, `#Model Optimization`, `#Hardware Efficiency`

---

<a id="item-5"></a>
## [FCC bans all foreign-made routers citing security risks](https://www.bloomberg.com/news/articles/2026-03-23/fcc-bans-all-foreign-made-routers-citing-security-risks?embedded-checkout=true) ⭐️ 8.0/10

The FCC has officially banned all newly manufactured foreign-made consumer routers from entering the US market due to cybersecurity and supply chain concerns, adding them to the 'Covered List' of regulated entities. Existing models already approved and in use are exempt from the ban. This move could significantly disrupt global tech supply chains and impact international trade, while also setting a precedent for stricter cybersecurity regulations on consumer networking equipment. It reflects growing concerns about foreign-made devices potentially compromising national security through vulnerabilities or backdoors. The ban applies only to new models seeking certification - existing approved routers can continue to be imported and sold. Manufacturers can apply for exemptions through the Department of Defense and other agencies.

telegram · zaihuapd · Mar 24, 01:17

**Background**: The FCC (Federal Communications Commission) is an independent US government agency responsible for regulating communications by radio, television, wire, satellite, and cable. Consumer routers have long been criticized for security vulnerabilities due to cost-cutting measures by manufacturers, including lack of firmware updates and inadequate security features.

<details><summary>References</summary>
<ul>
<li><a href="https://zh.wikipedia.org/zh-cn/联邦通信委员会">联邦通信委员会 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.secrss.com/articles/1373">研究：消费级路由器固件木马分析及防护建议 - 安全内参 | 决策者的网络安全知识库</a></li>
<li><a href="https://www.boringcompliance.com/post/untitled-144">美国FCC更新Covered List 将所有外国生产路由器列入国家安全风险清单</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#regulations`, `#networking`, `#trade-policy`, `#FCC`

---

<a id="item-6"></a>
## [Nvidia uses massive investments to consolidate AI dominance, accused of locking in customers](https://www.wsj.com/tech/nvidia-ai-market-competition-9db60e4c) ⭐️ 8.0/10

Nvidia has invested billions in AI startups like OpenAI, CoreWeave, and Reflection since 2022, acting as both supplier and investor to lock customers into its ecosystem. The company also faces antitrust scrutiny for tactics like its $20 billion deal with chip startup Groq, which included acquiring its core team. Nvidia's strategy could stifle competition in the AI industry by making it difficult for customers to switch to competitors like AMD. The company's financial dominance and aggressive tactics have drawn regulatory attention, potentially impacting the future of AI innovation and market fairness. CoreWeave specializes in GPU cloud infrastructure for AI, while Reflection focuses on autonomous coding agents. Nvidia's $20 billion deal with Groq included licensing its technology and acquiring key personnel, raising antitrust concerns.

telegram · zaihuapd · Mar 24, 03:02

**Background**: Nvidia has become a dominant force in AI through its GPUs, which are essential for training and running AI models. Startups like CoreWeave and Reflection rely on Nvidia's hardware, making them vulnerable to its financial influence. Groq is known for its AI accelerator chips that compete with Nvidia's offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave - Wikipedia</a></li>
<li><a href="https://medium.com/@fahey_james/what-is-reflection-ai-fa646df3b954">What is Reflection AI? | by James Fahey | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Groq">Groq - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Nvidia`, `#Antitrust`, `#Investment`, `#Market Competition`

---

<a id="item-7"></a>
## [Alibaba DAMO unveils Xuantie C950 RISC-V CPU with record performance](https://mp.weixin.qq.com/s/TTnqm8qm3Dxshj_0bxwtkw) ⭐️ 8.0/10

Alibaba DAMO Academy announced its flagship Xuantie C950 RISC-V CPU on March 24, 2026, claiming a record-breaking Specint2006 single-core score of over 70 points. The chip features native support for running billion-parameter AI models like Qwen3 and DeepSeek V3 through its integrated AI acceleration engine. This represents a major milestone for RISC-V adoption in high-performance computing, potentially disrupting ARM and x86 dominance in cloud/AI applications. The native AI model support positions it as a strong contender for next-generation AI infrastructure in China's tech ecosystem. The C950 targets cloud computing, generative AI, robotics and edge computing, with performance currently leading public RISC-V implementations. However, detailed architectural specifications and third-party benchmark verification are not yet available.

telegram · zaihuapd · Mar 24, 06:01

**Background**: RISC-V is an open-standard instruction set architecture gaining traction as an alternative to proprietary ARM and x86 architectures. Specint2006 is a standardized benchmark for measuring integer processing performance. Qwen3 and DeepSeek V3 are open-weight Chinese AI models comparable to GPT-4 in scale, recently made available on AWS Bedrock.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPECint">SPECint - Wikipedia</a></li>
<li><a href="https://www.aboutamazon.com/news/aws/alibaba-qwen3-deepseek-v3-amazon-bedrock">Qwen3 and DeepSeek-V3.1 models now available fully ...</a></li>

</ul>
</details>

**Tags**: `#RISC-V`, `#AI-Hardware`, `#Cloud-Computing`, `#Edge-Computing`, `#Semiconductors`

---

<a id="item-8"></a>
## [DarkSword exploit chain targets Safari users across multiple countries](https://t.me/zaihuapd/40482) ⭐️ 8.0/10

A sophisticated exploit chain called DarkSword has been actively used since November 2025 to infect iPhones through Safari, targeting users in Saudi Arabia, Turkey, Malaysia, and Ukraine. The attack chain combines six vulnerabilities to deliver payloads like GHOSTBLADE, affecting iOS versions 18.4 through 18.7 before being patched in iOS 26.3. This disclosure reveals a widespread, multi-stage attack that could compromise iPhones simply by visiting a malicious website, demonstrating the evolving sophistication of mobile threats. The international targeting and payload delivery show how exploit chains are being weaponized for real-world attacks across borders. One critical vulnerability in the chain (CVE-2025-43529) was a WebKit use-after-free flaw patched earlier in iOS 18.7.3. The exploit chain's modular design allowed different attackers to adapt it for various purposes, with Google tracking multiple distinct users of the technique.

telegram · zaihuapd · Mar 24, 11:45

**Background**: DarkSword represents an advanced iOS exploit chain that combines multiple vulnerabilities to bypass security protections. Such chains typically start with browser or rendering engine flaws (like WebKit in Safari), then escalate privileges through subsequent exploits. GHOSTBLADE appears to be a custom payload name rather than the Elder Scrolls reference found in search results.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain">The Proliferation of DarkSword : iOS Exploit Chain Adopted by...</a></li>
<li><a href="https://www.malwarebytes.com/blog/mobile/2026/03/a-darksword-hangs-over-unpatched-iphones">A DarkSword hangs over unpatched iPhones | Malwarebytes</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-43529">NVD - CVE-2025-43529</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#ios`, `#safari`, `#zero-day`, `#vulnerability`

---

<a id="item-9"></a>
## [Google launches Gemini-powered dark web intelligence AI for security ops](https://www.theregister.com/2026/03/23/google_dark_web_ai/) ⭐️ 8.0/10

Google has released a public preview of its Gemini-powered dark web intelligence service integrated with Google Threat Intelligence, analyzing 8-10 million daily dark web posts to identify organizational risks with 98% accuracy in internal tests. This represents a major advancement in proactive threat detection as it automates dark web monitoring at unprecedented scale, potentially disrupting initial access broker markets and preventing data breaches before they occur. The service first builds organizational profiles for clients, then specifically detects initial access broker activities, data leaks and insider threats from dark web content. It currently focuses on English-language forums but may expand to other languages.

telegram · zaihuapd · Mar 24, 13:15

**Background**: Initial Access Brokers (IABs) are cybercriminals who sell compromised network access to ransomware groups. The dark web hosts underground markets where such access and stolen data are traded. Google Threat Intelligence is a security platform that aggregates threat data from Google's infrastructure and VirusTotal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/2026/03/23/google_dark_web_ai/">Google unleashes Gemini AI agents on the dark web • The Register</a></li>
<li><a href="https://teamwin.in/google-says-gemini-ai-agents-are-crawling-the-dark-web-posts-to-detect-threats/">Google Says Gemini AI Agents are Crawling the Dark Web Posts to...</a></li>
<li><a href="https://cloud.google.com/security/products/threat-intelligence">Google Threat Intelligence - know who's targeting you</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#threat-intelligence`, `#dark-web`, `#Google`

---

<a id="item-10"></a>
## [Microsoft's 'Fix' for Windows 11 Draws Criticism](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/) ⭐️ 7.0/10

Microsoft's approach to addressing Windows 11 issues has been criticized as 'gaslighting' by users, with complaints about forced updates and intrusive features like Microsoft Start news that re-enables itself after being disabled. This highlights growing frustration with Microsoft's user-hostile practices in Windows 11, which could erode trust and push users towards alternative operating systems if not addressed properly. Specific complaints include Microsoft Start news displaying unwanted content, forced updates, and comparisons to Apple's similarly intrusive practices with macOS updates and iCloud promotions.

hackernews · h0ek · Mar 24, 09:36

**Background**: Windows 11 has faced criticism since its launch for its user interface changes, system requirements, and various built-in advertisements. Microsoft has a history of pushing unwanted features, dating back to the Internet Explorer-Netscape wars in the 1990s. The company's dominant market position in government and enterprise sectors has historically shielded it from consequences of poor user experience decisions.

**Discussion**: Comments reveal widespread frustration with Microsoft's practices, with users comparing them to domestic violence (though some found this comparison inappropriate), noting historical patterns of user abuse, and drawing parallels with Apple's increasingly intrusive practices. Some suggest the only solution is government organizations abandoning Microsoft products.

**Tags**: `#Microsoft`, `#Windows 11`, `#User Experience`, `#Tech Criticism`, `#Software Ethics`

---

<a id="item-11"></a>
## [Starlette 1.0 Released with ASGI Framework Updates](https://simonwillison.net/2026/Mar/22/starlette/#atom-everything) ⭐️ 7.0/10

Starlette 1.0, the foundational Python ASGI framework for FastAPI, has been officially released after eight years of development, introducing breaking changes including a new lifespan mechanism for startup/shutdown events. This release marks production-ready stability for a framework that powers FastAPI (used by 10M+ daily downloads) and enables easier LLM-assisted development, though compatibility breaks may affect existing AI-generated code. The lifespan system replaces on_startup/on_shutdown with async context managers, while maintaining optional dependencies like httpx for testing and Jinja2 for templating. The project has transferred to Marcelo Trylesinski's GitHub for better maintenance.

rss · Simon Willison · Mar 22, 23:57

**Background**: Starlette is a lightweight ASGI framework designed for async web services, offering WebSocket support and background tasks. It serves as the foundation for FastAPI but with lower-level control. ASGI (Asynchronous Server Gateway Interface) is Python's standard for async web servers and applications.

<details><summary>References</summary>
<ul>
<li><a href="https://starlette.dev/">Introduction - Starlette</a></li>
<li><a href="https://github.com/Kludex/starlette">GitHub - Kludex/starlette: The little ASGI framework that ...</a></li>
<li><a href="https://pypi.org/project/starlette/">starlette · PyPI Starlette: A Modern Python ASGI Framework - CodeRivers Python - Starlette - GeeksforGeeks Starlette 1.0.0: Eight Years on Zero-Ver and Finally a Stable ... Starlette</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Web Frameworks`, `#ASGI`, `#Starlette`, `#FastAPI`

---

<a id="item-12"></a>
## [PC Gamer's Web Performance Audit Reveals Extreme Bloat](https://simonwillison.net/2026/Mar/22/pcgamer-audit/#atom-everything) ⭐️ 7.0/10

An audit of PC Gamer's website revealed extreme performance issues, with a single article consuming 37MB due to auto-playing video ads and inefficient resource loading. The analysis was conducted using Claude Code and the Rodney CLI tool to investigate the page structure and loading behavior. This highlights the growing problem of web bloat affecting user experience, particularly from auto-playing ads, which is relevant for web developers and performance engineers optimizing modern websites. The novel approach using AI-assisted tools like Claude Code and Rodney demonstrates new methods for performance auditing. The audit found the page continued downloading hundreds more megabytes after initial load due to auto-playing video ads. Rodney was used to analyze the page's accessibility tree structure before crafting selectors, following its recommended best practices.

rss · Simon Willison · Mar 22, 22:49

**Background**: Rodney is a CLI tool for interacting with and analyzing web pages, recently developed by Simon Willison. Claude Code is Anthropic's cloud-based coding tool that can execute tasks, write code, and run tests through a web interface. Web bloat refers to the excessive size and complexity of modern web pages, often due to ads, trackers, and unnecessary JavaScript.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/rodney">GitHub - simonw/rodney: CLI tool for interacting with the web</a></li>
<li><a href="https://code.claude.com/docs/en/claude-code-on-the-web">Claude Code on the web - Claude Code Docs</a></li>
<li><a href="https://simonwillison.net/2026/Feb/10/showboat-and-rodney/">Introducing Showboat and Rodney, so agents can demo what they ...</a></li>

</ul>
</details>

**Tags**: `#web-performance`, `#web-bloat`, `#rodney`, `#claude-code`, `#audit`

---

<a id="item-13"></a>
## [JavaScript Sandboxing Techniques Compared](https://simonwillison.net/2026/Mar/22/javascript-sandboxing-research/#atom-everything) ⭐️ 7.0/10

Simon Willison published a detailed comparison of JavaScript sandboxing techniques, including isolated-vm, vm2, QuickJS variants, ShadowRealm, and Deno Workers, expanding on Aaron Harper's initial exploration of Node.js worker threads. This research provides valuable insights for developers needing to securely run untrusted JavaScript code, addressing a critical security challenge in web applications and server-side JavaScript environments. The comparison highlights tradeoffs between isolation and performance, with native V8 isolates (isolated-vm) offering speed while WebAssembly-based solutions (QuickJS) provide stronger isolation but with performance penalties and feature limitations.

rss · Simon Willison · Mar 22, 19:53

**Background**: JavaScript sandboxing is a security mechanism to isolate and safely execute untrusted code. Common approaches include V8 isolates, WebAssembly runtimes, and language-level proposals like ShadowRealm. Node.js and Deno offer different built-in sandboxing capabilities through worker threads and permission models.

<details><summary>References</summary>
<ul>
<li><a href="https://cybercorsairs.com/sandboxing-javascript-a-side-by-side-look-at-your-options/">JavaScript Sandboxing: Running Untrusted Code Safely</a></li>
<li><a href="https://letsdatascience.com/news/javascript-sandboxing-research-compares-nodejs-options-6f16be0b">JavaScript Sandboxing Research Compares Node.js Options</a></li>

</ul>
</details>

**Tags**: `#javascript`, `#sandboxing`, `#security`, `#nodejs`, `#deno`

---

<a id="item-14"></a>
## [Interactive CRDT-based Version Control Visualizer](https://simonwillison.net/2026/Mar/22/manyana/#atom-everything) ⭐️ 7.0/10

Simon Willison has created an interactive visualization tool for Bram Cohen's CRDT-based version control system called Manyana, using Pyodide to run Python in the browser and Claude AI to generate explanations. This provides a tangible way to understand CRDTs in version control systems, which could revolutionize collaborative editing by enabling conflict-free merging without centralized coordination. The visualization is based on Cohen's 470-line Python implementation, with the UI built using Pyodide which allows Python to run directly in web browsers through WebAssembly.

rss · Simon Willison · Mar 22, 18:57

**Background**: CRDTs (Conflict-Free Replicated Data Types) are data structures that automatically resolve conflicts in distributed systems. Pyodide is a Python distribution that runs in the browser via WebAssembly, enabling interactive Python applications without server-side processing. Bram Cohen is the creator of BitTorrent and has been working on next-generation version control systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/r-language/what-is-crdt-in-distributed-systems/">What is CRDT in Distributed Systems? - GeeksforGeeks</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 0.29.3</a></li>

</ul>
</details>

**Tags**: `#vcs`, `#pyodide`, `#crdt`, `#version-control`, `#python`

---

<a id="item-15"></a>
## [China's daily AI token usage surges over 1000x in two years](http://paper.people.com.cn/rmrb/pc/content/202603/24/content_30147015.html) ⭐️ 7.0/10

China's National Data Bureau reported that daily token usage in AI systems exceeded 140 trillion in March 2025, up from 100 billion in early 2024 - representing over 1000x growth in two years. This explosive growth indicates rapid commercialization of AI technologies in China and the formation of a new value system around tokenized data processing, which is becoming a key pathway for AI industry monetization. Tokens are the smallest units processed by AI models (roughly 1000 tokens ≈ 750 English words), with measurable, pricable and tradable characteristics that enable new economic models for AI services.

telegram · zaihuapd · Mar 24, 07:22

**Background**: Tokenization breaks down text/images into numerical representations that AI models can process. China's data element marketization reforms since 2020 have accelerated the development of token-based AI ecosystems. The growth aligns with national policies promoting data as a production factor.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sentisight.ai/tokens-explained-new-currency-of-generative-ai/">Tokens Explained: The Currency of Generative AI</a></li>
<li><a href="https://ideas.repec.org/a/eee/finana/v104y2025ipas1057521925004168.html">Data element marketization and corporate investment efficiency...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Tokenization`, `#China`, `#Data Economy`, `#Commercialization`

---

<a id="item-16"></a>
## [EU's age verification app may block non-Google Android systems](https://t.me/zaihuapd/40484) ⭐️ 7.0/10

The EU is developing an open-source age verification app that requires devices to pass Google's Play Integrity verification and be downloaded from the Play Store with a Google account, effectively blocking non-Google-authorized Android systems like GrapheneOS. This move could deepen reliance on US tech giants like Google, contradicting EU digital sovereignty goals, while raising privacy concerns as it excludes privacy-focused Android forks. The app will use Google's Play Integrity API (formerly SafetyNet) to verify device authenticity, requiring Google Play Services. This excludes security-focused Android variants that deliberately avoid Google services.

telegram · zaihuapd · Mar 24, 12:22

**Background**: Play Integrity API is Google's system to verify app authenticity and device integrity. GrapheneOS is a privacy-focused Android fork that removes Google services by design. The EU has been promoting digital sovereignty initiatives to reduce reliance on non-EU tech companies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Play_Integrity_API">Play Integrity API - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS: the private and secure mobile OS</a></li>

</ul>
</details>

**Discussion**: Developers and privacy advocates strongly oppose the move on GitHub, arguing it contradicts open-source principles and increases dependence on Google while excluding privacy-conscious users.

**Tags**: `#EU Regulation`, `#Android`, `#Digital Sovereignty`, `#Privacy`, `#Open Source`

---