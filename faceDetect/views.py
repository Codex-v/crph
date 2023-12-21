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
        if request.method == "POST":
                form = imageform(request.POST,request.FILES)
                data =request.FILES['image']
                image_name = Util.handle_uploaded_file(request.FILES['image'])
                total_number_files = Util.count_items_in_folder(f'{s.BASE_DIR}\\faceDetect\\media')
                print(total_number_files)
                media_directory = f'{s.BASE_DIR}\\faceDetect\\media'
                result = Util.compare_faces_with_uploaded_image(image_name)
                print(result)

                if result[1]:
                    binary_data = Util.imagetoBinary(f'{s.BASE_DIR}\\faceDetect\\media\\{result[0]}')
                    response = HttpResponse(binary_data, content_type='image/jpeg')
                    response['Content-Disposition'] = 'attachment; filename="image.jpg"'
                    print(response)
                    return response
                else:
                    return HttpResponse({"match not found!"})
        else:
                params = {"img": f'{s.BASE_DIR}'}
                return render(request, 'form.html',params)
