from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions,user
from django.core.paginator import Paginator
from .forms import UserForm 
lst = []
answers = Questions.objects.all()
anslist = []
for i in answers:
    anslist.append(i.answer)
def index(request):
    obj = Questions.objects.all()
    count = Questions.objects.all().count()
    paginator = Paginator(obj,1)
    try:
       page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    context = {
        'obj':obj,
        'questions':questions,
        'count':count
    }
    return render(request,'index.html',context)
def result(request):
    Question = Questions.objects.all()
    score =0
    for i in range(0,len(lst)):
        if lst[i]==anslist[i]:
            score +=1

    
    context = {
        'Question':Question,
        'score':score,
        'lst':lst,
        }
    return render(request,'result.html',context)
def save_ans(request):
    
    ans = request.GET['ans']
    lst.append(ans)

def welcome(request):
    users = user.objects.all()
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'users':users,
        'form':form
    }
    
    return render(request,'welcome.html',context)