# -*- coding: utf-8 -*-
import os
import time
import re
import json
import http.client

def check_straight(num):
    tnum = []
    straight = []
    temp = []
    cnt = 0
    i = 0
    while i < len(num):
        tnum.append(num[i])
        i+=1
    i=12
    while i >= 0 :
        if tnum[i] and tnum[i-1] and tnum[i-2] and tnum[i-3] and tnum[i-4]:
            cnt+=1
            for t in range(5):
                tnum[i-t]-=1
                temp.append(i-t)
            straight.append(temp)
            temp=[]
            i-=1
        else:
            i-=1
    return straight
def check_samecolor(num):   #using num_all
    samecolor=[]
    heit= []
    hongt= []
    meih= []
    fangk= []
    cnt=0
    for i in range(0, len(num), 1):
        if num[i] % 4 == 0:
            heit.append(num[i])
        elif num[i] % 4 == 1:
            hongt.append(num[i])
        elif num[i] % 4 == 2:
            meih.append(num[i])
        else:
            fangk.append(num[i])
    if len(heit) > 4:
        samecolor.append(heit)
        cnt+= 1
    if len(hongt) > 4:
        samecolor.append(hongt)
        cnt+=1
    if len(meih) > 4:
        samecolor.append(meih)
        cnt+= 1
    if len(fangk) > 4:
        samecolor.append(fangk)
        cnt+=1
    return samecolor
def check_bomb(num):
    temp=[]
    bomb=[]
    for i in range(13):
        if num[i] == '4':
            cnt += 1
            temp.append(i*4)
            temp.append(i*4+1)
            temp.append(i*4+2)
            temp.append(i*4+3)
            bomb.append(temp)
    return bomb
def classify_clr(): #根据花色不同分成四组
    i = 0
    key = ['heitao', 'hongtao', 'meihua', 'fangkuai']
    value = []
    heitao = []
    hongtao = []
    meihua = []
    fangkuai = []
    while i < 26:
        if poker[i] == '$':
            heitao.append(poker[i+1])
            i = i+1
        elif poker[i] == '&':
            hongtao.append(poker[i+1])
            i = i+1
        elif poker[i] == '*':
            meihua.append(poker[i+1])
            i = i+1
        elif poker[i] == '#':
            fangkuai.append(poker[i+1])
            i = i+1
        else:
            i=i+1

    value.append(heitao)
    value.append(hongtao)
    value.append(meihua)
    value.append(fangkuai)
    classify_flw=dict(zip(key,value))
    return classify_flw
def classify_num():#数字数组
    st=[]
    cntf=[]
    cntn=[]
    i=0
    for k in range(13):
        cntf.append(0)
    for j in range(0,52,1):
        st.append(0)
    for t in poker:
        if t=='$' or t=='&' or t=='*' or t=='#':    #0-51: heitao 2,hongtao2,meihua2,fangkuai2,3..51
            if t=='$':
                i=0
            elif t=='&':
                i=1
            elif t=='*':
                i=2
            else:
                i=3
        else:
            if t=='2':
                st[0*4 + i] += 1
                cntf[0]+=1
            elif t=='3':
                st[1*4 + i] += 1
                cntf[1] += 1
            elif t=='4':
                st[2*4 + i] += 1
                cntf[2] += 1
            elif t=='5':
                st[3*4 + i] += 1
                cntf[3] += 1
            elif t=='6':
                st[4*4 + i] += 1
                cntf[4] += 1
            elif t=='7':
                st[5*4 + i] += 1
                cntf[5] += 1
            elif t =='8':
                st[6*4 + i] += 1
                cntf[6] += 1
            elif t=='9':
                st[7*4 + i] += 1
                cntf[7] += 1
            elif t=='1':
                st[8*4 + i] += 1
                cntf[8] += 1
            elif t=='J':
                st[4*9 + i] += 1
                cntf[9] += 1
            elif t=='Q':
                st[10*4 + i] += 1
                cntf[10] += 1
            elif t=='K':
                st[11*4 + i] += 1
                cntf[11] += 1
            elif t=='A':
                st[12*4 + i] += 1
                cntf[12] += 1
            else:
                t=t
    for i in range(52):
        if st[i] >0 :
            cntn.append(i)
    return cntf, st, cntn
def find_same_straight(tnum):     #同花里找顺子
    straight = []
    temp = []
    cnt = 0
    for num in tnum:
        lens = len(num)-1
        i=lens
        while i > 1 :
            if num[i] == (num[i-1]+4):
                cnt+=1
            else:
                cnt=0
            if cnt == 4:
                for t in range(5):
                    temp.append(num[i]+4*t -4)
                straight.append(temp)
                temp = []
                i-=1
                cnt=0
            i-=1
    return straight
def check_all():
    allStyle=[]
    danzhang = []
    for i in range(13):
        if num_cnt[i] == 1:
            for j in range(4):
                if num_all[i * 4 + j]:
                    danzhang.append(i*4 + j)
                    break
    allStyle.append(danzhang)

    print("单张：",danzhang)


    duizi = []
    temp = []
    i=0
    while i<13:
        if num_cnt[i] == 2:  # 这个数字有两张
     #       print(" 两张：",i)
            for j in range(4):
                if num_all[i*4 + j]:
                    temp.append(i*4 +j)
        if len(temp)==2:
            duizi.append(temp)
            temp=[]
        i+=1
    allStyle.append(duizi)

    print("对子：", duizi)

    temp = []
    santiao = []
    for i in range(13):
        if num_cnt[i] == 3:
            for j in range(4):
                if num_all[i*4 + j]:
                    temp.append(i * 4 + j)
        if len(temp) == 3:
            santiao.append(temp)
            temp =[]
    allStyle.append(santiao)
    print("三条：", santiao)


    straight = check_straight(num_cnt)  # using num_cnt  返回的只是牌 没有花色
    allStyle.append(straight)
    print(" 顺子：", straight)

    samecolor = check_samecolor(num_rcd)
    allStyle.append(samecolor)
    print("同花", samecolor)

    hulu=[]
    temp=[]
    temp2=[]
    if len(santiao) and len(duizi):
        temp.append(santiao[-1] + duizi[0])
        hulu.append(temp[0])
        # if len(santiao) ==1 and len(duizi) ==1:
        #     temp.append(santiao[0]+duizi[0])
        #     hulu.append(temp[0])
        # elif len(santiao) >= 2 and len(duizi) >=2:
        #     temp.append(santiao[-1]+duizi[0])
        #     temp2.append(santiao[-2]+duizi[-1])
        #     hulu.append(temp[0])
        #     hulu.append(temp2[0])
        #     print('000000',temp[0])
        #     print('111111111111',temp2[0])
        # elif len(santiao) ==1 and len(duizi) >= 2:
        #     temp.append(santiao[0]+duizi[0])
        #     hulu.append(temp[0])
        # else:
        #     temp.append(santiao[0]+duizi[0])
        #     hulu.append(temp[0])
    allStyle.append(hulu)       ##  bug:葫芦： [[[0, 2, 3], 9, 10]] ### += append 用法

    print("葫芦：",hulu)

    bomb = check_bomb(num_all)
    allStyle.append(bomb)
    print("炸弹：", bomb)

    samestraight = []
    if len(samecolor):
        samestraight = find_same_straight(samecolor)
    allStyle.append(samestraight)
    print("同花顺", samestraight)

    return allStyle
def trans(num):
    temp=[]
    t=0
    for i in num:
        if i%4 ==0:
            temp+=('$')
        elif i%4 == 1:
            temp+=('&')
        elif i%4 == 2:
            temp+=('*')
        elif i%4==3:
            temp+=('#')

        num = int((i -i%4)/4)
        if num == 0:
            temp.append('2')
        elif num==1:
            temp.append('3')
        elif num==2:
            temp.append('4')
        elif num==3:
            temp.append('5')
        elif num==4:
            temp.append('6')
        elif num==5 :
            temp.append('7')
        elif num==6:
            temp.append('8')
        elif num==7:
            temp.append('9')
        elif num ==8:
            temp.append('10')
        elif num ==9:
            temp.append('J')
        elif num ==10:
            temp.append('Q')
        elif num==11:
            temp.append('K')
        else:
            temp.append('A')

        temp.append(' ')
    return temp

up = []
mid = []
down = []
result = []
allStyle = []
value=[]
key=[]
idnum=0
dict={}

name="xxx1010101"
code="password"

conn = http.client.HTTPSConnection("api.shisanshui.rtxux.xyz")
payload = "{\"username\":\"name\",\"password\":\"code\"}"
headers = { 'content-type': "application/json" }

conn.request("POST", "/auth/register", payload, headers)
res = conn.getresponse()
data = res.read()

#登录
seg={}
conn.request("POST", "/auth/login", payload, headers)
res = conn.getresponse()
data = res.read()
seg = json.loads(data)
status=seg['status']
seg=seg['data']
print('id+tk',seg)
idnum=seg['user_id']
token=seg['token']

print('id=',idnum)
print('token=',token)
#开始打牌
headers = { 'x-auth-token': token }
conn.request("POST", "/game/open", headers=headers)
res = conn.getresponse()
data = res.read()
seg = json.loads(data)
status=seg['status']
seg=seg['data']

gameid=seg['id']
poker =seg['card']
print('poker:',poker)

color = classify_clr()
num_cnt, num_all, num_rcd = classify_num()
# print("init cnt0:",num_cnt)  #记录某张牌的频率
# print("init all0:",num_all) #0-51 bool数组
# print("init rcd0:",num_rcd)  # 0-51 从小到大 记录出现的所有牌 13张

#找底墩
allStyle=check_all()
i=7
while i>=0:
    if len(allStyle[i]):
        if i==6 or i==3 or i==2 or i==1 or i==4:
            if i==6:    #炸弹 加一张牌 不拆顺子和同花的牌
                #print(" 底墩牌型： 炸弹")
                down=(allStyle[i][0])
                for i in num_rcd : #去找单牌
                    if i not in down and i not in allStyle[3][0]:
                        down += i
                        break
                    else:
                        down = down
            elif i==4:  #同花
                #print(" 底墩牌型： 同花")
                down=(allStyle[i][0])
                if len(down) > 5:
                    temp = []
                    temp.append(down[-1])
                    temp.append(down[-2])
                    temp.append(down[-3])
                    temp.append(down[-4])
                    temp.append(down[-5])
                    down = temp
            elif i==3:  #顺子
                #print(" 底墩牌型： 顺子")
                down=allStyle[i][0]
                temp=[]
                for t in down:
                    print(t)
                    for j in range(4):
                        if num_all[t*4+j]:
                            temp.append(t*4+j)
                            break
                down=temp
            elif i==2:# 三条
                #print(" 底墩牌型： 三条")
                down=(allStyle[i][0])
                cnt=0
                for i in num_rcd : #去找单牌
                    if i not in down :
                        down += i
                        cnt+=1
                        break
                    else:
                        down = down
                    if cnt ==2 :
                        break
            elif i==1:# 对子
                if len(allStyle[i]) >= 2:# 两对
                    #print(" 底墩牌型： 两对")
                    temp=allStyle[i][0][:2]
                    temp+=allStyle[i][1][:2]
                    temp += (allStyle[0][0])
                    down = temp
                else:   #一对
                    #print(" 底墩牌型： 一对")
                    down = (allStyle[i][0])
                    down += allStyle[0][0:3]
        elif i==0 :
            #print(" 底墩牌型： 乌龙")
            temp=allStyle[0]
            temp=temp[-5:-1]
            temp += allStyle[0][-1]
            down = (temp)
        else:
            #print(" 底墩牌型： 葫芦 同花顺")
            down=(allStyle[i][0])
        print("底墩:",down)
        print('牌型：',i)
        num_rcd=list(set(num_rcd).difference(set(down))) #更新num_rcd
        #更新num_all
        i=0
        while i<5:
            x = down[i]
            num_all[x] = 0
            i+=1
        #更新num_cnt
        i=0
        while i<5:
            x = int(down[i]/4)
            num_cnt[x]-=1
            i+=1
        break
    i-=1

# print("cnt1:",num_cnt)  #记录某张牌的频率
# print("all1:",num_all) #0-51 bool数组
# print("rcd1:",num_rcd)  # 0-51 从小到大 记录出现的所有牌 13张
#

#找中墩
allStyle=check_all()
i=7
while i >= 0:

    if len(allStyle[i]):
        print("中盾牌型：")
        if i == 6 or i==4 or i == 3 or i == 2 or i == 1:
            if i == 6:  # 炸弹 加一张牌 不拆顺子和同花的牌
                print("炸弹")
                mid = (allStyle[i][0])
                for i in num_rcd : #去找单牌
                    if i not in mid and i not in allStyle[3][0]:
                        mid += i
                        break
                    else:
                        mid = mid
            elif i==4:  #同花
                print("同花")
                mid = (allStyle[i][0])
                if len(mid) > 5:
                    temp = []
                    temp.append(down[-1])
                    temp.append(down[-2])
                    temp.append(down[-3])
                    temp.append(down[-4])
                    temp.append(down[-5])
                    mid = temp
            elif i == 3:  # 顺子
                print("顺子")
                mid = (allStyle[i][0])
                temp=[]
                for t in mid:
                    print(t)
                    for j in range(4):
                        if num_all[t*4+j]:
                            temp.append(t*4+j)
                            break
                mid=temp
            elif i == 2:#三条 加两张
                print("三条")
                mid = (allStyle[i][0])
                cnt=0
                for i in num_rcd : #去找单牌
                    if i not in mid :
                        mid += i
                        cnt+=1
                        break
                    else:
                        mid = mid
                    if cnt ==2 :
                        break
            elif i == 1:#对子
                if len(allStyle[i]) >= 2:# 有两对
                    temp = []
                    print("两对")
                    temp=allStyle[i][0][:2]
                    temp+=allStyle[i][1][:2]
                    mid = temp
                    temp = []
                    for j in num_rcd:
                        if j not in mid:
                            temp.append(j)
                            break
                    mid += temp
                else:   #只有一对
                    temp=[]
                 #   print("一对")
                    mid += allStyle[i][0]
                    mid += allStyle[0][0:3]
                    mid += temp
        elif i == 0:
          #  print("乌龙")
            temp =num_rcd[-5:-1]    ###输出后五位
            temp = num_rcd[-5:-1]
            mid += (temp)
            temp = []
            temp.append(num_rcd[-1])
            mid += temp
        else:
         #   print("葫芦、同花顺")
            mid.append(allStyle[i][0])
        print(mid)
        num_rcd = list(set(num_rcd).difference(set(mid)))  # 更新num_rcd
        # 更新num_all
        i=0
        while i<5 :
            x=mid[i]
            num_all[x] = 0
            i+=1
        # 更新num_cnt
        i=0
      #  print("中墩牌型：",mid)
        while i<5:
            x = int(mid[i]/4)
            num_cnt[x] -= 1
            i+=1
        break
    i -= 1

print("cnt2:",num_cnt)  #记录某张牌的频率
print("all2:",num_all) #0-51 bool数组
print("rcd2:",num_rcd)  # 0-51 从小到大 记录出现的所有牌 13张


#前墩
up=num_rcd

up=trans(up)
mid=trans(mid)
down=trans(down)
up = ''.join(up)
up=up[:-1]
mid = ''.join(mid)
mid= mid[:-1]

down = ''.join(down)
down=down[:-1]
result.append(up)
result.append(mid)
result.append(down)

print("result", result)

key = ['id','card']
value.append(gameid)
value.append(result)
dict=dict(zip(key,value))
jsonarr = json.dumps(dict, ensure_ascii=False,indent=True)
print(jsonarr)

#出牌
payload = jsonarr
print('payload:',payload)
headers = {
    'content-type': "application/json",
    'x-auth-token': token
    }
conn.request("POST", "/game/submit", payload, headers)
res = conn.getresponse()
data = res.read()

print(data)
