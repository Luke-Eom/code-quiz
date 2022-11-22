from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))
result = {number : 0 for number in numbers}
for card in cards:
    if card in result.keys():
        result[card] += 1
answer = []
for number in numbers:
    answer.append(result[number])
print(*answer)


# counter module 
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

count = Counter(cards)
answer = [count[number] if number in count else 0 for number in numbers]
print(*answer)