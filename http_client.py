"""
Небольшой HTTP-клиент поверх requests.

Задача модуля — не знать ничего о конкретных API (странах, собаках и т.д.),
а просто уметь выполнять GET/POST-запросы и сообщать, что произошло
(код статуса, ошибка соединения и т.п.). Вся логика "что делать с ответом"
живёт в main.py — так же, как в уроке publisher не должен знать про LLM.
"""

from typing import Any, Dict, Optional

import requests


def get(
    url: str,
    params: Optional[Dict[str, Any]] = None,
    timeout: int = 10,
) -> Optional[requests.Response]:
    """Выполняет GET-запрос. Возвращает Response или None при ошибке сети."""
    try:
        response = requests.get(url, params=params, timeout=timeout)
        _print_status(response)
        return response
    except requests.exceptions.RequestException as error:
        print(f"Ошибка запроса: {error}")
        return None


def post(
    url: str,
    data: Optional[Dict[str, Any]] = None,
    json_data: Optional[Dict[str, Any]] = None,
    timeout: int = 10,
) -> Optional[requests.Response]:
    """Выполняет POST-запрос. Возвращает Response или None при ошибке сети."""
    try:
        response = requests.post(url, data=data, json=json_data, timeout=timeout)
        _print_status(response)
        return response
    except requests.exceptions.RequestException as error:
        print(f"Ошибка запроса: {error}")
        return None


def _print_status(response: requests.Response) -> None:
    """Базовая проверка статуса: 2xx считаем успехом, всё остальное — ошибкой."""
    is_ok = 200 <= response.status_code < 300
    marker = "OK" if is_ok else "ОШИБКА"
    print(f"[{marker}] Код статуса: {response.status_code}")
