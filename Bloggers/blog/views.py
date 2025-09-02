from django.shortcuts import redirect, render,get_object_or_404,redirect
from .models import Blog
from .forms import Blog_Form,User_registration,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request,'blog_list.html',{'blogs':blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            return redirect(blog_list)
    else:
        form = Blog_Form()
    
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user = request.user)
    if request.method == 'POST':
        form =  Blog_Form(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            return redirect(blog_list)
    else:
        form = Blog_Form(instance=blog)
    return render(request,'blog_form.html',{'form':form})

    
@login_required
def blog_delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user = request.user)
    if request.method == 'POST':
        blog.delete()
        return  redirect(blog_list)
    return render(request,'blog_delete.html',{'blog':blog})

def register(request):
    if request.method == "POST":
        form = User_registration(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.set_password(form.cleaned_data['password1'])
            data.save()
            # Add a success message
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login') 
    else:
        form = User_registration()

    return render(request,'Registration/registration.html',{'form':form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect(blog_list)  
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'Registration/login.html', {'form': form})


def logout_view(request):
    logout(request)

    
    return render(request, 'Registration/logout.html')

