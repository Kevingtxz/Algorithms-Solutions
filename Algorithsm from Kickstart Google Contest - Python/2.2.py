t = int(input())
for case in range(1, t+1):
    [count, [l, r]] = [0, [int(s) for s in input().split(" ")]]
    for i in range(0, len(str(l))-2, 2):
        while l//10**i%2!=1 or l//10**(i+1)%2!=0:
            l+=10**i
    for i in range(len(str(r))-1, -1, -1):
        while l+2*10**i<=r:
            l, count = l+2*10**i, count+5**i
    print("Case #{}: {}".format(case, count+1))