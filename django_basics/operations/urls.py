# changes by Muhammad Shoaib Sikander

from django.urls import path

from .views import person_info

urlpatterns = [
    path('Person_Info/', person_info, name='person_info'),
    #path('', person_info, name='person_info'),
    #path("Person_Info/<name>", person_info, name="person_info"),
]