# Виджет банковских операций (bank_widget)

## Описание проекта

Этот проект представляет собой виджет для фильтрации и сортировки банковских операций пользователя, а также маскирования
конфиденциальных данных (номеров карт и счетов).

## Инструкция по установке

1. Клонируйте репозиторий:
   '''bash
   git clone https://github.com
   '''
2. Установите зависимость с помощью Poetry:
   '''bash
   poetry install
   '''

## Описание разработанных функций

### Модуль 'masks'

* 'get_mask_card_number(card_number)' - маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.
* 'get_mask_account_number(account_number)' - маскирует номер счета, оставляя видимыми только последние 4 цифры.

### Модуль 'processing'

* 'filter_by_state(data, state="EXECUTED)' - фильтрует список словарей по статусу операции.
* 'sort_by_date(data, reverse=True)' - сортирует список словарей по дате операции (по умолчанию от самых свежих к более
  старым).

## Примеры работы функций

```python
from src.processing import filter_by_state, sort_by_date

data = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.000000'},
{'id': 93971957, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.000000'}
]

# Сортировка по дате

sorted_data = sort_by_date(data)
print(sorted_data)

```

## Как запустить тесты и проверки

1. Запуск тестов:
   poetry run pytest

2. Проверка стиля кода:
   poetry run flake8 src tests

3. Проверка типов:
   poetry run mypy src tests

---

## 💻 Модуль `generators.py` и примеры использования

В проекте реализован новый модуль `src/generators.py` для работы с банковскими последовательностями и фильтрацией
данных.

### 1. Генератор номеров карт (`card_number_generator`)

Генерирует номера карт в 16-значном формате с разделением по 4 цифры пробелами в заданном диапазоне.

```python
from src.generators import card_number_generator

# Пример генерации номеров карт
for card in card_number_generator(1, 3):
    print(card)

# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
```

### 2. Извлечение описаний транзакций (`transaction_descriptions`)

Принимает список словарей с транзакциями и поочередно возвращает только текстовые описания каждой операции.

```python
from src.generators import transaction_descriptions

transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"}
]

for desc in transaction_descriptions(transactions):
    print(desc)

# Вывод:
# Перевод организации
# Перевод со счета на счет
```