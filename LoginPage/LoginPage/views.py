from django.shortcuts import redirect,render
from Register.models import Student

def Index(request):
    stud = Student.objects.all()

    context ={
        'stud':stud,
    }
    return render (request,'index.html',context)

def ADD(request):
    if request.method == 'POST':
        name = request.post.get('name')

       # email = request.post.get('email')
       # address = request.post.get('address')
       # phone = request.post.get('phone')

    stud = Student(
           name = name
       )
    stud.save()
    
    return redirect('home')

def Edit(request):
    stud = Student.objects.all()

    context = {
            'stud':stud,

    }
    return redirect(request,'index.html',context)

def Update(request,id):
    if request.method =='POST':
        name =request.post.get('name')

        stud = Student(
            id = id,
            name = name,
        )
        stud.save()

    return redirect('home')

    return redirect(request,'index.html')

def Delete(request,id):
    stud = Student.objects.filter(id= id)
    stud.delete()
    
    context = {
        'stud':stud,
    }
    return redirect('home')
    return redirect(request,'index.html',context)

