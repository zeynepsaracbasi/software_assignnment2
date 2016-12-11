from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required



def signup(request):

    if request.method == "POST":
        User.objects.create_user(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        return HttpResponse("Success!")

    return render(request, "register.html")


