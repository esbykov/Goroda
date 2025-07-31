from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"


key = '63e5eb15415b4679a88d546ae3e03d01'
city = "Эквадор"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")




