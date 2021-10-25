#Way1
list1 = [5, 10, 15, 20, 25, 50, 20]
value = list1.index(20)
print(value)
list1.insert(3,200)
print(list1)

#Way2
list2 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list2:
    index = list2.index(20)
    list2[index] = 200
    print(list2)



