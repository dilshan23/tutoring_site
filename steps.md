1. update a field in db

#tintin filled a new story

reporter = Reporters.objects.get(name = 'Tintin')
reporter.stories_filed += 1
reporter.save()





2. new project commands  

 django-admin startproject dilowntutor
 cd dilowntutor
 python3 -m venv env
 touch requirements.txt

-->edit requirments.txt

Django==2.2
django-allauth==0.37.1
requests==2.19.1
requests-oauthlib==1.0.0
whitenoise==3.3.1
gunicorn==19.7.1


source env/bin/activate


3. create the main app ,add app name to settings.py 

python3 manage.py startapp tutor




4. in tutor folder create urls.py and add app.urls to main projects urls.py

#new app ---> urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.login_user,name = 'login_user' ),
    path('register/', views.register,name = 'register'),
    
]


# main project ---> urls.py

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tutor.urls')),
]







5. setup register,login and logout

in views.py in main app

see auth.py


#create template folder in app
 and put register.html and login.html

#create index.html
 
def index(request):
	return render(request,'index.html')

6. set up main-app models



# after
makemigrations and migrate



7. create superuser/admin

#edit admin.py

from django.contrib import admin

from . models import Questions

admin.site.Register(Questions)



8. displaying data in index.html

{% if user.is_authenticated %}
      <p>Welcome, {{ user.get_username}}</p>
{% endif %}



9. models.py --> import user--->and other---->use it as a key in models 

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



10. display data and get post requests

 # form 
	<form action = "/" method = "POST">
		{% csrf_token %}
		Enter Answer: <br>
		<input type="text" name="answer">
		<input type="submit" value="Submit">
	</form>

















