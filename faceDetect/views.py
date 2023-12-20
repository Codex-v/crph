from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .utils import Util
from .serizailer import imageform
from .models import Imagetable
from time import  sleep
from django.conf import settings as s
from django.views.decorators.csrf import csrf_exempt
import os

# def save_theimage(req)
@csrf_exempt
def facescan(request):
        result = [0]
        # result = Util.match("9ui","ui")
        if request.method == "POST":
                form = imageform(request.POST,request.FILES)
                data =request.FILES['image']
                Util.handle_uploaded_file(request.FILES['image'])
                # total_number_files = Util.count_items_in_folder(f'{s.BASE_DIR}\\faceDetect\\media')
                # print(total_number_files)
                media_directory = f'{s.BASE_DIR}\\faceDetect\\media'
                files_in_media = os.listdir(media_directory)
                # sleep(5)

                # for i in range(total_number_files):
                #         result = Util.match(request.FILES['image'],f"{i}.jpg")
                #         if result[0]:
                #                 return HttpResponse(f"{i}.jpg")

                #         else:
                #                 return HttpResponse({"match not found!"})
                for file_name in files_in_media:
                    result = Util.match(request.FILES['image'], file_name)
                    if result[0]:
                        return HttpResponse(file_name)
                    else:
                        return HttpResponse({"match not found!"})
        else:
                params = {"img": f'{s.BASE_DIR}'}
                return render(request, 'form.html',params)
