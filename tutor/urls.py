from django.contrib import admin
from django.urls import path, include, re_path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#app_name = "tutor"
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.login_user,name = 'login_user' ),
    path('register/', views.register,name = 'register'),
    path("logout/",views.logout_user,name = 'logout'),
    #path("allquiz/",views.allquiz,name = 'allquiz'),
    path("quizlist/",views.quizlist,name = 'quizlist'),
    path("quiz/<int:question_id>/getting_answers/",views.getting_answers,name = 'getting_answers'),
    path('quiz/<int:question_id>/',views.quiz , name='quiz'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
