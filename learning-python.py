''' while True:
    name = input("Enter your name: ")
    a = len(name)
    if a < 5:
        print("Hello Mr.", name)
        break
    else:
        print("Please enter a valid name (less than 5 characters).")

        

while True :  
    name = input("enter your name ( or exit to leave):")
    if name != "exit":
        print("Hello Mr.", name)
        break
    else: 
        ##print("existing ...")
        break

while True:
    name = input("Enter your name (or 'exit' to leave): ")
    if name.lower() == "exit":
        break  # Exit the loop if the user types 'exit'
    elif len(name) >= 5:
        print("Please enter a valid name (less than 5 characters).")
        continue  # Skip the rest of the loop and prompt the user again
    else:
        print("Hello Mr.", name)
        break  # Exit the loop if a valid name is entered


for i in range(10, 0, -1):
    print(i)
   

def happy_birthday():
    print("Happy Birthday to you!")
    print("you are old")
    print("Happy Birthday to you!")
    print() 
countre = 0
while countre < 3:
    happy_birthday()
    countre += 1
 ''' 


def happy_birthday(age,name):  # Function definition
    print(f"happy birthday {name} you are {age} years old and {name} is a great name by the way")
    print("Happy Birthday to you!")

happy_birthday(10,"Joud")   