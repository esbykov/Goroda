from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language="ru")
        if results:
                return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"


key = '63e5eb15415b4679a88d546ae3e03d01'
city = "London"
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")




