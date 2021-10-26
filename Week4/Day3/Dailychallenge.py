
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = input()
s= int(input())
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))


# message = input("\n  Please enter the text you want to crypte")
# shift_number = int(input("\n How many you want to crypte"))
# print(shift_number)
#
# new_message = ""
#
# alphabet = {}
# letter = ['a','b','c','d','e']
#
# for index,values in enumerate(letter):
#     alphabet[values] = index+1
#
# print(alphabet)
