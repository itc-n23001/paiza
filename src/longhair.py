def f(r):
    return "yes" if r.count("yes") > r.count("no") else "no"


r = [str(input()) for i in range(5)]
print(f(r))
