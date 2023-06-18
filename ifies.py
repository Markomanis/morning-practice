# applicants = {
#     'josh' : 21,
#     'freddy' : 18,
#     'frankie' : 17
# }

# for name, age in applicants.items():
#     if age < 20:
#         print(f"You are not old enough to drive {name.title()}.")
#     else:
#         print(f"Here is your license {name.title()}.")

cars = ['toyota', 'BMW', 'subaru']

for car in cars:
    if car == 'Toyota'.lower():
        print('We do have Toyota in the stock')
    else: 
        print("Toyota is out of stock")
    break