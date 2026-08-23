# Awesome Open-Source SEO

**[中文版](./README.zh.md)**

A curated list of open-source SEO tools you can self-host, fork, and read line by line.

Every entry ships real source code under an open license. No SaaS trials, no affiliate links, no freemium walls.

> Why this list exists: existing awesome-seo lists mix tools with articles, courses, and paid products. This one is tools-only, source-available-only. If it doesn't run on your machine, it doesn't belong here.

Star counts are a snapshot (Aug 2026) — they drift, the code doesn't.

## Contents

- [All-in-One Platforms](#all-in-one-platforms)
- [Crawlers & Site Audit](#crawlers--site-audit)
- [Rank Tracking](#rank-tracking)
- [Analytics & Log Analysis](#analytics--log-analysis)
- [GSC Data Extraction](#gsc-data-extraction)
- [SERP & Keyword Research](#serp--keyword-research)
- [GEO & AI Search Visibility](#geo--ai-search-visibility)
- [Framework & CMS Integrations](#framework--cms-integrations)
- [Indexing & Sitemaps](#indexing--sitemaps)
- [CLI Toolkits](#cli-toolkits)
- [Other Curated Lists](#other-curated-lists)
- [Recommended Stacks](#recommended-stacks)

## All-in-One Platforms

- [open-seo](https://github.com/every-app/open-seo) — Open-source alternative to Semrush and Ahrefs. The most complete attempt at a full suite so far. (13.1k★, MIT)

## Crawlers & Site Audit

- [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) — Python tool that crawls a site and reports structural issues. One of the oldest projects in this space. (1.5k★)
- [linkinator](https://github.com/JustinBeckwith/linkinator) — Broken-link checker that crawls websites and validates links. Made by a Google engineer. (1.3k★, MIT)
- [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) — Free desktop SEO crawler, an open-source alternative to Screaming Frog. (873★, MIT)
- [seo-audits-toolkit](https://github.com/StanGirard/seo-audits-toolkit) — Lighthouse and security-header crawler that audits whole sites. (813★)
- [seonaut](https://github.com/StJudeWasHere/seonaut) — Open-source SEO audit tool with a web interface. Self-hostable. (768★, MIT)
- [crawlseo](https://github.com/crawlseo/crawlseo) — Open-source SEO monitoring: Search Console + crawler + Core Web Vitals in one. (554★, MIT)
- [search-solved-public-seo](https://github.com/searchsolved/search-solved-public-seo) — Collection of practical Python SEO scripts by Lee Foot. (409★)
- [lighthouse](https://github.com/GoogleChrome/lighthouse) — Google's official open-source auditor for performance, SEO, and best practices. Runs from CLI or CI. (30.7k★, Apache-2.0)
- [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) — Runs Lighthouse on every commit and asserts budgets in CI. (7.1k★, Apache-2.0)
- [scrapy](https://github.com/scrapy/scrapy) — The Python crawling framework. Not an SEO tool per se, but the standard way to build custom crawlers for JS-rendered pages and structured extraction. (64k★, BSD-3-Clause)
- [brozzler](https://github.com/internetarchive/brozzler) — Distributed, browser-based (Playwright) web crawler from the Internet Archive. (815★)

### Rank Tracking

- [SerpBear](https://github.com/towfiqi/serpbear) — Self-hosted rank tracker (Next.js + SQLite, Docker) with unlimited domains/keywords, GSC and Google Ads integration, Slack/Telegram alerts. The most-recommended self-hosted tracker. (1.4k★, GPL-3.0)
- [serposcope](https://github.com/serphacker/serposcope) — Long-running self-hosted rank monitor (Java) with multi-region, proxy, and captcha support. Legacy but battle-tested. (757★, GPLv3)
- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) — Multi-site SEO control panel (PHP + MySQL) with rank tracking, audits, backlink monitoring, and white-label reports for agencies. (137★, GPL-3.0)

### Analytics & Log Analysis

- [matomo](https://github.com/matomo-org/matomo) — Self-hosted Google Analytics alternative. First-party data, compliance-friendly. (21.8k★, GPL-3.0)
- [plausible](https://github.com/plausible/analytics) — Lightweight, cookieless, privacy-first analytics. (28.7k★, AGPL-3.0)
- [goaccess](https://github.com/allinurl/goaccess) — Real-time terminal log analyzer for Nginx/Apache. Watch Googlebot crawls, 404s, and bandwidth from raw logs — a technical SEO workhorse. (20.8k★, MIT)
- [OpenSearch](https://github.com/opensearch-project/OpenSearch) — Search engine for large-scale log and clickstream queries, including crawl-behavior analysis. (13.6k★, Apache-2.0)

### GSC Data Extraction

- [google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all) — Bulk CSV export of Search Console data, bypassing the 1,000-row UI limit. (10★)

## SERP & Keyword Research

- [advertools](https://github.com/eliasdabbas/advertools) — Online-marketing productivity and analysis library: crawling, SERP analysis, keyword processing. (1.4k★, MIT)
- [openserp](https://github.com/karust/openserp) — Self-hosted SERP API with browser-rendered Google results. For SEO and automation. (1.3k★, MIT)
- [clauneck](https://github.com/serpapi/clauneck) — Scrapes emails and social accounts from web pages, built for lead research. (202★, MIT)

## GEO & AI Search Visibility

The newest category. These tools measure and improve how sites appear in AI answers, not just blue links.

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — Universal SEO skill for Claude Code: 25 sub-skills and 18 sub-agents covering audit, content, and technical work. (14.8k★, MIT)
- [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) — GEO-first SEO skill for AI coding assistants, focused on AI-search optimization. (9.4k★, MIT)
- [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) — Open-source SEO, GEO, and marketing skills for AI agents. (3.4k★, MIT)
- [GEOFlow](https://github.com/yaojingang/GEOFlow) — GEO content engineering and multi-site distribution system. (3.3k★, Apache-2.0)
- [geolook](https://github.com/aigclink/geolook) — End-to-end GEO implementation: status analysis, diagnosis, and reporting. (581★, MIT)
- [searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo) — Open-source AEO/GEO/SEO stack for AI-native websites. (96★, MIT)
- [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) — Agent skill that runs a Python + LLM two-layer audit on any URL: robots, sitemap, canonicals, H1, schema, PSI. (729★, MIT)

## Framework & CMS Integrations

- [next-seo](https://github.com/garmeeh/next-seo) — SEO plugin for Next.js: meta, Open Graph, JSON-LD handled declaratively. (8.5k★, MIT)
- [meta-tags](https://github.com/kpumuk/meta-tags) — SEO meta tags for Ruby on Rails. (2.8k★, MIT)
- [wordpress-seo](https://github.com/Yoast/wordpress-seo) — Yoast SEO for WordPress, the plugin that runs a large share of the web. (2.0k★)
- [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) — Jekyll plugin adding metadata tags for search engines and social. (1.7k★, MIT)
- [nuxt-seo](https://github.com/harlan-zw/nuxt-seo) — Fully equipped technical SEO and AEO for Nuxt. (1.4k★, MIT)
- [astro-seo](https://github.com/jonasmerlin/astro-seo) — SEO component for Astro. (1.4k★, MIT)
- [laravel-seo](https://github.com/ralphjsmit/laravel-seo) — SEO handling for Laravel applications. (863★, MIT)
- [svelte-seo](https://github.com/artiebits/svelte-seo) — SEO meta tags for Svelte/SvelteKit. (562★, MIT)
- [the-seo-framework](https://github.com/sybrew/the-seo-framework) — Lightweight, automated SEO plugin for WordPress. (482★, GPL-3.0)

## Indexing & Sitemaps

- [google-indexing-script](https://github.com/goenning/google-indexing-script) — Script that gets your site indexed on Google fast, via the Indexing API. (7.7k★, MIT)
- [next-sitemap](https://github.com/iamvishnusankar/next-sitemap) — Sitemap and robots.txt generator for Next.js. (3.7k★, MIT)
- [laravel-sitemap](https://github.com/spatie/laravel-sitemap) — Sitemap generation for Laravel. (2.6k★, MIT)
- [jekyll-sitemap](https://github.com/jekyll/jekyll-sitemap) — Sitemap plugin for Jekyll. (984★, MIT)

## CLI Toolkits

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) — Maintained by this organization. Zero-dependency Python CLI with 19 tools: keyword research, SERP difficulty scoring, technical site audit, and a 16-dimension GEO score. On PyPI as `zens-ink`. (MIT)
- [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) — Google's SEO documentation turned into an AI prompt library. (539★, MIT)

## Other Curated Lists

- [awesome-seo (bmpi-dev)](https://github.com/bmpi-dev/awesome-seo) — Google SEO research and traffic monetization resources. (2.8k★, MIT)
- [awesome-seo (teles)](https://github.com/teles/awesome-seo) — General curated list of SEO links. (885★)
- [awesome-seo-tools (serpapi)](https://github.com/serpapi/awesome-seo-tools) — Curated list of SEO tools, includes commercial ones. (1.1k★)
- [search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) — Checklist-style collection of SEO resources. (2.8k★, MIT)

## Recommended Stacks

No single open-source tool replaces Semrush or Ahrefs — the moat there is the backlink index and search-volume data. But execution-layer work (audits, crawling, rank tracking, first-party analytics) is mature. A combined stack covers most daily needs. The honest boundary: for competitive backlink mining, keep one paid Ahrefs/Semrush read-only account for data, and let open source handle execution and your own data.

**Small sites / indie sites**

- [SerpBear](https://github.com/towfiqi/serpbear) (rank tracking) + [SEOnaut](https://github.com/StJudeWasHere/seonaut) (audits) + [Matomo](https://github.com/matomo-org/matomo) or [Plausible](https://github.com/plausible/analytics) (analytics) + [lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) (CI checks)

**Agencies**

- [Seo-Panel](https://github.com/sendtogeo/Seo-Panel) (multi-site management) + [SerpBear](https://github.com/towfiqi/serpbear) + GSC bulk export ([google-search-console-export-all](https://github.com/swalker-888/google-search-console-export-all)) + [seonaut](https://github.com/StJudeWasHere/seonaut) for recurring crawls

**Developers / AI workflows**

- [zens-ink](https://github.com/ZensInk/zens-ink-seo-package) or [RustySEO](https://www.rustyseo.com/) as the base + [scrapy](https://github.com/scrapy/scrapy) for custom crawls + [goaccess](https://github.com/allinurl/goaccess) for raw logs + [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) for LLM-assisted audits

## Contributing

PRs welcome. A project qualifies if it:

1. Is source-available under an open license, or explicitly licensed in the repo
2. Actually runs — you can install and execute it yourself
3. Does SEO/GEO work (tools, not content)
4. Is not a fork of an entry already listed

Self-promotion is allowed but disclose it in the PR, like everyone else does.

## License

[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/) — use this list however you want.
