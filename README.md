# Saucedemo - tests
Автотесты для saucedemo.com на Python + Selenium + pytest.

## Стек
- Python 3.x
- Selenium WebDriver
- pytest + pytest-html
- webdriver-manager

## Структура
- `locators/` — все локаторы ...
- `tests/auth`, `tests/cart`, `tests/purchase` — структура тестов
- `conftest.py` — фикстуры ...

## Сценарии
- "Неуспешная авторизация": вход с неверными данными, проверка ошибки «Epic sadface».
- "Очищение корзины": добавить товары → удалить → проверить пустоту корзины и URL.
- "Успешная покупка": добавить товар → оформить заказ → проверить «THANKS FOR YOUR ORDER!».

## Запуск тестов
1. Активировать venv: `.\venv\Scripts\Activate.ps1`
2. Установить зависимости: `pip install -r requirements.txt`
3. Запустить тесты: `pytest -v --html=report.html`

Отчёт будет в файле `report.html`.