from itertools import product
a="012345678"
comb=product(a,repeat=6) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
for i in comb:
    s=''.join(i)
    n=s.count('1')
    if n>=2 and  s[0]!="1" and  s[0]!="3" and  s[0]!="5" and  s[0]!="7" and s[5]!="3" and s[5]!="2" and s[0]!="0":
         c+=1
print(c)
