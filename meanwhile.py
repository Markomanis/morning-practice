# car_type = input("What kind of car you want? :")

# print(f"Let me see if I can find {car_type} for you.")

# guests = input("How many people are comming?")
# guests = int(guests)

# if guests < 8:
#     print(f"Only {guests}? That's no problem. Here is the table")
# else:
#     print(f"I am sorry you have to wait I don't have space for {guests} guests")

# number = input("Insert your number: ")

# if '0' in number:
#     print(f"{number} is multiple of 10")
# else:
#     print(f"{number} is not multiple of 10")

# parrot = ''

# while parrot != 'quit':
#     parrot = input("Tell me something and I will repeat it back to you: ")
#     if parrot == 'quit':
#         break
#     print(f"{parrot}")
#     print(f"Play again or type 'quit in order to stop the game.'")
      
# Pizza toppings program:
# choose_topping = []
# topping = ''
# while topping != 'quit':
#     topping = input("Choose your pizza topping (if you dont want more toppings, type 'quit'): ")
#     if topping == 'quit':
#         break
#     choose_topping.append(topping)
#     print(f"Adding {topping}")
# print(f"Your pizza will have following topping {choose_topping}")


active = True
age = ''
while active:
    age = input("What is your age? ('q' to quit the program): ")
    if age == 'q':
        active = False
    elif int(age) < 3:
        print("Ticket is free for you")
        
    elif int(age) >= 3 and int(age) < 12:
        print("Ticket costs 10$")
        
    else:
        print("Ticket is 15$")
        





    
    