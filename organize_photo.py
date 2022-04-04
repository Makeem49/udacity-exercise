import os
"""
Exercise to get photo into appropraite folder.
"""
places = []

for path in os.listdir(path='Photos'):
    # List all the files in the photos dir and split it in order to get the names o cities in the format and saving it to places list
    names = path.split('_')
    if names[1] not in places:
        places.append(names[1])

for place in places:
    # making dir of each cities in the places list by iterating it
    print(os.mkdir(place))


for photo in os.listdir(path='Photos'):
    #
    if photo.split("_")[1] in places:
        for place in places:
            if photo.split("_")[1] == place:
                os.rename('Photos/'+photo, place+'/'+photo)


print(places)

# Restructing the above code

# import os
# """
# Exercise to get photo into appropraite folder.
# """
# places = []

# def extract_name(string):
#     """Extracting the city name from string"""
#     split_string = string.split('_')
#     return split_string

# def add_city(name):
#     """Adding city to places if not added"""
#     if names[1] not in places:
#         places.append(names[1])

# for path in os.listdir(path='Photos'):
#     # List all the files in the photos dir and split it in order to get the names o cities in the format and saving it to places list
#     names = extract_name(path)
#     add_city(names)

# print(places)

# def create_a_folder(name):
#     """Function to create a single folder"""
#     os.mkdir(name)


# def create_all_folder(places):
#     """Function to create a list of folder"""
#     for place in places:
#         # making dir of each cities in the places list by iterating it
#         create_a_folder(place)

# create_all_folder(places)
