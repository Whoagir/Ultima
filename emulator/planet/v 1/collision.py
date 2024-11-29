class Collision():
    def __init__(self):
        ...

    def strength(self):
        dx = balls[j].real_x - balls[i].real_x
        dy = balls[j].real_y - balls[i].real_y
        d = (dx ** 2 + dy ** 2) ** 0.5
        if d == 0:
            continue
        ff = G * balls[i].m * balls[j].m / d ** 2

        balls[i].f[0] += dx * ff / d
        balls[i].f[1] += dy * ff / d

        balls[j].f[0] -= dx * ff / d
        balls[j].f[1] -= dy * ff / d

        if balls[i].real_r > d - balls[j].real_r:
            collisions.append((i, j))

    def interaction(self):
        t1 = balls[i[0]]
        t2 = balls[i[1]]
        if t1.status and t2.status:
            t1.status = False
            t2.status = False
            if t1.real_r > t2.real_r:
                c = t1.colour
            else:
                c = t2.colour

            t = Ball((t1.real_x * t1.m + t2.real_x * t2.m) / (t1.m + t2.m),
                     (t1.real_y * t1.m + t2.real_y * t2.m) / (t1.m + t2.m),
                     (t1.real_r ** 3 + t2.real_r ** 3) ** (1 / 3),
                     t1.m + t2.m,
                     c)
            t.speed[0] = (t1.m * t1.speed[0] + t2.m * t2.speed[0]) / (t1.m + t2.m)
            t.speed[1] = (t1.m * t1.speed[1] + t2.m * t2.speed[1]) / (t1.m + t2.m)
            balls.append(t)