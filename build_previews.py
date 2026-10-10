from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET

root = Path(__file__).parent
intro = "I'm a seventh-semester Computer Engineering undergraduate with project experience across different areas of computing, including artificial intelligence and software development. I enjoy connecting ideas, exploring new problems, and turning what I learn into working projects."

def banner(title, drawing):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="280" viewBox="0 0 960 280" role="img" aria-labelledby="title desc">
<title id="title">deniz-mn — Computer Engineering</title>
<desc id="desc">{title}</desc>
<defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101e30"/><stop offset="1" stop-color="#0b1220"/></linearGradient>
<clipPath id="clip"><rect width="960" height="280" rx="18"/></clipPath></defs>
<style>text{{font-family:'Segoe UI',Arial,sans-serif}}.trace{{stroke-dasharray:18 420;animation:travel 16s linear infinite}}.late{{animation-delay:-8s}}@keyframes travel{{from{{stroke-dashoffset:438}}to{{stroke-dashoffset:0}}}}.breathe{{animation:breathe 10s ease-in-out infinite}}@keyframes breathe{{0%,100%{{opacity:.35}}50%{{opacity:.8}}}}@media(prefers-reduced-motion:reduce){{.trace,.breathe{{animation:none}}}}</style>
<g clip-path="url(#clip)"><rect width="960" height="280" fill="url(#bg)"/>
<rect x="40" y="45" width="28" height="3" rx="1.5" fill="#83c8c0"/>
<text x="40" y="85" font-size="11" letter-spacing="2.5" fill="#9cafc6">COMPUTER ENGINEERING</text>
<text x="38" y="150" font-size="49" font-weight="600" letter-spacing="-1.8" fill="#f1f5fc">deniz-mn</text>
<text x="40" y="205" font-size="15" letter-spacing=".6" fill="#b6c5d9">Explore. Build. Understand.</text>
{drawing}</g></svg>'''

contours = '<g fill="none" stroke="#739cae" stroke-width="1.1">'
for i in range(8):
    x = 592 + i * 21
    contours += f'<path opacity="{0.22+i*.055:.3f}" d="M{x} -15 C{x-110} 72 {x+116} 125 {x+12} 203 S{x-12} 287 {x+65} 310"/>'
contours += '</g><g class="breathe" fill="none" stroke="#a2d7cf" stroke-width="1.6"><path d="M655 -15 C545 72 771 125 667 203 S643 287 720 310"/><path d="M718 -15 C608 72 834 125 730 203 S706 287 783 310"/></g>'

modules = '<g fill="none" stroke="#50667e" stroke-width="1.4"><path d="M605 92H696V140H810V92H865M605 190H658V140H696M810 140V204H865"/></g>'
modules += '<g fill="none" stroke="#a2d7cf" stroke-width="2"><path class="trace" d="M605 92H696V140H810V92H865"/><path class="trace late" d="M605 190H658V140H810V204H865"/></g>'
for x,y in [(590,77),(590,175),(681,125),(795,125),(850,77),(850,189)]:
    modules += f'<rect x="{x}" y="{y}" width="30" height="30" rx="7" fill="#172639" stroke="#8aa6bc" stroke-width="1.3"/><rect x="{x+11}" y="{y+11}" width="8" height="8" rx="2" fill="#9bc6ce"/>'

for name, description, drawing in [('contours','Slowly shifting light across mathematical contour lines.',contours),('modules','Subtle signals travel between connected software modules.',modules)]:
    svg = banner(description,drawing)
    ET.fromstring(svg)
    (root/'assets'/f'{name}-banner.svg').write_text(svg,encoding='utf-8')

dynamic = '''<style>
.orbit{transform-box:view-box;transform-origin:746px 140px;animation:orbit 12s linear infinite}.reverse{animation-direction:reverse;animation-duration:18s}.pulse{transform-box:fill-box;transform-origin:center;animation:pulse 3s ease-out infinite}.packet{stroke-dasharray:14 100;animation:packet 3s linear infinite}.core{animation:core 4s ease-in-out infinite}
@keyframes orbit{to{transform:rotate(360deg)}}@keyframes pulse{0%{transform:scale(.65);opacity:.65}100%{transform:scale(1.65);opacity:0}}@keyframes packet{to{stroke-dashoffset:-228}}@keyframes core{0%,100%{opacity:.5}50%{opacity:1}}
@media(prefers-reduced-motion:reduce){.orbit,.pulse,.packet,.core{animation:none}}
</style>
<g fill="none" stroke="#6c8ea9" opacity=".23"><circle cx="746" cy="140" r="104"/><circle cx="746" cy="140" r="78"/><path d="M610 140H882M746 14V266"/></g>
<g fill="none" stroke="#64dbc9" stroke-width="1.4"><circle class="pulse" cx="746" cy="140" r="48"/><circle class="pulse" style="animation-delay:-1.5s" cx="746" cy="140" r="48"/></g>
<g fill="none" stroke="#52738f" stroke-width="1.3"><path d="M614 70H698L746 140L824 202H889"/></g>
<g fill="none" stroke="#7aabce" stroke-width="1.3"><path d="M602 213H667L746 140L818 60H882"/></g>
<g class="packet" fill="none" stroke="#8fe5d6" stroke-width="2"><path d="M614 70H698L746 140L824 202H889"/><path d="M602 213H667L746 140L818 60H882"/></g>
<g class="orbit"><circle cx="746" cy="140" r="104" fill="none" stroke="#71b8d2" stroke-width="2" stroke-dasharray="50 604"/><circle cx="850" cy="140" r="5" fill="#a3dcf0"/><circle cx="642" cy="140" r="3" fill="#8aa8fa"/></g>
<g class="orbit reverse"><circle cx="746" cy="140" r="78" fill="none" stroke="#9b9af4" stroke-width="2" stroke-dasharray="30 460"/><circle cx="824" cy="140" r="4" fill="#b5afff"/></g>
<rect x="722" y="116" width="48" height="48" rx="13" fill="#172d43" stroke="#8bcbc9" stroke-width="1.5"/>
<path class="core" d="M739 132L731 140L739 148M753 132L761 140L753 148" fill="none" stroke="#b1f0e1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<g fill="#14293b" stroke="#91bfd0"><rect x="606" y="62" width="16" height="16" rx="4"/><rect x="594" y="205" width="16" height="16" rx="4"/><rect x="874" y="52" width="16" height="16" rx="4"/><rect x="881" y="194" width="16" height="16" rx="4"/></g>'''

svg = banner('Orbiting points, flowing signals and expanding pulses connect a central computing module.', dynamic)
ET.fromstring(svg)
(root/'assets'/'dynamic-banner.svg').write_text(svg, encoding='utf-8')

style = "*{box-sizing:border-box}body{margin:0;background:#ffffff;color:#1f2328;font:16px/1.7 'Segoe UI',Arial,sans-serif}main{max-width:1000px;margin:32px auto;padding:28px;border:1px solid #d1d9e0;border-radius:10px;background:white}img{display:block;width:100%}.intro,footer{text-align:center}h2{font-size:18px;margin-top:32px}h3{font-size:20px}hr{border:0;border-top:1px solid #d1d9e0;margin:28px 0}footer{font-size:12px;color:#59636e;margin-top:32px}.note{color:#59636e;font-size:14px}@media(max-width:640px){main{margin:12px;padding:16px}}"
page = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>deniz-mn · Profile preview</title><style>{style}</style><main><img src="assets/contours-banner.svg" alt="deniz-mn — Computer Engineering"><p class="intro">Seventh-semester Computer Engineering undergraduate</p><hr><h3>About</h3><p>{escape(intro)}</p><footer>Explore. Build. Understand.</footer></main></html>'''
(root/'preview.html').write_text(page.replace('assets/contours-banner.svg', 'assets/profile-penguin.svg'),encoding='utf-8')
comparison = f'''<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>دو پیشنهاد برای انیمیشن پروفایل</title><style>{style}</style><main><h2>۱. خطوط ریاضی — پیشنهاد من</h2><p class="note">تغییر آرام روشنایی روی منحنی‌ها؛ ساده، دانشگاهی و بدون تأکید روی یک گرایش خاص.</p><img src="assets/contours-banner.svg" alt="بنر خطوط ریاضی"><h2>۲. ماژول‌های متصل</h2><p class="note">حرکت آهستهٔ سیگنال میان ماژول‌ها؛ اشاره‌ای عمومی به ساختن، ارتباط و حل مسئله در مهندسی کامپیوتر.</p><img src="assets/modules-banner.svg" alt="بنر ماژول‌های متصل"><h2>متن معرفی مشترک</h2><p dir="ltr">{escape(intro)}</p></main></html>'''
(root/'animation-options.html').write_text(comparison,encoding='utf-8')
print('Generated two valid SVG banners and updated both previews.')
