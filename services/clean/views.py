from django.shortcuts import render,redirect
from clean.forms import EmpForm
from clean.models import Student
# Create your views here.

def index(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmpForm()
    return render(request,'index.html',{'gaurav':form})


def show(request):
    employees = Student.objects.all()
    return render(request,"show.html",{'gaurav':employees})



    # stu = EmpForm()  #object
    # return render(request,'index.html',{'gaurav':stu}) #dictonary key



# get is insecure post is used to transfer tge data