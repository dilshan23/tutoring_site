from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse # Used to generate URLs by reversing the URL patterns



# Create your models here.



class Question(models.Model):

	

	question = models.CharField(max_length = 225)

	

	category = models.CharField(max_length = 225)

	thumb = models.ImageField(blank = True)

	def __str__(self):
		return self.question

	


	        

class Student(models.Model):

	user = models.OneToOneField(User,on_delete = models.CASCADE)

	wins = models.IntegerField(default = 0,null = True,blank = True)

	losses = models.IntegerField(default = 0,null = True,blank = True)



	def __str__(self):
		return str(self.user)



class Answer(models.Model):

	question = models.ForeignKey(Question,on_delete = models.CASCADE)

	answer = models.CharField(blank = False,max_length = 225)


	def __str__(self):
		return str(self.answer)



class Teacher(models.Model):

	name = models.CharField(max_length = 225)

	def __str__(self):
		return str(self.name)

        


	





