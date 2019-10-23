from passwordGenerator import genPassword

try:
    password_length = int(input("Please input the password length (larger or equal to 4): "))
except:
    print("Input error!")
    exit()

if password_length < 4:
    print("Input length should be larger or equal to 4! ")
    exit()

password = genPassword(password_length)

print("A random password of length {0} is {1}".format(password_length, password))