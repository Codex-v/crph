from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FacedetectUser
from django.conf import settings as s
import os
from django.views.decorators.csrf import csrf_protect



@csrf_protect
def login(request):
    if request.method == 'POST':  
        if((FacedetectUser.objects.filter(email=request.POST['email']).exists())):
                user = FacedetectUser.objects.filter(email=request.POST['email'])[0]
                if ((request.POST['password']== user.password)):
                    request.session['id'] = user.id
                    request.session['name'] = user.first_name
                    request.session['surname'] = user.last_name
                    messages.add_message(request,messages.INFO,'Welcome to criminal detection system '+ user.first_name+' '+user.last_name)
                    return redirect("/dashboard")
                else:
                    messages.error(request, 'Oops, Wrong password, please try a diffrerent one')
                    return HttpResponse({"message": "WRONG PASSWORD"})
        else:
                messages.error(request, 'Oops, That police ID do not exist')
                return HttpResponse({"message": "DOESNT EXIST"})
    else:
        params = {"img": f'{s.BASE_DIR}'}
        return render(request, 'login.html',params)


