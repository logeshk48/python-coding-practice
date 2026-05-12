# Find the first non-repeating character using user input

text = input("Enter a string: ")

# Count frequency of each character
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Find the first non-repeating character
for char in text:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")
