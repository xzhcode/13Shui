import re
import json

keys = ["姓名","手机","地址"]
values = []
address=input()
s=str(address)
n=s[0]

def find_name(s):
    res_name=re.findall('!(.*)?,',s)
    values.append(res_name[0])
    
def find_tel(s):
    res_tel=re.findall('\d{11}',s)
    values.append(res_tel[0])

def find_address(s,n):
    addr=[]
    i=1
    if n >= '1':#七级地址
        for i in range(7):
            addr.append("")
    else:#五级地址
        for i in range(5):
            addr.append("")
 #   dizhi.append("dizhi1")
 #  dizhi.append("dizhi2")
 #   values.append(dizhi)
    values.append(addr)
find_name(s)
find_tel(s)
find_address(s,n)

person=dict(zip(keys,values))
res_json=json.dumps(person,ensure_ascii=False,indent=True)
print(res_json)