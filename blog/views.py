from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.


def blog(request):
    blog = Blog.objects
    return render(request,"blog.html",{"blogs":blog})

def blog_text(request,blog_id):
    blog_txt = get_object_or_404(Blog,pk = blog_id)
    return render(request,"blog_text.html",{"blog_txts":blog_txt})