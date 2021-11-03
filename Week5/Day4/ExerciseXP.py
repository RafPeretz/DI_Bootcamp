# # Exercise 1 – Random Sentence Generator
#
# import random
#
#
# def get_words_from_file():
#     fileobj = open("sowpods.txt")
#     list_word = []
#     for line in fileobj:
#         list_word.append(line.strip())
#     return list_word
#
#
# def get_random_sentence(lenght):
#     list_word = get_words_from_file()
#     sentence = ""
#
#     for index in range(lenght):
#         sentence += " " + random.choice(list_word)
#
#     print(sentence.lower())
#
#
# get_random_sentence(4)
#
#
# def main():
#     print("The program cretate a random sentence.")
#     words = int(input("Give the number of words you want your sentece , Please insert between 2 and 20."))
#
#     if words > 20 or words < 2:
#         print("Error please input a number between w and 20")
#
#     else:
#         get_random_sentence(words)
#
# Exercise 2: Working With JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":70000000000000000000,
            "bonus":800
         }
      }
   }
}"""

dic = json.loads(sampleJson)
print(dic["company"]["employee"]["payable"]["salary"])

dic["company"]["employee"]["birthday"] = "1995-12-30"

print(dic)

dic = "my_file.json"

with open('data.json', 'w') as f:
    json.dump(dic, f)
