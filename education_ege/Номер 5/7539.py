a=[]
for n in range(1,1000):
    s=bin(n)[2:]
    b=s.count("1")
    s=s+str(b%2)
    b1=s.count('1')
    s=s+str(b1%2)
    r=int(s,2)
    if r>75:
        print (r)