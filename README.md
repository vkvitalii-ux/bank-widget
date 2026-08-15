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

'''python
from src.processing import filter_by_state, sort_by_date

data = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.000000'},
{'id': 93971957, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.000000'}
]

# Сортировка по дате

sorted_data = sort_by_date(data)
print(sorted_data)
'''

## Как запустить тесты и проверки

1. Запуск тестов:
   poetry run pytest

2. Проверка стиля кода:
   poetry run flake8 src tests

3. Проверка типов:
   poetry run mypy src tests