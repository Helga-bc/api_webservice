# api_webservice

#### Компактный веб-сервис, позволяющий работать с авторами и книгами. Сервис предоставляет АПИ для работы с этими сущностями.

#### Сервис доступен онлайн по [ссылке](http://blashko-serviceapi.westeurope.cloudapp.azure.com/api/docs)


### Инструкция по рaзвертыванию

## вариант Docker:
Требования:
- docker
- docker-compose

Действия:
```bash
git clone https://github.com/Helga-bc/api_webservice.git
cd api_webservice
cp docker-compose.yml.sample docker-compose.yml
cp env.sample .env
docker compose build
docker compose up -d
```
Сбросить базу данных:
```bash
docker compose down -v
docker compose up -d
```

   
__Описание методов можно посмотреть по ссылке http://127.0.0.1/api/docs__

__Схема доступна по сслыке http://127.0.0.1/api/schema__

__Админка будет доступна по http://127.0.0.1/admin, пароль и логин указаны в файле .env__

  

## Вариант локально:
Требования:
- python 3.11+
- pip

Действия:
```bash
git clone https://github.com/Helga-bc/api_webservice.git
cd api_webservice
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


__Описание методов можно посмотреть по ссылке http://127.0.0.1:8000/api/docs__

__Схема доступна по сслыке http://127.0.0.1:8000/api/schema__
















