import requests
import json

try:
    url = "http://localhost:8000/cities/"
    data = {"name": "Тест_місто", "additional_info": "Тест"}

    print(f"Відправляю POST на {url}")
    print(f"Дані: {data}")

    response = requests.post(url, json=data)

    print(f"Статус: {response.status_code}")
    print(f"Заголовки: {response.headers}")
    print(f"Текст відповіді: {response.text}")

    if response.headers.get("content-type", "").startswith("application/json"):
        print(f"JSON: {response.json()}")

except Exception as e:
    print(f"Помилка: {e}")
    import traceback

    traceback.print_exc()
