# N = the number of levels in the game
# K = the current level you are in
# S = the level where you have to pick up the sword

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, k, s = [int(s) for s in input().split(" ")]

    if k/2 < s:
        print("Case #{}: {}".format(i, n+(k-s)*2))
    else:
        print("Case #{}: {}".format(i, n+k))
