import random

def genPassword(n):
    global lowercaseLetter, uppercaseLetter, numbers, symbols
    lowercaseLetter = "abcdefghijklmnopqrstuvwxyz"
    uppercaseLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    chars = lowercaseLetter+uppercaseLetter+numbers+symbols

    password = random.choice(lowercaseLetter)+random.choice(uppercaseLetter)+random.choice(numbers)+random.choice(symbols)

    for i in range(n-4):
        password = password + random.choice(chars)


    password = ''.join(random.sample(password, n))

    return password

if __name__ == "__main__":
    print("A random password of length 12 is {}".format(genPassword(12)))