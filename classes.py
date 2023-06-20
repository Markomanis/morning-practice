# class Restaurant:
    
#     def  __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} focus on {self.cuisine_type} kitchen.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open.")

# restaurant_1 = Restaurant('Boccelis', 'Italian')
# restaurant_2 = Restaurant('Palvos', 'Greek')
# restaurant_3 = Restaurant('U Feriho', 'Slovakian')

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()

class User:
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"User name: {self.first_name}, {self.last_name}"
              f" age of: {self.age}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

user_1 = User('Joe', 'Pesci', 20)
user_2 = User('Alfredo', 'Fetuccini', 41)

user_1.describe_user()
user_2.describe_user()

user_1.greet_user()
user_2.greet_user()

