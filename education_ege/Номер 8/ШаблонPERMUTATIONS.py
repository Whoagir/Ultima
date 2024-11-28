from itertools import permutations
a="МАНГУСТ" #ИСПОЛЬЗУЕМЫЕ БУКВЫ
comb=permutations(a)
c=0
for i in comb:
    s=''.join(i)
    for i in s:
        n=s.count('У')
        m=s.count('М')
        if (s[0])!='А' and n>=1 and m==2: #УСЛОВИЕ
            c+=1
print(c)