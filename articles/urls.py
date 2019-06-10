from django.urls import path
from . import views

urlpatterns = [
    #When adding accessing this page  => http://localhost:8080/articles/articles/  
    path('articles/', views.article_list),
]