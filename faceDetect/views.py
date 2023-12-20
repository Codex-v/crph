from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .utils import Util




@api_view(["GET"])
def facescan(request):
        


    return Response({"message":"Criminal's face is scaning"}) 
