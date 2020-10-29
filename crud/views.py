from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post , UserProfile
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages 
# Create your views here.


def home_view(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Homepage'
    }
    return render(request , "crud/home.html" , context)


@login_required
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


@login_required
def delete_page(request):
    context = {'posts' : Post.objects.all()}
    return render(request , 'crud/delete.html', context)

@login_required
def deletePost(request , id):

    if isinstance(id , int):

        Post.objects.get(id = id).delete()

        return redirect('/')


@login_required
def update(request):
    context = {'posts' : Post.objects.all()}
    return render(request , 'crud/update_page.html', context)

@login_required
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


@login_required
def register_user(request):
    
    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request , f'Account Created For {username}')

    else:
        form = UserRegistrationForm()


    return render(request , 'registration/register.html' , {'form' : form})



def user_blog_view(request , username):
    
    if isinstance(username , str):
        try :
            user = User.objects.get(username = username)
        except:
            user = None 
            return HttpResponse("Cannot find user")

        if user :

            posts = Post.objects.filter(user = user)

            context = {
                'posts' : posts 
            }

            return render(request , 'crud/home.html' , context)

        

    return HttpResponse(username)



@login_required

def profile_page(request):
    context = {}

    if request.user.is_authenticated:
        
        user = User.objects.get(username = request.user.username)
        
        if UserProfile.objects.get(user = user) == None:

            try : 

                newProfile = UserProfile(user = user , bio = "here your bio" )
                newProfile.save()
                profile = UserProfile.objects.get(user = user)

            except:

                return HttpResponse("Cannot Create Profile")

        profile = UserProfile.objects.get(user = user)


        context = { 'user' : user , 'profile' : profile }

        print(profile.image)

    
    return render(request , 'crud/profile.html', context  )