import json, urllib.request, sys, time
dois = """10.1088/1367-2630/15/5/053040
10.1073/pnas.1304884110
10.1088/1367-2630/16/12/123029
10.1103/RevModPhys.75.715
10.1103/RevModPhys.79.555
10.1038/nature08400
10.1088/1367-2630/12/3/033023
10.1103/PhysRevLett.99.240501
10.1103/PhysRevA.75.032304
10.1103/PhysRevA.81.062348
10.1103/PhysRevLett.104.080402
10.1007/BFb0080769
10.1007/3-540-62688-3_37
10.1080/00927877608822127
10.1038/ncomms2821
10.1007/s10701-011-9616-6
10.1103/PhysRevLett.108.130401
10.1088/1367-2630/13/6/063001
10.1086/289852
10.1103/PhysRevA.84.012311""".split()
out=[]
for d in dois:
    try:
        r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.crossref.org/works/"+d,headers={"User-Agent":"gtao-doi-check (mailto:none)"}),timeout=30))["message"]
        a=", ".join((x.get("family","")) for x in r.get("author",[])[:4])
        y=(r.get("issued",{}).get("date-parts",[[None]])[0][0])
        out.append(f"OK  {d} | {y} | {a} | {r.get('title',[''])[0]} | {r.get('container-title',[''])[0]} {r.get('volume','')}:{r.get('page',r.get('article-number',''))}")
    except Exception as e:
        out.append(f"ERR {d} {e}")
    time.sleep(0.3)
r=json.load(urllib.request.urlopen("https://api.datacite.org/dois/10.48550/arXiv.quant-ph/0101012",timeout=30))["data"]["attributes"]
out.append(f"DATACITE 10.48550/arXiv.quant-ph/0101012 | {r['publicationYear']} | {r['creators'][0]['name']} | {r['titles'][0]['title']}")
print("\n".join(out))
