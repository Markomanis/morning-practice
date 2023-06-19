# def favourite_book(title):
#     print(f"This {title} book is awesome")

# favourite_book('Python Crash Course')

# def make_shirt(printed_text, size = 'Large'):
#     print(f"Yout shirt size is {size} and your shirt will say: {printed_text}")

# make_shirt(printed_text = 'Yo brah')

def describe_city(city_name, country_name = 'Slovakia'):
    print(f"{city_name.title()} is in the {country_name.title()}")

describe_city('Koko')
describe_city('Kosice')
describe_city('Pele', 'Klokocovo')