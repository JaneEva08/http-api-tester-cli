# API HTTP Tester

Небольшой CLI-инструмент для тестирования HTTP-запросов к произвольным API прямо из консоли.

## Что внутри

- `http_client.py` — базовые функции `get()` и `post()` поверх `requests`, с проверкой статуса ответа.
- `main.py` — CLI-меню на русском:
  1. GET-запрос по произвольному URL
  2. GET-запрос по стране (api.sampleapis.com/countries) — с выделением ключевых полей
  3. Случайная собака (dog.ceo)
  0. Выход
- `requirements.txt` — зависимости (`requests`, `colorama`).

## Запуск

\`\`\`bash
python -m venv venv
source venv/bin/activate      # на Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
\`\`\`
