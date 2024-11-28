print("x y z w")
a = [True, False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f = ((y<=x) and (not (z)) and w)
                if f == 1:
                    print(int(x), int(y), int(z), int(w))