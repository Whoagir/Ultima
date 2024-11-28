# Логическая функция F задаётся выражением (x ˄ y) ˅ (y ≡ z) ˅ w. На рисунке приведён фрагмент таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
print("x y z w")
a = [True, False]
for x in a:
    for y in a:
        for z in a:
            for w in a:
                f = (x and y) or (y == z) or  w
                if f == 0:
                    print(int(x), int(y), int(z), int(w))
#Ответ zywx