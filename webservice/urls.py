"""
URL configuration for webservice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls))
    
    
    
    
    
    # path("api/authors/", AuthorViewSet.as_view(), name ='authors'),

    # path('api/authors/all/<uuid:author_id>/', get_author),
    
    # # create_author
    # # path('api/authors/all/<uuid:author_id>/', get_author), # get author by id
    # path('api/authors/all/', get_authors), #get all authors
    # path('api/authors/all/<uuid:author_id>/', update_author), 
    # path('api/authors/all/<uuid:author_id>/', delete_author),
    # path('api/authors/all/<str>/', search_authors),
    
    

    
    
    
    
    
    # должен быть ЮЗЕР???
    # добавить автора с валидацие автора
    # получить всех авторов
    # получить инфу о конкретном авторе
    # поиск автора по критериям
    # изменить информацию об авторе по его идентификатору...  Сервис сообщит пользователю, в чём именно его ошибка, при вводе некорректных данных.
    # удалить автора по идентификатору
    # удалить всех авторов
    # добавить книгу с валидацией?
    # получить инфу обо всех книгах
    # получить инфу о конкретной книге по идентификатору
    # поиск книги по критериям
    # изменить инфу о книге по ее идетнификатору ... Сервис сообщит пользователю, в чём именно его ошибка, при вводе некорректных данных.
    # удалить книгу по ее идентификатору
    # удалить все книги
    
    # 
    # 
    # 
    # 
]
