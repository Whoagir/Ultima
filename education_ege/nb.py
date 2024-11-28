def ctb(number,base):
    s=''
    while number>0:
        s=s+str(number%base)
        number=number//base
    return s[::-1]
print(ctb(int(input()),int(input())))