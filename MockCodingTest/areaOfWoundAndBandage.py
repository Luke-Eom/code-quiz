# size of wound n(1<= n <= 4,000)
# wounded = 1 not wounded = 0
# ex.
#  0 1 0 1 1
#  1 1 0 1 1
#  0 1 0 0 1

# get the size of bandage needed

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

l, r, u, d = n, 0, n, 0

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            l = min(l, j)
            u = min(u, i)
            r = max(r, j)
            d = max(d, i)


print((r - l + 1) * (d - u + 1))
