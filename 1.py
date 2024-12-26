import folium

stadiums_location = {
        "Лужники": (55.715551, 37.554191),
        "Спартак": (55.818015, 37.440262),
        "Динамо": (55.791540, 37.559809)
}

moscow_map = folium.Map(location=[55.7558, 37.6173], zoom_start=11)

for name, coords in stadiums_location.items():
    folium.Marker(location=coords, popup=name).add_to(moscow_map)

moscow_map.save("moscow_map.html")
print("Карта Москвы: moscow_map.html")
