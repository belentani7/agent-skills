# Agent Skills

Colección curada de **311 skills** para agentes CLI (Claude Code, OpenCode, Codex, Cline, Qwen Code, Gemini CLI, ZCode).

> Orden de idiomas del ecosistema: **PT > ES > EN > CA**.

## Instalación

### Windows (PowerShell) — crea junctions en todos los CLIs

```powershell
git clone https://github.com/belentani7/agent-skills.git
cd agent-skills
.\install.ps1
```

### Linux / macOS

```bash
git clone https://github.com/belentani7/agent-skills.git
cd agent-skills
./install.sh
```

## Estructura

```
agent-skills/
  registry.json     # índice maestro (id, descripción, versión, ruta)
  skills/<id>/SKILL.md
  install.ps1       # instala en todos los CLIs (Windows)
  install.sh        # instala en todos los CLIs (Unix)
```

## Skills (311)

| # | ID | Descripción |
|---|----|-------------|
| 1 | `academy-guide` | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and  |
| 2 | `access` | Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks to pair, approve someone, check who's allowed, or |
| 3 | `advanced-frontend-skill` | Create award-winning, cinematic frontend interfaces that feel ALIVE. Combines 10+ years of creative frontend experience with technical excellence. Specializes i |
| 4 | `agent-development` | This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent ex |
| 5 | `agents-sdk` | Build, debug, or review Cloudflare Agents SDK applications using the agents package. |
| 6 | `agile-kanban-solo` | Organizacion estructural para desarrollo solitario hiper-veloz. |
| 7 | `aider` | Delegate coding to Aider (code editor AI pair programming). Optimized for token efficiency. |
| 8 | `aider-cli-mastery` | Edicion autonoma de codigo mediante agentes de terminal con modo caveman. |
| 9 | `aider-opencode-integration` | Configuracion de Aider y OpenCode para edicion autonoma de codigo. |
| 10 | `airunway-aks-setup` | Set up AI Runway on AKS — from bare cluster to running model. Covers cluster verification, controller install, GPU assessment, provider setup, and first deploym |
| 11 | `algorithmic-art` | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generati |
| 12 | `animated-diagram` | Build animated technical diagrams (flowcharts, decision trees, pipelines) as Remotion + React videos. You describe the diagram in plain English, Claude writes M |
| 13 | `anomaly-detection` | Identificacion de patrones atipicos de usuarios para deteccion de fraude. |
| 14 | `anti-malware` | Defensive malware detection and analysis skill. Use when user needs to detect, analyze, or defend against malicious software - including static/dynamic analysis |
| 15 | `antivirus` | Antivirus/EDR/XDR engineering and signature development skill. Use when user needs to build, configure, or optimize antivirus/endpoint protection solutions - in |
| 16 | `appeals-process-design` | Estructuracion de flujos logicos para arbitraje y revision manual. |
| 17 | `appinsights-instrumentation` | Guidance for instrumenting webapps with Azure Application Insights. Provides telemetry patterns, SDK setup, and configuration references. WHEN: how to instrumen |
| 18 | `asd-ste100` | Rewrites ambiguous English into ASD-STE100 style — one meaning per word, active voice, simple tense, short sentences. Use when agent output is hard to parse; tr |
| 19 | `automated-flagging-systems` | Diseno de disparadores de alerta preventivos. |
| 20 | `awesome-ai-ecosystem-2026` | Curated registry of 100 essential AI agent repositories (2026) organized by category with asset types |
| 21 | `azure-ai` | Use for Azure AI: Search, Speech, OpenAI, Document Intelligence. Helps with search, vector/hybrid search, speech-to-text, text-to-speech, transcription, OCR. WH |
| 22 | `azure-aigateway` | Configure Azure API Management as an AI Gateway for AI models, MCP tools, and agents. WHEN: semantic caching, token limit, content safety, load balancing, AI mo |
| 23 | `azure-app-onboard` | End-to-end orchestrator: from a business idea, app idea, or existing app to running Azure deployment with cost estimates and pre-deploy approval. Analyzes your  |
| 24 | `azure-app-onboard-prereq` | Assess whether source code is ready to deploy to Azure — the check BEFORE infrastructure work. Evaluates build health, app completeness, dependencies and local  |
| 25 | `azure-cloud-migrate` | Assess and migrate cross-cloud workloads to Azure with reports and code conversion. Supports Lambda→Functions, Beanstalk/Heroku/App Engine→App Service, Fargate/ |
| 26 | `azure-compliance` | Run Azure compliance and security audits with azqr plus Key Vault expiration checks. Covers best-practice assessment, resource review, policy/compliance validat |
| 27 | `azure-compute` | Azure VM/VMSS router. WHEN: create / provision / deploy / spin-up VM, recommend VM size, compare VM pricing, VMSS, scale set, autoscale, burstable, lightweight  |
| 28 | `azure-cost` | Azure cost management: query costs, forecast spending, optimize to reduce waste. WHEN: "Azure costs", "Azure bill", "cost breakdown", "how much am I spending",  |
| 29 | `azure-deploy` | Execute Azure deployments for ALREADY-PREPARED applications that have existing .azure/deployment-plan.md and infrastructure files. DO NOT use this skill when th |
| 30 | `azure-diagnostics` | Debug Azure production issues on Azure using AppLens, Azure Monitor, resource health, and safe triage. WHEN: debug production issues, troubleshoot app service,  |
| 31 | `azure-enterprise-infra-planner` | Architect and provision enterprise Azure infrastructure from workload descriptions. For cloud architects and platform engineers planning networking, identity, s |
| 32 | `azure-kubernetes` | Plan, create, and configure production-ready Azure Kubernetes Service (AKS) clusters. Covers Day-0 checklist, SKU selection (Automatic vs Standard), networking  |
| 33 | `azure-kusto` | Query and analyze data in Azure Data Explorer (Kusto/ADX) using KQL for log analytics, telemetry, and time series analysis. WHEN: KQL queries, Kusto database qu |
| 34 | `azure-messaging` | Troubleshoot and resolve issues with Azure Messaging SDKs for Event Hubs and Service Bus. Covers connection failures, authentication errors, message processing  |
| 35 | `azure-prepare` | Prepare azd-based Azure projects for deployment: generates azure.yaml, infrastructure (Bicep/Terraform), and Dockerfiles for the Azure Developer CLI (azd) workf |
| 36 | `azure-quotas` | Check/manage Azure quotas and usage across providers. For deployment planning, capacity validation, region selection. WHEN: "check quotas", "service limits", "c |
| 37 | `azure-reliability` | Assess and improve the reliability posture of PaaS Applications (Azure Functions and Azure App Service). Scans deployed resources for zone redundancy, ZRS stora |
| 38 | `azure-resource-lookup` | List, find, and show Azure resources across subscriptions or resource groups. Handles prompts like "list the websites in my subscription", "list my web apps", " |
| 39 | `azure-resource-visualizer` | Analyze Azure resource groups and generate detailed Mermaid architecture diagrams showing the relationships between individual resources. WHEN: create architect |
| 40 | `azure-storage` | Azure Storage Services including Blob Storage, File Shares, Queue Storage, Table Storage, and Data Lake. Answers questions about storage access tiers (hot, cool |
| 41 | `azure-upgrade` | Assess and upgrade Azure workloads between plans, tiers, or SKUs, or modernize Azure SDK dependencies in source code. WHEN: upgrade Consumption to Flex Consumpt |
| 42 | `azure-validate` | Pre-deployment validation for Azure readiness. Run deep checks on configuration, infrastructure (Bicep or Terraform), RBAC role assignments, managed identity pe |
| 43 | `backend-expert` | Expert backend developer specializing in Node.js, Python, Go, Rust APIs, microservices, databases (PostgreSQL, MongoDB, Redis), authentication, and cloud infras |
| 44 | `bandwidth-optimization` | Reduccion extrema del peso final de aplicaciones empaquetadas. |
| 45 | `batch-api-optimization` | Uso de Batch API para trabajo diferido con descuento del 50%. |
| 46 | `belentani-premium-pdf` | Genera CVs y documentos PDF premium con diseño cognitivo de alto impacto. Basado en la estructura cognitiva de Ausubel + principios de dopamine design. Patrones |
| 47 | `bias-mitigation` | Monitoreo de impactos desproporcionados o respuestas sesgadas. |
| 48 | `brainstorming` | You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirem |
| 49 | `brand-guidelines` | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand color |
| 50 | `build-mcp-app` | This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP |
| 51 | `build-mcp-server` | This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Cl |
| 52 | `build-mcpb` | This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP",  |
| 53 | `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, d |
| 54 | `cardputer-buddy` | Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants |
| 55 | `cavecrew` | Decision guide for delegating to caveman-style subagents. Tells the main thread WHEN to spawn `cavecrew-investigator` (locate code), `cavecrew-builder` (1-2 fil |
| 56 | `caveman` | Ultra-compressed communication mode. Cuts output tokens 65% (measured) by speaking like caveman while keeping full technical accuracy. Supports intensity levels |
| 57 | `caveman-commit` | Write a Conventional Commits message compressed to intent only. Use for "write a commit", "commit message", /commit or /caveman-commit. |
| 58 | `caveman-compress` | Compress natural language memory files (CLAUDE.md, todos, preferences) into caveman format to save input tokens. Preserves all technical substance, code, URLs,  |
| 59 | `caveman-discover` | Find and label every LLM workflow in the repository so Caveman Cloud groups spend by workflow instead of one bucket. Use for "discover workflows" or breaking LL |
| 60 | `caveman-evidence-review` | Read-only review of Caveman Cloud evidence: cost, Cave Score, workflows, traces, latency, errors, routing, savings. Use when asked what Caveman found or where L |
| 61 | `caveman-explore` | Read-only repository explorer for cold-start orientation, broad cross-file localization, or when a direct search failed. Skip it when the exact file or symbol i |
| 62 | `caveman-help` | Quick-reference card for caveman modes, skills and commands. Trigger: /caveman-help or "caveman help". |
| 63 | `caveman-learn` | Act on a Caveman learn report - review the ranked token sinks, apply cost-lowering fixes with per-edit consent, and report what those fixes returned. Use when a |
| 64 | `caveman-manage` | Inspect Caveman Cloud's experiment lifecycle and block unsafe execution. Use when asked to start, approve, cancel, promote or roll back a Caveman experiment. |
| 65 | `caveman-optimize` | Turn a Caveman optimization observation into an operator-chosen candidate with a paired baseline evaluation. Use when asked to inspect or evaluate a Caveman opt |
| 66 | `caveman-review` | Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff". |
| 67 | `caveman-setup` | Wire a repository through the Caveman Cloud gateway so every LLM request is measured, with no behavior change. Use for "set up caveman" or adding LLM spend obse |
| 68 | `caveman-stats` | Show recorded output and cache-read token usage and mode attribution for the current Claude Code session, or locate the host's native usage report. Trigger: /ca |
| 69 | `changelog-generator` | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear,  |
| 70 | `claude-api` | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — |
| 71 | `claude-automation-recommender` | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wa |
| 72 | `claude-code-integration` | Integracion de Claude Code como agente de desarrollo. |
| 73 | `claude-md-improver` | Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix CLAUDE.md files. Scans for all CLAUDE.md files, e |
| 74 | `claude-security` | The Claude Security menu — pick a job: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or |
| 75 | `cloudflare` | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when |
| 76 | `cloudflare-email-service` | Implement or troubleshoot Cloudflare Email Sending and Email Routing integrations and their delivery configuration. |
| 77 | `cloudflare-one` | Design, configure, troubleshoot, or review Cloudflare One Zero Trust and SASE deployments. Use cloudflare-one-migrations for migration planning from other vendo |
| 78 | `cloudflare-one-migrations` | Assess and plan migrations from existing VPN, SWG, or SASE platforms to Cloudflare One, including policy mapping, parity gaps, and rollout. |
| 79 | `code-research` | Research open-source repositories to understand how something is built or works. |
| 80 | `code-review-checklist` | Revisar cambios de código (PR, merge request o diff local) con enfoque en corrección, regresiones, tests, cambios de API arriesgados y mantenibilidad. Usar cuan |
| 81 | `comfyui` | ComfyUI - Node-based AI workflow engine for image generation, voice synthesis, and video processing. |
| 82 | `command-development` | This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command fr |
| 83 | `community-guidelines` | Ajuste de parametros globales a ecosistemas focalizados. |
| 84 | `competitive-ads-extractor` | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. |
| 85 | `composition-patterns` | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reus |
| 86 | `configure` | Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do  |
| 87 | `connect` | Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ servic |
| 88 | `connect-apps` | Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in e |
| 89 | `content-research-writer` | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on ea |
| 90 | `context-window-scaling` | Gestion de memoria para lectura de repositorios completos y tracks de audio. |
| 91 | `continuous-integration` | Automatizaciones de integracion y compilacion desde terminal nativa. |
| 92 | `conventional-commits` | Escribir mensajes de commit claros y convencionales. Usar cuando el usuario pida crear un commit, escribir un mensaje de commit o estandarizar commits de un pro |
| 93 | `create-voltagent` | Skill for creating AI agent projects using the VoltAgent framework. Guide for CLI setup and manual bootstrapping. |
| 94 | `creative-web-algorithm` | Build or refactor premium creative-web experiences from an existing codebase using an observe-first execution algorithm. Use for HTML/CSS/JS/WebGL landing pages |
| 95 | `crisis-response-protocol` | Rutinas de contingencia y contencion ante incidentes graves. |
| 96 | `cross-platform-testing` | Verificacion rigorosa de consistencia tecnica del codigo local. |
| 97 | `database-schema-prisma` | Modelado y vinculacion relacional pura a traves de ORMs. |
| 98 | `debate-brainstorm` | Run two independent subagents through a structured debate on the same prompt: independent answers, cross-critique, revision, and a synthesized unified response. |
| 99 | `debugging-wizard` | Parses error messages, traces execution flow through stack traces, correlates log entries to identify failure points, and applies systematic hypothesis-driven m |
| 100 | `dependency-management` | Instalacion desatendida y empaquetado de repositorios NPM/Winget. |
| 101 | `deploy-to-vercel` | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", |
| 102 | `design-system` | Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, |
| 103 | `design-taste` | Elite frontend design taste for building, reviewing, and polishing web interfaces. Use whenever the user wants to design, redesign, shape, critique, audit, poli |
| 104 | `developer-growth-analysis` | Analyzes your recent Claude Code chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from |
| 105 | `discernment-nudge` | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, o |
| 106 | `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| 107 | `doc-coauthoring` | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, |
| 108 | `docker-container-ops` | Implementacion en contenedores para microservicios y bases de datos. |
| 109 | `docx` | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any  |
| 110 | `domain-name-brainstormer` | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming an |
| 111 | `durable-objects` | Build, debug, or review Cloudflare Durable Objects code for persistent state and coordination. |
| 112 | `easy-diffusion` | EasyDiffusion - 1-click AI image generator with browser UI. Easy Stable Diffusion setup for beginners. |
| 113 | `elite-legal-pdf` | Generador de documentos jurídicos PDF premium estilo firma de derechos humanos de élite (Olivia Pope / human rights law firm). Convierte textos, markdown y docu |
| 114 | `entra-agent-id` | Provision Microsoft Entra Agent Identity Blueprints, BlueprintPrincipals, and per-instance Agent Identities via Microsoft Graph, and configure OAuth 2.0 token e |
| 115 | `entra-app-registration` | Guides Microsoft Entra ID app registration, OAuth 2.0 authentication, and MSAL integration. USE FOR: create app registration, register Azure AD app, configure O |
| 116 | `escalation-management` | Rutas ordenadas de derivacion de quejas formales. |
| 117 | `excalidraw` | Create Excalidraw diagrams as JSON files for flowcharts, user journeys, system architectures, wireframes, and visual documentation. Use when the user asks to cr |
| 118 | `excalidraw-diagram` | Create Excalidraw diagram JSON files that make visual arguments. Use when the user wants to visualize workflows, architectures, or concepts. |
| 119 | `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| 120 | `explain-to-me` | Explains difficult concepts and unfamiliar code with adaptive, multilingual clarity. Use for “explain to me,” “help me understand,” “how does this work,” simple |
| 121 | `explaining-with-ascii` | Explains technical systems, abstract concepts, workflows, architecture, comparisons, loops, and tradeoffs using plain language and readable ASCII diagrams. Use  |
| 122 | `explicit-cache-strategy` | Estrategia de Prompt Caching explicito para ahorro del 90% en input. |
| 123 | `explore` | Explore unfamiliar code with semantic search when you don't know which files to read. Not needed for quick lookups where grep or a known file path gets you ther |
| 124 | `fastapi-backend` | Construccion de backend FastAPI con Qwen-Agent y ruteo de modelos. |
| 125 | `feature-research` | Research existing architecture before implementing a complex feature. |
| 126 | `ffmpeg-pipeline` | Pipeline de conversion y renderizado con ffmpeg-python. |
| 127 | `file-organizer` | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating c |
| 128 | `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express int |
| 129 | `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| 130 | `fl-studio-workflow` | Organizacion de patches, plugins y ruteo avanzado en FL Studio. |
| 131 | `flux-gen` | FLUX Image Generation by Black Forest Labs - State-of-the-art open image generation and editing. |
| 132 | `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making ch |
| 133 | `frontend-design-review` | Review and create distinctive, production-grade frontend interfaces with high design quality and design system compliance. Evaluates using three pillars: fricti |
| 134 | `frontend-expert` | Expert frontend developer specializing in React, Next.js, Vue, Angular, TypeScript, Tailwind CSS, and modern UI frameworks. Creates responsive, accessible, perf |
| 135 | `fullstack-app` | Crea aplicaciones fullstack completas de cero en minutos. Backend + Frontend + Database + Auth + Deploy. Usa para crear apps reales, MVPs, SaaS, dashboards, e-c |
| 136 | `gemini-api` | Use when the user asks about using Gemini in an enterprise environment or explicitly mentions Vertex AI, Google Cloud, or Agent Platform. Guides the usage of th |
| 137 | `gemini-live-api` | Generates a Gemini LiveAPI client service class in the user's chosen programming language. Use when the user wants to build, scaffold, or integrate a client tha |
| 138 | `git-repo-cleanup` | Auditoria masiva, eliminacion de duplicados y saneamiento de ramas. |
| 139 | `glsl-shader-programming` | Efectos de post-procesado visual en el navegador con GLSL. |
| 140 | `graphify` | Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question shoul |
| 141 | `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). |
| 142 | `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue |
| 143 | `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or w |
| 144 | `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physic |
| 145 | `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with Reac |
| 146 | `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax,  |
| 147 | `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when th |
| 148 | `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, |
| 149 | `gws` | This skill should be used when the user asks to "set up gws", "install Google Workspace CLI", "connect Gmail to Claude", "manage Google Drive from terminal", "s |
| 150 | `hate-speech-filtering` | Clasificacion lexica de comportamientos toxicos. |
| 151 | `heartmula` | HeartMuLa - Open-source music foundation model family by Fudan University. Music generation with lyrics. |
| 152 | `hook-development` | This skill should be used when the user asks to "create a hook", "add a PreToolUse/PostToolUse/Stop hook", "validate tool use", "implement prompt-based hooks",  |
| 153 | `image-enhancer` | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documen |
| 154 | `indie-release-strategy` | Preparacion integral del master y metadata para ciclo de lanzamiento. |
| 155 | `internal-comms` | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever  |
| 156 | `investigate-first` | Diagnose ambiguous failures before editing. Use for unknown causes, intermittent behavior, performance regressions, or investigations needing evidence-ranked hy |
| 157 | `invoice-organizer` | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting th |
| 158 | `javascript-pro` | Writes, debugs, and refactors JavaScript code using modern ES2023+ features, async/await patterns, ESM module systems, and Node.js APIs. |
| 159 | `json-schema-design` | Estructuracion precisa de variables para memoria e intercambio de datos. |
| 160 | `karpathy-coder` | Use when writing, reviewing, or committing code to enforce Karpathy's 4 coding principles — surface assumptions before coding, keep it simple, make surgical cha |
| 161 | `kilo` | Delegate coding to Kilo CLI (features, PRs). Optimized for token efficiency. |
| 162 | `kling-ai-video` | Generacion de video con Kling 2.1 via API y pipeline de render. |
| 163 | `kling-cli` | 可灵 AI（Kling）官方 CLI 的使用技能：文生图 / 参考图生图 / 文生视频 / 图生视频。CLI 通过 MCP 服务与可灵交互： 调用 text_to_image / image_to_image / text_to_video / image_to_video（模型与参数规格由 who_am_i 动态声明 |
| 164 | `kv-cache-quantization` | Compresion de KV Cache FP16 a Int8/FP8 para duplicar contexto. |
| 165 | `langsmith-fetch` | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool |
| 166 | `launch-your-agent` | Help a technical founder build whatever they want on Claude Managed Agents — an internal worker, a piece of their product, a customer-facing agent. Find out wha |
| 167 | `lead-research-assistant` | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategie |
| 168 | `lean-build` | Build feature work with high overbuilding risk. Use for new behavior, product slices, or integrations where repository reuse, strict scope, and an explicit stop |
| 169 | `librosa-dsp-analysis` | Analisis DSP: MFCCs, chroma, tempo, espectrogramas con librosa. |
| 170 | `limpiar-basura` | Limpieza segura de archivos basura en Windows y liberacion de espacio en disco: %TEMP%, C:\Windows\Temp, cache de Delivery Optimization, cache de miniaturas, ca |
| 171 | `local-api-routing` | Creacion de endpoints TRPC y APIs locales para modularidad. |
| 172 | `local-server-hosting` | Gestion de entornos y despliegue rapido por tuneles web cerrados. |
| 173 | `local-storage-state` | Persistencia de perfiles e interacciones sin bases de datos externas. |
| 174 | `m5-onboard` | End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware,  |
| 175 | `markdown-documentation` | Diseno de guias descriptivas, ReadMe y reportes arquitectonicos. |
| 176 | `math-olympiad` | Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked  |
| 177 | `mcp-builder` | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when b |
| 178 | `mcp-integration` | This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol",  |
| 179 | `md-document` | Converts long-form markdown (specs, RFCs, reports, plans, explainers) into a single-file, lightly-interactive HTML document with sticky TOC, scrollspy, search f |
| 180 | `meeting-insights-analyzer` | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, |
| 181 | `microsoft-foundry` | Build, deploy, evaluate, optimize, fine-tune, and manage Microsoft Foundry agents, models, and resources end to end. USE FOR: foundry, azd ai agent, azd provisi |
| 182 | `midi-orchestration` | Humanizacion de la interpretacion ritmica y velocity MIDI. |
| 183 | `migration` | Implement reversible compatibility-safe transitions. Use for schema, data, API, protocol, configuration, or dependency migrations requiring rollback and preserv |
| 184 | `military-history-strategist` | Researches, structures, and writes historical military campaigns, battles, strategy, factions, and orders of battle — for worldbuilding a fictional war, designi |
| 185 | `mimo` | Code manipulation and AI-assisted development. Optimized for token efficiency. |
| 186 | `mix-buss-compression` | Unificacion dinamica de canales de mezcla con compresion. |
| 187 | `model-auto-router` | Elige automaticamente el modelo/proveedor LLM mas barato capaz de resolver la tarea, con cadena de fallback entre las APIs verificadas del usuario. Trigger: 'qu |
| 188 | `morph-migrate` | Migrate this app's LLM calls onto a Morph open model (GLM-5.2), either fully or as a scored 5% production trial. Use when the user wants to move a provider/mode |
| 189 | `multi-cli-unified` | Unificacion de CLI (opencode, qwen, claude, codex) en un solo launcher. |
| 190 | `multi-engine` | Fan-out headless agent runs across claude/gemini/grok (and other adapters) via meta-cli, then collect results into memory/raw. Use for cross-provider review/div |
| 191 | `music21-midi-gen` | Generacion de progresiones armonicas y arreglos MIDI con music21. |
| 192 | `n8n-workflow-automation` | Diseno de flujos n8n para automatizacion no-code. |
| 193 | `nextjs-developer` | Use when building Next.js 14+ applications with App Router, server components, or server actions. Invoke to configure route handlers, implement middleware, set  |
| 194 | `nextjs-on-cloudflare` | Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers, |
| 195 | `nextjs-ssr-architecture` | Creacion de sitios web hiper-optimizados con Next.js 15 App Router. |
| 196 | `nvidia-rate-limit` | Presupuesto de peticiones del backend NVIDIA NIM (DeepSeek) — máximo 40 RPM, objetivo <35 RPM y ~1000 créditos de inferencia. Aplicar SIEMPRE: batch de tool cal |
| 197 | `offline-model-fallback` | Sistemas de contingencia de ejecucion sin internet con Ollama local. |
| 198 | `ollama-orchestration` | Despliegue de modelos locales con balanceo de VRAM y monitorizacion de GPUs. |
| 199 | `omni-route-integration` | Routing inteligente de modelos: elige el LLM mas barato capaz de resolver la tarea y encadena fallbacks entre las APIs verificadas. Ver la skill `model-auto-rou |
| 200 | `open-source-contribution` | Empaquetado estetico e higienizado para publicacion libre. |
| 201 | `openart-mcp-setup` | Connect OpenArt image and video generation models to AI tools (Claude, ChatGPT, Cursor) through the Model Context Protocol. Use when installing or authenticatin |
| 202 | `opencode` | Delegate coding to OpenCode CLI (features, PR review). Optimized for token efficiency. |
| 203 | `orchestrating-swarms` | Master multi-agent orchestration using Claude Code's TeammateTool and Task system. Use when coordinating multiple agents, running parallel code reviews, creatin |
| 204 | `pdf` | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple P |
| 205 | `pdf-generator` | Generación de PDFs profesionales con apariencia premium. Crea informes, reportes, documentos formales con diseños elegantes, tablas estilizadas, y estructura cl |
| 206 | `plan-skill` | Transforms workflow to use Manus-style persistent markdown files for planning, progress tracking, and knowledge storage. Use when starting complex tasks, multi- |
| 207 | `platform-policy-design` | Redaccion y actualizacion de normas de confianza y comportamiento. |
| 208 | `playground` | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, an |
| 209 | `playwright-best-practices` | Use when writing Playwright tests, fixing flaky tests, debugging failures, implementing Page Object Model, configuring CI/CD, optimizing performance, mocking AP |
| 210 | `playwright-cli` | Automate browser interactions, test web pages and work with Playwright tests. |
| 211 | `plugin-chain-optimization` | Cadenas de procesamiento eficientes que no saturen la CPU. |
| 212 | `plugin-settings` | This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-configurable plugin", ".local.md files", "plugin state |
| 213 | `plugin-structure` | This skill should be used when the user asks to "create a plugin", "scaffold a plugin", "understand plugin structure", "organize plugin components", "set up plu |
| 214 | `powershell-automation` | Creacion de comandos de purga y scripts autoejecutables en Windows. |
| 215 | `powershell-safe` | Escribir y ejecutar scripts de PowerShell 5.1 en Windows de forma robusta. Usar cuando haya que automatizar tareas en la terminal de Windows, manejar archivos,  |
| 216 | `pptx` | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentat |
| 217 | `project-artifact` | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the works |
| 218 | `prompt-engineer` | Writes, refactors, and evaluates prompts for LLMs — generating optimized prompt templates, structured output schemas, evaluation rubrics, and test suites. Use w |
| 219 | `prompt-engineering` | Prompt Engineering Patterns workflow skill. Use this skill when the user needs Expert guide on prompt engineering patterns, best practices, and optimization tec |
| 220 | `provider-commander` | Orquestador multi-proveedor con gestion de secretos, enmascarado de logs, throttling, rotacion de llaves, circuit breaker, backoff, fallback y tracking de coste |
| 221 | `python-appservice-deploy` | Deploy Python (Flask/Django/FastAPI) code to Azure App Service Linux. WHEN: "Flask App Service", "Django App Service", "FastAPI App Service", "deploy Python to  |
| 222 | `raffle-winner-picker` | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with transparency. |
| 223 | `rag-local-vector` | Creacion de bases de datos de conocimiento locales con embedding para samples. |
| 224 | `ralph` | Set up and run Ralph Wiggum loop - autonomous AI coding with clean slate iterations, PRD-driven features, and CI quality gates. Use for long-running autonomous  |
| 225 | `react-19-optimization` | Manejo de estado y abstraccion de hooks en React 19 con Server Components. |
| 226 | `react-best-practices` | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js c |
| 227 | `react-doctor` | Use when finishing a feature, fixing a bug, before committing React code, or when the user types `/doctor`, asks to scan, triage, or clean up React diagnostics. |
| 228 | `react-expert` | Use when building React 18+ applications in .jsx or .tsx files, Next.js App Router projects, or create-react-app setups. Creates components, implements custom h |
| 229 | `react-native-skills` | React Native and Expo best practices for building performant mobile apps. Use when building React Native components, optimizing list performance, implementing a |
| 230 | `react-view-transitions` | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view tran |
| 231 | `receipts` | Generate a personal Claude Code usage & impact report ("receipts") from this machine's local session transcripts — for justifying Claude Code usage/spend to a m |
| 232 | `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical  |
| 233 | `redis-upstash-caching` | Optimizacion estatica para manejo temporal masivo de datos. |
| 234 | `repo-hygiene` | Auditar y mantener repositorios de GitHub de forma segura. Usar cuando el usuario pida limpiar, archivar, borrar, auditar o revisar su cuenta de GitHub o lista  |
| 235 | `repo-metadata-repair` | Reparacion manual y correccion del indexado de proyectos dañados. |
| 236 | `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| 237 | `rgdp-studio-compliance` | Cumplimiento RGPD/EU AI Act para estudio de produccion musical. |
| 238 | `safe-refactor` | Restructure code while preserving behavior. Use for extraction, consolidation, ownership moves, or cleanup where verification must bracket structural edits. |
| 239 | `sandbox-migrate-to-next` | Migrate Cloudflare Sandbox apps from stable @cloudflare/sandbox to @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-next for apps already on the preview. |
| 240 | `sandbox-next` | Build or maintain Cloudflare Sandbox apps on @cloudflare/sandbox@next (SDK 1.0 preview). Use sandbox-migrate-to-next when porting a stable app. |
| 241 | `sandbox-stable` | Build or maintain Cloudflare Sandbox apps on the stable @cloudflare/sandbox package. Use sandbox-next for preview apps and sandbox-migrate-to-next for stable-to |
| 242 | `secure-t` | Audit any repo for security weaknesses, fix the code, push to GitHub fully configured (branches, protection, Pages, Actions, Dependabot), deploy the web UI to V |
| 243 | `secure-t-maestro` | Orquestación de agentes para el repositorio secure-t: mejora y mantenimiento de React/Vite, Express/TypeScript, IA gobernada, cyber-range, auditoría, accesibili |
| 244 | `session-report` | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. |
| 245 | `shadcn` | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. Provides project context, c |
| 246 | `shadcn-component-mastery` | Dominio de componentes shadcn/ui para diseno de audio y DAW. |
| 247 | `shao-music` | Shao - High-fidelity music generation by unified acoustic-token pipeline. Open-source complete music works. |
| 248 | `skill-creator` | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabil |
| 249 | `skill-development` | This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill co |
| 250 | `skill-share` | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery. |
| 251 | `slack-gif-creator` | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users  |
| 252 | `socket-io-realtime` | Habilitacion de interactividad multi-evento via WebSockets. |
| 253 | `song-generation` | SongGeneration / LeVo - Open-source commercial-grade AI music generation by Tencent. Text-to-music with lyrics. |
| 254 | `soulx-singer` | SoulX-Singer - Zero-shot singing voice synthesis by Soul AI Lab. Generate singing voices for any unseen singer. |
| 255 | `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| 256 | `surgical-patch` | Fix bugs and small behavior changes at the narrowest responsible layer. Use when regression proof, preserved surrounding behavior, and task-relevant tests matte |
| 257 | `svg-animation-paths` | Trazado interactivo de dibujos y graficos vectoriales. |
| 258 | `svg-art-skill` | Create SVG graphics through programmatic code generation. Use this skill when the user asks to create icons, logos, illustrations, diagrams, data visualizations |
| 259 | `system-environment-vars` | Gestion y ocultamiento en registro seguro de variables criticas. |
| 260 | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| 261 | `tailored-resume-generator` | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances |
| 262 | `tailwind-v4-mastery` | Estilizado reactivo y utilitario a nivel de produccion con Tailwind CSS 4. |
| 263 | `terminal-native-ai` | Integracion de asistentes mediante comandos de terminal con CLI unificado. |
| 264 | `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| 265 | `test-master` | Generates test files, creates mocking strategies, analyzes code coverage, designs test architectures, and produces test plans and defect reports across function |
| 266 | `theme-factory` | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fo |
| 267 | `threejs-animation` | Three.js animation workflows for AnimationMixer, AnimationClip, AnimationAction, keyframe tracks, skeletal animation, morph targets, fading, blending, additive  |
| 268 | `threejs-fundamentals` | Core Three.js scene architecture for scenes, cameras, WebGLRenderer, Object3D hierarchy, transforms, coordinate systems, resize handling, animation loops, and c |
| 269 | `threejs-geometry` | Three.js Geometry workflow skill. Use this skill when the user needs Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing.  |
| 270 | `threejs-interaction` | Three.js Interaction workflow skill. Use this skill when the user needs Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use wh |
| 271 | `threejs-lighting` | Three.js Lighting workflow skill. Use this skill when the user needs Three.js lighting - light types, shadows, environment lighting. Use when adding lights, con |
| 272 | `threejs-loaders` | Three.js Loaders workflow skill. Use this skill when the user needs Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D |
| 273 | `threejs-materials` | Three.js Materials workflow skill. Use this skill when the user needs Three.js materials - PBR, basic, phong, shader materials, material properties. Use when st |
| 274 | `threejs-postprocessing` | Three.js Post-Processing workflow skill. Use this skill when the user needs Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when addi |
| 275 | `threejs-shaders` | Three.js Shaders workflow skill. Use this skill when the user needs Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom  |
| 276 | `threejs-textures` | Three.js Textures workflow skill. Use this skill when the user needs Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when |
| 277 | `token-plan-optimization` | Optimizacion de costes del Token Plan de Alibaba Cloud. |
| 278 | `token-protocol` | Protocolo anti-quema de tokens para Qwen Code CLI / ModelStudio Token Plan. Aplicar SIEMPRE: sesiones cortas por tarea, /compact a ~25K, thinking OFF en tier ba |
| 279 | `turnstile-spin` | Set up, repair, or migrate to Cloudflare Turnstile bot verification in an existing frontend and backend, including server-side Siteverify. |
| 280 | `twitter-algorithm-optimizer` | Analyze and optimize tweets for maximum reach using Twitter's open-source algorithm insights. Rewrite and edit user tweets to improve engagement and visibility  |
| 281 | `typescript-pro` | Implements advanced TypeScript type systems, creates custom type guards, utility types, and branded types, and configures tRPC for end-to-end type safety. |
| 282 | `ui-ux-pro-max` | UI/UX Pro Max - Design Intelligence workflow skill. Use this skill when the user needs Comprehensive design guide for web and mobile applications. Use when desi |
| 283 | `user-privacy-protection` | Garantia de manejo etico y anonimato de interacciones (RGPD). |
| 284 | `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via n |
| 285 | `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions |
| 286 | `vercel-cli-with-tokens` | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. |
| 287 | `vercel-optimize` | Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel metrics, usag |
| 288 | `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output be |
| 289 | `verify-and-stop` | Prove existing work meets acceptance conditions without expanding scope. Use for validation-only tasks, completion checks, focused gate runs, and last-mile proo |
| 290 | `vidmuse` | Use when an AI agent needs to work with VidMuse projects, account state, subscription credits, video/audio/image/text/tool models, generated or uploaded assets, |
| 291 | `vidmuse-ai-video` | Gestion de produccion de video IA con VidMuse y generacion de clips. |
| 292 | `voltagent-best-practices` | VoltAgent architectural patterns and conventions. Covers agents vs workflows, project layout, memory, servers, and observability. |
| 293 | `vram-optimization` | Escalado de modelos masivos en hardware de consumo con KV Cache Int8. |
| 294 | `wan-video-pipeline` | Pipeline de video Wan 2.6 con audio-input y lip-sync. |
| 295 | `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for |
| 296 | `web-audio-api-synths` | Generacion matematica de sintetizadores y osciladores en tiempo real. |
| 297 | `web-design-guidelines` | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site  |
| 298 | `web-perf` | Audit, diagnose, or optimize website loading and interaction performance, Core Web Vitals, and Lighthouse performance scores. |
| 299 | `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing br |
| 300 | `whadoa` | Use when the user describes something they saw but cannot name — by how it looks, where they saw it, or what it was for — and expects identification: a file, ph |
| 301 | `windows-fast-safe-config` | Configure Windows 10/11 for maximum performance and security using only official Microsoft sources, with automatic rollback. Use when hardening Windows, improvi |
| 302 | `windows-terminal-pro` | Configuracion personalizada y flujos fluidos de consola en Windows. |
| 303 | `workers-best-practices` | Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers. |
| 304 | `wrangler` | Run or troubleshoot Wrangler CLI commands and configure Worker projects for local development, deployment, and Cloudflare resource management. |
| 305 | `wrap-up` | Close out (or revisit) a Claude Managed Agent build — refresh the overview page, recap every primitive the founder now owns, show the run log and live status, s |
| 306 | `writing-guidelines` | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or  |
| 307 | `writing-hookify-rules` | This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on ho |
| 308 | `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| 309 | `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| 310 | `xlsx` | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xl |
| 311 | `youtube-downloader` | Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports vari |

## Licencia

MIT para el contenido propio. Los skills de terceros conservan su licencia original — ver `THIRD-PARTY-NOTICES.md`.
