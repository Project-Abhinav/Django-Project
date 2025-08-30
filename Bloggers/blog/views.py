from django.shortcuts import redirect, render,get_object_or_404,redirect
from .models import Blog
from .forms import Blog_Form

# Create your views here.


def index(request):
    return render(request,'index.html')


def blog_list(request):
    blogs = Blog.objects.all().order_by('created_at')
    return render(request,'blog_list.html',{'blogs':blogs})

def blog_Create(request):
    if request.method == 'POST':
        form = Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            form.save()
            redirect(blog_list)
    else:
        form = Blog_Form()
    
    return render(request,'blog_form.html',{'form':form})

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

    

def blog_delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user = request.user)
    if request.method == 'POST':
        blog.delete()
        return  redirect(blog_list)
    return render(request,'blog_delete.html',{'blog':blog})

