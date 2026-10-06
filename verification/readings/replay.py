#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Lincker: exact retained token-to-value pairs, with explicit alternatives.
l=E/'Lincker_1672_partial_key_audit';v=js(l/'partial_key_check.json');alpha='abcdefghiklmnopqrstuwxyz';doubles=['CC','DD','EE','FF','GG','HH','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','WW','XX','YY','ZZ','AA','BB'];key=dict(zip(doubles,alpha))
for plain,base in {'a':20,'b':22,'c':24,'d':26,'e':28,'f':21,'g':23,'h':25,'i':27,'k':29,'l':70,'m':72,'n':74,'o':76,'p':78,'q':71,'r':73,'s':75,'t':77,'u':79,'w':120,'x':122,'y':124,'z':126}.items():
 for i in range(5):key[str(base+10*i)]=plain
key.update({'SYL_ST':'st','SYL_TT':'tt','SYL_LL':'ll','SYL_AU':'au','SYL_FF':'ff'});alt={'JJ?':['JJ'],'66_OR_86':['66','86'],'XX_OR_SYL_FF':['XX','SYL_FF']};result={}
for name in ['A','B']:
 out=''.join('{'+ '/'.join(key[y] for y in alt[x])+'}' if x in alt else key.get(x,'['+x+']') for x in v[name]['tokens']);assert out==v[name]['plaintext_without_editorial_wordspaces'];result[name]=out
record('lincker-1672',literal_outputs=result,limit='Known surviving-key reconstruction; existing historical glosses and out-of-range word codes remain separate.')

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
