# Микросервис для отображения статистики

Это приложение предоставляет возможность отслеживать и отображать статистические данные о просмотрах, кликах и затратах.

## Установка и настройка

### Требования
- Python 3.11
- Docker

### Шаги установки
1. Склонируйте репозиторий:
   ```shell
   git clone https://github.com/your-username/microservice-for-displaying-statistics.git

2. Перейдите в директорию проекта:
    ```shel
    cd microservice-for-displaying-statistics
3. Установите зависимости:
    ```shel
    pip install -r requirements.txt
4. Установите зависимости:
    ```shel
    docker-compose up
5. Приложение будет доступно по адресу http://localhost:8000

### Запуск приложения

1. Для запуска приложения выполните команду:
      ```shel
   python mcrservice/manage.py runserver
После запуска, приложение будет доступно по адресу http://localhost:8000/.

API Endpoints
Приложение предоставляет следующие API endpoints:

- GET /statistics/: Возвращает список всех записей статистики.
- POST /statistics/: Создает новую запись статистики. Параметры запроса:
  * date: Дата в формате "YYYY-MM-DD". 
  * views (опционально): Количество просмотров (целое число). 
  * clicks (опционально): Количество кликов (целое число). 
  * GET /statistics/filter_by_date/: Возвращает список записей статистики за указанный период. 
  * Параметры запроса:
    * start_date: Начальная дата в формате "YYYY-MM-DD". 
    * end_date: Конечная дата в формате "YYYY-MM-DD". 
  * DELETE /statistics/delete_all/: Удаляет все записи статистики.   
  
### Примеры запросов
1. GET /statistics/
   ```shel
   http://localhost:8000/statistics/
2. POST /statistics/ 
   ```shel
   http://localhost:8000/statistics/ -d "date=2023-07-20&views=100&clicks=50"
3. GET /statistics/filter_by_date/
   ```shel
   curl http://localhost:8000/statistics/filter_by_date/?start_date=2023-07-01&end_date=2023-07-15
4. DELETE /statistics/delete_all/
   ```shel
   curl -X DELETE http://localhost:8000/statistics/delete_all/

