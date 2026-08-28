# EngineeringAdvisor

> **29-工程-Engineering Level** 行业 Web 端顾问产品 · 内部代号 `EngineeringAdvisor`
>
> 状态:**v0.1.0 脚手架完整日**(5/5 脚手架已落地)· 0830 起启动 Phase 0 资产盘点

## 这是什么

基于张勇的 36 行业架构,EngineeringAdvisor 是**工程行业**的 Web 端顾问产品。
双栈形态:

- **前端**:Next.js 14 (App Router) + TypeScript 5 + React 18
- **后端**:FastAPI 0.115+ + Pydantic v2 + Python 3.9+

脚手架 5 日(0825-0829)手工落地,共 22 文件 / ~52 KB,**未跑 install**(后续按需 `pip install -e .` / `npm install`)。

## 架构

```
┌─────────────────────────────────────────────────────────┐
│  EngineeringAdvisor (双栈 Web)                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────┐         ┌──────────────────┐      │
│  │  Next.js 前端    │  HTTP   │  FastAPI 后端    │      │
│  │  app/ + tsconfig │ ◀────▶  │  api/ + Pydantic │      │
│  │  Port 3000       │  JSON   │  Port 8000       │      │
│  └──────────────────┘         └────────┬─────────┘      │
│                                       │                 │
│                          ┌────────────┼────────┐        │
│                          ▼            ▼        ▼        │
│                   ┌──────────┐ ┌─────────┐ ┌──────┐     │
│                   │ services │ │ routers │ │ lib  │     │
│                   │ 业务编排  │ │ 薄路由   │ │工具  │     │
│                   └──────────┘ └─────────┘ └──────┘     │
│                                                         │
└─────────────────────────────────────────────────────────┘

后续接入:飞书 bot (Phase 0) / Neo4j 知识图谱 (Phase 1) / LLM (Phase 1+)
```

## 目录结构

```
EngineeringWeb/
├── app/                   # Next.js 14 App Router (前端页面)
│   ├── layout.tsx · page.tsx · globals.css
├── api/                   # FastAPI 后端
│   ├── main.py            # create_app() 工厂 + 3 端点(/ /healthz /api/v1/info)
│   ├── core/              # 配置中心 (Pydantic Settings)
│   ├── models/            # DTO (Pydantic schemas)
│   ├── lib/               # 通用工具(后续 logging/exception/retry)
│   ├── services/          # 业务服务层(Phase 0+ 按域切分)
│   └── routers/           # HTTP 路由层(薄壳,业务下沉到 services)
├── tests/                 # pytest 根(镜像 api/ 结构)
├── docs/                  # 工程文档(ADR / 架构图 / Runbook)
├── pyproject.toml         # Python 依赖 + ruff/mypy/pytest 配置
├── package.json           # Node 依赖 + 脚本
├── tsconfig.json · next.config.mjs · next-env.d.ts
├── 项目开发计划.md         # 主计划(9 节,142 行,Phase 0/1/2/3 路线图)
├── .plan/                 # 每日 T4 增量计划(临时,T1 派位待消化)
└── .Log/                  # 每日 02:40 巡检报告(已入库 tracked)
```

## Quickstart

### 后端 (FastAPI)

```bash
# 1. 创建虚拟环境(可选但推荐)
python3.9+ -m venv .venv && source .venv/bin/activate

# 2. 安装依赖(可编辑模式)
pip install -e ".[dev]"

# 3. 启动(开发模式,自动重载)
uvicorn api.main:app --reload --port 8000
# 或 python -m api.main

# 4. 验证
curl http://localhost:8000/         # 项目标识 + 版本
curl http://localhost:8000/healthz  # 健康检查
curl http://localhost:8000/api/v1/info  # 详情(行业/Agent/启动时间)
# 5. 跑测试
pytest -v
```

API 文档自动生成:`http://localhost:8000/docs` (Swagger UI) · `/redoc` (ReDoc)

### 前端 (Next.js)

```bash
# 1. 安装依赖
npm install   # 或 pnpm install / yarn

# 2. 启动(开发模式)
npm run dev

# 3. 访问
open http://localhost:3000

# 4. 构建生产版本
npm run build && npm run start

# 5. 类型检查 + Lint
npm run lint
```

### 双栈联调

开两个终端,前端 `:3000` 后端 `:8000`,后续在前端通过 fetch 调 `http://localhost:8000/api/v1/...`。
**当前阶段**前端 `app/page.tsx` 是占位欢迎页,后端 3 端点是健康检查;**双栈联调逻辑在 Phase 1 才正式接入**。

## 关键链接

- **仓库**:
  - GitHub: <https://github.com/1500385678/EngineeringAdvisor>
  - Gitee:  <https://gitee.com/architectzy/EngineeringAdvisor>
- **文档**:
  - 主计划: [`项目开发计划.md`](./项目开发计划.md) — 9 节路线图(Phase 0/1/2/3)
  - 后端根: [`api/README.md`](./api/README.md) · [`api/lib/README.md`](./api/lib/README.md) · [`api/services/README.md`](./api/services/README.md) · [`api/routers/README.md`](./api/routers/README.md)
  - 前端根: [`app/`](./app/) (Next.js App Router,无独立 README 沿用 Next.js 约定)
  - 测试根: [`tests/README.md`](./tests/README.md)
  - 文档根: [`docs/README.md`](./docs/README.md)

## 开发节奏

| 时间 | 角色 | 动作 |
|---|---|---|
| 每日 02:00 | T4 顾问 | 读巡检 + 主计划,写当日 `.plan/{date}.md` 增量计划 |
| 每日 02:40 | T4 顾问 | 写 `.Log/巡检-工程-{date}.md` 巡检报告,5 项巡检 |
| 每日 03:40 | T4 顾问 | **按 plan 产 1 个小变更** → commit → push GitHub + Gitee |
| 触发式 | T1 (用户) | 拍板 `.plan/` 目录定位 / 主计划合稿 / Phase 启动决策 |

**5/5 脚手架完成日** = 2026-08-29(本 README 升级日)· 0830 起启动 Phase 0 资产盘点(2 周到 0912)· 0912 起 Phase 1 MVP(6 周到 1024)· 1024 起 Phase 2 代码审查(6-8 周到 1219)· 1219 起 Phase 3 可靠性分析器(8-12 周到 0327)。

## 技术栈

| 层 | 技术 | 版本 | 锁定策略 |
|---|---|---|---|
| 前端 | Next.js | 14.2.15 | 主版本(2.15 补丁可升级) |
| 前端 | React / React DOM | 18.3.1 | 精确锁定 |
| 前端 | TypeScript | 5.6.2 | 主版本 |
| 前端 | Node | >= 20.0.0 | `engines` 声明 |
| 后端 | FastAPI | >= 0.115.0, < 1.0 | 主版本 |
| 后端 | Pydantic | >= 2.8.0, < 3.0 | 主版本 |
| 后端 | Python | >= 3.9 | 最小版本 |
| 后端 | uvicorn[standard] | >= 0.30.0 | 主版本 |
| 工具 | ruff / mypy / pytest | 最新稳定 | dev 依赖 |

## 不做什么(项目级)

- ❌ 不跑 `npm install` / `pip install`(脚手架阶段手写,按需触发)
- ❌ 不主动入库 `工程顾问开发架构与计划.md`(19.5 KB untracked,等用户决策)
- ❌ 不擅自 `.gitignore` `.plan/` 目录(0827 T1 决策"留待 T1 拍板")
- ❌ 不做大规模重构(脚手架阶段每文件 < 3 KB,严格控制单日变更)

## 变更记录

- **2026-08-29** — v0.1.0 脚手架完整日:仓库根 README 升级(从 483 B 占位 → ~5 KB),含 quickstart + 架构图 + 目录树 + 关联文档;主计划第 9 节第 5 项 checkbox 勾选
- **2026-08-28** — 基础目录结构补全(`api/lib/ api/services/ api/routers/ tests/ docs/`),commit `63281bb`
- **2026-08-27** — FastAPI 骨架落地(`pyproject.toml` + 7 文件),commit `dd0c15e`
- **2026-08-26** — Next.js 14 脚手架(`app/` 6 文件),commit `767c2c6`
- **2026-08-25** — `.gitignore` 全栈补全 + `.Log/` 巡检目录创建,commit `b0f6c1c`
