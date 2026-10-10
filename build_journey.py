from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).parent
# Terrain repeats beyond the clipped viewport; neither endpoint is visible.
terrain = [(0,215),(190,215),(242,191),(258,191),(267,183),(288,183),(297,175),(318,175),(327,167),(390,167),(440,191),(485,191),(550,173),(605,173),(665,215),(800,215)]
def height(x):
    x %= 800
    for (a,ya),(b,yb) in zip(terrain,terrain[1:]):
        if a <= x <= b:
            return ya+(yb-ya)*(x-a)/(b-a)
    return 215
frames = ''.join(f'{i/2:.1f}%{{transform:translate(742px,{height(242+i*4):.2f}px)}}' for i in range(201))
paths = []
for shift in (-800,0,800,1600):
    pts=' '.join(f'{x+shift},{y}' for x,y in terrain)
    paths.append(f'<polygon points="{shift},300 {pts} {shift+800},300" fill="#f5f5f2"/><polyline points="{pts}" fill="none" stroke="#7e8788" stroke-width="2" stroke-linejoin="round"/>')
    for x,y in [(40,215),(355,167),(580,173)]:
        paths.append(f'<path d="M{x+shift} {y+8}v5m7 -5v5m7 -5v5" stroke="#d1d5d2"/>')
    paths.append(f'''<g transform="translate({shift},0)">
    <path d="M76 219H182V268H76Z" fill="white"/>
    <path d="M65 251Q124 272 190 249M72 259Q130 278 184 258" fill="none" stroke="#d4e6e6" stroke-width="1.5"/>
    <path d="M77 239Q129 209 181 239" fill="none" stroke="#a6a092" stroke-width="3"/>
    <path d="M77 215V243M103 215V225M129 215V222M155 215V225M181 215V243" stroke="#a6a092" stroke-width="1.6"/>
    <path d="M72 211H187M72 215H187" stroke="#8f8c80" stroke-width="2"/>
    <path d="M361 167V135M348 141H375L380 146L375 151H348Z" fill="#e7ece5" stroke="#9ba994" stroke-width="1.2"/>
    <text x="353" y="148" font-family="monospace" font-size="7" fill="#75836e">n+1</text>
    <path d="M455 191V170H477V191M453 170H480" fill="none" stroke="#b3ada2" stroke-width="1.4"/>
    <path d="M456 164L466 167L477 164V173L466 176L456 173Z" fill="#e0d6c3" stroke="#ac9e84" stroke-width="1"/>
    <path d="M466 167V176" stroke="#ac9e84"/>
    <path d="M570 173V149" stroke="#8d9690" stroke-width="1.3"/><path d="M570 149h15l-4 5 4 5h-15" fill="#9cae9f"/>
    <path d="M706 215V200M706 208Q696 209 697 201Q705 201 706 208M706 205Q716 204 714 196Q706 196 706 205" fill="#b9cbb7" stroke="#91aa92" stroke-width="1"/>
    </g>''')
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300" role="img" aria-labelledby="title desc">
<title id="title">deniz-mn — Learning is a journey</title>
<desc id="desc">An adult female university student with glasses and a backpack walks through an open-ended landscape with a bridge, ascending steps, a book station and a summit flag.</desc>
<defs><clipPath id="scene"><rect x="520" y="20" width="420" height="255" rx="8"/></clipPath><linearGradient id="fade"><stop stop-color="white"/><stop offset="1" stop-color="white" stop-opacity="0"/></linearGradient></defs>
<style>
text{font-family:'Segoe UI',Arial,sans-serif}.land{animation:land 24s linear infinite}.student{animation:height 24s linear infinite}.frontleg{animation:stride 1.1s ease-in-out infinite;transform-origin:0 -42px}.backleg{animation:stride 1.1s ease-in-out -.55s infinite;transform-origin:0 -42px}.arm{animation:arm 1.1s ease-in-out infinite;transform-origin:0 -80px}.body{animation:bob .55s ease-in-out infinite}
@keyframes land{from{transform:translateX(500px)}to{transform:translateX(-300px)}}@keyframes height{FRAMES}@keyframes stride{0%,100%{transform:rotate(-19deg)}50%{transform:rotate(19deg)}}@keyframes arm{0%,100%{transform:rotate(14deg)}50%{transform:rotate(-14deg)}}@keyframes bob{50%{transform:translateY(-1.5px)}}
@media(prefers-reduced-motion:reduce){.land,.student,.frontleg,.backleg,.arm,.body{animation:none}.land{transform:translateX(500px)}.student{transform:translate(742px,189px)}}
</style>
<rect width="960" height="300" fill="#fff"/>
<path d="M40 45H69" stroke="#738c80" stroke-width="3"/>
<text x="40" y="83" fill="#6e7875" font-size="11" letter-spacing="2.2">COMPUTER ENGINEERING</text>
<text x="38" y="149" fill="#303b3a" font-size="49" font-weight="600" letter-spacing="-1.6">deniz-mn</text>
<text x="40" y="191" fill="#68736f" font-size="16">Learning, one step at a time.</text>
<text x="40" y="234" fill="#89918d" font-size="11" letter-spacing="1.6">UNDERGRADUATE · SEMESTER 7</text>
<g clip-path="url(#scene)">
<path d="M490 157L591 121L672 145L789 85L916 135L994 108" fill="none" stroke="#eeefec" stroke-width="1.4"/>
<path d="M520 174L617 156L689 164L816 119L964 161" fill="none" stroke="#f2f2ef" stroke-width="1"/>
<g class="land">TERRAIN</g>
<g class="student">
<ellipse cx="0" cy="2" rx="17" ry="3" fill="#344440" opacity=".1"/>
<g class="backleg" fill="none" stroke="#777f7f" stroke-width="7" stroke-linecap="round"><path d="M-2 -43L-7 -23L-8 -5"/><path d="M-8 -4H0" stroke="#4a5453" stroke-width="5"/></g>
<g class="frontleg" fill="none" stroke="#424e50" stroke-width="7" stroke-linecap="round"><path d="M3 -43L5 -22L4 -4"/><path d="M4 -3H13" stroke="#303a3d" stroke-width="5"/></g>
<g class="body">
<path d="M-6 -110Q-19 -117 -20 -100Q-20 -86 -28 -82Q-11 -79 -12 -98L-5 -104Z" fill="#51484a"/>
<path d="M-16 -104Q-17 -90 -22 -87" stroke="#756365" stroke-width="1.4" fill="none"/>
<rect x="-21" y="-84" width="17" height="34" rx="5" fill="#9b8d76" stroke="#82755f" stroke-width="1"/>
<path d="M-19 -77H-8M-17 -64H-9" stroke="#c1b5a0" stroke-width="1.3"/>
<path d="M-7 -88Q3 -92 9 -83L8 -66L13 -46Q0 -41 -10 -47L-9 -65L-12 -75Z" fill="#718c80"/>
<path d="M-6 -85L-5 -56" stroke="#d3d8ce" stroke-width="2"/>
<path d="M1 -94V-85" stroke="#c3a58b" stroke-width="6"/>
<path d="M-6 -108Q0 -115 8 -110L11 -102L14 -99L10 -97L9 -91Q0 -88 -5 -96Z" fill="#d2b59d"/>
<path d="M-7 -101Q-12 -114 1 -116Q13 -117 11 -106L7 -109L2 -108L-2 -100L-3 -94L-8 -97Z" fill="#51484a"/>
<path d="M-14 -106L-10 -105" stroke="#b7a4bf" stroke-width="2.5" stroke-linecap="round"/>
<path d="M5 -102H12M6 -102V-99H10V-102" stroke="#555759" stroke-width="1" fill="none"/>
<path class="arm" d="M4 -80L9 -64L17 -57" stroke="#59766b" stroke-width="6" stroke-linecap="round" fill="none"/>
<circle cx="17" cy="-57" r="3" fill="#d2b59d"/>
</g></g>
<rect x="520" y="20" width="33" height="255" fill="url(#fade)"/><rect x="907" y="20" width="33" height="255" fill="url(#fade)" transform="rotate(180 923.5 147.5)"/>
</g>
<text x="742" y="287" text-anchor="middle" fill="#9aA19c" font-size="9" letter-spacing="1.6">KEEP MOVING. KEEP LEARNING.</text>
</svg>'''.replace('FRAMES',frames).replace('TERRAIN',''.join(paths))
ET.fromstring(svg)
(root/'assets'/'student-journey.svg').write_text(svg,encoding='utf-8')
print('Generated adult student and continuous scrolling terrain; SVG valid.')
