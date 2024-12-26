import requests

def find_southernmost_city(cities):
    southernmost = None
    min_latitude = float("inf")

    for city in cities:
        geocode_url = f"https://geocode-maps.yandex.ru/1.x/"
        geocode_params = {
            "geocode": city,
            "format": "json",
            "apikey": "0d997e8f-b415-4fd0-91b1-c9547916c893"
        }
        response = requests.get(geocode_url, params=geocode_params).json()
        try:
            point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lon, lat = map(float, point.split())
            if lat < min_latitude:
                southernmost = city
                min_latitude = lat
        except (KeyError, IndexError):
            print(f"Не удалось найти координаты для города {city}.")

    print(f"Самый южный город: {southernmost}")

find_southernmost_city(["Москва", "Сочи", "Воронеж"])
