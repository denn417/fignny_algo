N = int(input())

A = [0] * N

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

pointer = [0, 0]

direction = 0

for i in range(N):
    A[i] = int(input())

for i in range(N):
    pointer[0] += dx[direction] * A[i]
    pointer[1] += dy[direction] * A[i]
    direction += 1
    if direction == 4:
        direction = 0

print(pointer[0], pointer[1])