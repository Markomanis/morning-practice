# class Restaurant:
    
#     def  __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} focus on {self.cuisine_type} kitchen.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is now open.")

#     def customers_served(self):
#         print(f"Customers served: {self.number_served}")
    
#     def update_served(self, num):
#         self.number_served = num
    
#     def increment_served(self, inc):
#         self.number_served += inc


# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type, flavours):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavours = flavours

#     def flavours_display(self):
#         print(f"Available flavours are: {self.flavours}")

# flavours_list = ['chocolate', 'vanilla', 'banana']
# menu = IceCreamStand('Fratelli', 'Gelato', flavours_list)

# menu.flavours_display()

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name: {self.first_name}, {self.last_name}"
              f" age of: {self.age}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin's privileges: {self.privileges}")

admins_privileges = ['Can ban user', 'Can add user', 'Can remove user']
admin = Admin('Peter', 'Veducko', 28, admins_privileges)
admin.show_privileges()
admin.describe_user()

# user_1 = User('Joe', 'Pesci', 20)
# user_2 = User('Alfredo', 'Fetuccini', 41)

# user_1.describe_user()
# user_2.describe_user()

# user_1.greet_user()
# user_2.greet_user() 

# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(f"{user_1.first_name} {user_1.last_name} tried to log in:"
#       f" {user_1.login_attempts} times.")\

# user_1.reset_login_attempts()

# print(f"User log in attempts resets to: {user_1.login_attempts}")


