def f(n):
    return "lucky" if n % 7 == 0 else "unlcky"


h = int(input())
if h % 7 == 0:
    print("lucky")
else:
    print("unlucky")
