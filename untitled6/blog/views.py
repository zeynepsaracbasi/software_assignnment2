from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def show_blog(request):
    if request.method == "POST":
        Blog.objects.create(name=request.POST.get("blog_name"),
                            description=request.POST.get("blog_description"))

    return render(request, "my_blogs.html", {"my_blogs": Blog.objects.all()})


def get_blog(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        return render(request, "detailed_blogs.html",{"blog": blog} )
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")