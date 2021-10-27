import re
matrix = [
   ['7','i','3'],
   ['T','s','i'],
    ['h', '%', 'x'],
    ['i','#',''],
    ['s','M',''],
    ['$','a',''],
    ['#', 't','%'],
    ['^','r','!'],
]

def foo():
    word = ''
    for val in matrix:
        if(val[0].isalpha()):
            word+=val[0]
    return word

def foo2():
    word = ''
    for val in matrix:
        if(val[1].isalpha()):
            word+=val[1]
    return word

def foo3():
    word = ''
    for val in matrix:
        if (val[2].isalpha()):
            word += val[2]
    return word


value =foo()
value2=foo2()
value3=foo3()


sentence = value + value2 + value3
print(sentence)
