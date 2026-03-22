s = list(input())

vowels = []

for ch in s:
    if ch.lower() in "aeiou":
        vowels.append(ch)

i = 0
for j in range(len(s)):
    if s[j].lower() in "aeiou":
        s[j] = vowels[-(i+1)]
        i += 1

print("".join(s))
