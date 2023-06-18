applicants = {
    'josh' : 21,
    'freddy' : 18,
    'frankie' : 17
}

for name, age in applicants.items():
    if age < 20:
        print(f"You are not old enough to drive {name.title()}.")
    else:
        print(f"Here is your license {name.title()}.")

cars = ['toyota', 'BMW', 'subaru']

for car in cars:
    if car == 'Toyota'.lower():
        print('We do have Toyota in the stock')
    else: 
        print("Toyota is out of stock")
    break

alien_color = 'water'

if alien_color == 'green':
    print("5 points scored!")
elif alien_color == 'red':
    print("10 points scored!")
else:
    print("15 points scored!")

age = 101

if age < 2:
    print("This is a baby we talking about.")
if (age > 2) and (age < 4):
    print("This is a todler we talking about.")
if (age >= 4) and (age < 13):
    print("This is a kid we talking about.")
if (age >= 13) and (age < 20):
    print("This is a teen we talking about.")
if (age >= 20) and (age < 65):
    print("This is an adult we talking about.")
if age > 65:
    print("This is an elder we talking about.")

fav_fruits = ['banana', 'apple', 'orange']

for fruit in fav_fruits:
    if fruit == 'banana':
        print("I like banana!")
    if fruit == 'apple':
        print("I like apple!")
    if fruit == 'avocado':
        print('whateva')
    if fruit == 'ko':
        print("I like banana!")
    if fruit == 'orange':
        print("I like orange!")
    
available_toppings = ['olives', 'peppers', 'peperoni', 'tomato', 'anchovies', 
                      'funghi']

requested_toppings = ['olives', 'fries', 'peperoni']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"{requested_topping} not available")    

print("Making your pizza")

users = ['admin', 'frankie', 'jimothy', 'dynamo','koko']

for user in users:
    if user == 'admin':
        print(f"Hello {user}, would you like to see users report?")
    else:
        print(f"Hello {user.title()}, welcome")


users = []

if users == []:
    print("List is empty boss")
else:
    print("There are some rats")

current_users = ['user_1','user_2','user_3','user_4','user_5']

new_users = ['user_6','user_7','user_8','User_4','User_5']

for new_user in new_users:
    if new_user.lower() not in current_users:
        print(f"Name approved, welcome {new_user}")
    else:
#         print(f"Name {new_user} already exists, create new punk")    

numbers = [num for num in range(1,10)]

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd") 
    else:
        print(f"{num}th")  
    