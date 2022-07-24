from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q
from django.db import connection

# def student_list(request):
#     posts = Student.objects.filter(classroom=4) & Student.objects.filter(first_name__startswith='Shikanda')

#     return render(request, 'index.html', {'posts': posts})


# def student_list_(request):
#     posts = Student.objects.filter(Q(classroom=4) & Q(first_name__startswith='Shikanda'))

#     return render(request, 'index.html', {'posts': posts})


# def student_list_(request):
#     posts = Student.objects.all().values("first_name").union(
#         Teacher.objects.all().values_list('first_name'))
#     print(posts)
#     print(posts.query)
#     print(connection.queries)

#     return render(request, 'index.html', {'posts': posts})

# def student_list_(request):
#     posts = Student.objects.exclude(age=23) & Student.objects.exclude(first_name__startswith='Thomas')

    

#     print(posts)
#     print(posts.query)
#     print(connection.queries)

#     return render(request, 'index.html', {'posts': posts})


# def student_list_(request):
#     posts = Student.objects.filter(Q(age__gt=21) & Q(first_name__startswith='Thomas'))
    

#     print(posts)
#     print(posts.query)
#     print(connection.queries)

#     return render(request, 'index.html', {'posts': posts})


# def student_list(request):
#     posts = Student.objects.raw("SELECT * FROM student_student where age > 20 ")
    
#     print(posts)
#     print(posts.query)
#     print(connection.queries)

#     return render(request, 'index.html', {'posts': posts})



def student_list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student_student")
    r = cursor.fetchone()

    print(r)

    return render(request, 'index.html', {'posts': r})