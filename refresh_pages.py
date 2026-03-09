from pathlib import Path
from string import Template

ROOT = Path(r"C:\Users\jielosc\.openclaw\workspace\complex-analysis-review")

PAGES = [
    ("index.html", "总览", "总览与复习路线"),
    ("basics.html", "基本定义", "复数、区域、极限与连续"),
    ("analytic.html", "解析与 C-R", "复导数、C-R、调和函数"),
    ("integral.html", "复积分", "曲线积分、柯西积分定理、路径无关"),
    ("formula.html", "积分公式系", "柯西积分公式与典型推论"),
    ("series.html", "级数与留数", "洛朗、奇点、留数定理"),
    ("exam.html", "题型模板", "考场思路与综合例题"),
    ("flashcards.html", "翻卡速记", "主动回忆与速记训练"),
    ("checklist.html", "临考清单", "最后自查与冲刺建议"),
]

NAV = "\n".join(
    f'<a href="{filename}">{label} <span style="color: var(--muted);">· {desc}</span></a>'
    for filename, label, desc in PAGES
)

TEMPLATE = Template("""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>$title</title>
  <meta name=\"description\" content=\"$desc\" />
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\\\(', '\\\\)']],
        displayMath: [['\\\\[', '\\\\]']]
      },
      svg: { fontCache: 'global' }
    };
  </script>
  <script defer src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js\"></script>
  <link rel=\"stylesheet\" href=\"assets/styles.css\" />
</head>
<body data-page=\"$filename\">
  <div class=\"page\">
    <div class=\"topbar\">
      <div class=\"topbar-inner\">
        <div class=\"brand\">
          <small>复变函数复习站</small>
          <strong>$brand</strong>
        </div>
        <div class=\"top-actions\">
          <button class=\"btn btn-compact\" data-expand aria-label=\"展开本页证明卡片\" title=\"展开本页证明卡片\"><span class=\"btn-icon\">⊞</span><span class=\"btn-label\">展开证明</span></button>
          <button class=\"btn btn-compact\" data-collapse aria-label=\"收起本页证明卡片\" title=\"收起本页证明卡片\"><span class=\"btn-icon\">⊟</span><span class=\"btn-label\">收起证明</span></button>
        </div>
      </div>
    </div>

    <div class=\"layout\">
      <aside class=\"sidebar\">
        <h2>复变函数导航</h2>
        <p class=\"lead\">左侧目录可以直接切到不同专题。建议先看总览，再按薄弱点进入对应页面。</p>
        <nav class=\"nav\">
          $nav
        </nav>
        <div class=\"sidebar-box\">
          <strong>复习口令</strong>
          <p>先看 <span class=\"math-inline\">\\(\\text{解析性}\\)</span>，再看 <span class=\"math-inline\">\\(\\text{区域条件}\\)</span>，最后再决定用 <span class=\"math-inline\">\\(\\text{柯西定理}\\)</span>、<span class=\"math-inline\">\\(\\text{积分公式}\\)</span> 还是 <span class=\"math-inline\">\\(\\text{留数}\\)</span>。</p>
        </div>
        <div class=\"sidebar-box\">
          <strong>复习建议</strong>
          <ul>
            <li>定义与定理分开记忆，再用题型把它们串起来。</li>
            <li>先判断工具，再开始计算。</li>
            <li>每页都补了典型例题，适合临考前快速回忆。</li>
          </ul>
        </div>
      </aside>

      <main class=\"main\">
        <header class=\"hero\">
          <div class=\"eyebrow\">✦ 复变函数期末复习专题</div>
          <h1>$hero_title</h1>
          <p>$hero_text</p>
          <div class=\"hero-badges\">$hero_badges</div>
        </header>

        $content

        <div class=\"section\">
          <div class=\"pager\">$prev_link $next_link</div>
        </div>
      </main>
    </div>

    <div class=\"footer\">复变函数期末复习站</div>
  </div>
  <script src=\"assets/app.js\"></script>
</body>
</html>
""")


def badges(items):
    return "\n".join(f'<span class="hero-badge">{x}</span>' for x in items)


def page(filename, title, brand, hero_title, hero_text, hero_badges, content):
    idx = [p[0] for p in PAGES].index(filename)
    prev_link = "<span></span>"
    next_link = "<span></span>"
    if idx > 0:
        prev_link = f'<a class="link-btn" href="{PAGES[idx-1][0]}">← 上一页：{PAGES[idx-1][1]}</a>'
    if idx < len(PAGES) - 1:
        next_link = f'<a class="link-btn" href="{PAGES[idx+1][0]}">下一页：{PAGES[idx+1][1]} →</a>'
    return TEMPLATE.substitute(
        title=title,
        desc=brand,
        filename=filename,
        brand=brand,
        nav=NAV,
        hero_title=hero_title,
        hero_text=hero_text,
        hero_badges=hero_badges,
        content=content,
        prev_link=prev_link,
        next_link=next_link,
    )


pages = {
    "index.html": page(
        "index.html",
        "午夜星图 · 复变函数期末复习 · 总览",
        "复变函数 · 总览与复习路线",
        "先看全局：整门课其实是一条逻辑链",
        "如果把复变函数拆成零散知识点，会很碎；更好的方法是记住它的主干结构：从复导数出发，经由解析性走到柯西积分定理，再到积分公式，最后落到展开、奇点和留数。",
        badges(["解析主线", "积分理论", "留数方法"]),
        r'''
<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">总览</div>
      <h2>复习路线图</h2>
      <p class="intro">最建议你的复习顺序不是死按页码往后翻，而是沿着一条主线循环推进：先抓结构，再回填定义、定理与题型。</p>
    </div>
    <div class="badge">复习主线</div>
  </div>
  <div class="grid-4">
    <article class="card"><div class="kind definition">主线 1</div><h3>复导数与解析性</h3><p>从定义 <span class="math-inline">\(f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}\)</span> 出发，理解为什么复可导如此严格。</p></article>
    <article class="card"><div class="kind theorem">主线 2</div><h3>C-R 与调和</h3><p>解析函数会满足 <span class="math-inline">\(u_x=v_y,\;u_y=-v_x\)</span>，而实部与虚部会自然落到调和函数框架里。</p></article>
    <article class="card"><div class="kind theorem">主线 3</div><h3>柯西积分理论</h3><p>闭路积分为零、路径无关、原函数存在，这三件事在考试里往往连着一起出现。</p></article>
    <article class="card"><div class="kind exam">主线 4</div><h3>展开、奇点与留数</h3><p>真正的综合积分题，最后常常会落到内部奇点和留数计算。</p></article>
  </div>
  <div class="hero-ribbon"><strong>最值得记住的考场口令：</strong>先看 <span class="math-inline">\(\text{解析性}\)</span>，再看 <span class="math-inline">\(\text{区域条件}\)</span>，然后判断该用 <span class="math-inline">\(\text{柯西定理}\)</span>、<span class="math-inline">\(\text{积分公式}\)</span> 还是 <span class="math-inline">\(\text{留数}\)</span>。</div>
</section>

<section class="section">
  <div class="section-head">
    <div>
      <div class="kicker">目录入口</div>
      <h2>专题入口</h2>
      <p class="intro">把这页当成目录页来用就好。每个入口都对应一个专题，可以按自己的薄弱点直接切过去。</p>
    </div>
    <div class="badge">专题入口</div>
  </div>
  <div class="portal-grid">
    <article class="card portal-card"><div class="kind definition">基础</div><h3>基本定义</h3><p class="portal-meta">复数、模、辐角、区域、单连通、极限与连续</p><p>适合先补地基，尤其是总在前提条件上丢分的时候。</p><div class="portal-cta"><a class="link-btn" href="basics.html">进入基本定义 →</a></div></article>
    <article class="card portal-card"><div class="kind theorem">解析</div><h3>解析与 C-R</h3><p class="portal-meta">复导数、解析函数、调和函数、保角映射</p><p>如果你总在“这个函数到底解不解析”这里卡住，就先看这一页。</p><div class="portal-cta"><a class="link-btn" href="analytic.html">进入解析专题 →</a></div></article>
    <article class="card portal-card"><div class="kind theorem">积分</div><h3>复积分</h3><p class="portal-meta">曲线积分、ML 估计、柯西积分定理、路径无关</p><p>主要解决“见到积分该不该算、能不能直接判零”的问题。</p><div class="portal-cta"><a class="link-btn" href="integral.html">进入复积分 →</a></div></article>
    <article class="card portal-card"><div class="kind theorem">公式</div><h3>积分公式系</h3><p class="portal-meta">柯西积分公式、高阶导数、刘维尔、最大模</p><p>适合处理分母里出现 <span class="math-inline">\((z-a)\)</span> 的公式题和推论题。</p><div class="portal-cta"><a class="link-btn" href="formula.html">进入积分公式 →</a></div></article>
    <article class="card portal-card"><div class="kind theorem">级数</div><h3>级数与留数</h3><p class="portal-meta">泰勒、洛朗、奇点分类、留数计算</p><p>综合题最有杀伤力的一页，闭路积分的大题很多最后都落在这里。</p><div class="portal-cta"><a class="link-btn" href="series.html">进入级数与留数 →</a></div></article>
    <article class="card portal-card"><div class="kind exam">题型</div><h3>题型模板</h3><p class="portal-meta">常见题的识别方式、选择工具的顺序、易错点</p><p>适合考前快速过一遍，帮你把“看题先判断什么”固定下来。</p><div class="portal-cta"><a class="link-btn" href="exam.html">进入题型模板 →</a></div></article>
  </div>
  <div class="quick-links"><a class="link-btn" href="flashcards.html">翻卡速记</a><a class="link-btn" href="checklist.html">临考清单</a></div>
</section>

<section class="section">
  <div class="section-head">
    <div><div class="kicker">记忆主线</div><h2>最值得背下来的总公式链</h2><p class="intro">如果考前时间真的很紧，你至少把下面这条链记熟，它会帮你把整门课的骨架撑起来。</p></div>
    <div class="badge">核心链条</div>
  </div>
  <div class="stack">
    <div class="card"><div class="formula">\[f \text{ 解析} \Longrightarrow \oint_\gamma f(z)\,dz=0\]</div><p>这是从“解析性”走向“积分理论”的第一步。</p></div>
    <div class="card"><div class="formula">\[f(z_0)=\frac{1}{2\pi i}\oint_\gamma \frac{f(z)}{z-z_0}\,dz\]</div><p>这是从“积分为零”升级到“边界决定内部”的关键公式。</p></div>
    <div class="card"><div class="formula">\[\oint_\gamma f(z)\,dz = 2\pi i\sum \operatorname{Res}(f,a_k)\]</div><p>这是从“理论理解”走向“实际做题”的最终落点。</p></div>
  </div>
</section>
''',
    ),
    "basics.html": page(
        "basics.html",
        "午夜星图 · 复变函数期末复习 · 基本定义",
        "复变函数 · 基本定义",
        "基本定义：先把坐标系立稳",
        "很多同学做题失分，不是不会算，而是前面对象没弄清楚：区域到底是不是单连通？辐角是不是多值？极限是不是和路径有关？这一页就是把这些地基打稳。",
        badges(["复数表示", "区域与路径", "极限与连续"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">第 1 节</div><h2>复数的几何与代数表示</h2><p class="intro">复数既是代数对象，也是平面点。很多后续直觉都来自这个双重身份。</p></div><div class="badge">定义</div></div><div class="grid-3"><article class="card"><div class="kind definition">定义</div><h3>标准形式</h3><p>设 <span class="math-inline">\(z=x+iy\)</span>，其中 <span class="math-inline">\(x,y\in\mathbb{R}\)</span> 且 <span class="math-inline">\(i^2=-1\)</span>。</p><div class="formula">\[z=x+iy\]</div><p>这里 <span class="math-inline">\(x\)</span> 是实部，<span class="math-inline">\(y\)</span> 是虚部。</p></article><article class="card"><div class="kind definition">定义</div><h3>模与共轭</h3><div class="formula">\[|z|=\sqrt{x^2+y^2}, \qquad \overline{z}=x-iy\]</div><ul><li><span class="math-inline">\(|z|\)</span> 表示到原点的距离</li><li><span class="math-inline">\(\overline{z}\)</span> 常用于分母有复数时的化简</li></ul></article><article class="card"><div class="kind definition">定义</div><h3>极形式</h3><div class="formula">\[z=r(\cos\theta+i\sin\theta)=re^{i\theta}\]</div><p>这里 <span class="math-inline">\(r=|z|\)</span>，而 <span class="math-inline">\(\theta\)</span> 是辐角。要注意 <span class="math-inline">\(\operatorname{Arg}z\)</span> 是多值的。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 2 节</div><h2>区域、闭路与单连通</h2><p class="intro">后面几乎所有积分定理都会默认你先把区域条件检查完。</p></div><div class="badge">区域</div></div><div class="grid-2"><article class="card"><div class="kind definition">定义</div><h3>区域</h3><p>在复分析里，区域通常指开且连通的集合。连通表示可以在集合内部把任意两点连接起来。</p></article><article class="card"><div class="kind definition">定义</div><h3>闭路与单连通</h3><p><span class="math-inline">\(\gamma\)</span> 是闭路，表示起点与终点相同的分段光滑曲线。若区域中任一闭路都能连续缩成一点，则称该区域单连通。</p><div class="note">带洞区域通常不是单连通，这正是很多“闭路积分不一定为零”的来源。</div></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 3 节</div><h2>极限与连续</h2><p class="intro">复极限比实函数极限更严，因为趋近方向不止左右两个，而是无穷多个。</p></div><div class="badge">极限</div></div><div class="split"><article class="card"><div class="kind definition">定义</div><h3>极限</h3><div class="formula">\[\lim_{z\to z_0} f(z)=L\]</div><p>这意味着不管 <span class="math-inline">\(z\)</span> 沿什么路径趋向 <span class="math-inline">\(z_0\)</span>，函数值都必须趋向同一个 <span class="math-inline">\(L\)</span>。</p></article><article class="card"><div class="kind definition">定义</div><h3>连续</h3><p>若 <span class="math-inline">\(\lim_{z\to z_0}f(z)=f(z_0)\)</span>，则称 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 连续。</p><div class="formula">\[\lim_{z\to z_0}f(z)=f(z_0)\]</div></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">典型例题</div><h2>典型例题</h2><p class="intro">先做这种地基题，后面的章节会顺很多。</p></div><div class="badge">典型例题</div></div><div class="example-grid"><article class="card example-card"><div class="kind exam">例题 A</div><h3>已知 <span class="math-inline">\(z=1-\sqrt{3}i\)</span>，求 <span class="math-inline">\(|z|\)</span> 与主辐角</h3><p class="tagline">先看坐标，再看象限。</p><div class="formula">\[|z|=\sqrt{1^2+(\!-\sqrt{3})^2}=2\]</div><div class="formula">\[\arg z=-\frac{\pi}{3}\]</div><ol class="solution-list"><li>点 <span class="math-inline">\((1,-\sqrt{3})\)</span> 位于第四象限。</li><li>参考角满足 <span class="math-inline">\(\tan\theta=-\sqrt{3}\)</span>。</li><li>主辐角取 <span class="math-inline">\(( -\pi,\pi ]\)</span> 中的值，所以是 <span class="math-inline">\(-\pi/3\)</span>。</li></ol></article><article class="card example-card"><div class="kind exam">例题 B</div><h3>区域 <span class="math-inline">\(0&lt;|z|&lt;1\)</span> 是否单连通？</h3><p class="tagline">看有没有“洞”。</p><p>答案：<strong>不是</strong>。</p><ol class="solution-list"><li>这个区域是去掉原点的单位圆盘。</li><li>围绕原点的闭路无法在区域内部缩成一点。</li><li>因此它不是单连通区域。</li></ol></article></div></section>
''',
    ),
    "analytic.html": page(
        "analytic.html",
        "午夜星图 · 复变函数期末复习 · 解析与 C-R",
        "复变函数 · 解析与 C-R",
        "解析函数：一旦可导，结构就会突然变得很强",
        "复变函数的核心魅力就在这里：在复平面上“可导”不是一个轻量条件，它会逼出 C-R 方程、调和性、局部保角等一整串强性质。",
        badges(["复导数", "C-R 方程", "调和函数"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">第 1 节</div><h2>复导数与解析函数</h2><p class="intro">复导数的定义看起来像实导数，但因为 <span class="math-inline">\(h\)</span> 可以从任意方向趋近，所以要求严格得多。</p></div><div class="badge">复导数</div></div><div class="grid-2"><article class="card"><div class="kind definition">定义</div><h3>复导数</h3><div class="formula">\[f'(z_0)=\lim_{h\to 0}\frac{f(z_0+h)-f(z_0)}{h}\]</div><p>注意这里的 <span class="math-inline">\(h\)</span> 是复数，而不是只沿实轴趋近。</p></article><article class="card"><div class="kind definition">定义</div><h3>解析函数</h3><p>若函数在 <span class="math-inline">\(z_0\)</span> 的某个邻域内处处可导，则称它在 <span class="math-inline">\(z_0\)</span> 解析。若在整个复平面解析，则称为整函数。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 2 节</div><h2>柯西-黎曼方程</h2><p class="intro">这是“解析性”的第一道门。考试中最常见的基础题就是用它来判断函数在哪些地方解析。</p></div><div class="badge">C-R</div></div><div class="split"><article class="card"><div class="kind theorem">定理</div><h3>C-R 方程</h3><p>设 <span class="math-inline">\(f(z)=u(x,y)+iv(x,y)\)</span>，若 <span class="math-inline">\(f\)</span> 在某点可导，则有</p><div class="formula">\[u_x=v_y, \qquad u_y=-v_x\]</div><p>若在邻域内偏导连续并满足上式，则 <span class="math-inline">\(f\)</span> 在该邻域解析。</p></article><details class="fold" open><summary>证明思路：为什么 C-R 会出现？ <span style="color: var(--muted);">证明思路</span></summary><div class="details-body">从导数定义出发，分别令 <span class="math-inline">\(h=\Delta x\)</span> 和 <span class="math-inline">\(h=i\Delta y\)</span>，即分别沿实轴和虚轴趋近 <span class="math-inline">\(0\)</span>。由于极限必须相同，比较这两种取法得到的表达式，就会推出 C-R 方程。<div class="note">考试里写成“分别沿实轴与虚轴趋近并比较极限可得”通常就够了。</div></div></details></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 3 节</div><h2>调和函数与保角映射</h2><p class="intro">这两部分经常作为解析函数的推论出现，尤其在证明题和概念题里很常见。</p></div><div class="badge">重要推论</div></div><div class="grid-3"><article class="card"><div class="kind theorem">定理</div><h3>调和性</h3><p>若 <span class="math-inline">\(f=u+iv\)</span> 解析，则 <span class="math-inline">\(u\)</span> 与 <span class="math-inline">\(v\)</span> 都满足 Laplace 方程：</p><div class="formula">\[u_{xx}+u_{yy}=0, \qquad v_{xx}+v_{yy}=0\]</div></article><article class="card"><div class="kind definition">定义</div><h3>共轭调和函数</h3><p>若 <span class="math-inline">\(u\)</span> 与 <span class="math-inline">\(v\)</span> 满足 C-R 方程，则称 <span class="math-inline">\(v\)</span> 是 <span class="math-inline">\(u\)</span> 的一个共轭调和函数，此时 <span class="math-inline">\(u+iv\)</span> 解析。</p></article><article class="card"><div class="kind definition">定义</div><h3>保角映射</h3><p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 解析且 <span class="math-inline">\(f'(z_0)\neq 0\)</span>，则它在该点附近保持角度与方向，称为保角。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">典型例题</div><h2>典型例题</h2><p class="intro">判断解析的题非常适合通过例题训练手感。</p></div><div class="badge">典型例题</div></div><div class="example-grid"><article class="card example-card"><div class="kind exam">例题 A</div><h3>证明 <span class="math-inline">\(f(z)=z^2\)</span> 在全平面解析</h3><p class="tagline">把它改写成 <span class="math-inline">\(u+iv\)</span> 再检查 C-R。</p><div class="formula">\[z^2=(x+iy)^2=(x^2-y^2)+i(2xy)\]</div><ol class="solution-list"><li>取 <span class="math-inline">\(u=x^2-y^2\)</span>，<span class="math-inline">\(v=2xy\)</span>。</li><li>则 <span class="math-inline">\(u_x=2x=v_y\)</span>，<span class="math-inline">\(u_y=-2y=-v_x\)</span>。</li><li>偏导处处连续，所以 <span class="math-inline">\(f(z)=z^2\)</span> 在全平面解析。</li></ol></article><article class="card example-card"><div class="kind exam">例题 B</div><h3>判断 <span class="math-inline">\(f(z)=\overline{z}\)</span> 是否解析</h3><p class="tagline">这是最经典的反例之一。</p><div class="formula">\[\overline{z}=x-iy\]</div><ol class="solution-list"><li>取 <span class="math-inline">\(u=x\)</span>，<span class="math-inline">\(v=-y\)</span>。</li><li>则 <span class="math-inline">\(u_x=1\)</span>，但 <span class="math-inline">\(v_y=-1\)</span>，所以 <span class="math-inline">\(u_x\neq v_y\)</span>。</li><li>因此它在任何点都不满足 C-R 方程，所以 nowhere analytic。</li></ol></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 4 节</div><h2>考场模板：怎么判断函数是否解析</h2><p class="intro">这类题通常很流程化，关键在于别漏掉“邻域”和“偏导连续”。</p></div><div class="badge">题型</div></div><div class="timeline"><div class="step"><div class="num">1</div><div><h3>先写成 <span class="math-inline">\(u+iv\)</span></h3><p>把原函数中的实部和虚部分离出来。</p></div></div><div class="step"><div class="num">2</div><div><h3>算四个偏导</h3><p>即 <span class="math-inline">\(u_x,u_y,v_x,v_y\)</span>，并检查 C-R 方程。</p></div></div><div class="step"><div class="num">3</div><div><h3>补上充分条件</h3><p>若题目要求“在哪个区域解析”，记得说明偏导连续且在邻域内满足 C-R。</p></div></div></div></section>
''',
    ),
    "integral.html": page(
        "integral.html",
        "午夜星图 · 复变函数期末复习 · 复积分",
        "复变函数 · 复积分",
        "复积分：沿路径累积，但先别急着算",
        "复积分最容易出错的地方，是一看到积分就开始参数化。真正更高效的做法是先看函数是否解析、路径是不是闭路、区域是不是单连通。",
        badges(["曲线积分", "ML 估计", "柯西积分定理"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">第 1 节</div><h2>复曲线积分的定义</h2><p class="intro">参数化之后，复积分最终还是回到一元实积分上。</p></div><div class="badge">定义</div></div><div class="grid-2"><article class="card"><div class="kind definition">定义</div><h3>参数表示</h3><p>若曲线 <span class="math-inline">\(\gamma\)</span> 参数方程为 <span class="math-inline">\(z=z(t)\)</span>，其中 <span class="math-inline">\(a\le t\le b\)</span>，则</p><div class="formula">\[\int_{\gamma} f(z)\,dz = \int_a^b f(z(t))z'(t)\,dt\]</div></article><article class="card"><div class="kind definition">性质</div><h3>基本性质</h3><ul><li>反向积分会变号</li><li>可对分段光滑曲线逐段积分</li><li>线性性质与实积分相似</li></ul></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 2 节</div><h2>ML 估计</h2><p class="intro">这是证明某段弧线积分趋于零时最标准的工具。</p></div><div class="badge">估计</div></div><article class="card"><div class="kind theorem">定理</div><h3>ML 不等式</h3><div class="formula">\[\left|\int_{\gamma} f(z)\,dz\right| \le ML\]</div><p>其中 <span class="math-inline">\(M\)</span> 是曲线上 <span class="math-inline">\(|f(z)|\)</span> 的上界，<span class="math-inline">\(L\)</span> 是路径长度。</p></article></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 3 节</div><h2>柯西积分定理与路径无关</h2><p class="intro">这是复积分理论的核心。很多题一旦满足条件，就可以从“硬算”瞬间切换到“直接判零”。</p></div><div class="badge">柯西定理</div></div><div class="split"><article class="card"><div class="kind theorem">定理</div><h3>柯西积分定理</h3><p>若 <span class="math-inline">\(f\)</span> 在单连通区域 <span class="math-inline">\(D\)</span> 内解析，且 <span class="math-inline">\(\gamma\subset D\)</span> 为闭路，则</p><div class="formula">\[\oint_{\gamma} f(z)\,dz = 0\]</div></article><article class="card"><div class="kind theorem">定理</div><h3>路径无关与原函数</h3><p>若 <span class="math-inline">\(f\)</span> 在单连通区域解析，则存在原函数 <span class="math-inline">\(F\)</span>，满足 <span class="math-inline">\(F'(z)=f(z)\)</span>，并且积分只与端点有关：</p><div class="formula">\[\int_a^b f(z)\,dz = F(b)-F(a)\]</div></article></div><details class="fold" open style="margin-top:16px;"><summary>证明思路：柯西积分定理为什么成立？ <span style="color: var(--muted);">证明思路</span></summary><div class="details-body">设 <span class="math-inline">\(f=u+iv\)</span>，把复积分拆成两组实积分，再用 Green 公式处理。由于解析函数满足 C-R 方程，相关项互相抵消，于是闭路积分为零。<div class="note">一句话记忆：解析性让绕一圈的总“旋度贡献”消失。</div></div></details></section>
<section class="section"><div class="section-head"><div><div class="kicker">典型例题</div><h2>典型例题</h2><p class="intro">这类题的关键是先判断有没有必要真的去算。</p></div><div class="badge">典型例题</div></div><div class="example-grid"><article class="card example-card"><div class="kind exam">例题 A</div><h3>计算 <span class="math-inline">\(\oint_{|z|=1} z^3\,dz\)</span></h3><p class="tagline">先别参数化，先看解析性。</p><ol class="solution-list"><li><span class="math-inline">\(z^3\)</span> 是整函数，在整个复平面解析。</li><li>曲线 <span class="math-inline">\(|z|=1\)</span> 是闭路，内部区域单连通。</li><li>由柯西积分定理，<div class="formula">\[\oint_{|z|=1} z^3\,dz=0\]</div></li></ol></article><article class="card example-card"><div class="kind exam">例题 B</div><h3>计算 <span class="math-inline">\(\int_0^{1+i} 2z\,dz\)</span></h3><p class="tagline">优先找原函数。</p><ol class="solution-list"><li><span class="math-inline">\(f(z)=2z\)</span> 的一个原函数是 <span class="math-inline">\(F(z)=z^2\)</span>。</li><li>因此积分与路径无关，直接代端点。</li></ol><div class="formula">\[\int_0^{1+i}2z\,dz=(1+i)^2=2i\]</div></article></div></section>
''',
    ),
    "formula.html": page(
        "formula.html",
        "午夜星图 · 复变函数期末复习 · 积分公式系",
        "复变函数 · 积分公式系",
        "柯西积分公式：边界知道内部的一切",
        "如果说柯西积分定理是发动机，那么柯西积分公式就是推进器。很多看似独立的大定理，其实都只是它的延伸。",
        badges(["柯西积分公式", "高阶导数公式", "刘维尔 / 最大模"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">第 1 节</div><h2>柯西积分公式本体</h2><p class="intro">这是全课最值得背熟的一条公式之一。</p></div><div class="badge">核心公式</div></div><div class="grid-2"><article class="card"><div class="kind theorem">定理</div><h3>函数值公式</h3><div class="formula">\[f(z_0)=\frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z-z_0}\,dz\]</div><p>其中 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(\gamma\)</span> 及其内部解析，且 <span class="math-inline">\(z_0\)</span> 在曲线内部。</p></article><article class="card"><div class="kind theorem">定理</div><h3>高阶导数公式</h3><div class="formula">\[f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_{\gamma}\frac{f(z)}{(z-z_0)^{n+1}}\,dz\]</div><p>这直接说明解析函数可以无限次求导。</p></article></div><details class="fold" open style="margin-top:16px;"><summary>证明思路：为什么积分公式能“抽出函数值”？ <span style="color: var(--muted);">证明思路</span></summary><div class="details-body">把被积函数写成<div class="formula">\[\frac{f(z)}{z-z_0}=\frac{f(z)-f(z_0)}{z-z_0}+\frac{f(z_0)}{z-z_0}\]</div>第一项在 <span class="math-inline">\(z_0\)</span> 附近实际上是可去奇点，因此积分为零；第二项则恰好给出 <span class="math-inline">\(2\pi i f(z_0)\)</span>。</div></details></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 2 节</div><h2>典型推论</h2><p class="intro">这些大定理在逻辑上并不是独立冒出来的，它们和积分公式紧密相连。</p></div><div class="badge">重要推论</div></div><div class="grid-3"><article class="card"><div class="kind theorem">定理</div><h3>刘维尔定理</h3><div class="formula">\[f\text{ 为整函数且有界 }\Longrightarrow f\equiv \text{const}\]</div><p>对足够大的圆应用高阶导数公式，并让半径趋于无穷，即可推出导数为零。</p></article><article class="card"><div class="kind theorem">定理</div><h3>最大模原理</h3><p>非常数解析函数在区域内部不能达到模的最大值。模的极大值只能出现在边界。</p></article><article class="card"><div class="kind theorem">定理</div><h3>代数基本定理</h3><p>若多项式 <span class="math-inline">\(P(z)\)</span> 没有零点，则 <span class="math-inline">\(1/P(z)\)</span> 是整函数且有界，从 刘维尔定理得到矛盾。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">典型例题</div><h2>典型例题</h2><p class="intro">一旦识别出是积分公式题，计算会非常短。</p></div><div class="badge">典型例题</div></div><div class="example-grid"><article class="card example-card"><div class="kind exam">例题 A</div><h3>计算 <span class="math-inline">\(\oint_{|z|=2}\frac{e^z}{z}\,dz\)</span></h3><p class="tagline">直接套函数值公式。</p><ol class="solution-list"><li>令 <span class="math-inline">\(f(z)=e^z\)</span>，它在全平面解析。</li><li>点 <span class="math-inline">\(0\)</span> 位于 <span class="math-inline">\(|z|=2\)</span> 内部。</li><li>由柯西积分公式，</li></ol><div class="formula">\[\oint_{|z|=2}\frac{e^z}{z}\,dz = 2\pi i\]</div></article><article class="card example-card"><div class="kind exam">例题 B</div><h3>计算 <span class="math-inline">\(\oint_{|z|=2}\frac{e^z}{z^3}\,dz\)</span></h3><p class="tagline">这是高阶导数公式的标准形状。</p><ol class="solution-list"><li>写成 <span class="math-inline">\(\oint \frac{f(z)}{(z-0)^{2+1}}dz\)</span>，其中 <span class="math-inline">\(f(z)=e^z\)</span>。</li><li>由高阶导数公式，<div class="formula">\[\oint_{|z|=2}\frac{e^z}{z^3}\,dz = \frac{2\pi i}{2!}f''(0)\]</div></li><li>因为 <span class="math-inline">\(f''(0)=1\)</span>，所以结果是 <span class="math-inline">\(\pi i\)</span>。</li></ol></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 3 节</div><h2>考场识别：什么时候直接套公式</h2><p class="intro">看到分母里有 <span class="math-inline">\((z-a)\)</span> 或其高次幂时，先别展开，先看看是不是柯西积分公式题。</p></div><div class="badge">题型</div></div><div class="timeline"><div class="step"><div class="num">1</div><div><h3>先看点是否在圈内</h3><p>确认 <span class="math-inline">\(a\)</span> 是否真的位于闭路内部。</p></div></div><div class="step"><div class="num">2</div><div><h3>再看分子是否解析</h3><p>把分子整体看成 <span class="math-inline">\(f(z)\)</span>，检查它在曲线及内部是否解析。</p></div></div><div class="step"><div class="num">3</div><div><h3>决定是函数值公式还是导数公式</h3><p>若分母为 <span class="math-inline">\((z-a)\)</span>，通常直接用函数值公式；若为 <span class="math-inline">\((z-a)^{n+1}\)</span>，多半用高阶导数公式。</p></div></div></div></section>
''',
    ),
    "series.html": page(
        "series.html",
        "午夜星图 · 复变函数期末复习 · 级数与留数",
        "复变函数 · 级数与留数",
        "展开、奇点、留数：真正的解题武器库",
        "一旦你会把函数展开、会读主部、会提取留数，很多看起来麻烦的闭路积分题会突然变得非常短。",
        badges(["泰勒", "洛朗", "留数定理"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">第 1 节</div><h2>泰勒 与 洛朗 展开</h2><p class="intro">泰勒 负责“没有奇点”的局部展开，洛朗 负责“环域里带奇点”的展开。</p></div><div class="badge">级数</div></div><div class="grid-2"><article class="card"><div class="kind theorem">定理</div><h3>泰勒 展开</h3><div class="formula">\[f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n, \qquad a_n=\frac{f^{(n)}(z_0)}{n!}\]</div><p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 邻域解析，则它局部上就等于自己的幂级数。</p></article><article class="card"><div class="kind theorem">定理</div><h3>洛朗 展开</h3><div class="formula">\[f(z)=\sum_{n=0}^{\infty} a_n(z-z_0)^n+\sum_{n=1}^{\infty}\frac{b_n}{(z-z_0)^n}\]</div><p>若 <span class="math-inline">\(f\)</span> 在环域 <span class="math-inline">\(r&lt;|z-z_0|&lt;R\)</span> 内解析，则可写成上述形式。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 2 节</div><h2>奇点分类</h2><p class="intro">判断奇点最稳的方法，始终是看 洛朗 主部。</p></div><div class="badge">奇点</div></div><div class="grid-3"><article class="card"><div class="kind definition">定义</div><h3>可去奇点</h3><p>主部完全消失，即 洛朗 展开中没有负幂项。</p></article><article class="card"><div class="kind definition">定义</div><h3>极点</h3><p>主部只有有限项，例如最高到 <span class="math-inline">\((z-z_0)^{-m}\)</span>，则称 <span class="math-inline">\(z_0\)</span> 是 <span class="math-inline">\(m\)</span> 阶极点。</p></article><article class="card"><div class="kind definition">定义</div><h3>本性奇点</h3><p>主部中负幂项无限多，此时函数在奇点附近的行为最复杂。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">第 3 节</div><h2>留数与留数定理</h2><p class="intro">在 洛朗 展开里，真正能在闭路积分里“留下痕迹”的，只有一次负幂项。</p></div><div class="badge">留数</div></div><div class="split"><article class="card"><div class="kind definition">定义</div><h3>留数</h3><p>若 <span class="math-inline">\(f\)</span> 在 <span class="math-inline">\(z_0\)</span> 的 洛朗 展开中写成</p><div class="formula">\[f(z)=\cdots + \frac{b_1}{z-z_0}+\frac{b_2}{(z-z_0)^2}+\cdots\]</div><p>则 <span class="math-inline">\(\operatorname{Res}(f,z_0)=b_1\)</span>。</p></article><article class="card"><div class="kind theorem">定理</div><h3>留数定理</h3><div class="formula">\[\oint_{\gamma} f(z)\,dz = 2\pi i \sum \operatorname{Res}(f,a_k)\]</div><p>其中 <span class="math-inline">\(a_k\)</span> 是闭路内部的孤立奇点。</p></article></div><div class="grid-2" style="margin-top:16px;"><article class="card"><div class="kind theorem">定理</div><h3>常见留数公式</h3><ul><li>简单极点：<span class="math-inline">\(\operatorname{Res}(f,a)=\lim_{z\to a}(z-a)f(z)\)</span></li><li><span class="math-inline">\(m\)</span> 阶极点：<div class="formula">\[\operatorname{Res}(f,a)=\frac{1}{(m-1)!}\lim_{z\to a}\frac{d^{m-1}}{dz^{m-1}}\left[(z-a)^m f(z)\right]\]</div></li></ul></article><details class="fold" open><summary>证明思路：为什么只有留数会留下来？ <span style="color: var(--muted);">证明思路</span></summary><div class="details-body">在每个奇点附近挖一个小圆，把大闭路积分转成所有小圆边界积分之和。再把函数在每个小圆处作 洛朗 展开，你会发现除了 <span class="math-inline">\((z-a)^{-1}\)</span> 这一项外，别的项围一圈积分都为零。</div></details></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">典型例题</div><h2>典型例题</h2><p class="intro">这一页的例题建议你自己先展开一遍，再对答案。</p></div><div class="badge">典型例题</div></div><div class="example-grid"><article class="card example-card"><div class="kind exam">例题 A</div><h3>求 <span class="math-inline">\(\frac{1}{1-z}\)</span> 在 <span class="math-inline">\(|z|&lt;1\)</span> 的 泰勒 展开</h3><p class="tagline">直接使用几何级数。</p><div class="formula">\[\frac{1}{1-z}=\sum_{n=0}^{\infty} z^n, \qquad |z|&lt;1\]</div><p>所以它在 <span class="math-inline">\(0\)</span> 附近的 泰勒 展开就是 <span class="math-inline">\(1+z+z^2+\cdots\)</span>。</p></article><article class="card example-card"><div class="kind exam">例题 B</div><h3>求 <span class="math-inline">\(\frac{1}{z(z-1)}\)</span> 在 <span class="math-inline">\(0&lt;|z|&lt;1\)</span> 的 洛朗 展开与 <span class="math-inline">\(\operatorname{Res}(f,0)\)</span></h3><p class="tagline">先做部分分式，再按环域展开。</p><div class="formula">\[\frac{1}{z(z-1)}=-\frac{1}{z}+\frac{1}{z-1}\]</div><div class="formula">\[\frac{1}{z-1}=-\frac{1}{1-z}=-(1+z+z^2+\cdots),\qquad |z|&lt;1\]</div><div class="formula">\[\frac{1}{z(z-1)}=-\frac{1}{z}-1-z-z^2-\cdots\]</div><p>因此 <span class="math-inline">\((z-0)^{-1}\)</span> 项系数是 <span class="math-inline">\(-1\)</span>，所以 <span class="math-inline">\(\operatorname{Res}(f,0)=-1\)</span>。</p></article></div></section>
''',
    ),
    "exam.html": page(
        "exam.html",
        "午夜星图 · 复变函数期末复习 · 题型模板",
        "复变函数 · 题型模板",
        "题型模板：进考场以后先分类，再动手",
        "复变函数最讲究“看结构”。你如果一眼就能判断这题属于哪类，后面的计算量往往会下降很多。",
        badges(["先分类", "再选工具", "少走弯路"]),
        r'''
<section class="section"><div class="section-head"><div><div class="kicker">题型模板</div><h2>六类常见题的下手顺序</h2><p class="intro">下面这些步骤几乎可以直接拿来当考场口令。</p></div><div class="badge">题型模板</div></div><div class="timeline"><div class="step"><div class="num">1</div><div><h3>判断是否解析</h3><p>写成 <span class="math-inline">\(u+iv\)</span>，检查 <span class="math-inline">\(u_x=v_y\)</span> 与 <span class="math-inline">\(u_y=-v_x\)</span>，再补偏导连续。</p></div></div><div class="step"><div class="num">2</div><div><h3>积分题先看能不能不算</h3><p>若函数解析、路径闭合、区域合适，就优先想到 <span class="math-inline">\(\oint_\gamma f(z)\,dz=0\)</span> 或原函数存在。</p></div></div><div class="step"><div class="num">3</div><div><h3>看到 <span class="math-inline">\((z-a)\)</span> 分母先想积分公式</h3><p>不是所有积分都要展开，有些题直接一眼就是柯西积分公式。</p></div></div><div class="step"><div class="num">4</div><div><h3>判断奇点类型时先看主部</h3><p>主部为零、有限项、无限项，分别对应可去奇点、极点、本性奇点。</p></div></div><div class="step"><div class="num">5</div><div><h3>闭路积分大题往往落到留数</h3><p>先找圈内奇点，再逐个算留数，最后乘上 <span class="math-inline">\(2\pi i\)</span>。</p></div></div><div class="step"><div class="num">6</div><div><h3>展开题要先问中心和环域</h3><p>同一个函数围绕不同中心、在不同环域，洛朗 展开会变得完全不一样。</p></div></div></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">易错点</div><h2>最容易丢分的细节</h2><p class="intro">下面这些点经常不是“不会”，而是考场容易漏。</p></div><div class="badge">易错点</div></div><div class="grid-3"><article class="card"><div class="kind exam">Pitfall 1</div><h3>忘记检查区域是否单连通</h3><p>函数解析并不自动推出任意闭路积分为零，区域条件也必须满足。</p></article><article class="card"><div class="kind exam">Pitfall 2</div><h3>把“某点满足 C-R”误判成“邻域解析”</h3><p>解析是邻域性质，不只是某一点上的代数关系。</p></article><article class="card"><div class="kind exam">Pitfall 3</div><h3>留数题漏掉内部奇点</h3><p>不是所有奇点都要算，只算路径内部的；但内部的一个都不能漏。</p></article></div></section>
<section class="section"><div class="section-head"><div><div class="kicker">综合例题</div><h2>综合例题：看题后如何选工具</h2><p class="intro">这类例题的重点不只是算对，更是要看出为什么应该选“留数”这条路。</p></div><div class="badge">题型ple</div></div><article class="card example-card"><div class="kind exam">综合例题</div><h3>计算 <span class="math-inline">\(\oint_{|z|=2}\frac{z+2}{z(z-1)}\,dz\)</span></h3><p class="tagline">闭路积分 + 圈内有孤立奇点，优先考虑留数。</p><ol class="solution-list"><li>路径内部奇点是 <span class="math-inline">\(z=0\)</span> 与 <span class="math-inline">\(z=1\)</span>。</li><li>在 <span class="math-inline">\(z=0\)</span> 处，<div class="formula">\[\operatorname{Res}(f,0)=\lim_{z\to 0}\frac{z+2}{z-1}=-2\]</div></li><li>在 <span class="math-inline">\(z=1\)</span> 处，<div class="formula">\[\operatorname{Res}(f,1)=\lim_{z\to 1}\frac{z+2}{z}=3\]</div></li><li>留数和为 <span class="math-inline">\(1\)</span>，所以</li></ol><div class="formula">\[\oint_{|z|=2}\frac{z+2}{z(z-1)}\,dz = 2\pi i\]</div></article></section>
''',
    ),
}

for name, html in pages.items():
    ROOT.joinpath(name).write_text(html, encoding="utf-8")

print("pages refreshed")
