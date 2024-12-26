import math
import requests

def get_coords(address):
    geocode_url = f"https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": address,
        "format": "json",
        "apikey": "0d997e8f-b415-4fd0-91b1-c9547916c893"
    }
    response = requests.get(geocode_url, params=geocode_params).json()
    try:
        point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        return tuple(map(float, point.split()))
    except (KeyError, IndexError):
        print(f"Не удалось найти координаты для {address}.")
        return None

def calculate_distance(home, uni):
    def lonlat_distance(a, b):
        degree_to_meters = 111 * 1000
        a_lon, a_lat = a
        b_lon, b_lat = b
        radians_lat = math.radians((a_lat + b_lat) / 2.0)
        cos_lat = math.cos(radians_lat)
        dx = abs(a_lon - b_lon) * degree_to_meters * cos_lat
        dy = abs(a_lat - b_lat) * degree_to_meters
        return math.sqrt(dx ** 2 + dy ** 2)

    home_coords = get_coords(home)
    uni_coords = get_coords(uni)
    if home_coords and uni_coords:
        distance = lonlat_distance(home_coords, uni_coords)
        print(f"Расстояние от дома до университета: {distance / 1000:.2f} км")
    else:
        print("Не удалось рассчитать расстояние.")

calculate_distance("Красная площадь, Москва", "Ленинский проспект, 1")
