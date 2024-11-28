# (№ 3472) (Е. Джобс) Логическая функция F задаётся выражением ¬(x ≡ y → z).
print('x y z  f')
a=[True,False]
for x in a:
    for y in a:
        for z in a:
            f=not(x==(y<=z))
            print(int(x),int(y),int(z),int(f))