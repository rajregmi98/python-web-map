import folium
import pandas


data = pandas.read_csv("states.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
def color_producer(delovation):
    if delovation < 1000:
        return 'red'
    elif 1000<= delovation < 3000:
        return 'green'
    else:
        return 'orange'



map = folium.Map(location=[28, 84], zoom_start=6, tiles="Mapbox Bright" )
fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el in zip(lat, lon, elev):
     fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 7 ,popup=str(el)+" m",
     fill_color = color_producer(el),color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="population")
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))




map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


map.save("map1.html")
