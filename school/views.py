from django.views.generic import ListView


from .models import Student


class StudentList(ListView):
    model = Student
    template_name = 'school/students_list.html'
    ordering = 'group'
