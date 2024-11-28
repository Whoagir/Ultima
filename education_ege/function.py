def ctb(number,base):
    s=''
    while number>0:
        s=s+str(number%base)
        number=number//base
    return s[::-1]
m=0
x1=70000
for x in range(70000,60000,-1):
    j = 5 ** 2025 + 5 ** 400 - x
    g=ctb(j,5)
    m1=g.count('4')
    if m1>m:
        m=m1
        x1=x
print(x1)