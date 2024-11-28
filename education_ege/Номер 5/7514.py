for n in range(1,13):
    s=bin(n)[2:]
    if n%2==0:
        s=s+'10'
    else:
        s='1'+s+'01'
        r=int(s,2)
    print(r)