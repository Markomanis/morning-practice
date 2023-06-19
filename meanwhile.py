car_type = input("What kind of car you want? :")

print(f"Let me see if I can find {car_type} for you.")

guests = input("How many people are comming?")
guests = int(guests)

if guests < 8:
    print(f"Only {guests}? That's no problem. Here is the table")
else:
    print(f"I am sorry you have to wait I don't have space for {guests} guests")

number = input("Insert your number: ")

if '0' in number:
    print(f"{number} is multiple of 10")
else:
    print(f"{number} is not multiple of 10")

parrot = ''

while parrot != 'quit':
    parrot = input("Tell me something and I will repeat it back to you: ")
    if parrot == 'quit':
        break
    print(f"{parrot}")
    print(f"Play again or type 'quit in order to stop the game.'")
      
Pizza toppings program:
choose_topping = []
topping = ''
while topping != 'quit':
    topping = input("Choose your pizza topping (if you dont want more toppings, type 'quit'): ")
    if topping == 'quit':
        break
    choose_topping.append(topping)
    print(f"Adding {topping}")
print(f"Your pizza will have following topping {choose_topping}")


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
        
unverified_users = ['Joshua', 'Koko', 'Klement']
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()

    print(f"Verifying user {current_user}\n")

    print(f"User {current_user} verified\n")
    verified_users.append(current_user)

print(f"We have new verified users:")
for verified_user in verified_users:
    print(f"{verified_user.title()}")
    
pets = ['dog', 'cat', 'parrot', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

sandwich_orders = ['boloni', 'kalmenze', 'pastrami','funghi', 'panino', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami sandwiches boooyz!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"Your {sandwich} sandwich is ready.")
    finished_sandwiches.append(sandwich)

print("I made for you these sandwiches: ")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")


dream_vacation_poll = {}

poll_active = True
while poll_active:
    name = input(f"Hello sir, what is your name?: ")
    vacation = input(f"And tell me {name}, where would you like to go to vac?:")
    dream_vacation_poll[name] = vacation
    response = input(f"Would you like to another user to take the poll? (y/n)")
    if response == 'n':
        poll_active = False
    else:
        continue

for name, vacation in dream_vacation_poll.items():
    print(f"User {name} would like to visit {vacation}")

    
    