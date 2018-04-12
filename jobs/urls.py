from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('jobs_detail/<pk>/', views.jobs_detail, name='jobs_detail'),

] 