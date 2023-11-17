Тестовый проект:
"web-приложение для определения заполнения формы"

Реализован API в котором можно создавать шаблоны форм,
которым можно задать тип поля:
-email
-phone
-date
-text
В зависимости от типа поля проводиться валидация.

GET-запрос: """http://localhost:8000/api/formlist/""" -
масив шаблонов форм

GET-запрос: """http://localhost:8000/api/form/""" - 
масив созданных полей в котором храниться название поля,
значения поля и тип поля.

POST-запрос: """http://localhost:8000/api/get_form/""" - 
тело запроса: 
"""
{
'name_fild_1': 'value_1',
'name_fild_2': 'value_2',
}
"""
Передовать можно не ограниченное количество параметров, 
есои есть шаблон с такими названиеми полей и значениями то праграмма
вернет Имя шаблона, если шаблона такого нет, то вернет 
имя поля и тип его значения.

Перед сборкой проекта нужно создать .env фаил в корне проекта
директория validate_form, рядом с manage.py

Сьорка проекта:
"""docker-compose build"""
Запуск проекта:
"""docker-compose up"""

Загрузка фикстур:
"""docker exec -it id-контейнера(validate_form_web) python manage.py loaddata app/fixtures/001_form_temlate.json app/fixtures/002_form_data.json"""


Писал проект на Linux по этом с запуском проекта на Windows могутбыть
проблемы (с кадировкрой файлов)

Для теста можно выполнить скрип '''test.py''', для работы теста 
необходимо установить в окружение библиотеку '''requests'''