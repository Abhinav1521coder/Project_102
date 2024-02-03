print("This is a calculator that will help you in your Maths homework")
print("For division please use /")
print("For addition please use +")
print("For subtraction please use -")
print("For multiplication please use *")

yes = input("Would you like to continue type Y/N: ")

while yes == "Y":
    ask = input("What would you like to do today: ")
    if ask == "/":
        print("Please type you numbers here")
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))
        division = number1 / number2
        print("The answer is:", division)
        yes = input("Would you like to continue type Y/N: ")
        ask = input("What would you like to do today: ")

        
    elif ask == "+":
        print("Please type you numbers here")
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))
        addition = number1 + number2
        print("The answer is:", addition)
        yes = input("Would you like to continue type Y/N: ")
        ask = input("What would you like to do today: ")

    elif ask == "-":
        print("Please type you numbers here")
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))
        subtraction = number1 - number2
        print("The answer is:", subtraction)
        yes = input("Would you like to continue type Y/N: ")
        ask = input("What would you like to do today: ")

    elif ask == "*":
        print("Please type you numbers here")
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))
        multiplication = number1 * number2
        print("The answer is:", multiplication)
        yes = input("Would you like to continue type Y/N: ")
        ask = input("What would you like to do today: ")

if yes == "N":
    print("Thank you for using the calculator today")
