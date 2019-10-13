# -*- coding: utf-8 -*-
import os
import re
# classify
# def cnt_to_all(t):  # 6: 16\17\18\19
#     x = 4 * t
#     for i in range(13):
#         if num_all[i] >= x and num_all[i] <= x+3:
#             n=i
#             break
#     return n
def check_double(num):
    cnt=0
    double=[]
    temp=[]
    for i in range(13):
        if num[i]==2:
            cnt+=1
            temp.append(i)
            temp.append(i)
            #temp=cnt_to_all(temp)
            double.append(temp)
            temp=[]
    return cnt, double
def find_double(num):##直接从cnt_all找出对子的数值    #未完成
    double=[]
    temp=[]
    for i in range(13):
        for j in range(4):
            t = j*4
            if num[i]>=t and num[i]<=t+3:
                cnt++
        if cnt==2:
            double.append(num[i])
def check_triple(num):
    cnt=0
    triple=[]
    temp=[]
    for i in range(13):
        if num[i]==3:
            cnt+=1
            temp.append(i)
            temp.append(i)
            temp.append(i)
            triple.append(temp)
    return cnt, triple
def check_straight(tnum):
    straight = []
    temp = []
    cnt = 0
    i = 0
    while i < 9:
        if tnum[i] and tnum[i+1] and tnum[i+2] and tnum[i+3] and tnum[i+4]:
            cnt+=1
            for t in range(5):
                tnum[i+t]-=1
                temp.append(i+t)
            straight.append(temp)
            temp=[]
            i+=1
        else:
            i+=1
    return cnt, straight
def check_samecolor(num):
    samecolor=[]
    heit= []
    hongt= []
    meih= []
    fangk= []
    cnt=0
    for i in range(0, 13, 1):
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
    return cnt, samecolor
# def check_tripledouble():
#     cnt=0
#     if check_double() and check_triple():
#         cnt+=1
#     return cnt
def check_bomb(num):
    cnt = 0
    temp=[]
    bomb=[]
    for i in range(13):
        if num[i] == '4':
            cnt += 1
            temp.append(i)
            temp.append(i)
            temp.append(i)
            temp.append(i)
            bomb.append(temp)
    return cnt, bomb

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

    return cntf, cntn


num_cnt = []
num_all = []
color = []
style = []
up = []
mid = []
down = []
result = []

poker = input()
color = classify_clr()
num_cnt, num_all = classify_num()
print(num_cnt)
print(num_all)

cnt, style=check_straight(num_cnt)      #顺子
print("shunzi:")
print(cnt)
print(style)
#if cnt:


cnt, style=check_samecolor(num_all)   #返回同花个数
print("samecolr:")
print(cnt)
print(style)

cnt, style=check_double(num_cnt)    #对子
print("double:")
print(cnt)
print(style)

cnt, style=check_triple(num_cnt)    #三条
print("triple:")
print(cnt)
print(style)

cnt, style=check_bomb(num_cnt)      #炸弹
print("boom:")
print(cnt)
print(style)
