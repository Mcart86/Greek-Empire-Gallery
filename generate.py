#!/usr/bin/env python3
import os

DIR = "/home/claude/greek-empire-gallery"

CATS = [
    ("Spring Break",       "spring-break",       "Your organization's spring break run needs a shirt that keeps up."),
    ("Winter",             "winter",              "Cold weather, warm organization. Custom winter apparel built for the season."),
    ("Western",            "western",             "Your letters. Their hats. Custom western theme shirts done right."),
    ("Sixties",            "sixties",             "Groovy organization, iconic shirts. The sixties theme, elevated."),
    ("Halloween",          "halloween",           "The annual costume party deserves a design that haunts them all semester."),
    ("Formal",             "formal",              "Organization formals done right — from the bid to the bow tie."),
    ("Dog & Puppy",        "dog-and-puppy",       "Philanthropy events, big little reveals, and every excuse to put a dog on a shirt."),
    ("Christmas",          "christmas",           "Holiday organization events. Custom apparel that actually looks good."),
    ("5K Run",             "5k-run",              "Philanthropy runs, campus 5Ks, and everything in between."),
    ("Rush",               "rush",                "First impressions are everything. Make yours last four years."),
    ("Sports",             "sports",              "From intramurals to watch parties — custom sports apparel for your organization."),
    ("Fraternity",         "fraternity",          "Organization gear that represents who you are — not just where you're from."),
    ("Sisterhood Retreat", "sisterhood-retreat",  "The weekend that brings organizations together. Custom apparel for every retreat."),
    ("Cowgirl",            "cowgirl",             "Boots up. Custom cowgirl theme shirts built for your organization's biggest events."),
    ("Bid Day",            "bid-day",             "The best day of the year deserves a shirt to prove it."),
    ("Recruitment",        "recruitment",         "Your organization's first impression. Make it count."),
    ("Panhellenic",        "panhellenic",         "Custom apparel for Panhellenic events, councils, and community."),
    ("Philanthropy",       "philanthropy",        "Do good. Look good. Give back in custom apparel that means something."),
    ("Big Little",         "big-little",          "The reveal. The gift. The shirt they'll keep forever."),
    ("Beach",              "beach",               "Sun, sand, and your letters. Beach theme shirts built for the culture."),
    ("Shamrock",           "shamrock",            "St. Patrick's Day organization events deserve a shirt actually worth keeping."),
    ("Mixers",             "mixers",              "Social events, mixer nights, and the shirts everyone talks about the next day."),
    ("Mom's Day",          "moms-day",            "Your mom's weekend deserves custom apparel she'll actually wear home."),
    ("Weekend Getaway",    "weekend-getaway",     "Organization retreats and road trips deserve merch to match the memory."),
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
nav{display:flex;justify-content:space-between;align-items:center;padding:14px 60px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(10,10,10,0.97);backdrop-filter:blur(10px);z-index:100;}
.nav-logo{display:flex;align-items:center;text-decoration:none;}
.nav-logo img{height:52px;width:auto;}
.nav-back{font-size:12px;font-weight:400;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted);text-decoration:none;transition:color .2s;}
.nav-back:hover{color:var(--cream);}
.subnav{display:flex;justify-content:center;gap:48px;padding:15px 24px;background:#0A0A0A;border-bottom:1px solid var(--border);flex-wrap:wrap;}
.subnav a{color:var(--cream);font-size:12px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;transition:color .2s;white-space:nowrap;}
.subnav a:hover{color:var(--gold);}
.subnav a.active{color:var(--gold);position:relative;}
.subnav a.active::after{content:'';position:absolute;left:0;right:0;bottom:-15px;height:2px;background:var(--gold);}
.eyebrow{font-size:11px;font-weight:500;letter-spacing:0.28em;text-transform:uppercase;color:var(--gold);margin-bottom:18px;animation:headerFadeIn 0.6s ease both;}
.rule{width:48px;height:2px;background:var(--gold);margin:9px auto;}
.hero{text-align:center;padding:0;border-bottom:1px solid var(--border);border-top:3px solid var(--gold);position:relative;background:#FFFFFF;}
.hero-inner{padding:42px 60px 30px;position:relative;z-index:1;}
@keyframes shimmerGold{0%{background-position:0% 50%;}100%{background-position:200% 50%;}}
@keyframes headerFadeIn{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:translateY(0);}}
@keyframes headerScaleIn{from{opacity:0;transform:scale(0.94);}to{opacity:1;transform:scale(1);}}
.hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(44px,6vw,80px);font-weight:700;font-style:italic;line-height:1.25;padding-top:0.15em;background:linear-gradient(90deg,#7A5010 0%,#C4881A 20%,#F5D77A 35%,#FFF6D8 45%,#F0C840 55%,#C4901C 70%,#8B6212 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:headerScaleIn 0.7s cubic-bezier(.16,.8,.24,1) 0.2s both, shimmerGold 4s linear infinite;}
.hero h1 .bebas-line{font-family:'Bebas Neue',sans-serif;font-weight:400;font-style:normal;letter-spacing:0.02em;background:none;-webkit-background-clip:initial;-webkit-text-fill-color:#1A1A1A;background-clip:initial;color:#1A1A1A;animation:none;}
.hero-sub{font-size:14px;font-weight:300;color:#6B6459;font-style:italic;}
.cat-bg{background:#FFFFFF;}
.cat-section{padding:80px 60px 96px;max-width:1280px;margin:0 auto;}
.cat-count{font-size:11px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;color:#B8963E;margin-bottom:36px;}
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);}
.cat-item{font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:500;color:#1A1A1A;text-decoration:none;padding:18px 16px 18px 0;border-bottom:1px solid rgba(0,0,0,0.08);display:flex;align-items:center;letter-spacing:0.07em;transition:color .2s,padding-left .2s;}
.cat-item:before{content:'— ';font-size:14px;color:var(--gold);opacity:0;width:0;overflow:hidden;transition:opacity .2s,width .2s;white-space:nowrap;}
.cat-item:hover{color:var(--gold);padding-left:4px;}
.cat-item:hover:before{opacity:1;width:22px;}
.cta{text-align:center;padding:72px 60px 80px;border-top:1px solid var(--border);}
.cta h2{font-family:'Cormorant Garamond',serif;font-size:clamp(30px,4vw,48px);font-weight:600;color:var(--cream);margin-bottom:12px;}
.shimmer-h2{background:linear-gradient(90deg,#7A5010 0%,#C4881A 20%,#F5D77A 35%,#FFF6D8 45%,#F0C840 55%,#C4901C 70%,#8B6212 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmerGold 4s linear infinite;}
.cta p{font-size:14px;color:var(--muted);margin-bottom:32px;}
.follow-us-text{font-family:'Cormorant Garamond',serif;font-size:27px;font-weight:700;background:linear-gradient(135deg,#7A5010 0%,#C4881A 25%,#F0C840 50%,#C4901C 75%,#8B6212 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.cta-link{display:inline-block;padding:15px 40px;background:var(--gold);color:var(--obsidian);font-family:'DM Sans',sans-serif;font-size:11px;font-weight:500;letter-spacing:0.18em;text-transform:uppercase;text-decoration:none;transition:background .2s;}
.cta-link:hover{background:var(--gold-lt);}
footer{padding:36px 60px;border-top:1px solid var(--border);display:grid;grid-template-columns:1fr auto 1fr;align-items:start;gap:24px;}
.foot-left{display:flex;flex-direction:column;gap:6px;justify-self:start;}
.foot-brand{font-family:'Cormorant Garamond',serif;font-size:14px;font-weight:500;letter-spacing:0.22em;text-transform:uppercase;color:var(--muted);}
.foot-tag{font-size:12px;color:var(--muted);font-style:italic;}
.foot-address{font-size:12px;color:var(--muted);}
.foot-center{display:flex;flex-direction:column;align-items:center;gap:16px;justify-self:center;}
.foot-social{display:flex;align-items:center;gap:18px;}
.foot-social-link{color:var(--gold);display:flex;align-items:center;justify-content:center;width:44px;height:44px;border:1px solid var(--border);border-radius:50%;transition:color .2s,border-color .2s,background .2s,transform .2s;}
.foot-shield{width:70px;height:auto;opacity:0.9;}
.foot-social-link:hover{color:var(--obsidian);background:var(--gold);border-color:var(--gold);transform:translateY(-2px);}
.cta-social{display:flex;justify-content:center;gap:18px;}
.reveal{opacity:0;transform:translateY(28px);transition:opacity .7s cubic-bezier(.16,.8,.24,1),transform .7s cubic-bezier(.16,.8,.24,1);}
.reveal.revealed{opacity:1;transform:translateY(0);}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none;}}
.cat-hero-banner{position:relative;padding:48px 60px 32px;text-align:center;background:#FFFFFF;border-bottom:1px solid var(--border);border-top:3px solid var(--gold);}
.cat-hero-content{position:relative;z-index:1;}
.cat-hero-banner h1{font-family:'Cormorant Garamond',serif;font-size:clamp(48px,7vw,96px);font-weight:600;font-style:italic;line-height:1.25;padding-top:0.15em;margin-bottom:0;background:linear-gradient(90deg,#7A5010 0%,#C4881A 20%,#F5D77A 35%,#FFF6D8 45%,#F0C840 55%,#C4901C 70%,#8B6212 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:headerScaleIn 0.7s cubic-bezier(.16,.8,.24,1) 0.2s both, shimmerGold 4s linear infinite;}
.cat-hero-banner .eyebrow{font-family:'Bebas Neue',sans-serif;color:#1A1A1A;margin-bottom:20px;letter-spacing:0.2em;}
.cat-desc{font-size:15px;font-weight:300;color:#6B6459;max-width:520px;margin:0 auto 16px;line-height:1.7;}
.designs-section{padding:56px 60px 72px;max-width:1320px;margin:0 auto;}
.designs-label{font-size:11px;font-weight:500;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin-bottom:28px;}
.designs-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.design-card{background:var(--card);border:1px solid var(--border);box-shadow:0 4px 24px rgba(0,0,0,0.5);transition:border-color .3s,transform .25s,box-shadow .3s;display:block;}
.design-card:hover{border-color:var(--gold);transform:translateY(-4px);box-shadow:0 16px 48px rgba(0,0,0,0.65),0 0 0 1px rgba(184,150,62,0.25);}
.design-img{aspect-ratio:4/5;background:#F5F3EE;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative;overflow:hidden;}
.design-ph-label{font-size:9px;font-weight:500;letter-spacing:0.2em;text-transform:uppercase;color:#8A7060;}
.design-overlay{position:absolute;inset:0;background:rgba(10,10,10,0.6);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .3s;}
.design-card:hover .design-overlay{opacity:1;}
.customize-btn{padding:11px 20px;border:1px solid var(--gold-lt);background:rgba(10,10,10,0.55);color:#F0EBE0;font-family:'DM Sans',sans-serif;font-size:10px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;text-decoration:none;transition:background .2s,color .2s;white-space:nowrap;}
.customize-btn:hover{background:var(--gold);color:var(--obsidian);}
.design-info{padding:12px 14px;border-top:1px solid var(--border);}
.design-name{font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:500;color:var(--cream);display:block;margin-bottom:2px;}
.design-num{font-size:10px;color:var(--muted);letter-spacing:0.1em;}
.browse-section{padding:0 60px 72px;max-width:1320px;margin:0 auto;border-top:1px solid var(--border);padding-top:56px;}
.browse-label{font-size:11px;font-weight:500;letter-spacing:0.24em;text-transform:uppercase;color:var(--gold);margin-bottom:28px;}
.browse-grid{display:grid;grid-template-columns:repeat(4,1fr);}
.browse-item{font-family:'Cormorant Garamond',serif;font-size:18px;font-weight:400;color:var(--muted);text-decoration:none;padding:13px 12px 13px 0;border-bottom:1px solid rgba(184,150,62,0.1);display:block;transition:color .2s;}
.browse-item:hover{color:var(--cream);}
.cat-bg .design-card{background:#FFFFFF;border:1px solid rgba(0,0,0,0.1);box-shadow:0 4px 18px rgba(0,0,0,0.08);}
.cat-bg .design-card:hover{border-color:var(--gold);box-shadow:0 12px 30px rgba(0,0,0,0.12),0 0 0 1px rgba(184,150,62,0.25);}
.cat-bg .design-info{border-top:1px solid rgba(0,0,0,0.08);}
.cat-bg .design-name{color:#1A1A1A;}
.cat-bg .design-num{color:#7A756C;}
.cat-bg .browse-item{color:#5C5750;border-bottom:1px solid rgba(0,0,0,0.08);}
.cat-bg .browse-item:hover{color:#1A1A1A;}
.cust-hero{text-align:center;padding:34px 60px 22px;border-bottom:1px solid var(--border);border-top:3px solid var(--gold);background:#FFFFFF;}
.cust-hero h1{font-family:'Cormorant Garamond',serif;font-size:clamp(38px,5vw,60px);font-weight:600;font-style:italic;line-height:1.25;padding-top:0.15em;background:linear-gradient(90deg,#7A5010 0%,#C4881A 20%,#F5D77A 35%,#FFF6D8 45%,#F0C840 55%,#C4901C 70%,#8B6212 100%);background-size:250% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:headerScaleIn 0.7s cubic-bezier(.16,.8,.24,1) 0.2s both, shimmerGold 4s linear infinite;}
.cust-hero p{font-size:14px;color:#6B6459;max-width:460px;margin:18px auto 0;line-height:1.7;}
.progress-bar{display:flex;background:#0A0A0A;}
.progress-step{flex:1;display:flex;align-items:center;gap:14px;padding:20px 24px 20px 44px;background:#1A1A1A;color:#8A8378;position:relative;}
.progress-step:first-child{clip-path:polygon(0 0,calc(100% - 24px) 0,100% 50%,calc(100% - 24px) 100%,0 100%);padding-left:32px;z-index:3;}
.progress-step:nth-child(2){clip-path:polygon(0 0,calc(100% - 24px) 0,100% 50%,calc(100% - 24px) 100%,0 100%,24px 50%);margin-left:-24px;z-index:2;}
.progress-step:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%,24px 50%);margin-left:-24px;z-index:1;}
.progress-step.active{background:var(--gold);color:var(--obsidian);}
.progress-num{width:32px;height:32px;border:2px solid currentColor;display:flex;align-items:center;justify-content:center;font-family:'DM Sans',sans-serif;font-weight:600;font-size:14px;flex-shrink:0;}
.progress-text{display:flex;flex-direction:column;}
.progress-title{font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:0.05em;line-height:1.3;}
.progress-sub{font-size:11px;opacity:0.75;margin-top:2px;line-height:1.3;}
.cust-bg{background:#FFFFFF;}
.cust-wrap{max-width:1080px;margin:0 auto;padding:64px 60px 96px;}
.cust-grid{display:grid;grid-template-columns:320px 1fr;gap:56px;align-items:start;}
.cust-preview{position:sticky;top:96px;}
.preview-img{aspect-ratio:4/5;background:#F5F3EE;border:1px solid rgba(0,0,0,0.1);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;}
.preview-info{margin-top:18px;display:flex;flex-direction:column;gap:4px;}
.cust-form-col{min-width:0;}
.cust-summary-label{font-size:10px;font-weight:500;letter-spacing:0.2em;text-transform:uppercase;color:#9A7420;display:block;}
.cust-summary-name{font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:500;color:#1A1A1A;line-height:1.3;}
.cust-summary-num{font-size:12px;color:#7A756C;}
.field-group{margin-bottom:26px;}
.field-label{display:block;font-size:11px;font-weight:500;letter-spacing:0.14em;text-transform:uppercase;color:#9A7420;margin-bottom:10px;}
.required-mark{color:#B8341C;margin-left:2px;}
.field-input,.field-select,.field-textarea{width:100%;background:#FAF8F4;border:1px solid rgba(0,0,0,0.14);color:#1A1A1A;font-family:'DM Sans',sans-serif;font-size:14px;padding:13px 16px;transition:border-color .2s;}
.field-input::placeholder,.field-textarea::placeholder{color:#A8A198;}
.field-input:focus,.field-select:focus,.field-textarea:focus{outline:none;border-color:var(--gold);}
.field-textarea{resize:vertical;min-height:130px;line-height:1.6;}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.field-hint{font-size:11px;color:#8A8378;margin-top:8px;font-style:italic;}
.file-field{display:flex;align-items:center;gap:16px;flex-wrap:wrap;}
.file-btn-wrap{position:relative;overflow:hidden;display:inline-block;}
.file-btn{padding:12px 22px;border:1px solid #1A1A1A;background:#FFFFFF;color:#1A1A1A;font-family:'DM Sans',sans-serif;font-size:10px;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;cursor:pointer;transition:background .2s,color .2s;}
.file-btn-wrap:hover .file-btn{background:#1A1A1A;color:#FFFFFF;}
.file-input-hidden{position:absolute;left:0;top:0;width:100%;height:100%;opacity:0;cursor:pointer;}
.file-name{font-size:13px;color:#7A756C;}
.submit-row{display:flex;justify-content:flex-end;margin-top:16px;}
.submit-btn{width:auto;padding:16px 34px;background:var(--gold);color:#FFFFFF;border:none;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:0.16em;text-transform:uppercase;cursor:pointer;transition:background .2s;}
.submit-btn:hover{background:var(--gold-lt);}
.form-step.hidden{display:none;}
.step-title{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:600;color:#1A1A1A;margin-bottom:28px;}
.name-row{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.name-sub-label{font-size:11px;color:#8A8378;margin-top:6px;}
.recaptcha-box{border:1px solid rgba(0,0,0,0.14);background:#FAFAF8;padding:20px 22px;display:flex;align-items:center;gap:16px;max-width:360px;}
.recaptcha-checkbox{width:24px;height:24px;border:1px solid rgba(0,0,0,0.3);background:#FFFFFF;flex-shrink:0;cursor:pointer;position:relative;}
.recaptcha-checkbox.checked{background:var(--gold);border-color:var(--gold);}
.recaptcha-checkbox.checked::after{content:'\\2713';position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#FFFFFF;font-size:15px;}
.recaptcha-label{font-size:14px;color:#3C3C3C;}
.recaptcha-note{font-size:10px;color:#9A958C;margin-top:4px;}
.step-nav-row{display:flex;justify-content:space-between;align-items:center;margin-top:16px;}
.prev-btn{padding:16px 30px;background:transparent;border:1px solid #1A1A1A;color:#1A1A1A;font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:0.16em;text-transform:uppercase;cursor:pointer;transition:background .2s,color .2s;}
.prev-btn:hover{background:#1A1A1A;color:#FFFFFF;}
.success-box{display:none;text-align:center;padding:56px 24px;}
.success-box.show{display:block;}
.success-box h3{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:600;color:#1A1A1A;margin-bottom:14px;}
.success-box p{font-size:14px;color:#6B6459;line-height:1.7;max-width:400px;margin:0 auto;}
.color-swatches{display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;}
.swatch-input{display:none;}
.swatch-label{width:34px;height:34px;border-radius:50%;border:2px solid var(--border);cursor:pointer;display:block;transition:border-color .2s,transform .2s;}
.swatch-input:checked + .swatch-label{border-color:var(--gold);transform:scale(1.12);box-shadow:0 0 0 2px var(--obsidian),0 0 0 3px var(--gold);}
@media(max-width:1024px){
nav,footer{padding-left:32px;padding-right:32px;}
.hero-inner,.cat-hero-banner{padding-left:32px;padding-right:32px;}
.hero-inner{padding-top:34px;padding-bottom:26px;}
.cat-section,.designs-section,.browse-section{padding-left:32px;padding-right:32px;}
.cat-grid,.browse-grid{grid-template-columns:repeat(3,1fr);}
.designs-grid{grid-template-columns:repeat(3,1fr);}
.cta{padding:56px 32px;}
}
@media(max-width:640px){
nav,footer{padding-left:20px;padding-right:20px;}
.subnav{gap:22px;padding:13px 16px;justify-content:flex-start;overflow-x:auto;}
.subnav a{font-size:11px;}
.hero-inner,.cat-hero-banner{padding-left:20px;padding-right:20px;}
.hero-inner{padding-top:26px;padding-bottom:20px;}
.cat-hero-banner{padding-top:26px;padding-bottom:20px;}
.cat-section,.designs-section,.browse-section{padding-left:20px;padding-right:20px;}
.cat-grid,.browse-grid{grid-template-columns:repeat(2,1fr);}
.designs-grid{grid-template-columns:repeat(2,1fr);gap:10px;}
.cat-item{font-size:18px;}
.cta{padding:48px 20px;}
.cust-hero{padding:26px 20px 18px;}
.cust-wrap{padding:40px 20px 72px;}
.field-row{grid-template-columns:1fr;}
.cust-grid{grid-template-columns:1fr;gap:32px;}
.cust-preview{position:static;max-width:280px;margin:0 auto;}
.progress-bar{flex-direction:column;}
.progress-step,.progress-step:first-child,.progress-step:nth-child(2),.progress-step:last-child{clip-path:none;margin-left:0;padding:16px 20px;}
.progress-sub{display:none;}
footer{grid-template-columns:1fr;justify-items:center;gap:24px;text-align:center;}
.foot-left{align-items:center;}
}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">'

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Greek Empire</title>
<meta name="description" content="Greek Empire — College branded merchandise for the best years of your life. Browse designs by theme and customize for your campus organization.">
<link rel="icon" type="image/png" href="favicon.png">
<meta property="og:title" content="{title} — Greek Empire">
<meta property="og:description" content="College branded merchandise for the best years of your life.">
<meta property="og:image" content="https://greek-empire-gallery.vercel.app/shield-logo.png">
<meta property="og:type" content="website">
{FONTS}
<style>{CSS}</style>
</head>
<body>"""

def nav_bar(back_text=None, back_href=None):
    back_link_html = f'<a href="{back_href}" class="nav-back">{back_text}</a>' if back_text else ''
    return f"""<div class="meander"></div>
<nav>
  <a href="index.html" class="nav-logo"><img src="logo.png" alt="Greek Empire"></a>
  {back_link_html}
</nav>"""

def subnav():
    return """<div class="subnav">
  <a href="https://greekempire.swagflo.com/design-your-own">Design Your Own</a>
  <a href="index.html" class="active">Design Gallery</a>
  <a href="https://greek-empire-sorority.vercel.app/">Shop by Sorority</a>
  <a href="https://greek-empire-fraternity.vercel.app/">Shop by Fraternity</a>
  <a href="https://greek-empire-ambassador-landing-new.vercel.app/">Campus Ambassador</a>
</div>"""

def foot():
    return """<div class="meander"></div>
<footer>
  <div class="foot-left">
    <span class="foot-brand">Greek Empire</span>
    <span class="foot-tag">College Branded Merchandise for the Best Years of Your Life</span>
    <span class="foot-address">281 Benigno Blvd, Bellmawr, New Jersey 08031</span>
  </div>
  <div class="foot-center">
    <div class="foot-social">
      <a href="https://www.instagram.com/_greekempire_" target="_blank" rel="noopener" aria-label="Instagram" class="foot-social-link">
        <svg width="23" height="23" viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="5" stroke="currentColor" stroke-width="1.6"/><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.6"/><circle cx="17.3" cy="6.7" r="1.15" fill="currentColor"/></svg>
      </a>
      <a href="https://www.tiktok.com/@_greekempire_" target="_blank" rel="noopener" aria-label="TikTok" class="foot-social-link">
        <svg width="23" height="23" viewBox="0 0 24 24" fill="none"><path d="M16.5 2c.4 2.2 1.9 3.9 4 4.3v2.9c-1.5 0-2.9-.4-4-1.2v6.7c0 3.4-2.8 6.1-6.1 6.1S4.3 18.1 4.3 14.7c0-3.3 2.6-6 5.9-6.1v3c-1.6.1-2.9 1.4-2.9 3.1 0 1.7 1.4 3.1 3.1 3.1s3.1-1.4 3.1-3.1V2h2.9z" fill="currentColor"/></svg>
      </a>
    </div>
    <img src="shield-logo.png" alt="Greek Empire" class="foot-shield">
  </div>
</footer>
<script>
  (function() {
    var els = document.querySelectorAll('.reveal:not(.revealed)');
    if (!('IntersectionObserver' in window)) {
      els.forEach(function(el) { el.classList.add('revealed'); });
      return;
    }
    var counters = new Map();
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var parent = el.parentElement;
          var idx = counters.get(parent) || 0;
          el.style.transitionDelay = Math.min(idx * 60, 360) + 'ms';
          counters.set(parent, idx + 1);
          el.classList.add('revealed');
          io.unobserve(el);
        }
      });
    }, {threshold: 0.15, rootMargin: '0px 0px -40px 0px'});
    els.forEach(function(el) { io.observe(el); });
  })();
</script>
</body>
</html>"""

# Real uploaded designs — overrides the first N placeholder slots per category.
REAL_DESIGNS = {
    "Bid Day": [
        {"name": "Alpha Phi — Bid Day 24 Yeehaw", "image": "bid-day-alpha-phi.jpg"},
        {"name": "Delta Gamma — Bid Day 2024 Dream Big", "image": "bid-day-delta-gamma.jpg"},
        {"name": "Kappa Delta — Bid Day 24 Choose Joy", "image": "bid-day-kappa-delta.jpg"},
        {"name": "Delta Zeta — Ready, Set, Bid! Golf Cart", "image": "bid-day-delta-zeta.jpg"},
        {"name": "Good Things Are Ahead — Bid Day 2025", "image": "bid-day-good-things.jpg"},
        {"name": "Game On, Go Greek! — Bid Day 2025", "image": "bid-day-game-on.jpg"},
        {"name": "Alpha Chi — Bid Day RSVP Postcard", "image": "bid-day-alpha-chi.jpg"},
        {"name": "Delta Gamma — Bid Day 2026", "image": "bid-day-delta-gamma-2026.jpg"},
        {"name": "Pi Beta Phi — Bid Day Thank You Note", "image": "bid-day-pi-phi.jpg"},
        {"name": "Kappa Kappa Gamma — Bid Day Vinyl Record", "image": "bid-day-kkg.jpg"},
        {"name": "Sigma Kappa — Bid Day Racing", "image": "bid-day-sigma-kappa.jpg"},
        {"name": "Kappa Sigma — Bid Day 2022", "image": "bid-day-kappa-sigma.jpg"},
        {"name": "Theta Chi — Bid Day 2023", "image": "bid-day-theta-chi.jpg"},
        {"name": "Delta Gamma — Bid Day 2024 Daisy Smiley", "image": "bid-day-delta-gamma-daisy.jpg"},
        {"name": "Chi Omega — Bid Day 2026 Citrus", "image": "bid-day-chi-omega.jpg"},
        {"name": "Alpha Gamma Delta — Bid Day 2026 Denim Patch", "image": "bid-day-alpha-gam.jpg"},
        {"name": "Alpha Xi Delta — Bid Day 2019 Boho", "image": "western-axd-bid-day-2019.jpg"},
        {"name": "Alpha Xi Delta — Bid Day 2020 Boho", "image": "western-axd-bid-day-2020.jpg"},
        {"name": "Alpha Xi Delta — Bid Day 2021 Boho", "image": "western-axd-bid-day-2021.jpg"},
        {"name": "Delta Gamma — Bid Day 2026 Western", "image": "western-dg-bid-day-2026.jpg"},
        {"name": "Kappa Alpha Theta — Bid Day 2026 Western", "image": "western-kat-bid-day-2026.jpg"},
        {"name": "Sigma Chi — Bid Day 2026 Western", "image": "western-sigma-chi-bid-day-2026.jpg"},
    ],
    "Spring Break": [
        {"name": "Pi Kappa Alpha — Spring Break Miami Beach", "image": "spring-break-pika.jpg"},
        {"name": "Alpha Omicron Pi — Spring Break Hermosa Beach", "image": "spring-break-aopi.jpg"},
        {"name": "Sigma Chi — Spring Break Santa Barbara", "image": "spring-break-sigma-chi.jpg"},
        {"name": "Delta Chi — Spring Break South Padre Island", "image": "spring-break-delta-chi-south-padre.jpg"},
        {"name": "Delta Chi — Coastal Retreat Gulf Shores", "image": "spring-break-delta-chi-gulf-shores.jpg"},
        {"name": "Delta Chi — Summer Escape Huntington Beach", "image": "spring-break-delta-chi-huntington.jpg"},
        {"name": "Gamma Phi Beta — Spring 2024 Destin", "image": "spring-break-gamma-phi-beta.jpg"},
        {"name": "Sigma Kappa — Beach Weekend 2025 Clearwater", "image": "spring-break-sigma-kappa.jpg"},
        {"name": "Alpha Omicron Pi — Spring Rush 2024 Cocoa Beach", "image": "spring-break-aopi-rush.jpg"},
    ],
    "Halloween": [
        {"name": "Phi Kappa Psi — Halloween 2023", "image": "halloween-phi-kappa-psi.jpg"},
        {"name": "Delta Gamma — Halloween 2023", "image": "halloween-delta-gamma.jpg"},
        {"name": "Alpha Sigma Phi — Halloween 2023", "image": "halloween-alpha-sigma-phi.jpg"},
        {"name": "Phi Kappa Psi — Halloween Bash 2023", "image": "halloween-phi-kappa-psi-bash.jpg"},
        {"name": "Alpha Sigma Phi — Halloween Social 2023", "image": "halloween-alpha-sigma-phi-social.jpg"},
        {"name": "Kappa Kappa Gamma — Halloween Party 2023", "image": "halloween-kkg-party.jpg"},
        {"name": "Alpha Chi Omega — Spooky Season 2025", "image": "halloween-axo-spooky-season.jpg"},
        {"name": "Kappa Alpha Theta — Haunted Nights 2025", "image": "halloween-kat-haunted-nights.jpg"},
        {"name": "Delta Gamma — Trick or Treat 2025", "image": "halloween-dg-trick-or-treat.jpg"},
        {"name": "Phi Kappa Psi — Halloween Affair 2023", "image": "halloween-pkp-affair.jpg"},
        {"name": "Delta Gamma — Halloween Night 2023", "image": "halloween-dg-night.jpg"},
        {"name": "Alpha Sigma Phi — Haunted House 2023", "image": "halloween-asp-haunted-house.jpg"},
        {"name": "Sigma Alpha Epsilon — Halloween Bash 2022", "image": "halloween-sae-bash-2022.jpg"},
        {"name": "Alpha Tau Omega — Halloween Bash 2021", "image": "halloween-ato-bash-2021.jpg"},
        {"name": "Kappa Kappa Gamma — Halloween Bash 2023", "image": "halloween-kkg-bash-2023.jpg"},
        {"name": "Alpha Sigma Phi — Pumpkin Festival 2023", "image": "halloween-asp-pumpkin-festival.jpg"},
        {"name": "Sigma Alpha Epsilon — Pumpkin Harvest 2023", "image": "halloween-sae-pumpkin-harvest.jpg"},
        {"name": "Alpha Delta Pi — Pumpkin Season 2022", "image": "halloween-adpi-pumpkin-season.jpg"},
    ],
    "Formal": [
        {"name": "Alpha Delta Pi — Twilight Tropics Fall Formal 2025", "image": "formal-adpi-twilight-tropics-2025.jpg"},
        {"name": "Zeta Tau Alpha — Twilight Tropics Fall Formal 2026", "image": "formal-zta-twilight-tropics-2026.jpg"},
        {"name": "Kappa Kappa Gamma — Twilight Tropics Fall Formal 2028", "image": "formal-kkg-twilight-tropics-2028.jpg"},
        {"name": "Pi Kappa Phi — Spring Formal Santa Barbara", "image": "formal-pkp-spring-santa-barbara.jpg"},
        {"name": "Pi Kappa Phi — Spring Formal San Antonio", "image": "formal-pkp-spring-san-antonio.jpg"},
        {"name": "Pi Kappa Phi — Spring Formal Orlando", "image": "formal-pkp-spring-orlando.jpg"},
        {"name": "Alpha Chi Omega — Atlantic City Semi-Formal", "image": "formal-axo-atlantic-city-semiformal.jpg"},
        {"name": "Delta Gamma — Nashville Semi-Formal", "image": "formal-dg-nashville-semiformal.jpg"},
        {"name": "Kappa Kappa Gamma — New Orleans Semi-Formal", "image": "formal-kkg-new-orleans-semiformal.jpg"},
        {"name": "Alpha Chi Omega — Spring Formal 2024 San Diego", "image": "formal-axo-spring-san-diego-2024.jpg"},
        {"name": "Delta Gamma — Spring Formal 2025 Denver", "image": "formal-dg-spring-denver-2025.jpg"},
        {"name": "Pi Beta Phi — Spring Formal 2026 Chicago", "image": "formal-pbp-spring-chicago-2026.jpg"},
        {"name": "Gamma Phi Beta — Spring Formal 2027 Philadelphia", "image": "formal-gpb-spring-philadelphia-2027.jpg"},
        {"name": "Pi Beta Phi — Spring Formal March 2023", "image": "formal-pbp-spring-2023-march.jpg"},
        {"name": "Kappa Alpha Theta — Spring Formal April 2023", "image": "formal-kat-spring-2023-april.jpg"},
        {"name": "Delta Gamma — Spring Formal April 2023", "image": "formal-dg-spring-2023-april.jpg"},
        {"name": "Pi Beta Phi — Barn Dance 2024 Stillwater", "image": "formal-pbp-barn-dance-2024.jpg"},
        {"name": "Alpha Delta Pi — Barn Dance 2023 Fayetteville", "image": "formal-adpi-barn-dance-2023.jpg"},
        {"name": "Kappa Kappa Gamma — Barn Dance 2025 College Station", "image": "formal-kkg-barn-dance-2025.jpg"},
        {"name": "Delta Gamma — Fall Formal 2026 Dallas", "image": "western-dg-fall-formal-2026-dallas.jpg"},
        {"name": "Kappa Alpha Theta — Fall Formal 2026 Phoenix", "image": "western-kat-fall-formal-2026-phoenix.jpg"},
        {"name": "Alpha Omicron Pi — Fall Formal 2026 Lake Travis", "image": "western-aopi-fall-formal-2026-lake-travis.jpg"},
    ],
    "Western": [
        {"name": "Alpha Xi Delta — Bid Day 2019 Boho", "image": "western-axd-bid-day-2019.jpg"},
        {"name": "Alpha Xi Delta — Bid Day 2020 Boho", "image": "western-axd-bid-day-2020.jpg"},
        {"name": "Alpha Xi Delta — Bid Day 2021 Boho", "image": "western-axd-bid-day-2021.jpg"},
        {"name": "Delta Gamma — Fall Formal 2026 Dallas", "image": "western-dg-fall-formal-2026-dallas.jpg"},
        {"name": "Kappa Alpha Theta — Fall Formal 2026 Phoenix", "image": "western-kat-fall-formal-2026-phoenix.jpg"},
        {"name": "Alpha Omicron Pi — Fall Formal 2026 Lake Travis", "image": "western-aopi-fall-formal-2026-lake-travis.jpg"},
        {"name": "Delta Gamma — Bid Day 2026 Western", "image": "western-dg-bid-day-2026.jpg"},
        {"name": "Kappa Alpha Theta — Bid Day 2026 Western", "image": "western-kat-bid-day-2026.jpg"},
        {"name": "Sigma Chi — Bid Day 2026 Western", "image": "western-sigma-chi-bid-day-2026.jpg"},
        {"name": "Delta Gamma — Fall Rush 2025 Western", "image": "western-dg-fall-rush-2025.jpg"},
        {"name": "Kappa Alpha Theta — Fall Rush 2025 Western", "image": "western-kat-fall-rush-2025.jpg"},
        {"name": "Sigma Chi — Fall Rush 2025 Western", "image": "western-sigma-chi-fall-rush-2025.jpg"},
        {"name": "Delta Gamma — Fall Rush 2025 Cowboy", "image": "western-dg-fall-rush-2025-cowboy.jpg"},
        {"name": "Kappa Alpha Theta — Fall Rush 2025 Cowboy", "image": "western-kat-fall-rush-2025-cowboy.jpg"},
        {"name": "Sigma Chi — Fall Rush 2025 Cowboy", "image": "western-sigma-chi-fall-rush-2025-cowboy.jpg"},
        {"name": "Delta Gamma Chi — UFO Rush Austin 2024", "image": "rush-dg-chi-ufo-austin-2024.jpg"},
        {"name": "Kappa Sigma Chi — UFO Rush Phoenix 2024", "image": "rush-kappa-sigma-chi-ufo-phoenix-2024.jpg"},
        {"name": "Sigma Chi Omega — UFO Rush Dallas 2024", "image": "rush-sigma-chi-omega-ufo-dallas-2024.jpg"},
    ],
    "Rush": [
        {"name": "Delta Gamma — Fall Rush 2025 Western", "image": "western-dg-fall-rush-2025.jpg"},
        {"name": "Kappa Alpha Theta — Fall Rush 2025 Western", "image": "western-kat-fall-rush-2025.jpg"},
        {"name": "Sigma Chi — Fall Rush 2025 Western", "image": "western-sigma-chi-fall-rush-2025.jpg"},
        {"name": "Delta Gamma — Fall Rush 2025 Cowboy", "image": "western-dg-fall-rush-2025-cowboy.jpg"},
        {"name": "Kappa Alpha Theta — Fall Rush 2025 Cowboy", "image": "western-kat-fall-rush-2025-cowboy.jpg"},
        {"name": "Sigma Chi — Fall Rush 2025 Cowboy", "image": "western-sigma-chi-fall-rush-2025-cowboy.jpg"},
        {"name": "Delta Gamma Chi — UFO Rush Austin 2024", "image": "rush-dg-chi-ufo-austin-2024.jpg"},
        {"name": "Kappa Sigma Chi — UFO Rush Phoenix 2024", "image": "rush-kappa-sigma-chi-ufo-phoenix-2024.jpg"},
        {"name": "Sigma Chi Omega — UFO Rush Dallas 2024", "image": "rush-sigma-chi-omega-ufo-dallas-2024.jpg"},
    ],
    "5K Run": [
        {"name": "Run The Yard 5K — Arkansas–Fort Smith", "image": "5k-run-the-yard-arkansas-fort-smith.jpg"},
        {"name": "Lace Up Lead On 5K — Arkansas–Fort Smith", "image": "5k-lace-up-lead-on-arkansas-fort-smith.jpg"},
        {"name": "Spread The Legacy 5K — Arkansas–Fort Smith", "image": "5k-spread-the-legacy-arkansas-fort-smith.jpg"},
        {"name": "Baylor 5K — Alpha Xi Delta 2020", "image": "5k-baylor-alpha-xi-delta-2020.jpg"},
        {"name": "Auburn 5K — Delta Gamma 2020", "image": "5k-auburn-delta-gamma-2020.jpg"},
    ],
    "Shamrock": [
        {"name": "Kappa Delta — Shamrock 5K Run/Walk Green", "image": "shamrock-kd-5k-green.jpg"},
        {"name": "Kappa Delta — Shamrock 5K Run/Walk Blue", "image": "shamrock-kd-5k-blue.jpg"},
        {"name": "Kappa Delta — Shamrock 5K Run/Walk Pink", "image": "shamrock-kd-5k-pink.jpg"},
    ],
    "Philanthropy": [
        {"name": "Shoes Speak Louder — Prevent Child Abuse 2020", "image": "philanthropy-shoes-speak-louder-2020.jpg"},
        {"name": "Strides for Stronger Tomorrows — Prevent Child Abuse 2020", "image": "philanthropy-strides-stronger-tomorrows-2020.jpg"},
    ],
}

def design_cards(cat_name, cat_slug, cat_idx, count=12):
    import urllib.parse
    cards = ""
    base_num = 1000 + (cat_idx * 50)
    real_list = REAL_DESIGNS.get(cat_name, [])
    for i in range(count):
        num = base_num + (i + 1)
        if i < len(real_list):
            design_full_name = real_list[i]["name"]
            q = urllib.parse.urlencode({"design": design_full_name, "category": cat_name, "num": num, "image": real_list[i]["image"]})
            cards += f"""    <div class="design-card reveal">
      <div class="design-img">
        <img src="{real_list[i]['image']}" alt="{design_full_name}" style="width:100%;height:100%;object-fit:contain;">
        <div class="design-overlay">
          <a href="customize.html?{q}" class="customize-btn">Customize This Design</a>
        </div>
      </div>
      <div class="design-info">
        <span class="design-name">{design_full_name}</span>
        <span class="design-num">#{num}</span>
      </div>
    </div>
"""
        else:
            label = DESIGN_LABELS[i % len(DESIGN_LABELS)]
            design_full_name = f"{cat_name} — {label}"
            q = urllib.parse.urlencode({"design": design_full_name, "category": cat_name, "num": num})
            cards += f"""    <div class="design-card reveal">
      <div class="design-img">
        {COL_SVG_DARK}
        <span class="design-ph-label">Image Coming Soon</span>
        <div class="design-overlay">
          <a href="customize.html?{q}" class="customize-btn">Customize This Design</a>
        </div>
      </div>
      <div class="design-info">
        <span class="design-name">{cat_name} — {label}</span>
        <span class="design-num">#{num}</span>
      </div>
    </div>
"""
    return cards

def make_index():
    items = "\n".join(f'    <a href="{slug}.html" class="cat-item reveal">{name}</a>' for name, slug, _ in CATS)
    html = head("Design Gallery") + nav_bar() + subnav() + f"""
<section class="hero">
  <div class="hero-inner">
    <h1><span class="bebas-line">Hundreds of Collections.</span><br>Every Occasion.</h1>
    <div class="rule"></div>
    <p class="hero-sub">Start with a design built for the moment &mdash; then make it yours.</p>
  </div>
</section>
<div class="cat-bg"><section class="cat-section">
  <div class="cat-grid">
{items}
  </div>
</section></div>
<section class="cta">
  <h2 class="shimmer-h2">New Designs Drop First on the Feed.</h2>
</section>""" + foot()
    with open(f"{DIR}/index.html", "w") as f:
        f.write(html)
    print("✓ index.html")

def make_cat(idx, name, slug, desc):
    others = "\n".join(
        f'    <a href="{s}.html" class="browse-item">{n}</a>'
        for n, s, _ in CATS if s != slug
    )
    cards = design_cards(name, slug, idx, count=max(12, len(REAL_DESIGNS.get(name, []))))
    html = head(name) + nav_bar("&larr; The Collection", "index.html") + subnav() + f"""
<section class="cat-hero-banner">
  <div class="cat-hero-content">
    <p class="eyebrow">Design Gallery</p>
    <h1>{name}</h1>
    <div class="rule"></div>
    <p class="cat-desc">{desc}</p>
  </div>
</section>
<div class="cat-bg">
<section class="designs-section">
  <p class="designs-label">Browse Designs</p>
  <div class="designs-grid">
{cards}
  </div>
</section>
</div>
<section class="cta">
  <h2>Ready to Place Your Order?</h2>
  <p>Custom {name.lower()} apparel designed for your organization.</p>
  <a href="https://greekempire.swagflo.com/" class="cta-link">Start Your Order</a>
</section>
<div class="cat-bg">
<section class="browse-section">
  <p class="browse-label">Browse Other Categories</p>
  <div class="browse-grid">
{others}
  </div>
</section>
</div>""" + foot()
    with open(f"{DIR}/{slug}.html", "w") as f:
        f.write(html)
    print(f"✓ {slug}.html")

def make_customize():
    html = head("Customize This Design") + nav_bar("&larr; The Collection", "index.html") + subnav() + """
<section class="cust-hero">
  <p class="eyebrow">Custom Order Request</p>
  <h1>Customize This Design</h1>
  <p>Tell us the product, colors, and any changes you want &mdash; our art team will follow up with a proof.</p>
</section>

<div class="progress-bar" id="progressBar">
  <div class="progress-step active" id="progStep1">
    <div class="progress-num">1</div>
    <div class="progress-text">
      <span class="progress-title">Customize Your Design</span>
      <span class="progress-sub">Make this design your own</span>
    </div>
  </div>
  <div class="progress-step" id="progStep2">
    <div class="progress-num">2</div>
    <div class="progress-text">
      <span class="progress-title">Your Information</span>
      <span class="progress-sub">Contact information</span>
    </div>
  </div>
  <div class="progress-step" id="progStep3">
    <div class="progress-num">3</div>
    <div class="progress-text">
      <span class="progress-title">Confirmation</span>
      <span class="progress-sub">That&rsquo;s it. You&rsquo;re done.</span>
    </div>
  </div>
</div>

<div class="cust-bg">
<div class="cust-wrap">
<div class="cust-grid">

  <div class="cust-preview">
    <div class="preview-img" id="previewImgBox">
      """ + COL_SVG_DARK + """
      <span class="design-ph-label">Image Coming Soon</span>
    </div>
    <div class="preview-info">
      <span class="cust-summary-label">Selected Design</span>
      <span class="cust-summary-name" id="summaryName">&mdash;</span>
      <span class="cust-summary-num" id="summaryNum"></span>
    </div>
  </div>

  <div class="cust-form-col">
  <form id="customizeForm">

    <div class="form-step" id="stepDesign">

      <div class="field-group">
        <label class="field-label">Number of Shirts<span class="required-mark">*</span></label>
        <input type="text" class="field-input" id="quantity" placeholder="e.g. 60" required>
      </div>

      <div class="field-group">
        <label class="field-label">Garment<span class="required-mark">*</span></label>
        <select class="field-select" id="garmentType" required>
          <option value="">Select a Garment&hellip;</option>
          <option>T-Shirt</option>
          <option>Hoodie</option>
          <option>Hat</option>
          <option>Tank Top</option>
          <option>Drinkware</option>
        </select>
      </div>

      <div class="field-group">
        <label class="field-label">Color<span class="required-mark">*</span></label>
        <select class="field-select" id="colorSelect" required>
          <option value="">Select a Color&hellip;</option>
          <option>Black</option>
          <option>White</option>
          <option>Cream</option>
          <option>Gold</option>
          <option>Navy</option>
          <option>Charcoal</option>
          <option>Heather Grey</option>
          <option>Maroon</option>
          <option>Forest Green</option>
          <option>Light Blue</option>
        </select>
      </div>

      <div class="field-group">
        <label class="field-label">Would You Like to Make Any Changes?</label>
        <textarea class="field-textarea" id="customizeNotes" placeholder="Ex. I&rsquo;d like to change the design&rsquo;s wording from &lsquo;Alpha Phi&rsquo; to &lsquo;Beta Chi&rsquo;"></textarea>
      </div>

      <div class="field-group">
        <label class="field-label">Reference Images, Logos, etc. (Optional)</label>

        <div style="margin-bottom:18px;">
          <p style="font-size:13px;color:#4A453D;margin-bottom:8px;">Image 1</p>
          <div class="file-field">
            <div class="file-btn-wrap">
              <span class="file-btn">Choose File</span>
              <input type="file" class="file-input-hidden" id="refImage1" accept="image/*,.pdf" onchange="updateFileName('refImage1','fileName1')">
            </div>
            <span class="file-name" id="fileName1">No file chosen</span>
          </div>
          <p class="field-hint">Accepted file types: jpg, png, pdf. Max file size: 20 MB.</p>
        </div>

        <div>
          <p style="font-size:13px;color:#4A453D;margin-bottom:8px;">Image 2</p>
          <div class="file-field">
            <div class="file-btn-wrap">
              <span class="file-btn">Choose File</span>
              <input type="file" class="file-input-hidden" id="refImage2" accept="image/*,.pdf" onchange="updateFileName('refImage2','fileName2')">
            </div>
            <span class="file-name" id="fileName2">No file chosen</span>
          </div>
          <p class="field-hint">Accepted file types: jpg, png, pdf. Max file size: 20 MB.</p>
        </div>
      </div>

      <div class="submit-row">
        <button type="button" class="submit-btn" onclick="goToStep2()">Next Step &rarr;</button>
      </div>

    </div>

    <div class="form-step hidden" id="stepInfo">

      <h2 class="step-title">Your Information</h2>

      <div class="field-group">
        <label class="field-label">Your Name<span class="required-mark">*</span></label>
        <div class="name-row">
          <div>
            <input type="text" class="field-input" id="firstName" placeholder="First" required>
            <p class="name-sub-label">First</p>
          </div>
          <div>
            <input type="text" class="field-input" id="lastName" placeholder="Last" required>
            <p class="name-sub-label">Last</p>
          </div>
        </div>
      </div>

      <div class="field-group">
        <label class="field-label">Email Address<span class="required-mark">*</span></label>
        <input type="email" class="field-input" id="contactEmail" placeholder="you@school.edu" required>
      </div>

      <div class="field-group">
        <label class="field-label">Phone Number<span class="required-mark">*</span></label>
        <input type="tel" class="field-input" id="contactPhone" placeholder="(555) 555-5555" required>
      </div>

      <div class="field-group">
        <label class="field-label">Organization<span class="required-mark">*</span></label>
        <input type="text" class="field-input" id="orgName" placeholder="e.g. Kappa Alpha Theta" required>
      </div>

      <div class="field-group">
        <label class="field-label">School<span class="required-mark">*</span></label>
        <input type="text" class="field-input" id="schoolName" placeholder="e.g. University of Georgia" required>
      </div>

      <div class="field-group">
        <label class="field-label">State or Province<span class="required-mark">*</span></label>
        <select class="field-select" id="stateProvince" required>
          <option value="">&mdash; Select State &mdash;</option>
          <option>Alabama</option><option>Alaska</option><option>Arizona</option><option>Arkansas</option>
          <option>California</option><option>Colorado</option><option>Connecticut</option><option>Delaware</option>
          <option>Florida</option><option>Georgia</option><option>Hawaii</option><option>Idaho</option>
          <option>Illinois</option><option>Indiana</option><option>Iowa</option><option>Kansas</option>
          <option>Kentucky</option><option>Louisiana</option><option>Maine</option><option>Maryland</option>
          <option>Massachusetts</option><option>Michigan</option><option>Minnesota</option><option>Mississippi</option>
          <option>Missouri</option><option>Montana</option><option>Nebraska</option><option>Nevada</option>
          <option>New Hampshire</option><option>New Jersey</option><option>New Mexico</option><option>New York</option>
          <option>North Carolina</option><option>North Dakota</option><option>Ohio</option><option>Oklahoma</option>
          <option>Oregon</option><option>Pennsylvania</option><option>Rhode Island</option><option>South Carolina</option>
          <option>South Dakota</option><option>Tennessee</option><option>Texas</option><option>Utah</option>
          <option>Vermont</option><option>Virginia</option><option>Washington</option><option>West Virginia</option>
          <option>Wisconsin</option><option>Wyoming</option><option>District of Columbia</option>
        </select>
      </div>

      <div class="field-group">
        <div class="recaptcha-box">
          <div class="recaptcha-checkbox" id="recaptchaCheck" onclick="this.classList.toggle('checked')"></div>
          <div>
            <span class="recaptcha-label">I&rsquo;m not a robot</span>
            <p class="recaptcha-note">Verification will be enabled at checkout.</p>
          </div>
        </div>
      </div>

      <div class="step-nav-row">
        <button type="button" class="prev-btn" onclick="goToStep1()">&larr; Previous</button>
        <button type="submit" class="submit-btn">Send Request</button>
      </div>

    </div>

  </form>

  <div class="success-box" id="successBox">
    <p class="eyebrow" style="margin-bottom:16px;">Confirmation</p>
    <h3>You&rsquo;re All Set!</h3>
    <p>We have received your request and will be reaching out with an art proof soon.</p>
    <p style="margin-top:14px;">Thank you for the opportunity to bring your design to life.</p>
    <a href="index.html" class="cta-link" style="margin-top:32px;display:inline-block;">Return Home</a>
  </div>

  </div>
</div>
</div>
</div>

<div class="cat-bg">
<section class="designs-section" id="relatedSection">
  <p class="designs-label">You May Also Like</p>
  <div class="designs-grid" id="relatedDesigns"></div>
</section>
</div>

<script>
  const allDesignsData = ALL_DESIGNS_JSON_PLACEHOLDER;

  const params = new URLSearchParams(window.location.search);
  const design = params.get('design') || 'Custom Design';
  const category = params.get('category') || '';
  const num = params.get('num') || '';
  const image = params.get('image') || '';

  document.getElementById('summaryName').textContent = design;
  document.getElementById('summaryNum').textContent = num ? ('#' + num) : '';

  if (image) {
    document.getElementById('previewImgBox').innerHTML =
      '<img src="' + image + '" alt="' + design + '" style="width:100%;height:100%;object-fit:contain;">';
  }

  function renderRelatedDesigns() {
    const grid = document.getElementById('relatedDesigns');
    const section = document.getElementById('relatedSection');
    const list = allDesignsData[category];
    if (!list) {
      section.style.display = 'none';
      return;
    }
    const currentNum = parseInt(num, 10);
    const related = list.filter(function(d) { return d.num !== currentNum; }).slice(0, 4);
    if (related.length === 0) {
      section.style.display = 'none';
      return;
    }
    grid.innerHTML = related.map(function(d) {
      const qParams = {design: d.name, category: category, num: d.num};
      if (d.image) qParams.image = d.image;
      const q = new URLSearchParams(qParams).toString();
      const imgBlock = d.image
        ? '<img src="' + d.image + '" alt="' + d.name + '" style="width:100%;height:100%;object-fit:contain;">'
        : '<svg width="32" height="32" viewBox="0 0 44 44" fill="none" style="opacity:0.18"><rect x="6" y="38" width="32" height="3" fill="#3D2A0A"/><rect x="10" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="20" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="30" y="10" width="4" height="28" fill="#3D2A0A"/><rect x="6" y="6" width="32" height="4" fill="#3D2A0A"/><rect x="4" y="3" width="36" height="3" fill="#3D2A0A"/></svg><span class="design-ph-label">Image Coming Soon</span>';
      return '<div class="design-card reveal revealed">' +
        '<div class="design-img">' +
          imgBlock +
          '<div class="design-overlay"><a href="customize.html?' + q + '" class="customize-btn">Customize This Design</a></div>' +
        '</div>' +
        '<a href="customize.html?' + q + '" class="design-info" style="text-decoration:none;display:block;">' +
          '<span class="design-name">' + d.name + '</span>' +
          '<span class="design-num">#' + d.num + '</span>' +
        '</a>' +
      '</div>';
    }).join('');
  }
  renderRelatedDesigns();

  function updateFileName(inputId, labelId) {
    const input = document.getElementById(inputId);
    const label = document.getElementById(labelId);
    label.textContent = (input.files && input.files.length > 0) ? input.files[0].name : 'No file chosen';
  }

  function setProgress(stepNum) {
    document.getElementById('progStep1').classList.toggle('active', stepNum === 1);
    document.getElementById('progStep2').classList.toggle('active', stepNum === 2);
    document.getElementById('progStep3').classList.toggle('active', stepNum === 3);
  }

  function goToStep2() {
    const step1 = document.getElementById('stepDesign');
    const requiredFields = step1.querySelectorAll('[required]');
    for (const field of requiredFields) {
      if (!field.checkValidity()) {
        field.reportValidity();
        return;
      }
    }
    document.getElementById('stepDesign').classList.add('hidden');
    document.getElementById('stepInfo').classList.remove('hidden');
    setProgress(2);
    window.scrollTo({top: document.getElementById('customizeForm').offsetTop - 100, behavior: 'smooth'});
  }

  function goToStep1() {
    document.getElementById('stepInfo').classList.add('hidden');
    document.getElementById('stepDesign').classList.remove('hidden');
    setProgress(1);
    window.scrollTo({top: document.getElementById('customizeForm').offsetTop - 100, behavior: 'smooth'});
  }

  document.getElementById('customizeForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // NOTE: Not yet wired to a backend/email service.
    // Intended destination once connected: art@greekempire.com
    const submission = {
      design: design,
      category: category,
      designNumber: num,
      quantity: document.getElementById('quantity').value,
      garment: document.getElementById('garmentType').value,
      color: document.getElementById('colorSelect').value,
      notes: document.getElementById('customizeNotes').value,
      referenceImage1: (document.getElementById('refImage1').files[0] || {}).name || null,
      referenceImage2: (document.getElementById('refImage2').files[0] || {}).name || null,
      firstName: document.getElementById('firstName').value,
      lastName: document.getElementById('lastName').value,
      contactEmail: document.getElementById('contactEmail').value,
      contactPhone: document.getElementById('contactPhone').value,
      organization: document.getElementById('orgName').value,
      school: document.getElementById('schoolName').value,
      state: document.getElementById('stateProvince').value
    };
    console.log('Customize request (not yet emailed):', submission);

    document.getElementById('customizeForm').style.display = 'none';
    document.getElementById('successBox').classList.add('show');
    setProgress(3);
  });
</script>""" + foot()

    import json
    all_designs = {}
    for idx, (cname, cslug, cdesc) in enumerate(CATS):
        base_num = 1000 + (idx * 50)
        real_list = REAL_DESIGNS.get(cname, [])
        designs = []
        for i in range(max(12, len(real_list))):
            num = base_num + (i + 1)
            if i < len(real_list):
                designs.append({"name": real_list[i]["name"], "num": num, "image": real_list[i]["image"]})
            else:
                label = DESIGN_LABELS[i % len(DESIGN_LABELS)]
                designs.append({"name": f"{cname} — {label}", "num": num, "image": None})
        all_designs[cname] = designs
    html = html.replace("ALL_DESIGNS_JSON_PLACEHOLDER", json.dumps(all_designs))

    with open(f"{DIR}/customize.html", "w") as f:
        f.write(html)
    print("✓ customize.html")

make_index()
for idx, (name, slug, desc) in enumerate(CATS):
    make_cat(idx, name, slug, desc)
make_customize()

print(f"\nDone — {len(CATS) + 1} pages generated.")
