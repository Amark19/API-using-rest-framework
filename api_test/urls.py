
from django.urls import path
from . import views

urlpatterns = [
    path('',views.studentList.as_view()),
    path("fetchData/",views.studentData),
]