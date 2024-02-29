from django.urls import path

from school.views import StudentList

urlpatterns = [
    path('', StudentList.as_view(), name='students'),
]
