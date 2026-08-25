import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "EngineeringAdvisor",
  description: "29-工程-Engineering Level 行业顾问 · 技术决策可追溯平台",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
