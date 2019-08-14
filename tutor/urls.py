from django.contrib import admin
from django.urls import path, include, re_path
from . import views


app_name = "tutor"
urlpatterns = [
    path('',views.index,name = 'index'),

    path('login/',views.login_user,name = 'login_user' ),
    path('register/', views.register,name = 'register'),
    path("logout/",views.logout_user,name = 'logout'),
    #path("allquiz/",views.allquiz,name = 'allquiz'),
    path("quiz/<int:question_id>/getting_answers/",views.getting_answers,name = 'getting_answers'),
    path('quiz/<int:question_id>/',views.quiz , name='quiz'),


    #path('book/<int:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),


    


]
