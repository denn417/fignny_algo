N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []

for i in range(N):
    answer.append(A[i] - B[i])

print(*answer)