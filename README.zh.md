# Awesome Open-Source SEO（开源 SEO 工具精选）

一个只收录开源 SEO 工具的精选清单——可自托管、可 fork、可逐行读源码。

每一条都是真实源码 + 开放协议。不收 SaaS 试用、不放联盟链接、不搞免费增值墙。

> 为什么要有这个清单：现有的 awesome-seo 列表把工具、文章、课程、付费产品混在一起。本清单只收工具、只收有源码的——在你自己机器上跑不起来的，不配出现在这里。

星标数是 2026 年 8 月的快照，会漂移，代码不会。

**[English version](./README.md)**

## 目录

- [一站式平台](#一站式平台)
- [爬虫与站点审计](#爬虫与站点审计)
- [SERP 与关键词研究](#serp-与关键词研究)
- [GEO 与 AI 搜索可见性](#geo-与-ai-搜索可见性)
- [框架与 CMS 集成](#框架与-cms-集成)
- [收录与站点地图](#收录与站点地图)
- [CLI 工具集](#cli-工具集)
- [其他精选清单](#其他精选清单)

## 一站式平台

- [open-seo](https://github.com/every-app/open-seo) — Semrush 和 Ahrefs 的开源替代，目前最完整的一站式尝试。(13.1k★, MIT)

## 爬虫与站点审计

- [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) — Python 爬虫，抓整站并输出结构问题报告，这个领域最老的项目之一。(1.5k★)
- [linkinator](https://github.com/JustinBeckwith/linkinator) — 断链检查器，爬网站验证所有链接，作者是 Google 工程师。(1.3k★, MIT)
- [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) — 免费桌面端 SEO 爬虫，Screaming Frog 的开源替代。(873★, MIT)
- [seo-audits-toolkit](https://github.com/StanGirard/seo-audits-toolkit) — Lighthouse + 安全响应头爬虫，整站审计。(813★)
- [seonaut](https://github.com/StJudeWasHere/seonaut) — 带网页界面的开源 SEO 审计工具，可自托管。(768★, MIT)
- [crawlseo](https://github.com/crawlseo/crawlseo) — 开源 SEO 监控：Search Console + 爬虫 + Core Web Vitals 三合一。(554★, MIT)
- [search-solved-public-seo](https://github.com/searchsolved/search-solved-public-seo) — Lee Foot 的实用 Python SEO 脚本集。(409★)

## SERP 与关键词研究

- [advertools](https://github.com/eliasdabbas/advertools) — 在线营销生产力库：爬虫、SERP 分析、关键词处理一体化。(1.4k★, MIT)
- [openserp](https://github.com/karust/openserp) — 自托管 SERP API，浏览器渲染的真实 Google 结果。(1.3k★, MIT)
- [clauneck](https://github.com/serpapi/clauneck) — 从网页抓邮箱和社交账号，线索调研用。(202★, MIT)

## GEO 与 AI 搜索可见性

最新的品类。这些工具度量和优化的是站点在 AI 回答里的表现，而不只是蓝色链接。

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — Claude Code 的通用 SEO 技能：25 个子技能 + 18 个子代理，覆盖审计、内容与技术 SEO。(14.8k★, MIT)
- [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) — GEO 优先的 SEO 技能，专注 AI 搜索优化。(9.4k★, MIT)
- [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — 给 AI agent 用的开源 SEO、GEO 和营销技能。(3.4k★, MIT)
- [GEOFlow](https://github.com/yaojingang/GEOFlow) — GEO 内容工程与多站点分发系统。(3.3k★, Apache-2.0)
- [geolook](https://github.com/aigclink/geolook) — 端到端 GEO 实现：状态分析、诊断、报告。(581★, MIT)
- [searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo) — 面向 AI 原生站点的开源 AEO/GEO/SEO 技术栈。(96★, MIT)

## 框架与 CMS 集成

- [next-seo](https://github.com/garmeeh/next-seo) — Next.js SEO 插件：meta、Open Graph、JSON-LD 声明式处理。(8.5k★, MIT)
- [meta-tags](https://github.com/kpumuk/meta-tags) — Ruby on Rails 的 SEO meta 标签方案。(2.8k★, MIT)
- [wordpress-seo](https://github.com/Yoast/wordpress-seo) — Yoast SEO，WordPress 生态份额最大的 SEO 插件。(2.0k★)
- [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) — Jekyll 插件，为搜索引擎和社交网络输出 meta 标签。(1.7k★, MIT)
- [nuxt-seo](https://github.com/harlan-zw/nuxt-seo) — Nuxt 的全套技术 SEO 与 AEO。(1.4k★, MIT)
- [astro-seo](https://github.com/jonasmerlin/astro-seo) — Astro 的 SEO 组件。(1.4k★, MIT)
- [laravel-seo](https://github.com/ralphjsmit/laravel-seo) — Laravel 应用的 SEO 处理。(863★, MIT)
- [svelte-seo](https://github.com/artiebits/svelte-seo) — Svelte/SvelteKit 的 SEO meta 标签。(562★, MIT)
- [the-seo-framework](https://github.com/sybrew/the-seo-framework) — 轻量自动化的 WordPress SEO 插件。(482★, GPL-3.0)

## 收录与站点地图

- [google-indexing-script](https://github.com/goenning/google-indexing-script) — 用 Indexing API 快速让 Google 收录你的站。(7.7k★, MIT)
- [next-sitemap](https://github.com/iamvishnusankar/next-sitemap) — Next.js 的 sitemap 和 robots.txt 生成器。(3.7k★, MIT)
- [laravel-sitemap](https://github.com/spatie/laravel-sitemap) — Laravel 站点地图生成。(2.6k★, MIT)
- [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) — Jekyll 站点地图插件。(984★, MIT)

## CLI 工具集

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) — 本组织维护。零依赖 Python CLI，19 个工具：关键词挖掘、SERP 难度评分、技术站点审计、16 维度 GEO 评分。PyPI 包名 `zens-ink`。(MIT)
- [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) — 把 Google SEO 官方文档做成的 AI 提示词库。(539★, MIT)

## 其他精选清单

- [awesome-seo (bmpi-dev)](https://github.com/bmpi-dev/awesome-seo) — Google SEO 研究与流量变现资源。(2.8k★, MIT)
- [awesome-seo (teles)](https://github.com/teles/awesome-seo) — 通用 SEO 链接精选。(885★)
- [awesome-seo-tools (serpapi)](https://github.com/serpapi/awesome-seo-tools) — SEO 工具精选，含商业工具。(1.1k★)
- [search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) — 清单式 SEO 资源合集。(2.8k★, MIT)

## 贡献指南

欢迎提 PR。收录标准：

1. 开放协议下源码可见，或仓库内明确声明协议
2. 真的能跑——你自己装上执行过
3. 做的是 SEO/GEO 的事（工具，不是内容）
4. 不是已收录条目的 fork

允许自荐，但请在 PR 里说明，和所有人一样。

## 许可

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) — 本清单随意使用。
