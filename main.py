"""
Тестер HTTP-запросов — домашнее задание к уроку "Что такое API и как с ним работать".

Меню:
1 — GET-запрос по произвольному URL (сырой JSON-ответ)
2 — GET-запрос по стране (restcountries.com), с выделением ключевых полей
3 — Случайная собака (dog.ceo), ссылка на изображение
0 — Выход
"""

import json
from typing import Any

from colorama import Fore, Style, init

import http_client

init(autoreset=True)


def print_header(title: str) -> None:
    line = "=" * 50
    print(Fore.CYAN + Style.BRIGHT + f"\n{line}\n{title}\n{line}")


def show_json_pretty(data: Any) -> None:
    print(Fore.YELLOW + json.dumps(data, ensure_ascii=False, indent=2))


def parse_json(response) -> Any:
    """Пытается распарсить JSON из ответа, иначе возвращает None."""
    try:
        return response.json()
    except ValueError:
        print(Fore.RED + "Не удалось разобрать ответ как JSON.")
        return None


def do_get_by_url() -> None:
    """Пункт 1: сырой GET-запрос по любому URL, ответ выводим как есть."""
    url = input("Введите URL: ").strip()
    response = http_client.get(url)
    if response is None:
        return

    data = parse_json(response)
    if data is not None:
        show_json_pretty(data)
    else:
        print(Fore.YELLOW + response.text)


def do_get_by_country() -> None:
    """
    Пункт 2: минимум задания — получить JSON и выделить из него
    два-три ключевых поля (тут: название, столица, население).

    restcountries.com/v3.1 (использовавшийся в уроке) на момент написания
    кода уже отключён и требует платной регистрации, поэтому здесь
    используется другой бесплатный источник без ключа — sampleapis.com,
    который отдаёт список всех стран одним GET-запросом.
    """
    country = input("Введите название страны (на английском): ").strip()
    url = "https://api.sampleapis.com/countries/countries"
    response = http_client.get(url)
    if response is None:
        return

    data = parse_json(response)
    if data is None:
        return

    country_data = next(
        (item for item in data if item.get("name", "").lower() == country.lower()),
        None,
    )
    if country_data is None:
        print(Fore.RED + f"Страна не найдена: {country}")
        return

    population = country_data.get("population")

    print_header(f"Информация о стране: {country_data.get('name', '—')}")
    print(Fore.GREEN + "Столица: " + Style.RESET_ALL + country_data.get("capital", "—"))
    if population is not None:
        pretty_population = f"{population:,}".replace(",", " ")
    else:
        pretty_population = "—"
    print(Fore.GREEN + "Население: " + Style.RESET_ALL + pretty_population)
    print(Fore.GREEN + "Валюта: " + Style.RESET_ALL + country_data.get("currency", "—"))


def do_random_dog() -> None:
    """Пункт 3 (средний уровень): случайная собака с dog.ceo."""
    url = "https://dog.ceo/api/breeds/image/random"
    response = http_client.get(url)
    if response is None:
        return

    data = parse_json(response)
    if data is None:
        return

    print_header("Случайная собака")
    print(Fore.GREEN + "Ссылка на фото: " + Style.RESET_ALL + data.get("message", "—"))


def main() -> None:
    while True:
        print_header("Тестер HTTP-запросов")
        print("1. Выполнить GET-запрос по URL")
        print("2. Выполнить GET-запрос по стране")
        print("3. Случайная собака")
        print("0. Выйти")

        choice = input("\nВведите ваш выбор (0-3): ").strip()

        if choice == "1":
            do_get_by_url()
        elif choice == "2":
            do_get_by_country()
        elif choice == "3":
            do_random_dog()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print(Fore.RED + "Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
