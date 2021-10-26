import requests

# Enter your api key here
with open('apikey.txt', 'r') as file:
    api_key = file.read().replace('\n', '')
print(api_key)

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

# center defines the center of the map,
# equidistant from all edges of the map.
center = "New York"

# zoom defines the zoom
# level of the map
zoom = 13

# get method of requests module
# return response object
r = requests.get(url + "center=" + center + "&zoom=" +
                 str(zoom) + "&maptype=satellite" + "&scale=2" + "&size=400x400&key=" +
                 api_key)



# wb mode is stand for write binary mode
f = open('img', 'wb')

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()