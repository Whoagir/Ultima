from itertools import product
a="012345678"
comb=product(a,repeat=5) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
for i in comb:
    s=''.join(i)
    n=s.count('0')
    if n==1 and s[0]!="0" and not "01" in s and not "03" in s and not "05" in s and not "07" in s and not "10" in s and not "30" in s and not "50" in s and not "70" in s:
         c+=1
print(c)