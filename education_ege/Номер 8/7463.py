from itertools import product
a="01234567"
comb=product(a,repeat=5) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
for i in comb:
    s=''.join(i)
    n=s.count('7')
    if n<=2 and  s[0]!="1" and  s[0]!="3" and  s[0]!="5" and  s[0]!="7" and s[4]!="6" and s[4]!="2" and s[0]!="0":
         c+=1
print(c)