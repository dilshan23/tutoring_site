from django.contrib import admin

# Register your models here.
from . models import Questions,Student,Answer

admin.site.register(Questions)
admin.site.register(Student)
admin.site.register(Answer)

