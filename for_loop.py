fav_pizzas = ['margherita', 'formagi', 'funghi']
friends_fav_pizzas = fav_pizzas[:]
fav_pizzas.append('peperoni')
# print(fav_pizzas)
friends_fav_pizzas.append('calzoni')

print(f"My favourite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)

print(f"My friends fav pizzas are:")
for pizza in friends_fav_pizzas:
    print(pizza)
# for pizza in fav_pizzas:
#     print(f"I really like {pizza} pizza.")
# print("As you can see. I really like pizza!!!")

# pets = ['dog', 'cat', 'hamster']
# for pet in pets:
#     print(f"An {pet} is really good pet")
# print("All of them are good pets.")

# numbers = list(range(1,7))
# print(f" Last 3 items of the list are: {numbers[3:]}")

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# comprehension = [value**2 for value in range(1,11)]
# print(comprehension)

# milion = [num for num in range(1,1_000_001)]
# # print(milion)
# print(sum(milion))

# odd_numbers = [odd for odd in range(1,31,2)]
# print(odd_numbers)

# one_to_thirty = list(range(0,31,3))
# for num in one_to_thirty:
#     print(num)

# cubes = [cube**3 for cube in range(1,11)]
# print(cubes)

