print("x y z w")
a = [True, False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f = (x<=(z==w)) or not(y<=w)
                if f == 0:
                    print(int(x), int(y), int(z), int(w))