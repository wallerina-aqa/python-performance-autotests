# Python Performance Tests

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Locust](https://img.shields.io/badge/Locust-Performance%20Testing-green)
![gRPC](https://img.shields.io/badge/gRPC-API%20Testing-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)

Проект по нагрузочному тестированию банковских сервисов с использованием **Python** и
**Locust**.

Реализованы сценарии для **HTTP** и **gRPC API**, моделирующие пользовательские
операции банковского приложения.
Проект включает подготовку тестовых данных, конфигурацию профилей нагрузки, сбор
результатов и работу с инфраструктурой для мониторинга.

## Тестовый стенд

Для нагрузочного тестирования используется банковский тестовый стенд
[Performance QA Engineer](https://github.com/Nikita-Filonov/performance-qa-engineer-course).

Стенд представляет собой микросервисное приложение с HTTP- и gRPC-интерфейсами
и инфраструктурными компонентами для проведения и мониторинга нагрузочных тестов.

## Стек

**Тестирование:** Python · Locust · HTTPX · gRPC / grpcio · Pydantic

**Инфраструктура:** Docker Compose · PostgreSQL · Kafka · Redis · MinIO · Prometheus ·
Grafana · GitHub Actions

## Что реализовано

- Нагрузочное тестирование HTTP API
- Нагрузочное тестирование gRPC API
- 16 сценариев нагрузки: 8 HTTP и 8 gRPC
- Сценарии для существующих и новых пользователей
- Переиспользуемые HTTP- и gRPC-клиенты
- Подготовка тестовых данных перед запуском сценариев
- Индивидуальные профили нагрузки для каждого сценария
- Запуск Locust в headless-режиме
- Формирование HTML- и CSV-отчётов
- Сохранение распределения Locust-задач в JSON
- Интеграция с Load Testing Hub
- Мониторинг метрик через Prometheus и Grafana
- Локальная инфраструктура через Docker Compose

## Сценарии

Тесты покрывают основные пользовательские операции банковского приложения:

- получение счетов
- получение документов
- получение истории операций
- выпуск виртуальной карты
- выпуск физической карты
- выполнение покупки
- пополнение счёта

Сценарии разделены по протоколам HTTP и gRPC и находятся в каталоге `tests/`.

## Структура проекта

```text
contracts/                              # protobuf-контракты
dumps/                                  # данные для подготовки тестового окружения
locust_settings/                        # общие настройки Locust
schemas/                                # модели данных
seeds/                                  # подготовка тестовых данных
services/                               # методы HTTP- и gRPC-сервисов
tests/                                  # сценарии нагрузочного тестирования
tools/                                  # вспомогательные инструменты
config.py                               # конфигурация проекта
run_scenario.py                         # запуск сценария и сохранение распределения задач
docker-compose.load-testing-hub.yaml    # конфигурация Load Testing Hub
pyproject.toml                          # зависимости и настройки проекта
```

## Установка

```bash
git clone https://github.com/wallerina-aqa/python-performance-autotests.git
cd python-performance-autotests

uv sync
```

## Запуск инфраструктуры

Для запуска Load Testing Hub:

```bash
docker compose -f docker-compose.load-testing-hub.yaml up -d
```

Проверка состояния контейнеров:

```bash
docker compose -f docker-compose.load-testing-hub.yaml ps
```

## Запуск сценариев

Каждый сценарий содержит собственный `v1.conf` с параметрами нагрузки.

Например:

```bash
python run_scenario.py tests/http/gateway/existing_user_get_documents/v1.conf
```

Для gRPC:

```bash
python run_scenario.py tests/grpc/gateway/existing_user_get_documents/v1.conf
```

`run_scenario.py` запускает нагрузочный тест
и сохраняет распределение Locust-задач в `result_ratio.json`.

Параметры нагрузки — количество пользователей, скорость их создания
и продолжительность теста — задаются отдельно для каждого сценария в `v1.conf`.

## Результаты

После выполнения сценария Locust формирует:

- HTML-отчёт
- статистику запросов в CSV
- историю статистики
- список ошибок
- распределение задач в JSON

Результаты нагрузочных прогонов также доступны в Load Testing Hub.

## Мониторинг

Для наблюдения за состоянием тестового стенда используются:

- Prometheus - сбор метрик
- Grafana - визуализация метрик
- Kafka UI - работа с Kafka
- pgAdmin - работа с PostgreSQL

