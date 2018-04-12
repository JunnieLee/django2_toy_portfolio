from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'), # blog/ 뒤에 아무것도 없으면 view.allblogs 적용시키기! (ex) localhost:8000/blog
] 