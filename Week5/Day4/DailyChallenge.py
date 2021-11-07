# import re
# import string
#
#
# class Text:
#     def __init__(self,string):
#
#
#     def word_in_text(self):
#         frequency = {}
#         document_text = open('the_stranger.txt', 'r')
#         text_string = document_text.read().lower()
#         match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
#
#         for word in match_pattern:
#             count = frequency.get(word, 0)
#             frequency[word] = count + 1
#
#         frequency_list = frequency.keys()
#
#         for words in frequency_list:
#             print(words, frequency[words])
#
#     def maxfrquency(self, frequency):
#         res = self.wordInText()
#         maxValue = res.max(frequency[words])
#         return maxValue
#
# text = Text()
# print(text.word_in_text())
# max = text.maxfrquency()
# print(max)
#
