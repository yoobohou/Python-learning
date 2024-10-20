

while True:
    operation = input("enter the operation that you want to perform: ")

    if operation == "addition":
        a = int(input("enter the first number a: "))
        b = int(input("enter the first number b: "))
        print(a + b)

    elif operation == "subtraction":
        a = int(input("enter the first number a: "))
        b = int(input("enter the first number b: "))
        print(a - b)

    elif operation == "multiplication":
        a = int(input("enter the first number a: "))
        b = int(input("enter the first number b: "))
        print(a * b)

    elif operation == "division":
        a = int(input("enter the first number a: "))
        b = int(input("enter the first number b: "))
        print(a / b)
    else:
        print("please enter a valid operation")
    continue
 
