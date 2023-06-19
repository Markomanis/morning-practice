# car_type = input("What kind of car you want? :")

# print(f"Let me see if I can find {car_type} for you.")

# guests = input("How many people are comming?")
# guests = int(guests)

# if guests < 8:
#     print(f"Only {guests}? That's no problem. Here is the table")
# else:
#     print(f"I am sorry you have to wait I don't have space for {guests} guests")

number = input("Insert your number: ")

if '0' in number:
    print(f"{number} is multiple of 10")
else:
    print(f"{number} is not multiple of 10")