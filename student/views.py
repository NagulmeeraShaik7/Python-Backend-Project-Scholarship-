from django.shortcuts import render,redirect

from .models import Student
from .forms import StudentForm

# Create your views here.

def student_list(request):
    context ={'student_list':Student.objects.all()}

    return render(request,'student/list.html',context)

def student_form(request,id=0):
    if request.method=='GET':
        if id==0:

            form =StudentForm()
            return render(request,'student/form.html',{'form':form})
        else:
            s1 =Student.objects.get(pk=id)

            form =StudentForm(instance=s1 )
            return render(request,'student/form.html',{'form':form})


    else:
        if id==0:
            form =StudentForm(request.POST)
        else:
            s1 =Student.objects.get(pk=id)
            form =StudentForm(request.POST,instance=s1)
        
        if form.is_valid():
                form.save()
        return redirect('/tggov/studentlist/')




def student_delete(request,id):
    s2 =Student.objects.get(pk=id)
    s2.delete()
    return redirect('/tggov/studentlist/')



