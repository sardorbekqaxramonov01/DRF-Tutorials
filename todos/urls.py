# from django.urls import path 
# from .views import *

# urlpatterns = [
#     path("", index, name="index"),
# ]


from django.urls import path

from .views import ListTodo, DetailTodo

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
]
