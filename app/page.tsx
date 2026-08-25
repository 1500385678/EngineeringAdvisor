export default function Home() {
  return (
    <main className="container">
      <h1>EngineeringAdvisor</h1>
      <p className="subtitle">29-工程-Engineering Level · 行业顾问产品</p>

      <section>
        <h2>项目阶段</h2>
        <ul>
          <li>Phase 0 · 资产盘点 (1-2 周)</li>
          <li>Phase 1 · MVP (4-6 周)</li>
          <li>Phase 2 · 代码审查 (6-8 周)</li>
          <li>Phase 3 · 可靠性 (8-12 周)</li>
        </ul>
      </section>

      <section>
        <h2>核心模块</h2>
        <ol>
          <li>技术方案库 (ADR 中心)</li>
          <li>技术选型决策器</li>
          <li>代码评审辅助</li>
          <li>可靠性分析器</li>
          <li>技术雷达</li>
        </ol>
      </section>

      <footer>
        <p>脚手架版本 v0.1 · 2026-08-26</p>
      </footer>
    </main>
  );
}
