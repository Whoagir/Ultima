def ctb(n,b):
    d='0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯWZ'
    s=''
    while n>0:
        s=d[n%b]+s
        n=n//b
    return s
def e45(n):
    d = '0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯWZ'
    return d.find(n)
mr=int(10**100)
for n in range(1000,100000):
    s=ctb(n,45)
    sm1=sum(e45(i) for i in s[::2])
    sm2=sum(e45(i) for i in s[1::2])
    #print (sm1,sm2,s)
    sm45n=ctb(sm1,45)
    sm45c=ctb(sm2,45)
    s=sm45n+s+sm45c if sm1>sm2 else sm45c+s+sm45n
    #print(s)
    r=0
    s=s[::-1]
    for i in range(len(s)-1,-1,-1):
        r+=e45(s[i])*45**i
        #print (s[i],i)
    #print(r)
    if r<mr:
        mr=r
        print(n,s,r)
print(mr)
