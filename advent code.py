


"""advent code day 2"""

s=open("advent2.txt").read().split('\n')

print("2.2 answer is:")

tab=[]
for nr1 in range(249):
    for nr2 in range(nr1,249):
        for i in range(len(s[0])):
            if s[nr1][i]!=s[nr2][i]:
                tab.append(s[nr1][i])
        if len(tab)==1:
            print(nr1," ",s[nr1])
            print(nr2," ",s[nr2])
        tab=[]
        


"""+++++++++++++++++++"""
"""advent code day 3"""
print("++++++++++")

s=open("advent3.txt").read().split('\n')


for j in range(len(s)):
    s[j]=s[j].strip("#")
    s[j]=s[j].replace(" @ ",",").replace(": ",",").replace("x",",").split(",")


tabx=[[0 for x in range(1000)]for y in range(1000)]

for ii in range(len(s)-1):
    for x1 in range(int(s[ii][3])):
        for y1 in range(int(s[ii][4])):
            if tabx[int(s[ii][1])+x1][int(s[ii][2])+y1]==0:
                tabx[int(s[ii][1])+x1][int(s[ii][2])+y1]=1
            else: tabx[int(s[ii][1])+x1][int(s[ii][2])+y1]=2
                                             
count=0;
for xx in range(1000):
    for yy in range(1000):
        if tabx[xx][yy]==2:
            count=count+1
print("3.1 answer is:", count)


for ii in range(len(s)-1):
    c=0
    for x1 in range(int(s[ii][3])):
        for y1 in range(int(s[ii][4])):
            if tabx[int(s[ii][1])+x1][int(s[ii][2])+y1]==1:
                c=c+1
    if c==int(s[ii][3])*int(s[ii][4]):
        print("3.2 answer is:", s[ii][0])


'''
"""no idea how to do it, yet"""
"""+++++++++++++++++++"""
"""advent code day 4"""

s=open("advent4.txt").read().split('\n')
s.sort()

for j in range(len(s)):
    s[j]=s[j].replace("#"," ")


sn=[]
for i in range(len(s)):
    for g in s[i].split():
        if g=="Guard":
            sn.append(int("".join(filter(str.isdigit, s[i].split()))))
'''



"""+++++++++++++++++++"""
"""advent code day 5"""

import string
s=open("advent5.txt").read()

alpl=string.ascii_lowercase
alpu=string.ascii_uppercase

string=[]
for a in range(len(alpl)):
    string.append(alpl[a]+alpu[a])
    string.append(alpu[a]+alpl[a])
   
for n in range(800):
    for i in string:
        if i in s:
            s=s.replace(i,'')
print("5.1 answer is:",len(s)) 


s=open("advent5.txt").read()

string2=[0]*len(alpl)
for b in range(len(alpl)):
   string2[b]=alpl[b]+alpu[b]


pollen=[]
for num in range(len(string2)):
    s2=s.replace(string2[num][0],'')
    s2=s2.replace(string2[num][1],'')
    for n in range(1300):
        for i in string:
            if i in s2:
                s2=s2.replace(i,'')
    pollen.append(len(s2))

print("5.2 answer is:",min(pollen))        
    
'''
"""WORKING on THAT"""
"""advent code day 6"""

from pylab import plot, show
from math import sqrt

s=open("advent6.txt").read().split('\n')


sx=[]
sy=[]
for i in range(len(s)):
    s1=s[i].split(",")
    sx.append(int(s1[0]))
    sy.append(int(s1[1]))


def dist(px,py,x,y):
    return sqrt((px-x)**2+(py-y)**2)
    

area=[0 for x in range(len(s))]


d1=0

for x in range(min(sx),max(sx)):
    for y in range(min(sy),max(sy)):
        for i in range(len(s)):
            d1=dist(sx[i],sy[i],x,y)
                for j in range(len(s)-1):       
print(area)

for x in range(min(sx),max(sx)):
    for y in range(min(sy),max(sy)):
        if dist(sx[0],sy[0],x,y)>dist(sx[1],sy[1],x,y):
            dis1=dis1+1
        else: dis2=dis2+1

print(dis1,dis2)
'''
