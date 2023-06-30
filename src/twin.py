def y(s, t):
    return "".join(l)


s = int(input())
t = int(input())
l = list("-" * s)
l[t - 1] = "+"
print(y(s, t))
