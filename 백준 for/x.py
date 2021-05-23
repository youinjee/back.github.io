n, x = map(int, input().split())
a = list(map(int, input().split()))
for t in a:
    if t < x:
        print(t)