from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import zipfile

root=Path(__file__).parent
out=root/'github-ready'
(out/'assets').mkdir(parents=True,exist_ok=True)
sheet=Image.open(root/'assets/cartoon-penguin-walk-sheet.png').convert('RGBA')
def font(size,bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/'+('seguisb.ttf' if bold else 'segoeui.ttf'),size)
frames=[]
for i in range(8):
    col,row=i%4,i//4
    tile=sheet.crop((round(col*sheet.width/4),round(row*sheet.height/2),round((col+1)*sheet.width/4),round((row+1)*sheet.height/2)))
    tile=tile.resize((99,99),Image.Resampling.LANCZOS)
    canvas=Image.new('RGB',(960,285),'white')
    d=ImageDraw.Draw(canvas)
    d.text((40,48),'COMPUTER ENGINEERING',font=font(11),fill='#818b92')
    d.text((38,81),'deniz-mn',font=font(46,True),fill='#303b47')
    d.text((40,148),'Learning, one step at a time.',font=font(16),fill='#707c87')
    d.text((40,201),'UNDERGRADUATE · SEMESTER 7',font=font(11),fill='#818b92')
    d.line((580,245,915,245),fill='#e2eaf0')
    canvas.paste(tile,(703,151),tile)
    frames.append(canvas)
frames[0].save(out/'assets/profile-banner.gif',save_all=True,append_images=frames[1:],duration=150,loop=0,optimize=False,disposal=2)
readme=(root/'README.md').read_text(encoding='utf-8')
import re
readme=re.sub(r'<img[^>]+>', '<img src="./assets/profile-banner.gif" alt="deniz-mn — Computer Engineering, semester 7. A cartoon penguin with a red scarf walks beside the introduction." width="960" />',readme,count=1)
(out/'README.md').write_text(readme,encoding='utf-8')
(root/'README.md').write_text(readme.replace('./assets/profile-banner.gif','./github-ready/assets/profile-banner.gif'),encoding='utf-8')
with zipfile.ZipFile(root/'deniz-mn-github-profile.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in [out/'README.md',out/'assets/profile-banner.gif']:
        z.write(p,p.relative_to(out))
gif=Image.open(out/'assets/profile-banner.gif')
assert gif.n_frames==8 and gif.info['loop']==0
frames[0].save(out/'preview-check.png')
print('ZIP ready; GIF verified: 8 frames, 1.2 second loop.',(out/'assets/profile-banner.gif').stat().st_size)
