import json,sys,urllib.request,urllib.parse,random
def match(points, cond, radius_m=150, table='postpass_pointpolygon', sample=None, chunk=150):
    pts=list(points)
    if sample and len(pts)>sample:
        random.seed(1); pts=random.sample(pts,sample)
    hits=0; res={}
    for i in range(0,len(pts),chunk):
        ch=pts[i:i+chunk]
        vals=",".join(f"('{str(p[0]).replace(chr(39),'')}',{float(p[1])},{float(p[2])})" for p in ch)
        d=radius_m/111000.0
        sql=f"""SELECT v.id, (SELECT count(*) FROM {table} t WHERE t.geom && ST_Expand(ST_SetSRID(ST_MakePoint(v.lon,v.lat),4326),{d*1.6}) AND ST_DWithin(t.geom::geography, ST_SetSRID(ST_MakePoint(v.lon,v.lat),4326)::geography,{radius_m}) AND ({cond})) AS n FROM (VALUES {vals}) AS v(id,lon,lat)"""
        data=urllib.parse.urlencode({'data':sql,'options[geojson]':'false'}).encode()
        r=json.load(urllib.request.urlopen('https://postpass.geofabrik.de/api/interpreter',data,timeout=300))
        for row in r['result']:
            res[row['id']]=row['n']
    hits=sum(1 for v in res.values() if v>0)
    return hits,len(res),res
if __name__=='__main__':
    pass
