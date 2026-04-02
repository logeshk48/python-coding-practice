arr = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

freq = {}
count = 0

for num in arr:
    if target - num in freq:
        count += freq[target - num]
    freq[num] = freq.get(num, 0) + 1

print("Pairs count:", count)
