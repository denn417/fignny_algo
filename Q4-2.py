N, L = map(int, input().split())

scores = [list(map(int, input().split())) for _ in range(L)]

high_scores = [0] * N
high_score_student = [0] * N

for i in range(L):
    for j in range(N):
        if high_scores[j] < scores[i][j]:
            high_scores[j] = scores[i][j]
            high_score_student[j] = i


answer = [0] * L

for i in range(N):
    answer[high_score_student[i]] += 1

high_count = max(answer)

print(answer.index(high_count) + 1, high_count)