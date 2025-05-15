N, X = map(int, input().split())
A = list(input().split())

X = str(X)

rlt = 0

for control in A:
    if X in control:
        rlt += 1

print(rlt)
