from itertools import product
a="КОСУФ"
comb=product(a,repeat=5) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
v=0
for i in comb:
    s=''.join(i)
    c+=1
    n=s.count('Ф')
    m=s.count('У')
    print(c)
    if n==0 and m==2:
        v=c
print(v)
