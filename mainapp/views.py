from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Complaint
from .forms import ComplaintForm


def index(request):
    return render(request, 'mainapp/index.html')

def contact(request):
    return render(request, 'mainapp/contact.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'signup.html', {
                'error': 'All fields are required'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'mainapp/auth/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(username=username,email=email, password=password)
        user.save()
        
        return redirect('login')

    return render(request, 'mainapp/auth/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST.get('next') or 'index'

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, 'mainapp/auth/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'mainapp/auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def file_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('my_complaint')
    else:
        form = ComplaintForm()

    return render(request, 'mainapp/user/file_complaint.html', {'form': form})


@login_required
def my_complaint(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'mainapp/user/my_complaint.html', {'complaints': complaints})


@login_required
def edit_complaint(request, cid):
    complaint = get_object_or_404(Complaint, id=cid, user=request.user)

    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('my_complaint')
    else:
        form = ComplaintForm(instance=complaint)

    return render(request, 'mainapp/user/edit_complaint.html', {'form': form})


@login_required
def delete_complaint(request, cid):
    complaint = get_object_or_404(Complaint, id=cid, user=request.user)
    complaint.delete()
    return redirect('my_complaint')



def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin)
def admin_home(request):
    return render(request, 'mainapp/admin/admin_home.html')


@user_passes_test(is_admin)
def admin_all_firs(request):
    complaints = Complaint.objects.all()
    return render(request, 'mainapp/admin/admin_all_firs.html', {
        'complaints': complaints
    })


@user_passes_test(is_admin)
def update_status(request, cid):
    complaint = get_object_or_404(Complaint, id=cid)

    if request.method == 'POST':
        complaint.status = request.POST['status']
        complaint.save()

    return redirect('admin_all_firs')
