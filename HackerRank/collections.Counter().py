from collections import Counter

X = int(input())
sizes_dict = Counter(map(int, input().split()))
N = int(input())
income = 0

for n in range(N):
    size, price = map(int, input().split())
    if size in sizes_dict:
        sizes_dict[size] -= 1
        income += price
        if sizes_dict[size] == 0:
            del sizes_dict[size]

print(income)
