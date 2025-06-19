import uvicorn
import logging

if __name__ == "__main__":
    # Налаштовуємо детальні логи
    logging.basicConfig(level=logging.DEBUG)

    # Запускаємо сервер
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000, reload=True, log_level="debug"
    )
