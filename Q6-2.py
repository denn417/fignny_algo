N = int(input())
S = input()

record = set()
point = 00
record.add(point)
flag = "No"

for char in S:
    if char == "R":
        point += 10
    elif char == "L":
        point -= 10
    elif char == "U":
        point += 1
    elif char == "D":
        point -= 1
    if point in record:
        flag = "Yes"
        break
    else:
        record.add(point)

print(flag)