N = int(input())
A = list(map(int, input().split()))

num_set = set()

for num in A:
    num_set.add(num)

if len(A) == len(num_set):
    print("YES")
else:
    print("NO")