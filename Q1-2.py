S = input()
N = int(input())
P = list(map(int, input().split()))

for meal in P:
    S += " " + "a" * meal

print(S)