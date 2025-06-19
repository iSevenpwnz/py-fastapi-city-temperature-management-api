import requests

try:
    # Тест головної сторінки
    response = requests.get("http://localhost:8001/")
    print(f"Головна сторінка: {response.json()}")

    # Тест створення міста
    import time

    timestamp = int(time.time())
    city_data = {
        "name": f"Тест_синхронний_{timestamp}",
        "additional_info": "Тестове місто",
    }
    response = requests.post("http://localhost:8001/cities/", json=city_data)
    print(f"Створення міста - статус: {response.status_code}")

    if response.status_code == 201:
        city = response.json()
        print(f"Створено місто: {city}")
    else:
        print(f"Помилка: {response.text}")

except Exception as e:
    print(f"Помилка: {e}")
