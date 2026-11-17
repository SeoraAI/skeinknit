import math, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
OUT=os.path.dirname(os.path.abspath(__file__))
INK="#2B1F18"; CHESTNUT="#8A4B2F"; CREAM="#FAF6F0"; CARD="#F3ECE2"
f=lambda v: ("%.2f"%v).rstrip("0").rstrip(".")

# ---- The S mark: two equal rings, centres two radii apart, each cut 230 degrees.
# Ring thickness is 36% of the centreline radius, as in the shipped app icon.
R=100.0; W=18.0; CY=R+W; C1=R+W; C2=C1+2*R
def pt(cx,r,deg): a=math.radians(deg); return (cx+r*math.cos(a), CY+r*math.sin(a))
def mark_path(ox=0, oy=0, s=1.0):
    def P(p): return f"{f(ox+p[0]*s)} {f(oy+p[1]*s)}"
    ro, ri = (R+W)*s, (R-W)*s
    a=pt(C1,R+W,230); b=pt(C1,R+W,0)          # left outer, ccw to the joint
    c=pt(C2,R-W,50)                            # right inner, cw to the end
    d=pt(C2,R+W,50); e=pt(C2,R+W,180)          # right outer, ccw back to the joint
    g=pt(C1,R-W,230)                           # left inner, cw to the start
    return (f"M{P(a)}A{f(ro)} {f(ro)} 0 1 0 {P(b)}"
            f"A{f(ri)} {f(ri)} 0 1 1 {P(c)}L{P(d)}"
            f"A{f(ro)} {f(ro)} 0 1 0 {P(e)}"
            f"A{f(ri)} {f(ri)} 0 1 1 {P(g)}Z")
MARK_W, MARK_H = C2+R+W, 2*(R+W)

# ---- Wordmark: SKEIN in Inter ExtraLight (200), capitals tracked 0.42em,
# as on skeinknit.com and in the app's navigation titles. Outlined, so it
# needs no font to display.
font=TTFont("/usr/share/fonts/opentype/inter/Inter-ExtraLight.otf")
gs=font.getGlyphSet(); cmap=font.getBestCmap(); upm=font["head"].unitsPerEm
cap=font["OS/2"].sCapHeight
def wordmark(cap_px, ox=0, oy=0, track=0.42):
    s=cap_px/cap; x=0.0; d=[]; adv_total=0
    for i,ch in enumerate("SKEIN"):
        gn=cmap[ord(ch)]; pen=SVGPathPen(gs)
        tp=TransformPen(pen,(s,0,0,-s,ox+x,oy+cap_px))
        gs[gn].draw(tp); d.append(pen.getCommands())
        x+=gs[gn].width*s
        if i<4: x+=track*upm*s
    # drop the side bearing of the S so the word starts flush
    bp=BoundsPen(gs); gs[cmap[ord("S")]].draw(bp); lsb=bp.bounds[0]*s
    bp=BoundsPen(gs); gs[cmap[ord("N")]].draw(bp); rsb=(gs[cmap[ord("N")]].width-bp.bounds[2])*s
    return " ".join(d), x-lsb-rsb, lsb

def svg(w,h,body,bg=None,title="Skein"):
    rect=f'<rect width="{f(w)}" height="{f(h)}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" width="{f(w)}" height="{f(h)}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{rect}{body}</svg>\n')

files={}
def put(name,content): files[name]=content; open(os.path.join(OUT,name),"w").write(content)

for cname,col in (("ink",INK),("chestnut",CHESTNUT),("cream",CREAM)):
    # mark alone
    put(f"skein-mark-{cname}.svg", svg(MARK_W,MARK_H,f'<path fill="{col}" d="{mark_path()}"/>',title="Skein mark"))
    # wordmark alone, cap height 100
    capw=100; d,ww,lsb=wordmark(capw, ox=0)
    d,ww,lsb=wordmark(capw, ox=-lsb)
    put(f"skein-wordmark-{cname}.svg", svg(ww,capw,f'<path fill="{col}" d="{d}"/>',title="Skein"))
    # horizontal lockup: mark height 236; cap height 40% of it; gap 34% of it
    capw=MARK_H*0.40; gap=MARK_H*0.34
    _,ww,lsb=wordmark(capw)
    d,_,_=wordmark(capw, ox=MARK_W+gap-lsb, oy=(MARK_H-capw)/2)
    put(f"skein-lockup-horizontal-{cname}.svg", svg(MARK_W+gap+ww,MARK_H,
        f'<path fill="{col}" d="{mark_path()}"/><path fill="{col}" d="{d}"/>'))
    # stacked lockup: wordmark as wide as the mark
    _,w1,_=wordmark(100); capw=100*MARK_W/w1*0.78
    _,ww,lsb=wordmark(capw); gap=MARK_H*0.42; tot_w=max(MARK_W,ww)
    d,_,_=wordmark(capw, ox=(tot_w-ww)/2-lsb, oy=MARK_H+gap)
    put(f"skein-lockup-stacked-{cname}.svg", svg(tot_w,MARK_H+gap+capw,
        f'<path fill="{col}" d="{mark_path(ox=(tot_w-MARK_W)/2)}"/><path fill="{col}" d="{d}"/>'))

# app icon / avatar: mark on card cream, 1024 square, mark 72% of the width
S=1024; s=S*0.72/MARK_W
put("skein-app-icon.svg", svg(S,S,f'<path fill="{INK}" d="{mark_path(ox=(S-MARK_W*s)/2, oy=(S-MARK_H*s)/2, s=s)}"/>',bg=CARD,title="Skein app icon"))
# Instagram avatar: circle-safe, mark 60%
s=S*0.60/MARK_W
put("skein-avatar.svg", svg(S,S,f'<path fill="{CREAM}" d="{mark_path(ox=(S-MARK_W*s)/2, oy=(S-MARK_H*s)/2, s=s)}"/>',bg=CHESTNUT,title="Skein avatar"))
print(sorted(files))
