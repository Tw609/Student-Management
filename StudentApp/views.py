from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == 'i' and password == '1':
            request.session['username']=username
            messages.success(request, 'Login Successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Login Unsuccessfully!')
    return render(request,'login.html')

def dashboard(request):
    if 'username' not in request.session:
        return redirect('login')
    return render(request,'dashboard.html')

def student_list(request):
    students = request.session.get('students', [])
    return render(request, 'student/list.html', {'students': students})

def student_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        students = request.session.get('students', [])
        students.append({'name': name})
        request.session['students'] = students
        messages.success(request, 'Student name has been added successfully!')
        return redirect('student_list')
    return render(request, 'student/add.html')

def student_edit(request, index):
    students = request.session.get('students', [])
    if request.method == "POST":
        name = request.POST.get('name')
        if 0 <= index < len(students):
            students[index]['name'] = name
            request.session['students'] = students
            messages.success(request, 'Student has been edited!')
            return redirect('student_list')
    return render(request, 'student/edit.html', {'student': students[index]})

def student_delete(request, index):
    students = request.session.get('students', [])
    if 0 <= index < len(students):
        students.pop(index)
        request.session['students'] = students
        messages.success(request, 'Student has been deleted!')
        return redirect('student_list')