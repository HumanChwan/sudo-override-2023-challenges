from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from .models import Blog
from .utility import BlogSaveing

# Create your views here.
def home(request):
    # TODO : Server static home page : DONE
    return render(request, 'home.html')

def register(request):
    # TODO : handle Register to default user model : DONE
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'home.html')
    else:
        return redirect('')
    

def login(request):
    # TODO : handle login to default user model
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'home.html')
        else:
            return redirect('')

def logout(request):
    # TODO : handle logout from default user model : DONE :
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('')
    

def create_blog(request):
    # TODO : handle create blog : DONE :
    if not request.user.is_authenticated:
        return redirect('')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user

        saved_blog = BlogSaveing(content)
        saved_blog.save()
        filename = saved_blog.getfilename()
        blog = Blog(title=title, content=filename, author=author)
        blog.save()
        return render(request, 'home.html')
    else:
        return redirect('')

def view_blog(request):
    # TODO : handle view blog : DONE :
    if not request.user.is_authenticated:
        return redirect('')
    user = request.user
    blogs = Blog.objects.filter(author=user)
    return render(request, 'view_blog.html', {'blogs': blogs})

def handle_single_view(request, id):
    # TODO : handle single view : DONE :
    if not request.user.is_authenticated:
        return redirect('')

    blog = Blog.objects.get(id=id)
    if blog.public:
        return render(request, "blogs/" + blog.content)
    elif blog.author == request.user:
        return render(request, "blogs/" + blog.content)
    else:
        return redirect('')