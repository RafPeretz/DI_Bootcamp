from functools import reduce
str = input("give us your list")
arr = []
mot = ""
for i in str:
    if i != ",":
        mot += i
    else:
        arr.append(mot)
        mot=""
arr.append(mot)
arr=sorted(arr)
def cama_btw(first, second):
    return first+","+second
reduced_list = reduce(cama_btw, arr)
print(reduced_list)