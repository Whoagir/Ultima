from itertools import product
a="0123456789ABCDE"
comb=product(a,repeat=5)
c=0
for i in comb:
    s=''.join(i)
    print(s)
    n=s.count('8')
    t=s.count('A')
    y=s.count('B')
    u=s.count('C')
    i=s.count('D')
    o=s.count('E')
    if (s[0]!="0") and n==1 and ((t+y+u+i+o)>=2):
         c+=1
print(c)
