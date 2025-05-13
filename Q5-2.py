H, W = map(int, input().split())

gridA = [list(input()) for _ in range(H)]
gridB = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if gridA[0][0] == gridB[i][j]:
            for k in range(H):
                flag = 1
                for l in range(W):
                    if not gridA[k][l] == gridB[(i+k) % H][(j+l) % W]:
                        flag = 0
                        break
                if not flag:
                    break
            else:
                print("Yes")
                exit()
else:
    print("No")