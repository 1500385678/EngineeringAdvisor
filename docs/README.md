# `docs/` — 工程文档

> Sphinx / MkDocs 工程文档源文件。后续 ADR 中心、架构图、API 文档都放这里。

## 规划

| 子目录 | 内容 | 触发 |
|---|---|---|
| `adr/` | ADR 模板 + 已有 ADR 副本(可入库版本) | Phase 1 |
| `architecture/` | 架构图(PlantUML / Mermaid 源) | Phase 1 |
| `api/` | 自动生成的 OpenAPI 描述(可选) | Phase 1 |
| `runbook/` | 事故复盘 + 运维手册 | Phase 3 |
| `index.md` | MkDocs 入口 | 0829 README 升级同步 |

## 不做什么

- ❌ 不放计划文档(那是根 `项目开发计划.md`)
- ❌ 不放巡检/日报(那是 `.Log/` 目录)
- ❌ 不放代码注释(那是源码内 docstring)

## 工具选型(待定)

候选:
- **MkDocs + Material**:Markdown 友好,本地预览简单
- **Sphinx + MyST**:扩展性更强,Python 生态默认
- **Docusaurus**:React 生态,可与 Next.js 共享组件

**0829 README 升级时一并拍板**。

## 当前状态

- 仅 `README.md` 占位,无子目录、无源文件
- 0829 起按需填充
