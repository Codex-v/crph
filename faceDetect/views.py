from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .utils import Util
from .serizailer import imageform
from .models import Imagetable
from time import  sleep

# def save_theimage(req)

def facescan(request):
        result = [0]
        # result = Util.match("9ui","ui")
        if request.method == "POST":
                form = imageform(request.POST,request.FILES)
                data =request.FILES['image']
                Util.handle_uploaded_file(request.FILES['image'])
                total_number_files = Util.count_items_in_folder("D:\\police_facil_recogination\\facialReco\\faceDetect\\media")
                sleep(5)

                for i in range(total_number_files):

                        result = Util.match(request.FILES['image'],f"{i}.jpg")
                        if result[0]:
                                return HttpResponse(f"{i}.jpg")

                        else:
                                return HttpResponse({"match not found!"})
        else:
                params = {"img": f'{s.BASE_DIR}'}
                return render(request, 'login.html',params)
