from itertools import product
a="АИМНР"
comb=product(a,repeat=8) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
for i in comb:
    s=''.join(i)
    n=s.count('МАРИАННА')
    c+=1
    if n>=1: #УСЛОВИЕ
        break
print(c)
