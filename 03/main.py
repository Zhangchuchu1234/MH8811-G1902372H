from p01 import helloWorld
from p02_1 import helloUser
from p02_2 import CelsiusFahrenheitConverter

def main():
    end = False
    while (end is False):
        choice = input("\n"
                       "----------------\n"
                       "Please choose one of the following sub-programs: \n"
                       "(1) Output 'Hello, World!'\n"
                       "(2) Input user's name and output 'Hello' with user's name\n"
                       "(3) Input temperature in Celsius and output the temperature in Fahrenheit\n"
                       "(4) Exit \n"
                       "----------------\n")


        if not choice.isdigit():
            print("Invalid Choice! ")
        elif (int(choice) == 1):
            helloWorld()
        elif (int(choice) == 2):
            helloUser()
        elif (int(choice) == 3):
            CelsiusFahrenheitConverter()
        elif (int(choice) == 4):
            end = True
        else:
            print("Invalid Choice!")

if __name__ == '__main__':
    main()