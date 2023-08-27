from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from django.shortcuts import render
from .utils import *
# Create your views here.
import base64
import cv2
from PIL import Image
import io
import base64
import numpy as np
import os
current_path = os.path.dirname(__file__)
# image_folder = os.path.join(current_path, images)
POTTER_FOLDER =  os.path.join(current_path, 'potterfaces/')

@api_view(('POST',))
def Potter_face_match(request):
    return
    # if request.method == 'POST':
    #     coded = request.data["encoded"]
    #     decod=base64.b64decode(coded)
    #     np_data=np.fromstring(decod,np.uint8)
    #     face_img=cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    #     # face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)


        
    #     (raw_img,names,percentages)=potter_similar_face_finder(POTTER_FOLDER,face_img)
    #     pil = Image.fromarray(raw_img)
    #     buff=io.BytesIO()
    #     pil.save(buff,format='PNG')
    #     img_str=base64.b64encode(buff.getvalue())
    #     encoded_result = ''+str(img_str)
    #     response_data = {}
    #     response_data['image'] = encoded_result
    #     response_data['main_name'] = names[0]
    #     response_data['main_percent'] = percentages[0]
    #     response_data['names'] = names
    #     response_data['percentages'] = percentages
    #     return Response(response_data)
  
pickle_addres={
    "HP":""
}

@api_view(('POST',))
def face_match(request):
    if request.method == 'POST':
        coded = request.data["encoded"]
        hash = request.data["hash"]
        app = request.data["app"]
        decod=base64.b64decode(coded)
        np_data=np.fromstring(decod,np.uint8)
        face_img=cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)

        #use app to get pickle adds
        #use hash to make sure itcomes from app
        
        # face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)


        
        (raw_img,names,percentages)=potter_similar_face_finder(POTTER_FOLDER,face_img)
        pil = Image.fromarray(raw_img)
        buff=io.BytesIO()
        pil.save(buff,format='PNG')
        img_str=base64.b64encode(buff.getvalue())
        encoded_result = ''+str(img_str)
        response_data = {}
        response_data['image'] = encoded_result
        response_data['main_name'] = names[0]
        response_data['main_percent'] = percentages[0]
        response_data['names'] = names
        response_data['percentages'] = percentages
        return Response(response_data)
  
