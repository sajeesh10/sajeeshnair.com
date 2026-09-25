import random, math
W,H=1200,300
def dots():
    return '<rect width="1200" height="300" class="b-bg"/>'
# A: converge
def converge():
    random.seed(7); out=[dots()]
    n=13; cx=820; cy=150
    for i in range(n):
        y0=30+i*(240/(n-1))+random.uniform(-6,6)
        pts=[]
        for x in range(40,cx+1,10):
            t=(x-40)/(cx-40); e=t*t*(3-2*t)
            amp=(1-e)*14
            y=y0+(cy-y0)*e+math.sin(x/37+i*1.7)*amp*random.uniform(.4,1)
            pts.append(f"{x},{y:.1f}")
        out.append(f'<polyline points="{" ".join(pts)}" class="b-line" fill="none" stroke-width="1.3"/>')
        out.append(f'<circle cx="40" cy="{y0:.1f}" r="3" class="b-node"/>')
    out.append(f'<line x1="{cx}" y1="{cy}" x2="1160" y2="{cy}" class="b-red" stroke-width="2.6"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="5" class="b-redf"/>')
    out.append(f'<path d="M1150 142 L1164 150 L1150 158" fill="none" class="b-red" stroke-width="2.6"/>')
    out.append('<text x="40" y="288" class="b-lab">many systems, many people</text>')
    out.append('<text x="1160" y="288" text-anchor="end" class="b-lab">one direction</text>')
    return out
# B: p99 trace
def trace():
    random.seed(3); out=[dots()]
    L,R,T,B=70,1160,40,240
    for v,y in [(800,T),(400,(T+B)/2),(0,B)]:
        out.append(f'<line x1="{L}" y1="{y}" x2="{R}" y2="{y}" class="b-grid"/>')
        out.append(f'<text x="{L-12}" y="{y+4}" text-anchor="end" class="b-lab">{v}</text>')
    fx=640
    pts=[]
    for x in range(L,R+1,6):
        if x<fx:
            base=150+random.uniform(-40,40)
            if random.random()<.09: base=random.uniform(55,95)
        else:
            t=min(1,(x-fx)/90); base=(150*(1-t)+212*t)+random.uniform(-5,5)
        pts.append(f"{x},{base:.1f}")
    pre=[p for p in pts if float(p.split(',')[0])<=fx]; post=[p for p in pts if float(p.split(',')[0])>=fx]
    out.append(f'<polyline points="{" ".join(pre)}" fill="none" class="b-line2" stroke-width="1.4" stroke-linejoin="round"/>')
    out.append(f'<polyline points="{" ".join(post)}" fill="none" class="b-red" stroke-width="2.2" stroke-linejoin="round"/>')
    out.append(f'<line x1="{fx}" y1="{T-12}" x2="{fx}" y2="{B}" class="b-red" stroke-width="1" stroke-dasharray="3 4"/>')
    out.append(f'<text x="{fx+10}" y="{T-2}" class="b-labr">change shipped</text>')
    out.append(f'<text x="{L}" y="282" class="b-lab">p99 latency, ms</text>')
    out.append(f'<text x="{R}" y="282" text-anchor="end" class="b-lab">time →</text>')
    return out
# C: flame graph
def flame():
    random.seed(11); out=[dots()]
    rowh=38; base=262
    rows=[
      [("main",0,1)],
      [("systems",0,.52),("teams",.53,1)],
      [("latency",0,.2),("throughput",.21,.4),("io",.41,.52),("hiring",.53,.68),("trust",.69,.88),("1:1s",.89,1)],
      [("gc",0,.09),("locks",.1,.2),("queues",.21,.33),("cache",.34,.4),("backups",.41,.51),("bar",.53,.62),("feedback",.69,.8),("clarity",.81,.88)],
      [("tlab",0,.05),("contention",.1,.19),("backpressure",.21,.31),("growth",.69,.79)],
      [("p99",.22,.3),("coaching",.69,.78)],
    ]
    hot={"main","teams","trust","feedback","growth","coaching"}
    hot2={"systems","queues","backpressure"}
    L,R=40,1160
    for d,row in enumerate(rows):
        y=base-(d+1)*rowh
        for name,a,b in row:
            x=L+(R-L)*a; w=(R-L)*(b-a)-3
            cls="b-hot" if name in hot else ("b-f"+str(1+(d+len(name))%3))
            out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{rowh-3}" class="{cls}"/>')
            if w>len(name)*11+14:
                tc="b-ftxth" if name in hot else "b-ftxt"
                out.append(f'<text x="{x+8:.1f}" y="{y+24}" class="{tc}">{name}</text>')
    out.append('<text x="40" y="290" class="b-lab">where the time goes</text>')
    return out
def svg(parts,label):
    return f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'+"".join(parts)+'</svg>'
import json
json.dump({"a":svg(converge(),"Many grey lines converging into one red line"),
 "b":svg(trace(),"A noisy latency trace that settles low after a change is shipped"),
 "c":svg(flame(),"A flame graph mixing systems and team work, with the team path in red")},open("banners.json","w"))
