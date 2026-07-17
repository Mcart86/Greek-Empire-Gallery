#!/usr/bin/env python3
import os

DIR = "/home/claude/greek-empire-gallery"

CATS = [
    ("Spring Break",       "spring-break",       "Your chapter's spring break run needs a shirt that keeps up."),
    ("Winter",             "winter",              "Cold weather, warm chapter. Custom winter apparel built for the season."),
    ("Western",            "western",             "Your letters. Their hats. Custom western theme shirts done right."),
    ("Sixties",            "sixties",             "Groovy chapter, iconic shirts. The sixties theme, elevated."),
    ("Halloween",          "halloween",           "The annual costume party deserves a design that haunts them all semester."),
    ("Formal",             "formal",              "Chapter formals done right — from the bid to the bow tie."),
    ("Dog & Puppy",        "dog-and-puppy",       "Philanthropy events, big little reveals, and every excuse to put a dog on a shirt."),
    ("Christmas",          "christmas",           "Holiday chapter events. Custom apparel that actually looks good."),
    ("5K Run",             "5k-run",              "Philanthropy runs, campus 5Ks, and everything in between."),
    ("Rush",               "rush",                "First impressions are everything. Make yours last four years."),
    ("Sports",             "sports",              "From intramurals to watch parties — custom sports apparel for your chapter."),
    ("Fraternity",         "fraternity",          "Chapter gear that represents who you are — not just where you're from."),
    ("Sisterhood Retreat", "sisterhood-retreat",  "The weekend that brings chapters together. Custom apparel for every retreat."),
    ("Cowgirl",            "cowgirl",             "Boots up. Custom cowgirl theme shirts built for your chapter's biggest events."),
    ("Bid Day",            "bid-day",             "The best day of the year deserves a shirt to prove it."),
    ("Recruitment",        "recruitment",         "Your chapter's first impression. Make it count."),
    ("Panhellenic",        "panhellenic",         "Custom apparel for Panhellenic events, councils, and community."),
    ("Philanthropy",       "philanthropy",        "Do good. Look good. Give back in custom apparel that means something."),
    ("Big Little",         "big-little",          "The reveal. The gift. The shirt they'll keep forever."),
    ("Beach",              "beach",               "Sun, sand, and your letters. Beach theme shirts built for the culture."),
    ("Shamrock",           "shamrock",            "St. Patrick's Day chapter events deserve a shirt actually worth keeping."),
    ("Mixers",             "mixers",              "Social events, mixer nights, and the shirts everyone talks about the next day."),
    ("Mom's Day",          "moms-day",            "Your mom's weekend deserves custom apparel she'll actually wear home."),
    ("Weekend Getaway",    "weekend-getaway",     "Chapter retreats and road trips deserve merch to match the memory."),
]

DESIGN_LABELS = [
    "Classic Design","Letters Edition","Vintage Print","Bold Script",
    "Modern Design","Premium Edition","Heritage Print","Signature Edition",
    "Arch Design","Block Letter Print","Crest Edition","Script Design",
]

MEANDER_URL = "data:image/svg+xml,%3Csvg width='40' height='12' viewBox='0 0 40 12' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 6h6V0h8v6h2V0h8v8h-6v4h-2v-4h-8v6H0z' fill='rgba(184,150,62,0.18)'/%3E%3C/svg%3E"
MEANDER_DARK_URL = "data:image/svg+xml,%3Csvg width='40' height='12' viewBox='0 0 40 12' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 6h6V0h8v6h2V0h8v8h-6v4h-2v-4h-8v6H0z' fill='rgba(184,150,62,0.06)'/%3E%3C/svg%3E"

COL_SVG_DARK = '<svg width="32" height="32" viewBox="0 0 44 44" fill="none" style="opacity:0.18"><rect x="6" y="38" width="32" height="3" fill="#3D2A0A"/><rect x="10" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="20" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="30" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="6" y="6" width="32" height="4" fill="#3D2A0A"/><rect x="4" y="3" width="36" height="3" fill="#3D2A0A"/></svg>'

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
:root{--obsidian:#0A0A0A;--gold:#B8963E;--gold-lt:#D4AF60;--cream:#F0EBE0;--muted:#5C5750;--border:rgba(184,150,62,0.2);--card:#111111;}
body{background:var(--obsidian);color:var(--cream);font-family:'DM Sans',sans-serif;min-height:100vh;}
.meander{width:100%;height:12px;background-image:url('""" + MEANDER_URL + """');background-repeat:repeat-x;}
nav{display:flex;justify-content:space-between;align-items:center;padding:22px 60px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,10,10,0.97);backdrop-filter:blur(10px);z-index:100;}
.nav-logo{display:flex;align-items:center;text-decoration:none;}
.nav-logo img{height:52px;width:auto;}
.nav-back{font-size:12px;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);text-decoration:none;transition:color .2s;}
.nav-back:hover{color:var(--cream);}
.eyebrow{font-size:11px;font-weight:500;letter-spacing:0.28em;text-transform:uppercase;color:var(--gold);margin-bottom:18px;}
.rule{width:36px;height:1px;background:var(--gold);margin:22px auto;}
.hero{text-align:center;padding:88px 60px 72px;border-bottom:1px solid var(--border);}
.hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(44px,6vw,80px);font-weight:700;line-height:1;background:linear-gradient(135deg,#7A5010 0%,#C4881A 25%,#F0C840 50%,#C4901C 75%,#8B6212 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero-sub{font-size:14px;font-weight:300;color:var(--muted);font-style:italic;}
.cat-bg{background:#FFFFFF;}
.cat-section{padding:64px 60px 80px;max-width:1280px;margin:0 auto;}
.cat-count{font-size:11px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;color:#B8963E;margin-bottom:36px;}
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);}
.cat-item{font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:500;color:#1A1A1A;text-decoration:none;padding:16px 16px 16px 0;border-bottom:1px solid rgba(0,0,0,0.08);display:flex;align-items:center;transition:color .2s,padding-left .2s;}
.cat-item:before{content:'— ';font-size:14px;color:var(--gold);opacity:0;width:0;overflow:hidden;transition:opacity .2s,width .2s;white-space:nowrap;}
.cat-item:hover{color:var(--gold);padding-left:4px;}
.cat-item:hover:before{opacity:1;width:22px;}
.cta{text-align:center;padding:72px 60px 80px;border-top:1px solid var(--border);}
.cta h2{font-family:'Cormorant Garamond',serif;font-size:clamp(30px,4vw,48px);font-weight:600;color:var(--cream);margin-bottom:12px;}
.cta p{font-size:14px;color:var(--muted);margin-bottom:32px;}
.cta-link{display:inline-block;padding:15px 40px;background:var(--gold);color:var(--obsidian);font-family:'DM Sans',sans-serif;font-size:11px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;text-decoration:none;transition:background .2s;}
.cta-link:hover{background:var(--gold-lt);}
footer{padding:28px 60px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;}
.foot-brand{font-family:'Cormorant Garamond',serif;font-size:14px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;color:var(--muted);}
.foot-tag{font-size:12px;color:var(--muted);font-style:italic;}
.cat-hero-banner{position:relative;padding:120px 60px 88px;text-align:center;background:linear-gradient(160deg,#070707 0%,#100E04 100%);overflow:hidden;border-bottom:1px solid var(--border);}
.cat-hero-banner::before{content:'';position:absolute;inset:0;background-image:url('""" + MEANDER_DARK_URL + """');background-repeat:repeat;background-size:40px 12px;pointer-events:none;}
.cat-hero-content{position:relative;z-index:1;}
.cat-hero-banner h1{font-family:'Cormorant Garamond',serif;font-size:clamp(48px,7vw,96px);font-weight:600;line-height:0.9;color:var(--cream);margin-bottom:0;}
.cat-hero-banner .eyebrow{color:var(--gold);margin-bottom:20px;}
.cat-desc{font-size:15px;font-weight:300;color:var(--muted);max-width:520px;margin:0 auto 40px;line-height:1.8;}
.designs-section{padding:56px 60px 72px;max-width:1320px;margin:0 auto;}
.designs-label{font-size:11px;font-weight:500;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin-bottom:28px;}
.designs-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.design-card{background:var(--card);border:1px solid var(--border);transition:border-color .3s,transform .25s;cursor:pointer;text-decoration:none;display:block;}
.design-card:hover{border-color:var(--gold);transform:translateY(-3px);}
.design-img{aspect-ratio:4/5;background:#F5F3EE;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative;overflow:hidden;}
.design-ph-label{font-size:9px;font-weight:500;letter-spacing:0.2em;text-transform:uppercase;color:#8A7060;}
.design-info{padding:12px 14px;border-top:1px solid var(--border);}
.design-name{font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:500;color:var(--cream);display:block;margin-bottom:2px;}
.design-num{font-size:10px;color:var(--muted);letter-spacing:0.1em;}
.browse-section{padding:0 60px 72px;max-width:1320px;margin:0 auto;border-top:1px solid var(--border);padding-top:56px;}
.browse-label{font-size:11px;font-weight:500;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin-bottom:28px;}
.browse-grid{display:grid;grid-template-columns:repeat(4,1fr);}
.browse-item{font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--muted);text-decoration:none;padding:13px 12px 13px 0;border-bottom:1px solid rgba(184,150,62,0.1);display:block;transition:color .2s;}
.browse-item:hover{color:var(--cream);}
@media(max-width:1024px){
nav,footer{padding-left:32px;padding-right:32px;}
.hero,.cat-hero-banner{padding-left:32px;padding-right:32px;}
.cat-hero-banner{padding-top:80px;padding-bottom:64px;}
.cat-section,.designs-section,.browse-section{padding-left:32px;padding-right:32px;}
.cat-grid,.browse-grid{grid-template-columns:repeat(3,1fr);}
.designs-grid{grid-template-columns:repeat(3,1fr);}
.cta{padding:56px 32px;}
}
@media(max-width:640px){
nav,footer{padding-left:20px;padding-right:20px;}
.hero,.cat-hero-banner{padding-left:20px;padding-right:20px;}
.cat-hero-banner{padding-top:64px;padding-bottom:48px;}
.cat-section,.designs-section,.browse-section{padding-left:20px;padding-right:20px;}
.cat-grid,.browse-grid{grid-template-columns:repeat(2,1fr);}
.designs-grid{grid-template-columns:repeat(2,1fr);gap:10px;}
.cat-item{font-size:18px;}
.cta{padding:48px 20px;}
footer{flex-direction:column;gap:8px;text-align:center;}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Greek Empire</title>
{FONTS}
<style>{CSS}</style>
</head>
<body>"""

def nav_bar(back_text, back_href):
    return f"""<div class="meander"></div>
<nav>
  <a href="index.html" class="nav-logo"><img src="logo.png" alt="Greek Empire"></a>
  <a href="{back_href}" class="nav-back">{back_text}</a>
</nav>"""

def foot():
    return """<div class="meander"></div>
<footer>
  <span class="foot-brand">Greek Empire</span>
  <span class="foot-tag">College Branded Merchandise for the Best Years of Your Life</span>
</footer>
</body>
</html>"""

def design_cards(cat_name, cat_idx, count=12):
    cards = ""
    base_num = 1000 + (cat_idx * 50)
    for i in range(count):
        label = DESIGN_LABELS[i % len(DESIGN_LABELS)]
        num = base_num + (i + 1)
        cards += f"""    <a href="#" class="design-card">
      <div class="design-img">
        {COL_SVG_DARK}
        <span class="design-ph-label">Image Coming Soon</span>
      </div>
      <div class="design-info">
        <span class="design-name">{cat_name} — {label}</span>
        <span class="design-num">#{num}</span>
      </div>
    </a>
"""
    return cards

def make_index():
    items = "\n".join(f'    <a href="{slug}.html" class="cat-item">{name}</a>' for name, slug, _ in CATS)
    html = head("Design Gallery") + nav_bar("&larr; Back to Site", "https://greek-empire.vercel.app") + f"""
<section class="hero">
  <h1>Design Gallery</h1>
  <div class="rule"></div>
  <p class="hero-sub">Designed for the moments that define your college years.</p>
</section>
<div class="cat-bg"><section class="cat-section">
  <div class="cat-grid">
{items}
  </div>
</section></div>
<section class="cta">
  <h2>Don&rsquo;t See What You Need?</h2>
  <p>We design for any event, any theme, any chapter.</p>
  <a href="https://greek-empire.vercel.app" class="cta-link">Start Your Order</a>
</section>""" + foot()
    with open(f"{DIR}/index.html", "w") as f:
        f.write(html)
    print("✓ index.html")

def make_cat(idx, name, slug, desc):
    others = "\n".join(
        f'    <a href="{s}.html" class="browse-item">{n}</a>'
        for n, s, _ in CATS if s != slug
    )
    cards = design_cards(name, idx, count=12)
    html = head(name) + nav_bar("&larr; Design Gallery", "index.html") + f"""
<section class="cat-hero-banner">
  <div class="cat-hero-content">
    <p class="eyebrow">Design Gallery</p>
    <h1>{name}</h1>
    <div class="rule"></div>
    <p class="cat-desc">{desc}</p>
    <a href="https://greek-empire.vercel.app" class="cta-link">Start Your Order</a>
  </div>
</section>
<section class="designs-section">
  <p class="designs-label">Browse Designs</p>
  <div class="designs-grid">
{cards}
  </div>
</section>
<section class="cta">
  <h2>Ready to Place Your Order?</h2>
  <p>Custom {name.lower()} apparel designed for your chapter.</p>
  <a href="https://greek-empire.vercel.app" class="cta-link">Start Your Order</a>
</section>
<section class="browse-section">
  <p class="browse-label">Browse Other Categories</p>
  <div class="browse-grid">
{others}
  </div>
</section>""" + foot()
    with open(f"{DIR}/{slug}.html", "w") as f:
        f.write(html)
    print(f"✓ {slug}.html")

make_index()
for idx, (name, slug, desc) in enumerate(CATS):
    make_cat(idx, name, slug, desc)

print(f"\nDone — {len(CATS) + 1} pages generated.")
