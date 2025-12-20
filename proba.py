def f(x):
    if x == 20:
        return 99
    return min(99, max(20, 16+4*x))

for i in range(1, 21):
    print(i, 16+round(83/20*i))
