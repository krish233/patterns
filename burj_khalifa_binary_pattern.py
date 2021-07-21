n=int(input())
for i in range(n+1):
    print(' '*(len(bin(n) [2:])-len(bin(i) [2:]))+bin(i) [2:])
