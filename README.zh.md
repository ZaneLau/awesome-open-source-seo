# Awesome Open-Source SEO（开源 SEO 工具精选）

一个只收录开源 SEO 工具的精选清单——可自托管、可 fork、可逐行读源码。

每一条都是真实源码 + 开放协议。不收 SaaS 试用、不放联盟链接、不搞免费增值墙。

> 为什么要有这个清单：现有的 awesome-seo 列表把工具、文章、课程、付费产品混在一起。本清单只收工具、只收有源码的——在你自己机器上跑不起来的，不配出现在这里。

星标数是 2026 年 8 月的快照，会漂移，代码不会。

**[English version](./README.md)**

## 目录

- [一站式平台](#一站式平台)
- [爬虫与站点审计](#爬虫与站点审计)
- [排名追踪](#排名追踪)
- [分析与日志](#分析与日志)
- [GSC 数据导出](#gsc-数据导出)
- [SERP 与关键词研究](#serp-与关键词研究)
- [GEO 与 AI 搜索可见性](#geo-与-ai-搜索可见性)
- [框架与 CMS 集成](#框架与-cms-集成)
- [收录与站点地图](#收录与站点地图)
- [CLI 工具集](#cli-工具集)
- [其他精选清单](#其他精选清单)
- [推荐组合](#推荐组合)

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
- [lighthouse](https://github.com/GoogleChrome/lighthouse) — Google 官方开源审计器，性能 + SEO + 最佳实践，CLI 或 CI 运行。(30.7k★, Apache-2.0)
- [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) — 每次提交跑 Lighthouse 并在 CI 里断言预算。(7.1k★, Apache-2.0)
- [scrapy](https://github.com/scrapy/scrapy) — Python 爬虫框架。本身不是 SEO 工具，但是给 JS 渲染页和定制化抽取写爬虫的标准方式。(64k★, BSD-3-Clause)
- [brozzler](https://github.com/internetarchive/brozzler) — Internet Archive 出品的分布式浏览器（Playwright）爬虫。(815★)

### 排名追踪

- [SerpBear](https://github.com/towfiqi/serpbear) — 自托管排名追踪（Next.js + SQLite，Docker），无限域名/关键词，接 GSC 和 Google Ads，Slack/Telegram 告警。最常被推荐的自托管追踪器。(1.4k★, GPL-3.0)
- [serposcope](https://github.com/serphacker/serposcope) — 老牌自托管排名监控（Java），多地区、代理、验证码支持。Legacy 但久经考验。(757★, GPLv3)
- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) — 多站点 SEO 控制面板（PHP + MySQL），含排名、审计、外链监控、白标报告，适合 Agency。(137★, GPL-3.0)

### 分析与日志

- [matomo](https://github.com/matomo-org/matomo) — 自托管 Google Analytics 替代。一手数据，合规友好。(21.8k★, GPL-3.0)
- [plausible](https://github.com/plausible/analytics) — 轻量、无 Cookie、隐私优先的分析。(28.7k★, AGPL-3.0)
- [goaccess](https://github.com/allinurl/goaccess) — 实时终端日志分析器（Nginx/Apache）。从原始日志看 Googlebot 抓取、404、带宽，技术 SEO 神器。(20.8k★, MIT)
- [OpenSearch](https://github.com/opensearch-project/OpenSearch) — 大规模日志与点击流查询的搜索引擎，含爬取行为分析。(13.6k★, Apache-2.0)

### GSC 数据导出

- [google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all) — 批量 CSV 导出 Search Console 数据，绕过界面 1000 行限制。(10★)

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
- [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) — Agent skill，Python + LLM 双层审计任意 URL：robots、sitemap、canonical、H1、schema、PSI。(729★, MIT)

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

## 推荐组合

没有哪个开源工具能单挑 Semrush 或 Ahrefs，它们的护城河是外链库和搜索量数据。但执行层（审计、爬取、排名追踪、自有数据分析）已经成熟，组合一套能覆盖大部分日常需求。诚实的边界：要做竞品外链挖掘，留一个 Ahrefs/Semrush 只读账号买数据，执行和自有数据交给开源。

**小站 / 独立站**

- [SerpBear](https://github.com/towfiqi/serpbear)（排名） + [SEOnaut](https://github.com/StJudeWasHere/seonaut)（审计） + [Matomo](https://github.com/matomo-org/matomo) 或 [Plausible](https://github.com/plausible/analytics)（分析） + [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci)（CI 检查）

**Agency**

- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel)（多站管理） + [SerpBear](https://github.com/towfiqi/serpbear) + GSC 批量导出（[google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all)） + [seonaut](https://github.com/StJudeWasHere/seonaut) 做定期爬取

**开发者 / AI 工作流**

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) 或 [RustySEO](https://www.rustyseo.com/) 打底 + [scrapy](https://github.com/scrapy/scrapy) 补定制爬取 + [goaccess](https://github.com/allinurl/goaccess) 看原始日志 + [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) 做 LLM 辅助审计

## 贡献指南

欢迎提 PR。收录标准：

1. 开放协议下源码可见，或仓库内明确声明协议
2. 真的能跑——你自己装上执行过
3. 做的是 SEO/GEO 的事（工具，不是内容）
4. 不是已收录条目的 fork

允许自荐，但请在 PR 里说明，和所有人一样。

## 许可

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) — 本清单随意使用。
