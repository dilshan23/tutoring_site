
from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from . models import Question,Student,Answer
from django.urls import reverse
from django.views.generic import ListView,DetailView,CreateView
from django.db.models import F

def won():
    Student.objects.update(wins=F('wins') + 1)

def loss():
    Student.objects.update(losses=F('losses') + 1)

def index(request):
	return render(request,'index.html')

def quiz(request,question_id):
    questions = Question.objects.get(id=question_id)
    return render(request,'quiz.html',{'data1' :questions})

def quizlist(request):
    questions = Question.objects.all()
    return render(request,'questions_list.html',{'data1' : questions})

def getting_answers(request,question_id):
    answers = list(Answer.objects.all())
    print (len(answers)+1)
    answer1 = Answer.objects.get(id=question_id)
    print (str(answer1))

    if request.method == 'POST':
         if request.POST['answer'] == str(answer1).lower():
            won()
            print("correct")
            request.session['response'] = "Answer is Right"
            if (question_id + 1 )!= len(answers)+1:
                return redirect(reverse('quiz',args=(question_id+1,)))
            elif (question_id + 1) == len(answers)+1:
                return redirect('/')         
         else:
            loss()
            print("wrong")
            request.session['response'] = "Answer is Wrong"
            return redirect(reverse('quiz',args=(question_id+1,)))           
    else:
        return redirect('/')    

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect("index")
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    print('logout function working')
    return redirect('login_user')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # important replace "index" wtih "tutor.idex" after adding "app_name=tutor" in urls.py
    else:  #^ also example of namespace in templates {% url 'polls:index' %}
        form = UserCreationForm()
    
    
    return render(request, 'register.html', {'form': form})

