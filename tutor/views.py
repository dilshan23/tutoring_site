from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages
from . models import Question,Student,Answer


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


"""

class allquiz(ListView):
    model = Question
"""

def getting_answers(request,question_id):

    answer1 = Answer.objects.get(id=question_id)
    print (str(answer1))

    if request.method == 'POST':
         if request.POST['answer'] == str(answer1):
            won()
            print("correct")
            request.session['response'] = "You win"
            return redirect('/')
         else:
            loss()
            print("wrong")
            request.session['response'] = "You lost"
            return redirect('/')
            


    else:
        return redirect('/')



	#answer1 = Answer.objects.get(pk = pk)

    

	
	
	
   	 
			



			







	


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
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
