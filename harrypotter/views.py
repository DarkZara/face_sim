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
import pickle
from django.http import HttpResponse
from decouple import config
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
    "HP":"hp.pickle"
}

@api_view(('POST',))
def face_match(request,pickle_addres=pickle_addres):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')

    if authorization_header:
        if authorization_header.startswith('Bearer '):
            token = authorization_header.split('Bearer ')[1]
            if not str(token)==str(config('SECRET_KEY')):
                return Response({"status":401,"error":"You are not using this inside the correct application!"})
    if request.method == 'POST':
        coded = request.data["encoded"]

        app = request.data["app"]
        header, data = coded.split(',', 1)
        image_data = base64.b64decode(data)
        np_array = np.frombuffer(image_data, np.uint8)
        face_img = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
        face_embedding=None
        # print("here")
        try:
            face_embedding = DeepFace.represent(face_img, model_name="Facenet", detector_backend="ssd")
        except Exception as e:
             # print("\n",e,"\n")
             return Response({"status":403,"error":"Could not detecet a face from your photo, please try another image with better quality."})
        
        script_dir = os.path.dirname(__file__) 
        rel_path = "data_sets/"+pickle_addres[app]
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'rb') as handle:
            b = pickle.load(handle)
        top3 = face_find_match(b,face_embedding[0]["embedding"])
        return Response({"status":200,
                         "one_name":top3[0]['name'],
                         "one_acc":top3[0]['value'],
                         "one_url":top3[0]['url'],
                         "two_name":top3[1]['name'],
                         "two_acc":top3[1]['value'],
                         "two_url":top3[1]['url'],
                         "three_name":top3[2]['name'],
                         "three_acc":top3[2]['value'],
                         "three_url":top3[2]['url'],})
        #use app to get pickle adds
        #use hash to make sure itcomes from app
        
        # face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)


        
        # (raw_img,names,percentages)=potter_similar_face_finder(POTTER_FOLDER,face_img)
        # pil = Image.fromarray(raw_img)
        # buff=io.BytesIO()
        # pil.save(buff,format='PNG')
        # img_str=base64.b64encode(buff.getvalue())
        # encoded_result = ''+str(img_str)
        # response_data = {}
        # response_data['image'] = encoded_result
        # response_data['main_name'] = names[0]
        # response_data['main_percent'] = percentages[0]
        # response_data['names'] = names
        # response_data['percentages'] = percentages
        # return Response(response_data)
  
