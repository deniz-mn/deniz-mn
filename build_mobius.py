"""Build a self-contained animated SVG from a projected Mobius surface."""
from pathlib import Path
import math
import xml.etree.ElementTree as ET

root = Path(__file__).parent

def point(u, v):
    r = 124 + v * math.cos(u / 2)
    return (744 + r * math.cos(u), 162 + .40 * r * math.sin(u) - .92 * v * math.sin(u / 2))

def xy(p):
    return f'{p[0]:.2f},{p[1]:.2f}'

panels = []
for i in range(180):
    a, b = 2 * math.pi * i / 180, 2 * math.pi * (i + 1) / 180
    pts = [point(a,-22), point(b,-22), point(b,22), point(a,22)]
    shade = (math.cos(a/2)+1)/2
    rgb = tuple(round(x*(1-shade)+y*shade) for x,y in zip((162,143,213),(226,219,249)))
    color = '#%02x%02x%02x' % rgb
    panels.append((math.sin(a), f'<polygon points="{" ".join(map(xy,pts))}" fill="{color}" stroke="{color}" stroke-width=".7"/>'))
surface = ''.join(p for _,p in sorted(panels))
edges = ''
for v in [-22,22]:
    edges += '<polyline points="'+' '.join(xy(point(i*math.pi/90,v)) for i in range(181))+'" fill="none" stroke="#8874b2" stroke-width="1" opacity=".65"/>'

frames=[]
last_angle = None
for i in range(121):
    u = 4*math.pi*i/120 + math.pi
    x,y=point(u,0)
    nx = -math.sin(u/2)*math.cos(u)
    ny = -.4*math.sin(u/2)*math.sin(u)-.92*math.cos(u/2)
    angle = math.degrees(math.atan2(nx,-ny))
    if last_angle is not None:
        while angle-last_angle>180: angle-=360
        while angle-last_angle < -180: angle+=360
    last_angle=angle
    frames.append(f'{i/120*100:.4f}%{{transform:translate({x:.2f}px,{y:.2f}px) rotate({angle:.2f}deg)}}')

svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="300" viewBox="0 0 960 300" role="img" aria-labelledby="title desc">
<title id="title">deniz-mn — A little explorer on a Mobius strip</title>
<desc id="desc">A cute round-headed student with a mint backpack walks around a lilac Mobius strip, turning upside down and returning upright after two circuits. White background.</desc>
<style>
text{font-family:'Segoe UI',Arial,sans-serif}.walker{animation:journey 24s linear infinite}.stepA{animation:step .65s ease-in-out infinite;transform-origin:0 -9px}.stepB{animation:step .65s ease-in-out -.325s infinite;transform-origin:0 -9px}.bob{animation:bob .325s ease-in-out infinite}.eyes{transform-box:fill-box;transform-origin:center;animation:blink 4.7s infinite}
@keyframes journey{FRAMES}
@keyframes step{0%,100%{transform:rotate(-16deg)}50%{transform:rotate(16deg)}}@keyframes bob{50%{transform:translateY(-1.3px)}}@keyframes blink{0%,44%,48%,100%{transform:scaleY(1)}46%{transform:scaleY(.1)}}
@media(prefers-reduced-motion:reduce){.walker,.stepA,.stepB,.bob,.eyes{animation:none}.walker{transform:translate(744px,112px)}}
</style>
<rect width="960" height="300" rx="18" fill="white"/>
<path d="M40 43H70" stroke="#9274c7" stroke-width="4" stroke-linecap="round"/>
<text x="40" y="82" fill="#726881" font-size="11" letter-spacing="2.3">COMPUTER ENGINEERING</text>
<text x="37" y="148" fill="#30283e" font-size="51" font-weight="650" letter-spacing="-2">deniz-mn</text>
<text x="40" y="191" fill="#706779" font-size="16">Stay curious. Keep exploring.</text>
<rect x="40" y="215" width="107" height="28" rx="14" fill="#f3effa"/>
<text x="57" y="234" fill="#7b659c" font-size="11">SEMESTER 7</text>
<ellipse cx="744" cy="244" rx="129" ry="9" fill="#f4f1f8"/>
SURFACE
EDGES
<g class="walker"><ellipse cx="0" cy="1" rx="9" ry="3" fill="#65547e" opacity=".16"/>
<path class="stepA" d="M-4 -12L-5 -3L-10 -2" fill="none" stroke="#615174" stroke-width="4" stroke-linecap="round"/>
<path class="stepB" d="M4 -12L5 -3L10 -2" fill="none" stroke="#615174" stroke-width="4" stroke-linecap="round"/>
<g class="bob">
<rect x="6" y="-34" width="14" height="23" rx="6" fill="#9bd2be" stroke="#608f7e" stroke-width="1.5"/>
<path d="M12 -28V-19" stroke="#d5efe5" stroke-width="2" stroke-linecap="round"/>
<rect x="-10" y="-33" width="22" height="22" rx="8" fill="#a997da" stroke="#766298" stroke-width="1.4"/>
<path class="stepA" d="M-9 -29L-14 -19" stroke="#766298" stroke-width="4" stroke-linecap="round"/>
<path d="M8 -29L11 -21" stroke="#e4d9f4" stroke-width="3" stroke-linecap="round"/>
<circle cx="0" cy="-47" r="18" fill="#fff1df" stroke="#806780" stroke-width="1.5"/>
<path d="M-17 -51Q-12 -71 4 -64Q16 -63 18 -49Q9 -53 5 -59Q-3 -50 -17 -51" fill="#655174"/>
<path d="M-2 -64Q-6 -73 1 -71" fill="none" stroke="#655174" stroke-width="2.5" stroke-linecap="round"/>
<g class="eyes" fill="#594764"><ellipse cx="-6" cy="-46" rx="2" ry="3"/><ellipse cx="7" cy="-46" rx="2" ry="3"/></g>
<ellipse cx="-11" cy="-40" rx="4" ry="2.5" fill="#edb5bb" opacity=".7"/><ellipse cx="12" cy="-40" rx="4" ry="2.5" fill="#edb5bb" opacity=".7"/>
<path d="M-3 -39Q1 -35 5 -39" fill="none" stroke="#946578" stroke-width="1.5" stroke-linecap="round"/>
</g></g>
<text x="744" y="278" text-anchor="middle" font-size="10" fill="#9688a4" letter-spacing="1.5">ONE SURFACE. ENDLESS CURIOSITY.</text>
</svg>'''.replace('FRAMES',''.join(frames)).replace('SURFACE\n',surface+'\n').replace('EDGES',edges)
ET.fromstring(svg)
(root/'assets'/'mobius-banner.svg').write_text(svg,encoding='utf-8')
print('Built Mobius banner with 180 surface panels and a two-circuit walking cycle.')
