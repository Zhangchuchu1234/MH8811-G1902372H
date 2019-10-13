import json
import sys


def serialize(data_structure):
    # check the type of the data structure
    data_type = type(data_structure)
    # if it is a list, list item are separated by '|' and the type of the item is separated by ','
    if data_type is list:
        res = "list|"
        for item in data_structure:
            res = res + str(item)
            res = res + ","
            res = res + str(type(item))
            res = res + "|"
        return res[:-1]

    #if it is a dictionary, disctionary item are separated by '|', key and value are separated by ':'
    # and type of the item is separated by ','
    elif data_type is dict:
        res = "dict|"
        for item in data_structure:
            res = res + str(item)
            res = res + ":"
            res = res + str(data_structure[item])
            res = res + ","
            res = res + str(type(data_structure[item]))
            res = res + "|"
        return res[:-1]



def deserialize(s):
    list_of_str = s.split("|")
    # first string saves the type of the data structure
    data_type = list_of_str[0]
    list_of_str = list_of_str[1:]

    if data_type == 'list':
        res = list()
        for string in list_of_str:
            item = string.split(",")
            value = item[0]
            value_type = item[1]

            # according to information of value's type, convert it back to the corresponding type.
            if value_type == "<class 'int'>":
                res.append(int(value))
            elif value_type == "<class 'float'>":
                res.append(float(value))
            elif value_type == "<class 'str'>":
                res.append(value)
        return res

    elif data_type == 'dict':
        res = dict()
        for string in list_of_str:
            string_split = string.split(":")
            key = string_split[0]
            item = string_split[1]

            item = item.split(",")
            value = item[0]
            value_type = item[1]

            if value_type == "<class 'int'>":
                res[key] = int(value)
            elif value_type == "<class 'float'>":
                res[key] = float(value)
            elif value_type == "<class 'str'>":
                res[key] = value
        return res


# function to compare if two data structures (list/dictionary) are the same
def compare(s1, s2):
    if type(s1) != type(s2):
        return False
    else:
        if isinstance(s1, list):
            if s1 == s2:
                return True
            else:
                return False
        if isinstance(s1, dict):
            if len(s1) != len(s2):
                return False
            for key in s1:
                if key not in s2:
                    return False
                if s1[key] != s2[key]:
                    return False
            return True


# ask user for a path to the json file
data_path = input("Please input the path and name of the json file: ")

# load the data structure from the json file
try:
    data_structure_file = open(data_path)
    data_structure = json.load(data_structure_file)
    data_structure_file.close()
except:
    print("No such file exists or error in json format!")
    sys.exit()



# convert the original data structure into a string using serializer
serialize_string = serialize(data_structure)


# write the string to a file
file_name = input("Please input the file name to store the data structure: ")
f = open(file_name, 'w')
f.write(serialize_string)
f.close()

# read the string back from the file
f2 = open(file_name)
string_from_file = f2.read()
f2.close()

# return a restored data structure using deserialization
ldeserialize_data_structure = deserialize(string_from_file)


# compare if two data structures are the same
if compare(data_structure, ldeserialize_data_structure):
    print("Success!")
else:
    print("Not success!")
