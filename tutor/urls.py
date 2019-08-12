from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),

    path('login/',views.login_user,name = 'login_user' ),
    path('register/', views.register,name = 'register'),
    path("logout/",views.logout_user,name = 'logout'),
     #path("quiz/",views.quiz,name = 'quiz'),
     path("getting_answers/",views.getting_answers,name = 'getting_answers'),
     path('quiz/<int:id>/',views.quiz , name='question-detail'),


    


]