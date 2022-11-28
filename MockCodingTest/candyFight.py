# n candies / t games
# a person can take 1 or 3 candies
# print out winner's won game number or "tie" when it ends in tie
# t(1<= t <= 1,000,000)
# n(1<= n <= 2,000,000,000)

t = int(input())
gr = 0
mo = 0

matrix = list(map(int, input().split()))

for n in matrix:
    if n % 2 == 1:
        gr += 1
    else:
        mo += 1

if gr < mo:
    print(mo)
elif gr == mo:
    print("tie")
else:
    print(gr)