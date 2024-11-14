# SwaggerQT

[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![PyQT](https://img.shields.io/badge/build_with-PyQT-blue)](https://pypi.org/project/PyQt6/)

SwaggerQT is a GUI builder of [swagger](https://swagger.io).
Swagger can build pretty interactive UI of your API, as well as generate code out of your API model in `swagger.yaml`

## Description

SwaggerQT будет представлять собой мощный инструмент для разработчиков,
позволяющий легко создавать и управлять документацией Swagger для REST API.
Приложение будет включать в себя следующие ключевые компоненты:
- Главный экран: Интуитивно понятный интерфейс, где пользователи смогут начать новый проект или открыть существующий.
- Редактор схем: Модуль для создания и редактирования JSON OpenAPI схем с поддержкой автозаполнения и подсказок.
- Генератор swagger.yaml: Функция, позволяющая пользователям собирать swagger.yaml файл, проверять его на ошибки и сохранять.
- Документация и поддержка: Встроенная справка и примеры использования для облегчения работы с приложением.

## Ожидаемые результаты:
- Создание полноценного десктопного приложения для работы с документацией Swagger API. 
- Упрощение процесса создания и редактирования OpenAPI схем для разработчиков. 
- Повышение качества документации REST API за счет удобного интерфейса и функционала приложения. 

## Getting Started

### Dependencies

- Python 
- PyQT6
more in `pyproject.toml`

### Installing

```shell
git clone https://github.com/HayKor/SwaggerQT.git
cd SwaggerQT
python -m venv .venv
```

Install dependencies using **poetry**:

```shell
poetry install
```

Or using **pip**:
```shell
pip install -r requirements.txt
```

### Executing program

Activate the venv first:

```shell
source .venv/scripts/activate
```

Run the `main.py` file:

```shell
python swaggerqt/main.py
```
