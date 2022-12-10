from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {'a':'Saved Sucessfully'}
        return render(request,'contact.html',context)
    else:
        return render(request,'contact.html',{})
def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    return render(request,'trainers.html')
def events(request):
    return render(request,'events.html')
def courses(request):
    return render(request,'courses.html')
def info(request):
    all_members = Member.objects.all
    context = {'all':all_members}
    return render(request,'info.html',context)

