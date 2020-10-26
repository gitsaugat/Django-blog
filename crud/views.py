from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User 
# Create your views here.


def home_view(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Homepage'
    }
    return render(request , "crud/home.html" , context)



def create_post(request):

    context = {}

    if request.method == "POST":

        title = request.POST["title"]
        content = request.POST["content"]

        if request.user.is_authenticated:
            newPost = Post(title = title , content = content , user = request.user)
            newPost.save()

            return redirect('/')
        return redirect('/')

    return render(request , "crud/create.html" , context)



def delete_page(request):
    context = {'posts' : Post.objects.all()}
    return render(request , 'crud/delete.html', context)


def deletePost(request , id):

    if isinstance(id , int):

        Post.objects.get(id = id).delete()

        return redirect('/')



def update(request):
    context = {'posts' : Post.objects.all()}
    return render(request , 'crud/update_page.html', context)


def update_post(request , id):

    
    context  = {'post'  : Post.objects.get(id = id)}

    if isinstance(id , int):

        if request.method == "POST":

            post = Post.objects.get(id = id)

            post.title = request.POST["title"]
            post.content = request.POST["content"]

            post.save()

            return redirect('/')

            
    return render(request , 'crud/update.html' , context)
