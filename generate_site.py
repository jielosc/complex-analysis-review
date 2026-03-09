from pathlib import Path
from string import Template

ROOT = Path(r"C:\Users\jielosc\.openclaw\workspace\complex-analysis-review")
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

SITE_TITLE = "午夜星图 · 复变函数期末复习"

CSS = r'''
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500;700;900&family=Noto+Sans+SC:wght@400;500;700;900&display=swap');

:root {
  --bg: #07101d;
  --bg-2: #0c1628;
  --bg-3: #111f37;
  --panel: rgba(10, 17, 31, 0.78);
  --panel-strong: rgba(11, 19, 35, 0.94);
  --line: rgba(255,255,255,0.1);
  --line-strong: rgba(243, 200, 104, 0.22);
  --text: #edf4ff;
  --muted: #9caec8;
  --gold: #f4ca72;
  --gold-soft: #fff1cb;
  --cyan: #81e4ff;
  --violet: #acaaff;
  --rose: #ff96c5;
  --mint: #90efcf;
  --shadow: 0 24px 80px rgba(0,0,0,0.36);
  --radius-xl: 30px;
  --radius-lg: 24px;
  --radius-md: 18px;
  --radius-sm: 14px;
  --max-width: 1480px;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
  color: var(--text);
  line-height: 1.72;
  background:
    radial-gradient(circle at 12% 18%, rgba(129, 228, 255, 0.14), transparent 22%),
    radial-gradient(circle at 85% 10%, rgba(172, 170, 255, 0.14), transparent 20%),
    radial-gradient(circle at 80% 82%, rgba(255, 150, 197, 0.10), transparent 18%),
    linear-gradient(160deg, #050a13 0%, #091221 35%, #0b1424 62%, #070d18 100%);
  min-height: 100vh;
}

body::before,
body::after {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: -1;
}

body::before {
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 42px 42px;
  mask-image: linear-gradient(to bottom, rgba(255,255,255,0.55), transparent 88%);
  opacity: .22;
}

body::after {
  background:
    radial-gradient(circle at 18% 22%, rgba(255,255,255,.22) 0 1px, transparent 1.4px),
    radial-gradient(circle at 70% 20%, rgba(255,255,255,.18) 0 1px, transparent 1.4px),
    radial-gradient(circle at 80% 70%, rgba(255,255,255,.16) 0 1px, transparent 1.4px),
    radial-gradient(circle at 40% 84%, rgba(255,255,255,.13) 0 1px, transparent 1.4px);
  background-size: 280px 280px, 360px 360px, 320px 320px, 420px 420px;
  opacity: .45;
}

.page {
  width: min(calc(100% - 28px), var(--max-width));
  margin: 0 auto;
  padding: 18px 0 40px;
}

.topbar {
  position: sticky;
  top: 14px;
  z-index: 30;
  margin-bottom: 18px;
  border: 1px solid var(--line);
  border-radius: 22px;
  background: rgba(8, 14, 25, 0.7);
  backdrop-filter: blur(18px);
  box-shadow: var(--shadow);
}

.topbar-inner {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: space-between;
  padding: 14px 16px;
}

.brand {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.brand small {
  color: var(--gold);
  letter-spacing: .08em;
  text-transform: uppercase;
}

.brand strong {
  font-family: 'Noto Serif SC', serif;
  font-size: 1.02rem;
  color: var(--gold-soft);
}

.top-actions {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn,
.link-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,.12);
  background: rgba(255,255,255,.05);
  color: var(--text);
  text-decoration: none;
  padding: 10px 14px;
  font-size: .92rem;
  transition: .2s ease;
  cursor: pointer;
  font-family: inherit;
}

.btn:hover,
.link-btn:hover {
  transform: translateY(-1px);
  border-color: rgba(255,255,255,.22);
  background: rgba(255,255,255,.08);
}

.layout {
  display: grid;
  grid-template-columns: 290px minmax(0, 1fr);
  gap: 22px;
  align-items: start;
}

.sidebar {
  position: sticky;
  top: 96px;
  border: 1px solid var(--line);
  border-radius: 28px;
  background: rgba(8, 14, 26, 0.76);
  backdrop-filter: blur(18px);
  box-shadow: var(--shadow);
  padding: 18px;
}

.sidebar h2 {
  margin: 0 0 10px;
  font-family: 'Noto Serif SC', serif;
  color: var(--gold-soft);
  font-size: 1.08rem;
}

.sidebar .lead {
  color: var(--muted);
  font-size: .93rem;
  margin: 0 0 16px;
}

.nav {
  display: grid;
  gap: 9px;
}

.nav a {
  text-decoration: none;
  color: #dbe8f8;
  border-radius: 16px;
  padding: 11px 12px;
  background: rgba(255,255,255,.035);
  border: 1px solid rgba(255,255,255,.06);
  transition: .2s ease;
}

.nav a:hover,
.nav a.active {
  transform: translateX(4px);
  color: var(--gold-soft);
  border-color: rgba(243, 200, 104, .26);
  background: linear-gradient(135deg, rgba(243,200,104,.12), rgba(129,228,255,.07));
}

.sidebar-box {
  margin-top: 16px;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.04);
  padding: 14px;
}

.sidebar-box strong {
  display: block;
  margin-bottom: 8px;
  color: var(--gold-soft);
}

.sidebar-box p,
.sidebar-box li { color: #d5e5f8; }
.sidebar-box ul { margin: 0; padding-left: 18px; }

.main {
  display: grid;
  gap: 18px;
}

.hero {
  position: relative;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 34px;
  background: linear-gradient(140deg, rgba(12,21,38,.96), rgba(10,18,32,.92));
  box-shadow: var(--shadow);
  padding: 28px;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 14% 18%, rgba(243, 200, 104, .12), transparent 18%),
    radial-gradient(circle at 84% 18%, rgba(129, 228, 255, .14), transparent 18%),
    radial-gradient(circle at 80% 80%, rgba(255, 150, 197, .08), transparent 18%);
  pointer-events: none;
}

.eyebrow {
  display: inline-flex;
  gap: 8px;
  align-items: center;
  padding: 8px 14px;
  border-radius: 999px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.08);
  color: var(--gold);
  font-size: .9rem;
  margin-bottom: 16px;
}

.hero h1 {
  margin: 0;
  font-family: 'Noto Serif SC', serif;
  font-weight: 900;
  letter-spacing: -.04em;
  line-height: 1.06;
  font-size: clamp(2.2rem, 5vw, 4.5rem);
  color: var(--gold-soft);
}

.hero p {
  max-width: 900px;
  margin: 14px 0 0;
  color: #d8e5f7;
  font-size: 1.04rem;
}

.hero-badges {
  margin-top: 18px;
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.badge,
.hero-badge {
  display: inline-flex;
  gap: 8px;
  align-items: center;
  border-radius: 999px;
  padding: 8px 12px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.08);
  color: #eff6ff;
  font-size: .9rem;
}

.section {
  border: 1px solid var(--line);
  border-radius: 30px;
  background: linear-gradient(180deg, rgba(10,17,31,.88), rgba(9,16,29,.74));
  box-shadow: var(--shadow);
  padding: 24px;
}

.section-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 16px;
}

.kicker {
  color: var(--gold);
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .84rem;
  margin-bottom: 10px;
}

.section h2 {
  margin: 0;
  font-family: 'Noto Serif SC', serif;
  font-size: clamp(1.5rem, 3vw, 2.5rem);
  letter-spacing: -.03em;
  color: var(--gold-soft);
}

.section .intro {
  color: var(--muted);
  margin-top: 8px;
  max-width: 880px;
}

.grid-2,
.grid-3,
.grid-4 {
  display: grid;
  gap: 16px;
}
.grid-2 { grid-template-columns: repeat(2, minmax(0,1fr)); }
.grid-3 { grid-template-columns: repeat(3, minmax(0,1fr)); }
.grid-4 { grid-template-columns: repeat(4, minmax(0,1fr)); }

.card {
  position: relative;
  overflow: hidden;
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,.08);
  background: linear-gradient(180deg, rgba(255,255,255,.05), rgba(255,255,255,.03));
  padding: 18px;
}

.card::after {
  content: '';
  position: absolute;
  width: 180px;
  height: 180px;
  right: -60px;
  top: -90px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,.08), transparent 64%);
  pointer-events: none;
}

.kind {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 10px;
  border-radius: 999px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.08);
  font-size: .8rem;
  margin-bottom: 12px;
  letter-spacing: .05em;
  text-transform: uppercase;
  color: #d9e9fb;
}

.kind::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--cyan);
  box-shadow: 0 0 14px rgba(129, 228, 255, .7);
}

.kind.definition::before { background: var(--cyan); }
.kind.theorem::before { background: var(--gold); box-shadow: 0 0 14px rgba(243, 200, 104, .7); }
.kind.proof::before { background: var(--rose); box-shadow: 0 0 14px rgba(255, 150, 197, .7); }
.kind.exam::before { background: var(--mint); box-shadow: 0 0 14px rgba(144, 239, 207, .7); }

.card h3,
.card h4 {
  margin: 0 0 10px;
  color: var(--gold-soft);
  font-size: 1.08rem;
}

.card p,
.card li,
.card ol {
  color: #dbe7f6;
}

.card ul,
.card ol {
  margin: 10px 0 0;
  padding-left: 18px;
}

.formula {
  margin: 12px 0;
  padding: 12px 14px;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(5, 9, 17, .42);
  overflow-x: auto;
  font-size: 1rem;
}

.formula mjx-container,
.math-inline mjx-container {
  margin: 0 !important;
}

.note {
  margin-top: 10px;
  padding-left: 14px;
  border-left: 2px solid rgba(243, 200, 104, .34);
  color: #fff1c8;
}

details.fold {
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.04);
  padding: 0 16px;
}

summary {
  cursor: pointer;
  list-style: none;
  padding: 15px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  color: var(--gold-soft);
  font-weight: 700;
}
summary::-webkit-details-marker { display: none; }
.details-body { padding: 0 0 16px; color: #dbe7f6; }

.split {
  display: grid;
  grid-template-columns: 1.1fr .9fr;
  gap: 16px;
}

.timeline,
.stack {
  display: grid;
  gap: 14px;
}

.step {
  display: grid;
  grid-template-columns: 60px 1fr;
  gap: 14px;
  border-radius: 22px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.035);
  padding: 16px;
}

.num {
  width: 60px;
  height: 60px;
  display: grid;
  place-items: center;
  border-radius: 20px;
  background: linear-gradient(135deg, var(--gold), #ffefbc);
  color: #09101d;
  font-weight: 900;
}

.pager {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
}

.flash-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 14px;
}

.flashcard {
  perspective: 1200px;
  min-height: 240px;
}

.flash-inner {
  position: relative;
  min-height: 240px;
  transform-style: preserve-3d;
  transition: transform .7s ease;
  cursor: pointer;
}

.flashcard.flipped .flash-inner {
  transform: rotateY(180deg);
}

.flash-face {
  position: absolute;
  inset: 0;
  backface-visibility: hidden;
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,.08);
  background: linear-gradient(180deg, rgba(13,24,43,.94), rgba(10,16,30,.92));
  box-shadow: var(--shadow);
  padding: 18px;
}

.flash-face.back {
  transform: rotateY(180deg);
  background: linear-gradient(180deg, rgba(20,31,54,.95), rgba(11,18,33,.94));
}

.flash-face small {
  color: var(--muted);
  display: block;
  margin-bottom: 10px;
}

.checklist {
  display: grid;
  gap: 12px;
}

.checkitem {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,.08);
  background: rgba(255,255,255,.04);
  padding: 14px 16px;
}

.checkitem input {
  width: 18px;
  height: 18px;
  margin-top: 4px;
  accent-color: var(--mint);
}

.footer {
  margin-top: 18px;
  padding-top: 4px;
  text-align: center;
  color: #90a5bf;
  font-size: .92rem;
}

@media (max-width: 1180px) {
  .layout,
  .split,
  .grid-4,
  .grid-3,
  .grid-2 {
    grid-template-columns: 1fr;
  }
  .sidebar { position: static; }
}

@media (max-width: 760px) {
  .page { width: min(calc(100% - 16px), var(--max-width)); }
  .topbar-inner,
  .step {
    grid-template-columns: 1fr;
  }
  .hero,
  .section,
  .sidebar {
    padding: 18px;
  }
  .topbar-inner {
    display: grid;
  }
}
'''

JS = r'''
document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  const pageKey = body.dataset.page || '';
  document.querySelectorAll('.nav a').forEach(link => {
    const target = link.getAttribute('href');
    if (target === pageKey || target === pageKey + '.html' || target === './' + pageKey + '.html') {
      link.classList.add('active');
    }
  });

  document.querySelectorAll('[data-expand]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('details.fold').forEach(d => d.open = true);
    });
  });

  document.querySelectorAll('[data-collapse]').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('details.fold').forEach(d => d.open = false);
    });
  });

  document.querySelectorAll('.flashcard').forEach(card => {
    card.addEventListener('click', () => card.classList.toggle('flipped'));
  });

  document.querySelectorAll('[data-check]').forEach(box => {
    const key = `complex-analysis-check:${box.dataset.check}`;
    box.checked = localStorage.getItem(key) === '1';
    box.addEventListener('change', () => {
      localStorage.setItem(key, box.checked ? '1' : '0');
    });
  });
});
'''

PAGES = [
    ("index.html", "index", "总览", "总览与复习路线"),
    ("basics.html", "basics", "基本定义", "复数、区域、极限与映射"),
    ("analytic.html", "analytic", "解析与 C-R", "复导数、解析性、调和函数"),
    ("integral.html", "integral", "复积分", "曲线积分、柯西积分定理、路径无关"),
    ("formula.html", "formula", "积分公式系", "柯西积分公式、Liouville、最大模"),
    ("series.html", "series", "级数与留数", "Taylor、Laurent、奇点、留数定理"),
    ("exam.html", "exam", "题型模板", "考场判断路线与解题模板"),
    ("flashcards.html", "flashcards", "翻卡速记", "主动回忆与速记训练"),
    ("checklist.html", "checklist", "临考清单", "最后自查与冲刺建议"),
]

nav_html = '\n'.join(
    f'<a href="{filename}">{label} <span style="color: var(--muted);">· {desc}</span></a>'
    for filename, slug, label, desc in PAGES
)

page_template = Template(r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>$title</title>
  <meta name="description" content="$description" />
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']]
      },
      svg: { fontCache: 'global' }
    };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
  <link rel="stylesheet" href="assets/styles.css" />
</head>
<body data-page="$data_page">
  <div class="page">
    <div class="topbar">
      <div class="topbar-inner">
        <div class="brand">
          <small>midnight atlas</small>
          <strong>$brand</strong>
        </div>
        <div class="top-actions">
          <button class="btn" data-expand>展开本页证明卡片</button>
          <button class="btn" data-collapse>收起本页证明卡片</button>
        </div>
      </div>
    </div>

    <div class="layout">
      <aside class="sidebar">
        <h2>复变函数导航</h2>
        <p class="lead">左侧栏是整站目录，可以按专题切换页面复习。</p>
        <nav class="nav">
          $nav
        </nav>
        <div class="sidebar-box">
          <strong>复习口令</strong>
          <p>先看 <span class="math-inline">\(\text{解析性}\)</span>，再看 <span class="math-inline">\(\text{区域条件}\)</span>，最后再决定是用 <span class="math-inline">\(\text{积分定理}\)</span>、<span class="math-inline">\(\text{积分公式}\)</span> 还是 <span class="math-inline">\(\text{留数}\)</span>。</p>
        </div>
      </aside>

      <main class="main">
        <header class="hero">
          <div class="eyebrow">✦ 复变函数期末复习专题</div>
          <h1>$hero_title</h1>
          <p>$hero_text</p>
          <div class="hero-badges">
            $hero_badges
          </div>
        </header>

        $content

        <div class="section">
          <div class="pager">
            $prev_link
            $next_link
          </div>
        </div>
      </main>
    </div>

    <div class="footer">复变函数期末复习站</div>
  </div>
  <script src="assets/app.js"></script>
</body>
</html>
''')

def wrap_badges(items):
    return '\n'.join(f'<span class="hero-badge">{item}</span>' for item in items)

contents = {}

contents['index'] = {
    'title': SITE_TITLE + ' · 总览',
    'description': '复变函数期末复习站总览页。',
    'brand': '复变函数 · 总览与复习路线',
    'hero_title': '先看全局：整门课其实是一条逻辑链',
    'hero_text': '如果把复变函数拆成零散知识点，会很碎；更好的方法是记住它的主干结构：从复导数出发，经由解析性走到柯西积分定理，再到积分公式，最后落到展开、奇点和留数。',
    'hero_badges': wrap_badges(['解析主线', '积分理论', '留数方法']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">overview</div>
      <h2>复习路线图</h2>
      <p class="intro">最建议你的复习顺序不是“从第一页读到最后一页”，而是沿着这一条主线来回走：先抓结构，再回填细节。</p>
    </div>
    <div class="badge">Study Route</div>
  </div>
  <div class="grid-4">
    <article class="card">
      <div class="kind definition">Step 1</div>
      <h3>复导数与解析性</h3>
      <p>从定义 <span class="math-inline">\(f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}\)</span> 出发，理解为什么复可导非常严格。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Step 2</div>
      <h3>C-R 与调和</h3>
      <p>解析函数会满足 <span class="math-inline">\(u_x=v_y,\;u_y=-v_x\)</span>，实部和虚部常与调和函数联系在一起。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Step 3</div>
      <h3>柯西积分理论</h3>
      <p>闭路积分为零、路径无关、原函数存在，这三件事在考试里几乎总是一起出现。</p>
    </article>
    <article class="card">
      <div class="kind exam">Step 4</div>
      <h3>展开、奇点与留数</h3>
      <p>很多真正的积分题，最后都归结为找内部奇点并计算留数。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">how to use</div>
      <h2>每个页面分别看什么</h2>
      <p class="intro">现在内容分成不同页面，你复习时可以按自己的薄弱点单独进入。</p>
    </div>
    <div class="badge">Pages</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind definition">Basics</div>
      <h3>基本定义页</h3>
      <p>负责补齐最基础的对象：<span class="math-inline">\(z=x+iy\)</span>、模、辐角、区域、单连通、极限、连续。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Analytic</div>
      <h3>解析与 C-R 页</h3>
      <p>重点放在解析函数、C-R 方程、调和函数、保角映射，以及“如何判断解析”。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Integral</div>
      <h3>复积分页</h3>
      <p>负责曲线积分、ML 估计、柯西积分定理、路径无关与原函数。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Formula</div>
      <h3>积分公式系页</h3>
      <p>包含柯西积分公式、高阶导数公式、Liouville 定理、最大模原理与代数基本定理。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Series</div>
      <h3>级数与留数页</h3>
      <p>专门处理 Taylor、Laurent、奇点分类、留数计算与留数定理。</p>
    </article>
    <article class="card">
      <div class="kind exam">Exam</div>
      <h3>题型模板页</h3>
      <p>把常见题分成判断解析、闭路积分、积分公式题、奇点题、留数题来处理。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">memory cue</div>
      <h2>最值得背下来的总公式链</h2>
      <p class="intro">如果考前时间真的很紧，你至少把下面这条链记熟。</p>
    </div>
    <div class="badge">Core Chain</div>
  </div>
  <div class="stack">
    <div class="card">
      <div class="formula">\[\text{若 } f \text{ 在单连通区域 } D \text{ 内解析，且 } \gamma\subset D \text{ 为闭路，则 } \oint_\gamma f(z)\,dz=0\]</div>
      <p>这是从“解析性”走向“积分理论”的第一步，但要记得它还依赖闭路与区域条件。</p>
    </div>
    <div class="card">
      <div class="formula">\[f(z_0)=\frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z-z_0}\,dz\]</div>
      <p>这是从“积分为零”升级到“边界决定内部”的关键公式。</p>
    </div>
    <div class="card">
      <div class="formula">\[\oint_\gamma f(z)\,dz = 2\pi i\sum \operatorname{Res}(f,a_k)\]</div>
      <p>这是从“理论理解”走向“实际做题”的最终落点。</p>
    </div>
  </div>
</section>
'''
}

contents['basics'] = {
    'title': SITE_TITLE + ' · 基本定义',
    'description': '复变函数基本定义与基础对象。',
    'brand': '复变函数 · 基本定义',
    'hero_title': '基本定义：先把坐标系立稳',
    'hero_text': '很多同学做题失分，不是不会算，而是前面对象没弄清楚：区域到底是不是单连通？辐角是不是多值？极限是不是和路径有关？这一页就是把这些地基打稳。',
    'hero_badges': wrap_badges(['复数表示', '区域与路径', '极限与连续']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 01</div>
      <h2>复数的几何与代数表示</h2>
      <p class="intro">复数既是代数对象，也是平面点。很多后续直觉都来自这个双重身份。</p>
    </div>
    <div class="badge">Definitions</div>
  </div>
  <div class="grid-3">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>标准形式</h3>
      <p>设 <span class="math-inline">\(z=x+iy\)</span>，其中 <span class="math-inline">\(x,y\in\mathbb{R}\)</span> 且 <span class="math-inline">\(i^2=-1\)</span>。</p>
      <div class="formula">\[z=x+iy\]</div>
      <p>这里 <span class="math-inline">\(x\)</span> 是实部，<span class="math-inline">\(y\)</span> 是虚部。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>模与共轭</h3>
      <div class="formula">\[|z|=\sqrt{x^2+y^2}, \qquad \overline{z}=x-iy\]</div>
      <ul>
        <li><span class="math-inline">\(|z|\)</span> 表示到原点的距离</li>
        <li><span class="math-inline">\(\overline{z}\)</span> 常用于分母有复数时的化简</li>
      </ul>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>极形式</h3>
      <div class="formula">\[z=r(\cos\theta+i\sin\theta)=re^{i\theta}\]</div>
      <p>这里 <span class="math-inline">\(r=|z|\)</span>，而 <span class="math-inline">\(\theta\)</span> 是辐角。通常 <span class="math-inline">\(\arg z\)</span> 表示辐角的多值集合；若取主值，则记作 <span class="math-inline">\(\operatorname{Arg} z\in(-\pi,\pi]\)</span>。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 02</div>
      <h2>区域、闭路与单连通</h2>
      <p class="intro">后面几乎所有积分定理都会默认你先把区域条件检查完。</p>
    </div>
    <div class="badge">Region</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>区域</h3>
      <p>在复分析里，区域通常指开且连通的集合。连通表示可以在集合内部把任意两点连接起来。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>闭路与单连通</h3>
      <p><span class="math-inline">\(\gamma\)</span> 是闭路，表示起点与终点相同的分段光滑曲线。若区域中任一闭路都能连续缩成一点，则称该区域单连通。</p>
      <div class="note">带洞区域通常不是单连通，这正是很多“闭路积分不一定为零”的来源。</div>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 03</div>
      <h2>极限与连续</h2>
      <p class="intro">复极限比实函数极限更严，因为趋近方向不止左右两个，而是无穷多个。</p>
    </div>
    <div class="badge">Limit</div>
  </div>
  <div class="split">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>极限</h3>
      <div class="formula">\[\lim_{z\to z_0} f(z)=L\]</div>
      <p>这意味着不管 <span class="math-inline">\(z\)</span> 沿什么路径趋向 <span class="math-inline">\(z_0\)</span>，函数值都必须趋向同一个 <span class="math-inline">\(L\)</span>。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>连续</h3>
      <p>若 <span class="math-inline">\(\lim_{z\to z_0}f(z)=f(z_0)\)</span>，则称 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 连续。</p>
      <div class="formula">\[\lim_{z\to z_0}f(z)=f(z_0)\]</div>
    </article>
  </div>
</section>
'''
}

contents['analytic'] = {
    'title': SITE_TITLE + ' · 解析与 C-R',
    'description': '复导数、解析函数、Cauchy-Riemann 方程与调和函数。',
    'brand': '复变函数 · 解析与 C-R',
    'hero_title': '解析函数：一旦可导，结构就会突然变得很强',
    'hero_text': '复变函数的核心魅力就在这里：在复平面上“可导”不是一个轻量条件，它会逼出 C-R 方程、调和性、局部保角等一整串强性质。',
    'hero_badges': wrap_badges(['复导数', 'C-R 方程', '调和函数']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 01</div>
      <h2>复导数与解析函数</h2>
      <p class="intro">复导数的定义看起来像实导数，但因为 <span class="math-inline">\(h\)</span> 可以从任意方向趋近，所以要求严格得多。</p>
    </div>
    <div class="badge">Derivative</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>复导数</h3>
      <div class="formula">\[f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}\]</div>
      <p>注意这里的 <span class="math-inline">\(h\)</span> 是复数，而不是只沿实轴趋近。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>解析函数</h3>
      <p>若函数在 <span class="math-inline">\(z_0\)</span> 的某个邻域内处处可导，则称它在 <span class="math-inline">\(z_0\)</span> 解析。若在整个复平面解析，则称为整函数。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 02</div>
      <h2>Cauchy-Riemann 方程</h2>
      <p class="intro">这是“解析性”的第一道门。考试中最常见的基础题就是用它来判断函数在哪些地方解析。</p>
    </div>
    <div class="badge">C-R</div>
  </div>
  <div class="split">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>C-R 方程</h3>
      <p>设 <span class="math-inline">\(f(z)=u(x,y)+iv(x,y)\)</span>，若 <span class="math-inline">\(f\)</span> 在某点可导，则有</p>
      <div class="formula">\[u_x=v_y, \qquad u_y=-v_x\]</div>
      <p>若在邻域内偏导连续并满足上式，则 <span class="math-inline">\(f\)</span> 在该邻域解析。</p>
    </article>
    <details class="fold" open>
      <summary>证明思路：为什么 C-R 会出现？ <span style="color: var(--muted);">Proof Sketch</span></summary>
      <div class="details-body">
        从导数定义出发，分别令 <span class="math-inline">\(h=\Delta x\)</span> 和 <span class="math-inline">\(h=i\Delta y\)</span>，即分别沿实轴和虚轴趋近 <span class="math-inline">\(0\)</span>。由于极限必须相同，比较这两种取法得到的表达式，就会推出 C-R 方程。
        <div class="note">考试里写成“分别沿实轴与虚轴趋近并比较极限可得”通常就够了。</div>
      </div>
    </details>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 03</div>
      <h2>调和函数与保角映射</h2>
      <p class="intro">这两部分经常作为解析函数的推论出现，尤其在证明题和概念题里很常见。</p>
    </div>
    <div class="badge">Consequences</div>
  </div>
  <div class="grid-3">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>调和性</h3>
      <p>若 <span class="math-inline">\(f=u+iv\)</span> 解析，则 <span class="math-inline">\(u\)</span> 与 <span class="math-inline">\(v\)</span> 都满足 Laplace 方程：</p>
      <div class="formula">\[u_{xx}+u_{yy}=0, \qquad v_{xx}+v_{yy}=0\]</div>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>共轭调和函数</h3>
      <p>若 <span class="math-inline">\(u,v\)</span> 在某区域内具有连续一阶偏导，并满足 C-R 方程，则 <span class="math-inline">\(u+iv\)</span> 在该区域解析；这时常称 <span class="math-inline">\(v\)</span> 是 <span class="math-inline">\(u\)</span> 的一个共轭调和函数。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>保角映射</h3>
      <p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 解析且 <span class="math-inline">\(f'(z_0)\neq 0\)</span>，则它在该点附近保持角度与方向，称为保角。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 04</div>
      <h2>考场模板：怎么判断函数是否解析</h2>
      <p class="intro">这类题通常很流程化，关键在于别漏掉“邻域”和“偏导连续”。</p>
    </div>
    <div class="badge">Exam</div>
  </div>
  <div class="timeline">
    <div class="step">
      <div class="num">1</div>
      <div>
        <h3>先写成 <span class="math-inline">\(u+iv\)</span></h3>
        <p>把原函数中的实部和虚部分离出来。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">2</div>
      <div>
        <h3>算四个偏导</h3>
        <p>即 <span class="math-inline">\(u_x,u_y,v_x,v_y\)</span>，并检查 C-R 方程。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">3</div>
      <div>
        <h3>补上充分条件</h3>
        <p>若题目要求“在哪个区域解析”，记得说明偏导连续且在邻域内满足 C-R。</p>
      </div>
    </div>
  </div>
</section>
'''
}

contents['integral'] = {
    'title': SITE_TITLE + ' · 复积分',
    'description': '复积分、柯西积分定理与路径无关。',
    'brand': '复变函数 · 复积分',
    'hero_title': '复积分：沿路径累积，但先别急着算',
    'hero_text': '复积分最容易出错的地方，是一看到积分就开始参数化。真正更高效的做法是先看函数是否解析、路径是不是闭路、区域是不是单连通。',
    'hero_badges': wrap_badges(['曲线积分', 'ML 估计', '柯西积分定理']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 01</div>
      <h2>复曲线积分的定义</h2>
      <p class="intro">参数化之后，复积分最终还是回到一元实积分上。</p>
    </div>
    <div class="badge">Definition</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>参数表示</h3>
      <p>若曲线 <span class="math-inline">\(\gamma\)</span> 参数方程为 <span class="math-inline">\(z=z(t)\)</span>，其中 <span class="math-inline">\(a\le t\le b\)</span>，则</p>
      <div class="formula">\[\int_{\gamma} f(z)\,dz = \int_a^b f(z(t))z'(t)\,dt\]</div>
    </article>
    <article class="card">
      <div class="kind definition">Properties</div>
      <h3>基本性质</h3>
      <ul>
        <li>反向积分会变号</li>
        <li>可对分段光滑曲线逐段积分</li>
        <li>线性性质与实积分相似</li>
      </ul>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 02</div>
      <h2>ML 估计</h2>
      <p class="intro">这是证明某段弧线积分趋于零时最标准的工具。</p>
    </div>
    <div class="badge">Estimate</div>
  </div>
  <article class="card">
    <div class="kind theorem">Theorem</div>
    <h3>ML 不等式</h3>
    <div class="formula">\[\left|\int_{\gamma} f(z)\,dz\right| \le ML\]</div>
    <p>其中 <span class="math-inline">\(M\)</span> 是曲线上 <span class="math-inline">\(|f(z)|\)</span> 的上界，<span class="math-inline">\(L\)</span> 是路径长度。</p>
  </article>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 03</div>
      <h2>柯西积分定理与路径无关</h2>
      <p class="intro">这是复积分理论的核心。很多题一旦满足条件，就可以从“硬算”瞬间切换到“直接判零”。</p>
    </div>
    <div class="badge">Cauchy Theorem</div>
  </div>
  <div class="split">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>柯西积分定理</h3>
      <p>若 <span class="math-inline">\(f\)</span> 在单连通区域 <span class="math-inline">\(D\)</span> 内解析，且 <span class="math-inline">\(\gamma\subset D\)</span> 为闭路，则</p>
      <div class="formula">\[\oint_{\gamma} f(z)\,dz = 0\]</div>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>路径无关与原函数</h3>
      <p>若 <span class="math-inline">\(f\)</span> 在单连通区域解析，则存在原函数 <span class="math-inline">\(F\)</span>，满足 <span class="math-inline">\(F'(z)=f(z)\)</span>，并且积分只与端点有关：</p>
      <div class="formula">\[\int_a^b f(z)\,dz = F(b)-F(a)\]</div>
    </article>
  </div>
  <details class="fold" open style="margin-top:16px;">
    <summary>证明思路：柯西积分定理为什么成立？ <span style="color: var(--muted);">Proof Sketch</span></summary>
    <div class="details-body">
      设 <span class="math-inline">\(f=u+iv\)</span>，把复积分拆成两组实积分，再用 Green 公式处理。由于解析函数满足 C-R 方程，相关项互相抵消，于是闭路积分为零。
      <div class="note">一句话记忆：解析性让绕一圈的总“旋度贡献”消失。</div>
    </div>
  </details>
</section>
'''
}

contents['formula'] = {
    'title': SITE_TITLE + ' · 积分公式系',
    'description': '柯西积分公式、高阶导数公式以及典型推论。',
    'brand': '复变函数 · 积分公式系',
    'hero_title': '柯西积分公式：边界知道内部的一切',
    'hero_text': '如果说柯西积分定理是发动机，那么柯西积分公式就是推进器。很多看似独立的大定理，其实都只是它的延伸。',
    'hero_badges': wrap_badges(['柯西积分公式', '高阶导数公式', 'Liouville / 最大模']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 01</div>
      <h2>柯西积分公式本体</h2>
      <p class="intro">这是全课最值得背熟的一条公式之一。</p>
    </div>
    <div class="badge">Core Formula</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>函数值公式</h3>
      <div class="formula">\[f(z_0)=\frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z-z_0}\,dz\]</div>
      <p>其中 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(\gamma\)</span> 及其内部解析，且 <span class="math-inline">\(z_0\)</span> 在曲线内部。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>高阶导数公式</h3>
      <div class="formula">\[f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_{\gamma}\frac{f(z)}{(z-z_0)^{n+1}}\,dz\]</div>
      <p>这直接说明解析函数可以无限次求导。</p>
    </article>
  </div>
  <details class="fold" open style="margin-top:16px;">
    <summary>证明思路：为什么积分公式能“抽出函数值”？ <span style="color: var(--muted);">Proof Sketch</span></summary>
    <div class="details-body">
      把被积函数写成
      <div class="formula">\[\frac{f(z)}{z-z_0}=\frac{f(z)-f(z_0)}{z-z_0}+\frac{f(z_0)}{z-z_0}\]</div>
      第一项在 <span class="math-inline">\(z_0\)</span> 附近实际上是可去奇点，因此积分为零；第二项则恰好给出 <span class="math-inline">\(2\pi i f(z_0)\)</span>。
    </div>
  </details>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 02</div>
      <h2>典型推论</h2>
      <p class="intro">这些大定理在逻辑上并不是独立冒出来的，它们和积分公式紧密相连。</p>
    </div>
    <div class="badge">Consequences</div>
  </div>
  <div class="grid-3">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>Liouville 定理</h3>
      <div class="formula">\[f\text{ 为整函数且有界 }\Longrightarrow f\equiv \text{const}\]</div>
      <p>对足够大的圆应用高阶导数公式，并让半径趋于无穷，即可推出导数为零。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>最大模原理</h3>
      <p>非常数解析函数在区域内部不能达到模的最大值。模的极大值只能出现在边界。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>代数基本定理</h3>
      <p>若多项式 <span class="math-inline">\(P(z)\)</span> 没有零点，则 <span class="math-inline">\(1/P(z)\)</span> 是整函数且有界，从 Liouville 定理得到矛盾。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 03</div>
      <h2>考场识别：什么时候直接套公式</h2>
      <p class="intro">看到分母里有 <span class="math-inline">\((z-a)\)</span> 或其高次幂时，先别展开，先看看是不是柯西积分公式题。</p>
    </div>
    <div class="badge">Exam</div>
  </div>
  <div class="timeline">
    <div class="step">
      <div class="num">1</div>
      <div>
        <h3>先看点是否在圈内</h3>
        <p>确认 <span class="math-inline">\(a\)</span> 是否真的位于闭路内部。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">2</div>
      <div>
        <h3>再看分子是否解析</h3>
        <p>把分子整体看成 <span class="math-inline">\(f(z)\)</span>，检查它在曲线及内部是否解析。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">3</div>
      <div>
        <h3>决定是函数值公式还是导数公式</h3>
        <p>若分母为 <span class="math-inline">\((z-a)\)</span>，通常直接用函数值公式；若为 <span class="math-inline">\((z-a)^{n+1}\)</span>，多半用高阶导数公式。</p>
      </div>
    </div>
  </div>
</section>
'''
}

contents['series'] = {
    'title': SITE_TITLE + ' · 级数与留数',
    'description': 'Taylor 展开、Laurent 展开、奇点分类与留数定理。',
    'brand': '复变函数 · 级数与留数',
    'hero_title': '展开、奇点、留数：真正的解题武器库',
    'hero_text': '一旦你会把函数展开、会读主部、会提取留数，很多看起来麻烦的闭路积分题会突然变得非常短。',
    'hero_badges': wrap_badges(['Taylor', 'Laurent', '留数定理']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 01</div>
      <h2>Taylor 与 Laurent 展开</h2>
      <p class="intro">Taylor 负责“没有奇点”的局部展开，Laurent 负责“环域里带奇点”的展开。</p>
    </div>
    <div class="badge">Series</div>
  </div>
  <div class="grid-2">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>Taylor 展开</h3>
      <div class="formula">\[f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n, \qquad a_n=\frac{f^{(n)}(z_0)}{n!}\]</div>
      <p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 邻域解析，则它局部上就等于自己的幂级数。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>Laurent 展开</h3>
      <div class="formula">\[f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n+\sum_{n=1}^{\infty}\frac{b_n}{(z-z_0)^n}\]</div>
      <p>若 <span class="math-inline">\(f\)</span> 在环域 <span class="math-inline">\(r&lt;|z-z_0|&lt;R\)</span> 内解析，则可写成上述形式。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 02</div>
      <h2>奇点分类</h2>
      <p class="intro">判断奇点最稳的方法，始终是看 Laurent 主部。</p>
    </div>
    <div class="badge">Singularity</div>
  </div>
  <div class="grid-3">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>可去奇点</h3>
      <p>主部完全消失，即 Laurent 展开中没有负幂项。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>极点</h3>
      <p>主部只有有限项，例如最高到 <span class="math-inline">\((z-z_0)^{-m}\)</span>，则称 <span class="math-inline">\(z_0\)</span> 是 <span class="math-inline">\(m\)</span> 阶极点。</p>
    </article>
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>本性奇点</h3>
      <p>主部中负幂项无限多，此时函数在奇点附近的行为最复杂。</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">section 03</div>
      <h2>留数与留数定理</h2>
      <p class="intro">在 Laurent 展开里，真正能在闭路积分里“留下痕迹”的，只有一次负幂项。</p>
    </div>
    <div class="badge">Residue</div>
  </div>
  <div class="split">
    <article class="card">
      <div class="kind definition">Definition</div>
      <h3>留数</h3>
      <p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 的 Laurent 展开中写成</p>
      <div class="formula">\[f(z)=\cdots + \frac{b_1}{z-z_0}+\frac{b_2}{(z-z_0)^2}+\cdots\]</div>
      <p>则 <span class="math-inline">\(\operatorname{Res}(f,z_0)=b_1\)</span>。</p>
    </article>
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>留数定理</h3>
      <div class="formula">\[\oint_{\gamma} f(z)\,dz = 2\pi i \sum \operatorname{Res}(f,a_k)\]</div>
      <p>其中 <span class="math-inline">\(a_k\)</span> 是闭路内部的孤立奇点。</p>
    </article>
  </div>
  <div class="grid-2" style="margin-top:16px;">
    <article class="card">
      <div class="kind theorem">Theorem</div>
      <h3>常见留数公式</h3>
      <ul>
        <li>简单极点：<span class="math-inline">\(\operatorname{Res}(f,a)=\lim_{z\to a}(z-a)f(z)\)</span></li>
        <li><span class="math-inline">\(m\)</span> 阶极点：
          <div class="formula">\[\operatorname{Res}(f,a)=\frac{1}{(m-1)!}\lim_{z\to a}\frac{d^{m-1}}{dz^{m-1}}\left[(z-a)^m f(z)\right]\]</div>
        </li>
      </ul>
    </article>
    <details class="fold" open>
      <summary>证明思路：为什么只有留数会留下来？ <span style="color: var(--muted);">Proof Sketch</span></summary>
      <div class="details-body">
        在每个奇点附近挖一个小圆，把大闭路积分转成所有小圆边界积分之和。再把函数在每个小圆处作 Laurent 展开，你会发现除了 <span class="math-inline">\((z-a)^{-1}\)</span> 这一项外，别的项围一圈积分都为零。
      </div>
    </details>
  </div>
</section>
'''
}

contents['exam'] = {
    'title': SITE_TITLE + ' · 题型模板',
    'description': '复变函数常见题型与考场下手路线。',
    'brand': '复变函数 · 题型模板',
    'hero_title': '题型模板：进考场以后先分类，再动手',
    'hero_text': '复变函数最讲究“看结构”。你如果一眼就能判断这题属于哪类，后面的计算量往往会下降很多。',
    'hero_badges': wrap_badges(['先分类', '再选工具', '少走弯路']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">exam patterns</div>
      <h2>六类常见题的下手顺序</h2>
      <p class="intro">下面这些步骤几乎可以直接拿来当考场口令。</p>
    </div>
    <div class="badge">Templates</div>
  </div>
  <div class="timeline">
    <div class="step">
      <div class="num">1</div>
      <div>
        <h3>判断是否解析</h3>
        <p>写成 <span class="math-inline">\(u+iv\)</span>，检查 <span class="math-inline">\(u_x=v_y\)</span> 与 <span class="math-inline">\(u_y=-v_x\)</span>，再补偏导连续。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">2</div>
      <div>
        <h3>积分题先看能不能不算</h3>
        <p>若函数解析、路径闭合、区域合适，就优先想到 <span class="math-inline">\(\oint_\gamma f(z)\,dz=0\)</span> 或原函数存在。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">3</div>
      <div>
        <h3>看到 <span class="math-inline">\((z-a)\)</span> 分母先想积分公式</h3>
        <p>不是所有积分都要展开，有些题直接一眼就是柯西积分公式。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">4</div>
      <div>
        <h3>判断奇点类型时先看主部</h3>
        <p>主部为零、有限项、无限项，分别对应可去奇点、极点、本性奇点。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">5</div>
      <div>
        <h3>闭路积分大题往往落到留数</h3>
        <p>先找圈内奇点，再逐个算留数，最后乘上 <span class="math-inline">\(2\pi i\)</span>。</p>
      </div>
    </div>
    <div class="step">
      <div class="num">6</div>
      <div>
        <h3>展开题要先问中心和环域</h3>
        <p>同一个函数围绕不同中心、在不同环域，Laurent 展开会变得完全不一样。</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">mini advice</div>
      <h2>最容易丢分的细节</h2>
      <p class="intro">下面这些点经常不是“不会”，而是考场容易漏。</p>
    </div>
    <div class="badge">Pitfalls</div>
  </div>
  <div class="grid-3">
    <article class="card">
      <div class="kind exam">Pitfall 1</div>
      <h3>忘记检查区域是否单连通</h3>
      <p>函数解析并不自动推出任意闭路积分为零，区域条件也必须满足。</p>
    </article>
    <article class="card">
      <div class="kind exam">Pitfall 2</div>
      <h3>把“某点满足 C-R”误判成“邻域解析”</h3>
      <p>解析是邻域性质，不只是某一点上的代数关系。</p>
    </article>
    <article class="card">
      <div class="kind exam">Pitfall 3</div>
      <h3>留数题漏掉内部奇点</h3>
      <p>不是所有奇点都要算，只算路径内部的；但内部的一个都不能漏。</p>
    </article>
  </div>
</section>
'''
}

contents['flashcards'] = {
    'title': SITE_TITLE + ' · 翻卡速记',
    'description': '复变函数速记翻卡页面。',
    'brand': '复变函数 · 翻卡速记',
    'hero_title': '翻卡速记：适合考前最后十分钟',
    'hero_text': '点一下卡片就会翻面。真正有效的复习不是“看过”，而是你能不能自己说出答案。',
    'hero_badges': wrap_badges(['主动回忆', '公式速记', '临考冲刺']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">flashcards</div>
      <h2>翻卡自测</h2>
      <p class="intro">建议你先自己回答，再点开看答案。</p>
    </div>
    <div class="badge">Active Recall</div>
  </div>
  <div class="flash-grid">
    <div class="flashcard">
      <div class="flash-inner">
        <div class="flash-face front">
          <small>卡片 1</small>
          <h3>解析函数首先满足什么偏导关系？</h3>
          <p>试着自己写出完整公式。</p>
        </div>
        <div class="flash-face back">
          <small>答案</small>
          <h3>Cauchy-Riemann 方程</h3>
          <div class="formula">\[u_x=v_y, \qquad u_y=-v_x\]</div>
        </div>
      </div>
    </div>

    <div class="flashcard">
      <div class="flash-inner">
        <div class="flash-face front">
          <small>卡片 2</small>
          <h3>什么时候闭路积分直接为零？</h3>
          <p>注意别忘了区域条件。</p>
        </div>
        <div class="flash-face back">
          <small>答案</small>
          <h3>柯西积分定理</h3>
          <div class="formula">\[f\text{ 在单连通区域 } D \text{ 内解析，且 } \gamma\subset D \text{ 为闭路 }\Longrightarrow \oint_\gamma f(z)\,dz=0\]</div>
        </div>
      </div>
    </div>

    <div class="flashcard">
      <div class="flash-inner">
        <div class="flash-face front">
          <small>卡片 3</small>
          <h3>留数在展开式里到底是哪一项？</h3>
          <p>请说出它和 Laurent 展开的关系。</p>
        </div>
        <div class="flash-face back">
          <small>答案</small>
          <h3>一次负幂项的系数</h3>
          <div class="formula">\[\operatorname{Res}(f,a)=\text{Laurent 展开中 }(z-a)^{-1}\text{ 的系数}\]</div>
        </div>
      </div>
    </div>

    <div class="flashcard">
      <div class="flash-inner">
        <div class="flash-face front">
          <small>卡片 4</small>
          <h3>为什么有界整函数一定是常数？</h3>
          <p>试着自己说出所用定理。</p>
        </div>
        <div class="flash-face back">
          <small>答案</small>
          <h3>Liouville 定理</h3>
          <div class="formula">\[f\text{ 整且有界 }\Longrightarrow f\equiv \text{const}\]</div>
        </div>
      </div>
    </div>
  </div>
</section>
'''
}

contents['checklist'] = {
    'title': SITE_TITLE + ' · 临考清单',
    'description': '复变函数期末临考清单。',
    'brand': '复变函数 · 临考清单',
    'hero_title': '临考清单：最后把这些事情勾掉',
    'hero_text': '这一页不讲新知识，只做最后确认。你能把下面这些点都勾上，复习就已经比较扎实了。',
    'hero_badges': wrap_badges(['自查清单', '本地保存', '冲刺收尾']),
    'content': r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">final checklist</div>
      <h2>考前最后确认</h2>
      <p class="intro">勾选状态会保存在浏览器本地，所以你可以一点点完成。</p>
    </div>
    <div class="badge">Checklist</div>
  </div>
  <div class="checklist">
    <label class="checkitem"><input type="checkbox" data-check="b1" /><span>我能默写复导数定义 <span class="math-inline">\(f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}\)</span>，并知道为什么它比实导数严格。</span></label>
    <label class="checkitem"><input type="checkbox" data-check="b2" /><span>我能正确写出 C-R 方程，并知道它的必要性和常见充分条件。</span></label>
    <label class="checkitem"><input type="checkbox" data-check="b3" /><span>我知道什么时候能用柯西积分定理，什么时候该用柯西积分公式。</span></label>
    <label class="checkitem"><input type="checkbox" data-check="b4" /><span>我会用 Taylor / Laurent 展开判断函数在某点附近的结构。</span></label>
    <label class="checkitem"><input type="checkbox" data-check="b5" /><span>我能区分可去奇点、极点、本性奇点，并知道如何计算简单极点留数。</span></label>
    <label class="checkitem"><input type="checkbox" data-check="b6" /><span>我做积分题时会先判断解析性、区域条件和内部奇点，而不是立刻开始参数化。</span></label>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">last-minute advice</div>
      <h2>最后 30 分钟该怎么用</h2>
      <p class="intro">如果时间真的不多，建议按这个顺序来。</p>
    </div>
    <div class="badge">Plan</div>
  </div>
  <div class="timeline">
    <div class="step"><div class="num">1</div><div><h3>先翻一遍翻卡页</h3><p>确认自己能否主动说出核心结论。</p></div></div>
    <div class="step"><div class="num">2</div><div><h3>回到题型模板页</h3><p>把常见题的判断路线再过一遍。</p></div></div>
    <div class="step"><div class="num">3</div><div><h3>最后看积分公式页和留数页</h3><p>这两块往往最容易变成综合大题。</p></div></div>
  </div>
</section>
'''
}

filename_by_slug = {slug: filename for filename, slug, _, _ in PAGES}
labels_by_slug = {slug: label for filename, slug, label, _ in PAGES}
slugs = [slug for _, slug, _, _ in PAGES]

ASSETS.joinpath('styles.css').write_text(CSS, encoding='utf-8')
ASSETS.joinpath('app.js').write_text(JS, encoding='utf-8')

for idx, slug in enumerate(slugs):
    info = contents[slug]
    prev_link = '<span></span>'
    next_link = '<span></span>'
    if idx > 0:
        prev_slug = slugs[idx - 1]
        prev_link = f'<a class="link-btn" href="{filename_by_slug[prev_slug]}">← 上一页：{labels_by_slug[prev_slug]}</a>'
    if idx < len(slugs) - 1:
        next_slug = slugs[idx + 1]
        next_link = f'<a class="link-btn" href="{filename_by_slug[next_slug]}">下一页：{labels_by_slug[next_slug]} →</a>'

    html = page_template.substitute(
        title=info['title'],
        description=info['description'],
        data_page=filename_by_slug[slug],
        brand=info['brand'],
        nav=nav_html,
        hero_title=info['hero_title'],
        hero_text=info['hero_text'],
        hero_badges=info['hero_badges'],
        content=info['content'],
        prev_link=prev_link,
        next_link=next_link,
    )
    ROOT.joinpath(filename_by_slug[slug]).write_text(html, encoding='utf-8')

print('site generated')
