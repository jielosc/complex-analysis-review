# 复变函数期末复习网站

一个面向**期末备考**的多页面静态网站，用来系统复习《复变函数》课程内容。

在线访问：<https://jielosc.github.io/complex-analysis-review/>

## 项目特点

- 多页面结构，按专题拆分，适合分块复习
- 重要数学公式尽量使用 **LaTeX + MathJax** 渲染
- 包含：
  - 重要定义
  - 核心定理
  - 简短证明思路
  - 典型例题
  - 翻卡速记
  - 临考清单
- 已针对移动端做过适配

## 页面结构

- `index.html`：总览 / 专题入口
- `basics.html`：基本定义
- `analytic.html`：解析与 C-R 方程
- `integral.html`：复积分与柯西积分定理
- `formula.html`：柯西积分公式及其推论
- `series.html`：级数、奇点、留数
- `exam.html`：题型模板与综合例题
- `flashcards.html`：翻卡速记
- `checklist.html`：临考清单

## 本地预览

直接用浏览器打开：

- `index.html`

即可浏览整个网站。

## 技术说明

- 纯静态网站
- 样式文件：`assets/styles.css`
- 页面交互脚本：`assets/app.js`
- 公式渲染：MathJax CDN

## 部署方式

本项目已部署到 **GitHub Pages**：

- 仓库：`jielosc/complex-analysis-review`
- 站点地址：<https://jielosc.github.io/complex-analysis-review/>

## 维护说明

如果后续要继续优化内容，建议优先保持以下原则：

- 数学公式尽量统一使用 LaTeX
- 页面内容优先保持中文界面一致性
- 新增内容尽量按专题拆分，不要重新堆回单页
- 移动端阅读体验优先，避免整页横向滚动

## 适用场景

这个网站适合：

- 期末前按章节复习
- 快速回忆核心定理与公式
- 临考前看典型题型和清单
- 手机上碎片化浏览复习
