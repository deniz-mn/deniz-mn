"""Reuse the scrolling landscape with a separately drawn penguin mascot."""
from pathlib import Path
import runpy
import math
import re
import xml.etree.ElementTree as ET

root = Path(__file__).parent
runpy.run_path(str(root/'build_journey.py'))
svg = (root/'assets'/'student-journey.svg').read_text(encoding='utf-8')
start = svg.index('<g class="student">')
end = svg.index('<rect x="520" y="20" width="33"', start)
penguin = '''<g class="student">
<ellipse cx="0" cy="3" rx="29" ry="4" fill="#818d99" opacity=".12"/>
<g class="penguin">
<path class="foot back" d="M-16 -9Q-29 -5 -26 0Q-13 5 -5 -1L-6 -9Z" fill="#d9ad70"/>
<path class="foot" d="M6 -9Q2 -3 9 1Q22 4 30 0Q28 -6 16 -10Z" fill="#e5b779"/>
<g class="roundbody">
<!-- Backpack, notebook and shoulder loop. -->
<path d="M-29 -71Q-43 -73 -44 -57L-44 -27Q-42 -18 -30 -22L-21 -30V-62Z" fill="#9ab9ac" stroke="#7d9e92" stroke-width="1.2"/>
<path d="M-39 -69L-39 -80L-29 -82L-28 -68" fill="#e8dec6" stroke="#b8ac91" stroke-width="1"/>
<path d="M-36 -78L-31 -79M-36 -75L-31 -76" stroke="#c5b99f"/>
<path d="M-40 -46Q-33 -49 -28 -43V-31Q-34 -26 -40 -30Z" fill="#b5cec1"/>
<path d="M-31 -70Q-27 -82 -21 -70" stroke="#7d9e92" stroke-width="3" fill="none"/>
<!-- Soft pear-shaped silhouette, a single connected face and belly. -->
<path d="M-27 -70C-28 -94 -15 -108 3 -106C24 -105 31 -88 29 -67C33 -48 41 -24 24 -12C13 -4 -15 -4 -28 -16C-40 -27 -33 -52 -27 -70Z" fill="#485460"/>
<path d="M-19 -69C-24 -92 -7 -99 2 -87C13 -101 29 -89 23 -68C24 -52 33 -32 20 -20C9 -11 -10 -12 -20 -22C-31 -36 -23 -55 -19 -69Z" fill="#fafaf7"/>
<path d="M-8 -104Q-7 -113 0 -110M-1 -105Q5 -112 9 -108" stroke="#485460" stroke-width="3" fill="none" stroke-linecap="round"/>
<!-- Small academic glasses; blinking remains visible through the lenses. -->
<g class="penguinEyes" fill="#394652"><ellipse cx="-7" cy="-77" rx="2.1" ry="3"/><ellipse cx="15" cy="-77" rx="2.1" ry="3"/></g>
<g stroke="#7a8992" stroke-width="1.25" fill="none"><circle cx="-7" cy="-77" r="7.5"/><circle cx="15" cy="-77" r="7.5"/><path d="M.5 -78Q4 -80 7.5 -78M-15 -79L-21 -81"/></g>
<path d="M1 -71Q7 -75 13 -69Q7 -63 1 -71Z" fill="#e1b473"/>
<ellipse cx="-15" cy="-65" rx="4.5" ry="2" fill="#e9cfbf" opacity=".65"/>
<!-- Scarf follows the stride with a gentle secondary motion. -->
<path class="scarfEnd" d="M-22 -59Q-37 -57 -42 -66L-45 -56Q-35 -46 -20 -51Z" fill="#a9c7bb"/>
<path d="M-25 -62Q-3 -54 25 -62L26 -54Q1 -44 -26 -53Z" fill="#88ad9d"/>
<path d="M15 -54L22 -35L13 -33L8 -53Z" fill="#9bbfae"/>
<!-- Flipper balances the walker instead of a human arm. -->
<path class="flipper" d="M24 -52Q38 -47 42 -26Q37 -20 27 -32L20 -44Z" fill="#596774"/>
<path d="M-26 -46Q-36 -41 -32 -26" fill="none" stroke="#637480" stroke-width="2" stroke-linecap="round"/>
</g></g></g>
'''
svg = svg[:start]+penguin+svg[end:]
css = '''
.penguin{animation:waddle 1.2s ease-in-out infinite;transform-origin:0 -8px}.foot{animation:feet 1.2s ease-in-out infinite;transform-origin:9px -4px}.foot.back{animation-delay:-.6s}.flipper{animation:balance 1.2s ease-in-out infinite;transform-origin:24px -50px}.scarfEnd{animation:flutter 1.8s ease-in-out infinite;transform-origin:-22px -56px}.penguinEyes{transform-box:fill-box;transform-origin:center;animation:blink 5s infinite}
@keyframes waddle{0%,100%{transform:rotate(-3deg)}25%,75%{transform:translateY(-2px)}50%{transform:rotate(3deg)}}@keyframes feet{0%,100%{transform:translate(0,0) rotate(0)}50%{transform:translate(3px,-4px) rotate(-10deg)}}@keyframes balance{0%,100%{transform:rotate(-7deg)}50%{transform:rotate(9deg)}}@keyframes flutter{50%{transform:rotate(9deg)}}@keyframes blink{0%,43%,47%,100%{transform:scaleY(1)}45%{transform:scaleY(.1)}}
@media(prefers-reduced-motion:reduce){.penguin,.foot,.flipper,.scarfEnd,.penguinEyes{animation:none}}
'''
svg = svg.replace('</style>',css+'</style>')
svg = svg.replace('An adult female university student with glasses and a backpack', 'A round penguin student with glasses, a red scarf and a backpack')
svg = svg.replace('#7e8788','#b2bdb5').replace('#f5f5f2','#f6f8f4').replace('#8f8c80','#aaa08c')
svg = svg.replace('#a9c7bb','#e46a67').replace('#88ad9d','#cf464e').replace('#9bbfae','#de5960')

# A new rolling landscape replaces the entire angular terrain, not just its colors.
def ground(x):
    return 219 - 13*(1-math.cos(2*math.pi*x/800)) - 4*math.sin(4*math.pi*x/800)

land = []
for offset in [-800,0,800,1600]:
    line = ' '.join(f'{x+offset},{ground(x):.2f}' for x in range(0,801,4))
    land.append(f'<polygon points="{offset},300 {line} {offset+800},300" fill="#f0f6eb"/><polyline points="{line}" fill="none" stroke="#bbd4ae" stroke-width="2.5" stroke-linecap="round"/>')
    land.append(f'''<g transform="translate({offset},0)">
    <path d="M487 197Q475 215 490 234T483 275H535Q550 250 531 232T536 199Z" fill="#e2f3f8"/>
    <path d="M492 211Q508 214 526 210M499 231Q512 235 529 231M490 251Q507 255 530 251" stroke="#acd9e7" stroke-width="1.5" fill="none" stroke-linecap="round"/>
    <ellipse cx="480" cy="201" rx="11" ry="4" fill="#cfdbcd"/><ellipse cx="540" cy="203" rx="12" ry="4" fill="#cfdbcd"/>
    <ellipse cx="608" cy="220" rx="8" ry="3.5" fill="#d5ddce"/><ellipse cx="629" cy="226" rx="5" ry="2.5" fill="#dce4d6"/>
    </g>''')
    for x in [95,180,325,680,743]:
        y=ground(x)
        land.append(f'<g transform="translate({offset+x},{y:.2f})"><path d="M0 0Q-3 -12 0 -20M-1 -6Q-12 -7 -9 -13Q-2 -13 -1 -6" fill="#a7c99b" stroke="#95b88a" stroke-width="1.1"/><g fill="{ "#f3d79a" if x%2 else "#e9bec7" }"><circle cx="0" cy="-22" r="4"/><circle cx="-4" cy="-18" r="4"/><circle cx="4" cy="-18" r="4"/><circle cx="0" cy="-14" r="4"/></g><circle cx="0" cy="-18" r="2.5" fill="#fff8df"/></g>')
    # A little stack of books rests beside the path, keeping the academic cue.
    y=ground(390)
    land.append(f'<g transform="translate({390+offset},{y+12:.2f})" stroke-linejoin="round"><rect x="-15" y="-4" width="29" height="6" rx="2" fill="#b5c8dd"/><rect x="-11" y="-10" width="29" height="6" rx="2" fill="#e4c8a8"/><path d="M-8 -7H14M-12 -1H11" stroke="#fffaf0" stroke-width="2"/></g>')

start=svg.index('<g class="land">')
end=svg.index('<g class="student">',start)
svg=svg[:start]+'<g class="land">'+''.join(land)+'</g>\n'+svg[end:]
frames=[]
for i in range(401):
    x=(242+i*2)%800
    # The character clears the stream in a continuous, synchronized small hop.
    hop=28*math.sin(math.pi*(x-468)/86) if 468<x<554 else 0
    frames.append(f'{i/4:.2f}%{{transform:translate(742px,{ground(x)-hop:.2f}px)}}')
a=svg.index('@keyframes height{')
b=svg.index('@keyframes stride',a)
svg=svg[:a]+'@keyframes height{'+''.join(frames)+'}'+svg[b:]
svg=re.sub(r'<path d="M490 157.*?/>\s*<path d="M520 174.*?/>', '''<ellipse cx="758" cy="156" rx="160" ry="86" fill="#fbfcf6"/>
<g fill="#eef4f6"><path d="M578 73Q580 62 591 65Q598 51 610 62Q624 59 626 73Z"/><path d="M857 98Q859 86 870 89Q877 76 888 87Q902 85 906 98Z"/></g>''',svg)
butterfly='''<g class="butterfly"><g transform="translate(820 99) rotate(-14)"><g class="wings" fill="#d4b6e5"><ellipse cx="-5" cy="-4" rx="6" ry="8"/><ellipse cx="5" cy="-4" rx="6" ry="8"/><ellipse cx="-4" cy="4" rx="4" ry="5"/><ellipse cx="4" cy="4" rx="4" ry="5"/></g><path d="M0 -8V7M0 -7L-3 -11M0 -7L3 -11" stroke="#a38bb3" stroke-width="1.2" fill="none" stroke-linecap="round"/></g></g>'''
svg=svg.replace('<rect x="520" y="20" width="33"',butterfly+'<rect x="520" y="20" width="33"')
svg=svg.replace('</style>','''.butterfly{animation:drift 6s ease-in-out infinite}.wings{transform-box:fill-box;transform-origin:center;animation:wing .3s ease-in-out infinite}@keyframes drift{0%,100%{transform:translate(0,0)}50%{transform:translate(-16px,-12px)}}@keyframes wing{50%{transform:scaleX(.35)}}@media(prefers-reduced-motion:reduce){.butterfly,.wings{animation:none}.student{transform:translate(742px,198px)}}
</style>''')
svg=svg.replace('with a bridge, ascending steps, a book station and a summit flag.', 'with soft hills, flowers, a stream and a fluttering butterfly. The penguin hops over the stream.')
ET.fromstring(svg)
(root/'assets'/'penguin-journey.svg').write_text(svg,encoding='utf-8')
print('Penguin SVG generated and XML validated.')
