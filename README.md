# API HTTP Tester

Домашнее задание к уроку "Что такое API и как с ним работать" (Модуль 4, курс "Профессия вайб-кодер").

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
