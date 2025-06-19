import requests
import json
import time


def test_api():
    base_url = "http://localhost:8000"

    # Створити місто з унікальною назвою
    timestamp = int(time.time())
    city_data = {
        "name": f"Тестове_місто_{timestamp}",
        "additional_info": "Тестове місто",
    }
    print("Створюємо місто...")
    response = requests.post(f"{base_url}/cities/", json=city_data)
    print(f"Статус: {response.status_code}")
    if response.status_code == 201:
        city = response.json()
        print(f"Створено місто: {city}")

        # Додати температуру
        temp_data = {"city_id": city["id"], "temperature": 25.5}
        print("\nДодаємо температуру...")
        response = requests.post(f"{base_url}/temperatures/", json=temp_data)
        print(f"Статус: {response.status_code}")
        if response.status_code == 201:
            temp = response.json()
            print(f"Додано температуру: {temp}")
        else:
            print(f"Помилка: {response.text}")

        # Отримати всі міста
        print("\nОтримуємо всі міста...")
        cities = requests.get(f"{base_url}/cities/").json()
        print(f"Міста: {cities}")

        # Отримати останню температуру
        print("\nОтримуємо останню температуру...")
        latest = requests.get(
            f'{base_url}/temperatures/city/{city["id"]}/latest'
        ).json()
        print(f"Остання температура: {latest}")
    else:
        print(f"Помилка створення міста: {response.text}")


if __name__ == "__main__":
    test_api()
