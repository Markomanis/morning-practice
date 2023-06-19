# def favourite_book(title):
#     print(f"This {title} book is awesome")

# favourite_book('Python Crash Course')

# def make_shirt(printed_text, size = 'Large'):
#     print(f"Yout shirt size is {size} and your shirt will say: {printed_text}")

# make_shirt(printed_text = 'Yo brah')

# def describe_city(city_name, country_name = 'Slovakia'):
#     print(f"{city_name.title()} is in the {country_name.title()}")

# describe_city('Koko')
# describe_city('Kosice')
# describe_city('Pele', 'Klokocovo')

# def city_country(city_name, country_name):
#     print(f"{city_name.title()}, {country_name.title()} ")

# city_country('Kosice', 'Slovakia')

def make_album(artist_name, album_name, songs = None):
    album = {'name' : artist_name, 'album' : album_name}
    if songs:
        album['songs'] = songs
    print(album)

while True:
    print(f"Let's create album and artist. To quit anytime press 'q'. ")


    artist_name = input(f"Insert here artist name: ")
    if artist_name == 'q':
        break
    
    album_name = input(f"Instert album name: ")
    if album_name == 'q':
        break

    answer = input(f"Wish to save album? (y/n): ")
    if answer == 'y':
        break
    if answer == 'n':
        continue

make_album(artist_name, album_name )

