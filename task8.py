text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

if len(text) > 0:
    result += text[-1] + str(count)

print("Original Text:", text)
print("Compressed Text:", result)