# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import Todo


# def index(req):
#     # todo = Todo.objects.all()
#     data = {'Key':"value"}
#     # return HttpResponse("<h1>Data</h1>", content_type="text/plain")
#     return JsonResponse(data, safe=False)


from rest_framework import generics

from todos import models
from .serializers import TodoSerializer

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer