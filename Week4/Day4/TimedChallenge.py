str = input("Enter a sentence")
character = input("Enter a character")

count = 0

for value in str:
    if value == character:
        count +=1

print(count)