import sys

number=int(sys.stdin.readline())
for t in range(number):
    a,b=map(int, sys.stdin.readline().split())
    print(a+b)