N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rlt = []

for i in range(N):
    if A[i] == B[i]:
        rlt.append(i+1)

if rlt:
    rlt = " ".join(map(str, rlt))
    print(rlt)
else:
    print(0)