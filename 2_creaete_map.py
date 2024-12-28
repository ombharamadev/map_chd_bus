import requests
import json
import folium
from folium.plugins import Geocoder
url = "https://ctumobileapi.amnex.com/ListofLocations/GetLocations_v1?lan=en"
header = {
    "User-Agent":"Nasa"
}
data = requests.get(url,headers=header)
print(data)
#print(data.text)
json_d = json.loads(data.text)
a = json.loads(json_d["data"])
print(a[0])



# Sample data (you will replace this with your actual data)
data = a
# Create a map centered around the mean latitude and longitude
# For the initial map center, you can use an average or a central point of your data.
map_center = [30.75861, 76.78966]  # Choose a center location (e.g., the first station's coordinates)
mymap = folium.Map(location=map_center, zoom_start=13)

# Add markers for each station
for point in data:
    lat = point['latitude']
    lon = point['longitude']
    name = point['stationname']
    
    # Create a marker for each station
    folium.Marker(
        location=[lat, lon],
        popup=name,  # Display the station name when clicked
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(mymap)
# Add a Geocoder to search for an area (geocoding functionality)
Geocoder().add_to(mymap)
# Save the map to an HTML file
mymap.save('stations_map.html')

print("Map has been saved as 'stations_map.html'.")
