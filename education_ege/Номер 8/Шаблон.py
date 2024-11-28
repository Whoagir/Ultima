a=("АВСХ") #ИСПОЛЬЗУЕМЫЕ БУКВЫ
counter=0
for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a: #КОЛ-ВО БУКВ В СЛОВАХ
                    s=(i1+i2+i3+i4+i5)
                    n=s.count('Х')
                    if ((s[4])=='Х' and n==1)or n==0: #УСЛОВИЕ
                        counter+=1
print(counter)