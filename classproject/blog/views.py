from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone #Django tutorial
from django.shortcuts import render, get_object_or_404 #Django tutorial

# Create your views here.
def index(request):
    sentence = "This is the first django view thing"
    return render(request, "index.html", {"sentence": sentence})
 # render to a specific page/send it to a partucular page

 #This second view I am attempting to create
def c_1(request):
    topic = "This page for Topics"
    return render(request, "topic.html", {"topic": topic})

def show_post(request):
    post = Post.objects.all()
    return render(request, "post_list.html", {"post": post})

def add_post(request):
    blogform = PostForm()
    if request.method == "POST":#if the submit button has been pressed
        blogform = PostForm(request.POST)
        if blogform.is_valid():#Do not need this statement but is good practice
            blogform.save()
            return redirect("show_post")
    return render(request, "post_form.html", {"blogform":blogform})

#create a view to show specific posts
def find_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post})

#creating an update view
def update_post(request, id):
    #Thnis part changes because is is fetching the details fo the single post
    post = get_object_or_404(Post, id=id)
    # Putting the details inside our form
    blogform = PostForm(instance=post)
    if request.method == "POST":# if submit is clicked
        blogform = PostForm(request.POST, instance=post)# Use form details  of the id
        if blogform.is_valid():#Do not need this statement but is good practice
            blogform.save()#save it
            return redirect("show_post")
    return render(request, "post_form.html", {"blogform": blogform})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("show_post")

#From Django tutorial
def post_list(request):
     posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
     #posts = Post.objects.filter(id,__lte=timezone.now()).order_by('created_at')
     #return render(request, 'post_list.html', {'Post': Post})
     return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):#Django tutorial
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})

def post_new(request):
    form = PostForm()
    return render(request,'post_edit.html', {'form': form })
