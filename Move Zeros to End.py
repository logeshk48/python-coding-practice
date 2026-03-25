arr = list(map(int, input().split()))

result = []

for num in arr:
    if num != 0:
        result.append(num)

for num in arr:
    if num == 0:
        result.append(num)

print(*result)
