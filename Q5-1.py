N, Q = map(int, input().split())
players = [0] * N

for i in range(Q):
    process, target = map(int, input().split())
    if process < 3:
        players[target - 1] += process
    elif players[target - 1] > 1:
        print("Yes")
    else:
        print("No")