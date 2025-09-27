from django.shortcuts import render
from .models import Post

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