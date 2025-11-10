# Flask Docker App

**Версия: 1.0.1**

Простое Flask приложение, упакованное в Docker.

## Функциональность

- Главная страница с приветствием "Hello, CI/CD World!"
- Health check endpoint (/health)
- Version endpoint (/version)
- Автоматическое тестирование на Python 3.9, 3.10, 3.11
- Docker контейнеризация


## CI/CD Pipeline

- Matrix тестирование на 3 версиях Python
- Сборка и тестирование Docker образа
- Защита ветки main (обязательные проверки перед мержем)
- Автоматическая генерация документации
- Health-check контейнера
- Release management с тегами

## Запуск

```bash
docker-compose up --build
```

## Branch Protection

Ветка main защищена правилами, требующими прохождения:
- Docker build тестов
- Unit тестов на Python 3.9, 3.10, 3.11