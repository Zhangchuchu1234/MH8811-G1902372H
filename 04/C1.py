
myList = [9, 41, 12, 3, 74, 15]

min = None

for number in myList:
    if min is None:
        min = number
    elif min > number:
        min = number

print("List is: {}".format(myList))
print("Minimum of this list is {}".format(min))
