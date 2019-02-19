import folium

map = folium.Map(location=[40.2969, -111.6946], zoom_start=20)
print(map.save('test.html'))