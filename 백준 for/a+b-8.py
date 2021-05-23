number=int(input())
for t in range(1, number+1):
    a,b=map(int, input().split())
    print(f'Case #{t}: {a} + {b} = {a+b}')