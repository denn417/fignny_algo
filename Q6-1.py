N = int(input())
X = list(map(int, input().split()))
X = sorted(X)

rlt = 0

for i in range(N, N * 4):
    rlt += X[i]

print(rlt / (N * 3))