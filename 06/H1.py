from passwordGenerator import genPassword

try:
    password_length = int(input("Please input the password length, which is larger or equal to 4: "))
except:
    print("Input error!")
    exit()

password = genPassword(password_length)

print("A random password of length {0} is {1}".format(password_length, password))