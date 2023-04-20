#Первое задание
n = int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
x=int(input())
s=0
for i in range(n):
    if a[i]==x:
        s=s+1
print(s)
#Второе задание
n1 = int(input())
a1=[]
for i in range(0,n):
    a1.append(int(input()))
x1=int(input())
s=9999
for i in range(n1):
    if (abs(a1[i]-x1)<s):
        s=abs(a1[i]-x1)
        d=a1[i]
print(d)
#Задание третье
S=input()
f1=['A','E','I','O','U','L','N','S','T','R',"А","В","Е","И","Н","О","Р","С","Т"]
f2=['D','G','Д','К','Л','М','П','У']
f3=['B','C','M','P','Б','Г','Ё','Ь','Я']
f4=['F','H','V','W','Y','Й','Ы']
f5=['K','Ж','З','Х','Ц','Ч']
f6=['J','X','Ш','Э','Ю']
f7=['Q','Z','Ф','Щ','Ъ']
h=0
for i in range(len(S)):
    if S[i] in f1:
        h=h+1
    if S[i] in f2:
        h=h+2
    if S[i] in f3:
        h=h+3
    if S[i] in f4:
        h=h+4
    if S[i] in f5:
        h=h+5
    if S[i] in f6:
        h=h+8
    if S[i] in f7:
        h=h+10
print(h)