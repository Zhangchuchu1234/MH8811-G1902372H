import math

def my_min(list):

    minimum = None
    for number in list:
        if minimum is None:
            minimum = number
            continue
        if minimum > number:
            minimum = number
    return minimum

def my_max(list):

    maximum = None
    for number in list:
        if maximum is None:
            maximum = number
            continue
        if maximum < number:
            maximum = number

    return maximum


def my_average(list):
    if len(list) is 0:
        return None

    sum = 0
    for number in list:
        sum = sum + number
    avg = sum/len(list)

    return avg


def my_median(list):
    if len(list) is 0:
        return None

    list.sort()
    r = int(len(list) / 2)
    if len(list) % 2 == 1:
        median = list[r]
    else:
        median = (list[r-1] + list[r]) / 2

    return median


def my_range(list):
    if len(list) is 0:
        return None

    range = my_max(list)-my_min(list)
    return range


def my_sample_variance(list):
    if len(list) is 0:
        return None

    sum = 0
    for number in list:
        sum = sum+math.pow((number-my_average(list)),2)
    s_v = sum/(len(list)-1)

    return s_v



def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    fhandle.close()
    return lines


myList = getFileLines("MH8811-04-Data.csv")
myList = list(map(int, myList))

print("The list is {}".format(myList))

print("Minimum of this list is {0}".format(my_min(myList)))
print("Maximum of this list is {0}".format(my_max(myList)))
print("Average of this list is {0:5.3f}".format(my_average(myList)))
print("Median of this list is {0}".format(my_median(myList)))
print("Range of this list is {0}".format(my_range(myList)))
print("Sample Variance of this list is {0:8.3f}".format(my_sample_variance(myList)))

