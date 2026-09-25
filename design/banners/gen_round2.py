import random, json
W=1000
def T(x,y,s,cls,anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'

# ---------- C2: flame graph ----------
def N(name,w,*kids,hot=False): return dict(name=name,w=w,kids=list(kids),hot=hot)
tree=N("main",100,
  N("systems",43,
    N("performance",20,
      N("latency",10,N("gc",4,N("young_gen",2)),N("locks",3,N("contention",2)),N("syscalls",2)),
      N("throughput",8,N("queues",5,N("backpressure",3)),N("batching",2)),
      N("profiling",3)),
    N("storage",12,N("backups",8,N("dedupe",4,N("chunking",2)),N("snapshots",3)),N("io",4)),
    N("cloud",10,N("vpc",4),N("autoscale",5,N("capacity",3)))),
  N("teams",56,
    N("hiring",9,N("interviews",6,N("bar_raiser",3)),N("onboard",2)),
    N("trust",28,
      N("feedback",20,N("one_on_ones",17,N("coaching",14,N("growth",10,N("promotion",4),hot=True),hot=True),hot=True),N("candor",3)),
      N("delegation",8,N("ownership",5,N("autonomy",3))),hot=True),
    N("planning",11,N("pessimism",6,N("risks",4)),N("first_principles",4)),
    N("learning",6,N("reading",4,N("notes",2)))),hot=True)
tree["kids"][1]["kids"][1]["kids"][0]["hot"]=True
FW=2800
def flame():
    random.seed(5)
    L,R=0,FW; rowh=27; base=292
    out=[]
    # chrome of flamegraph.svg, kept inside the part a desktop screen shows
    out.append(T(520,26,"Reset Zoom","fg-ui"))
    out.append(T(FW-520,26,"Search","fg-ui","end"))
    def lay(n,x0,x1,d,side):
        y=base-(d+1)*rowh
        w=x1-x0-1.5
        if d==1: side=n["name"]
        if n["hot"]: cls="fg-hot"
        elif side=="teams": cls="fg-r%d"%random.randint(1,3)
        elif side=="systems": cls="fg-g%d"%random.randint(1,3)
        else: cls="fg-g3"
        out.append(f'<rect x="{x0:.1f}" y="{y}" width="{w:.1f}" height="{rowh-1.5}" rx="1" class="{cls}"/>')
        label=n["name"]; cw=9
        if w>len(label)*cw+10:
            out.append(T(x0+5,y+18,label,"fg-txth" if n["hot"] else "fg-txt"))
        elif w>5*cw:
            k=int((w-10)/cw)-2
            if k>=2: out.append(T(x0+5,y+18,label[:k]+"..","fg-txth" if n["hot"] else "fg-txt"))
        tot=sum(k["w"] for k in n["kids"]); span=x1-x0
        cx=x0
        for k in n["kids"]:
            kw=span*k["w"]/n["w"]
            lay(k,cx,cx+kw,d+1,side); cx+=kw
        # jagged leaf towers
        if not n["kids"] and span>30:
            cx=x0
            for i in range(random.randint(1,2)):
                kw=span*random.uniform(.3,.6)
                if cx+kw>x1: break
                yy=y-rowh
                c="fg-hot" if n["hot"] else cls.replace("hot","r1")
                out.append(f'<rect x="{cx:.1f}" y="{yy}" width="{kw-1.5:.1f}" height="{rowh-1.5}" rx="1" class="{c}" opacity=".75"/>')
                cx+=kw+random.uniform(2,10)
    lay(tree,L,R,-1+0,None) if False else None
    # draw root at d=0
    def root():
        lay(tree,L,R,0,None)
    root()
    out.append(T(520,314,"Function: coaching (14,020 samples, 14.00%)","fg-ui"))
    return out,320

# ---------- D: distributed trace ----------
def trace():
    out=[]; L=250; R=940; x=lambda ms:L+(R-L)*ms/1000
    for t in (0,250,500,750,1000):
        out.append(f'<line x1="{x(t):.1f}" y1="30" x2="{x(t):.1f}" y2="286" class="tr-grid"/>')
        out.append(T(x(t),22,f"{t}ms","tr-ax","middle"))
    rows=[("team","deliver-v2",0,1000,0,True),
          ("people","hire",0,190,1,False),
          ("people","onboard",170,330,1,False),
          ("systems","design-review",310,470,1,True),
          ("systems","build",450,760,1,True),
          ("systems","measure-p99",600,720,2,False),
          ("systems","ship",750,860,1,True),
          ("people","retro",860,975,1,True)]
    y=40
    for svc,op,a,b,ind,crit in rows:
        out.append(T(16+ind*16,y+16,svc,"tr-svc"))
        out.append(T(16+ind*16+len(svc)*9.6+10,y+16,op,"tr-op"))
        cls="tr-crit" if crit else "tr-span"
        out.append(f'<rect x="{x(a):.1f}" y="{y+3}" width="{x(b)-x(a):.1f}" height="18" rx="2" class="{cls}"/>')
        lab=f"{b-a}ms"
        if a==0 and b==1000: pass
        elif b<880: out.append(T(x(b)+8,y+16.5,lab,"tr-dur"))
        else: out.append(T(x(a)-8,y+16.5,lab,"tr-dur","end"))
        y+=31
    return out,290

# ---------- E: top ----------
def top():
    out=[]
    out.append(T(16,26,"top - 09:41:07 up 16 yrs,  2 teams,  load average: 0.72, 0.64, 0.58","tp-dim"))
    out.append(T(16,50,"Tasks: 14 total,   3 running,  11 sleeping    %Cpu(s): 64.0 people,  36.0 systems","tp-dim"))
    cols=[(16,"PID"),(90,"USER"),(200,"%CPU"),(300,""),(560,"TIME+"),(680,"COMMAND")]
    out.append(f'<rect x="8" y="64" width="984" height="26" class="tp-head"/>')
    for cx,h in cols: out.append(T(cx,82,h,"tp-h"))
    rows=[(1204,"coaching",38.2,"1204:17"),(311,"design-review",21.5,"611:02"),(96,"perf-tuning",14.8,"2980:44"),
          (412,"hiring",11.1,"388:10"),(88,"one-on-ones",8.9,"1720:05"),(27,"backups-dedupe",3.4,"904:31")]
    y=112
    for i,(pid,cmd,cpu,tm) in enumerate(rows):
        hot=i==0
        if hot: out.append(f'<rect x="8" y="{y-18}" width="984" height="26" class="tp-sel"/>')
        c="tp-hot" if hot else "tp-row"
        out.append(T(16,y,pid,c)); out.append(T(90,y,"sajeesh",c)); out.append(T(200,y,f"{cpu:.1f}",c))
        out.append(f'<rect x="300" y="{y-11}" width="230" height="10" class="tp-track"/>')
        out.append(f'<rect x="300" y="{y-11}" width="{230*cpu/40:.1f}" height="10" class="{"tp-barh" if hot else "tp-bar"}"/>')
        out.append(T(560,y,tm,c)); out.append(T(680,y,cmd,"tp-cmdh" if hot else "tp-cmd"))
        y+=30
    return out,290

# ---------- F: git graph ----------
def git():
    out=[]; ym=150; yu=75; yd=225
    xs=lambda i:90+i*53
    # lanes
    out.append(f'<path d="M{xs(0)} {ym} H{xs(16)}" class="gt-main" fill="none"/>')
    def branch(a,b,y,cls):
        out.append(f'<path d="M{xs(a)} {ym} C{xs(a)+30} {ym} {xs(a)+10} {y} {xs(a)+40} {y} H{xs(b)-40} C{xs(b)-10} {y} {xs(b)-30} {ym} {xs(b)} {ym}" class="{cls}" fill="none"/>')
    branch(1,6,yu,"gt-sys"); branch(4,10,yd,"gt-ppl"); branch(8,14,yu,"gt-sys"); branch(11,15,yd,"gt-ppl")
    commits=[(i,ym,"m") for i in range(17)]
    commits+=[(i,yu,"s") for i in (2,3,4,5)]+[(i,yd,"p") for i in (5,6,7,8,9)]+[(i,yu,"s") for i in (9,10,11,12,13)]+[(i,yd,"p") for i in (12,13,14)]
    for i,y,k in commits:
        cls={"m":"gt-dm","s":"gt-ds","p":"gt-dp"}[k]
        out.append(f'<circle cx="{xs(i)}" cy="{y}" r="{6 if k=="m" else 5}" class="{cls}"/>')
    labs=[(3,yu-16,"profile gc pauses","gt-l"),(5,yd+26,"first hire","gt-l"),(8,yd+26,"1:1s every week","gt-l"),
          (11,yu-16,"p99 -40%","gt-l"),(13,yd+26,"grow a lead","gt-l")]
    for i,y,s,c in labs: out.append(T(xs(i),y,s,c,"middle"))
    out.append(T(24,ym-14,"main","gt-bm"))
    out.append(T(24,yu+5,"systems","gt-b")); out.append(T(24,yd+5,"people","gt-b"))
    out.append(f'<rect x="{xs(16)-40}" y="{ym+14}" width="80" height="24" rx="3" class="gt-tag"/>')
    out.append(T(xs(16),ym+31,"v16.0","gt-tagt","middle"))
    return out,300

res={}
for k,(fn,label) in {"c2":(flame,"A flame graph of systems and team work, with the path through trust, feedback and coaching in red"),
 "d":(trace,"A distributed trace where people and systems spans make up one request"),
 "e":(top,"A top screen whose busiest process is coaching"),
 "f":(git,"A git graph where systems and people branches merge back into main")}.items():
    parts,h=fn()
    vw=FW if k=="c2" else W
    par=' preserveAspectRatio="xMidYMax slice"' if k=="c2" else ""
    res[k]=f'<svg viewBox="0 0 {vw} {h}"{par} role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg">'+"".join(parts)+'</svg>'
json.dump(res,open("banners2.json","w"))

# ---------- C3: the same flame graph in HTML, so it can stretch to any width ----------
def flame_html():
    random.seed(5)
    fr=[]
    def f(x0,x1,d,cls,label="",op=False):
        st=f'left:{x0:.2f}%;width:{max(x1-x0-.12,.05):.2f}%;--d:{d}'
        fr.append(f'<span class="f {cls}{" fade" if op else ""}" style="{st}">{label}</span>')
    def lay(n,x0,x1,d,side):
        if d==1: side=n["name"]
        if d==0: cls="fg-root"
        elif n["hot"]: cls="fg-hot"
        elif side=="teams": cls="fg-r%d"%random.randint(1,3)
        elif side=="systems": cls="fg-g%d"%random.randint(1,3)
        else: cls="fg-g3"
        f(x0,x1,d,cls,n["name"] if x1-x0>=3.5 else "")
        span=x1-x0; cx=x0
        for k in n["kids"]:
            kw=span*k["w"]/n["w"]; lay(k,cx,cx+kw,d+1,side); cx+=kw
        if not n["kids"] and span>1:
            cx=x0
            for i in range(random.randint(1,2)):
                kw=span*random.uniform(.3,.6)
                if cx+kw>x1: break
                f(cx,cx+kw,d+1,"fg-hot" if n["hot"] else cls,"",True); cx+=kw+random.uniform(.2,.8)
    lay(tree,0,100,0,None)
    return ('<div class="fg" role="img" aria-label="A flame graph of systems and team work, with the path through trust, feedback and coaching in red">'
            '<div class="fg-bar"><span>Reset Zoom</span><span>Search</span></div>'
            '<div class="fg-stack">'+"".join(fr)+'</div>'
            '<div class="fg-bar"><span>Function: coaching (14,020 samples, 14.00%)</span></div></div>')
open("banner.html","w").write(flame_html()+"\n")
