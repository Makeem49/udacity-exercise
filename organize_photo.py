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
                os.rename('Photos/'+photo , place+'/'+photo)



print(places)
