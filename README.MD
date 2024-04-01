# Учебный проект по тестированию Api

Этот проект представляет собой пример использования библиотек requests, pytest и allure для тестирования Api

https://restful-api.dev/

## Функциональность

1. GET запросы одного или нескольких объектов
2. POST/CREATE запросы по созданию нового объекта
3. DELETE запросы по удалению элмента
4. UPDATE запросы по изменению существующего объекта

## Используемые инструменты

- Python
- Pytest
- Requests
- Allure

## Инструкции по установке и запуску

1. Откройте среду разработки для Python
2. Установите библиотеки, перечисленные в файле `requirements.txt`, с помощью команды: 

```shell
pip install -r requirements.txt
```

3. Установите Allure
4. Запустите тесты с помощью Pytest и генерируйте отчеты Allure:

```shell
pytest --alluredir=allure-results
```

```shell
allure serve allure-results
```
