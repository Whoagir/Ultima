from itertools import product
a="01234567"
comb=product(a,repeat=6) #КОЛ-ВО БУКВ В СЛОВЕ
c=0
for i in comb:
    s=''.join(i)
    n=s.count('4')
    if (n==2 and s[0]!="0"):
        if not ("44" in s):
            if s.count('0')<=1 and s.count('1')<=1 and s.count('2')<=1 and s.count('3')<=1 and s.count('5')<=1 and s.count('6')<=1 and s.count('7')<=1:
                s1=s[s.find('4')+1:s.rfind('4')]
                if (not('0' in s1)) and (not('1' in s1)) and (not('2' in s1)) and (not('3' in s1)):
                    c+=1
print(c)