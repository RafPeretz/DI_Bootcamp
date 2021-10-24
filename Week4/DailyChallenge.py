import random
print("Please enter a string")
str = input()
sizeStr = len(str)

if(sizeStr < 10):
    print("string not long enough")

else:
    print("string too long")

    print(str[0])
    print(str[sizeStr-1])

    string = ""
    for x in str:

        string += x
        print(string)


#random.shuffle(str)

#print(str)
