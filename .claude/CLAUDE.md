# Horizon — 国际科技新闻采集器

> 状态：✅ 运行中 | 部署：GitHub Actions | 更新：2026-03-24

## 项目定位

feedloop 的**国际 AI 深度**信息源。从多个自定义源采集新闻 → AI 评分过滤 → 中英双语日报。

在 feedloop 架构中的角色：**4 源之一（上游采集层）**

```
Horizon → feedloop_hub.py → 统一表「信息中枢」→ 消费端
```

## 工作方式

- 信息源：Hacker News / arxiv / X(Twitter) / Reddit 等可自定义
- AI 评分：过滤低质量内容，只保留有价值的
- 输出：Feishu Bitable（feedloop 读取）+ GitHub Pages 在线演示

## 部署

| 项 | 值 |
|---|---|
| 运行方式 | GitHub Actions（定时触发） |
| 仓库 | 本地 clone，上游：Thysrael/Horizon |
| 文档 | README_zh.md |

## 注意

- 这是开源项目的本地定制版本，升级前检查 upstream 变更
- 配置文件在 `config/` 目录，不要随意改信息源（影响 feedloop 数据质量）
