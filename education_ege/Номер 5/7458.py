for n in range(1000,1,-1):
    s=bin(n)[2:]
    b=s.count('1')
    if b%2==0:
        #print (s)
        s='10'+s[2:]+'0'
        #print(s)
    else:
        s='11'+s[2:]+'1'
    r=int(s,2)
    if r<35:
        print(n)