import folium
from geopy.distance import geodesic


def create_path_map(coords):
    path_map = folium.Map(location=coords[0], zoom_start=12)
    folium.PolyLine(coords, color="blue", weight=2.5, opacity=1).add_to(path_map)

    middle_index = len(coords) // 2
    middle_point = coords[middle_index]
    folium.Marker(location=middle_point, popup="Средняя точка").add_to(path_map)

    path_map.save("path_map.html")
    print("Карта пути создана: path_map.html")

    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += geodesic(coords[i], coords[i + 1]).meters
    return total_distance

coords = [(60, 30), (63, 31), (62, 32)]
print(f"Общая длина пути: {create_path_map(coords):.2f} м")
