N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)

rlt = 0

for budget in B:
    for price in A:
        if budget >= price:
            rlt += price
            break

print(rlt)

