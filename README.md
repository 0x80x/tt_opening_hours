## Описание проекта

Проект представляет собой реализацию API для форматирования рабочего времени ресторана в удобочитаемый текстовый формат. Входные данные предоставляются в формате JSON, а вывод представляет собой отформатированную строку с часами работы для каждого дня недели.

## Используемые технологии

- Python 3.10
- FastAPI
- Pydantic
- Uvicorn
- Docker

## Документация

После запуска документация будет доступна по ссылке [http://localhost:8000/docs](http://localhost:8000/docs)

## Порядок запуска

### Локальный запуск

1. Установите зависимости, перечисленные в файле `requirements.txt`, используя следующую команду:

   ```shell
   pip3 install -r requirements.txt
   ```

2. Запустите приложение с помощью команды:

   ```shell
   python3 main.py
   ```

3. Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

### Запуск с использованием Docker

1. Убедитесь, что у вас установлен Docker на вашей машине.

2. Соберите Docker-образ, выполнив следующую команду в корневой директории проекта:

   ```shell
   docker-compose build
   ```

3. Запустите контейнер с помощью команды:

   ```shell
   docker-compose up
   ```

4. Приложение будет доступно по адресу [http://localhost:8000](http://localhost:8000).

Теперь вы можете использовать API для отправки запросов на `/opening-hours` и получения отформатированного текста с рабочим временем ресторана.