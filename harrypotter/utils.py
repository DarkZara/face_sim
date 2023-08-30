from deepface import DeepFace
from operator import itemgetter
import deepface
def face_find_match(img):
    try:
        DeepFace.extract_faces(img)
        return True
    except:
        return False
        
def face_find_match(list_of_embeddings,main_embedding):
    results = []
    for ekey in list(list_of_embeddings.keys()):
        embedding = list_of_embeddings[ekey]
        # result = DeepFace.verify(embedding['embedding'], main_embedding,enforce_detection=False)
        result=deepface.commons.distance.findCosineDistance(embedding['embedding'], main_embedding)
        results.append({"value":1 - result,
                 "url":embedding['url'],
                 "name":embedding['name']})
    sorted_results = sorted(results, key=itemgetter('value'),reverse=True) 
    return sorted_results[:3]
    

# import cv2
# import face_recognition
# import os
# import json
# import pickle



# def potter_similar_face_finder(faces,my_face):
#     img_database=[]
#     celebrety_names=[]
#     def load_images_from_folder(faces):
#         for filename in os.listdir(faces):
#             # print(filename)
#             celebrety_names.append(filename)
#             img=face_recognition.load_image_file(faces+filename)
#             if img is not None:
#                 img_database.append(img)
#     load_images_from_folder(faces)
#     # print(len(img_database))
#     encodings_database=[]
#     def encodings(img_database):
#       for i in range(len(img_database)):
#         img_encoder=img_database[i]
#         print(i,face_recognition.face_encodings(img_encoder))
#         if len(face_recognition.face_encodings(img_encoder))>0:
#             encodingss=face_recognition.face_encodings(img_encoder)[0]
#             encodings_database.append(encodingss)
#         # else:
#         #     cv2.imshow(img_encoder)
#         #     encodings_database.append([])

#     if(os.path.isfile('pottermain.pickle')):
#         with open('pottermain.pickle', 'rb') as handle:
#             data = pickle.load(handle)
#         # f = open('enc.json')
#         # data = json.load(f)
#         encodings_database=data['data']
#         # f.close()
#     else:
#         encodings(img_database)
#         with open('pottermain.pickle', 'wb') as handle:
#             pickle.dump({'data':encodings_database}, handle, protocol=pickle.HIGHEST_PROTOCOL)



#     me=face_recognition.load_image_file(my_face)
#     me_encode=face_recognition.face_encodings(me)[0]

#     similarity_data=[]
#     for i in range(len(encodings_database)):
#         a=face_recognition.face_distance([me_encode], encodings_database[i])
#         similarity_data.append(a)

#     most_similar=min(similarity_data)
#     print(1-most_similar)
#     second_most_similar=sorted(similarity_data)
#     index_of_most_similar=similarity_data.index(most_similar)
#     img_rgb = cv2.cvtColor(img_database[index_of_most_similar], cv2.COLOR_BGR2RGB)
#     # img_rgb=img_database[index_of_most_similar]
#     img_rgb=cv2.resize(img_rgb,(400,350))
#     print(celebrety_names[similarity_data.index(second_most_similar[1])]+str(1-second_most_similar[1]),celebrety_names[similarity_data.index(second_most_similar[2])]+str(1-second_most_similar[2]))
#     # celebrety_names=celebrety_names[similarity_data.index(most_similar)]
#     first_three_name=[celebrety_names[similarity_data.index(most_similar)],celebrety_names[similarity_data.index(second_most_similar[1])],celebrety_names[similarity_data.index(second_most_similar[2])]]
#     first_three_percent=[str(1-second_most_similar[0]),str(1-second_most_similar[1]),str(1-second_most_similar[2])]
#     return img_rgb,first_three_name,first_three_percent


# #on device
# # cap = cv2.VideoCapture(0)
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# # while cap.isOpened():
# #     _, img = cap.read()
# #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     facess = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     for (x, y, w, h) in facess:
# #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #         cv2.putText(img, "Press T to see your celebrity", ((x-120)+(x-w),(y-120)+(y-h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 2, cv2.LINE_AA)

# #     cv2.imshow('YOU', img)

# #     if cv2.waitKey(1) & 0xFF == ord('t'):
# #         cv2.imwrite('current.jpg',img)
# #         break
# # my_similar_face,celebrety_name=similar_face_finder('faces','current.jpg')
# # while cap.isOpened():
# #     _, img = cap.read()
# #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     facess = face_cascade.detectMultiScale(gray, 1.1, 4)
# #     for (x, y, w, h) in facess:
# #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #         cv2.putText(img, "Celebrity you look like: ", ((x-120)+(x-w),(y-120)+(y-h)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,255), 2, cv2.LINE_AA)
# #         cv2.putText(img, celebrety_name[:-3], ((x-80) + (x - w), (y-80) + (y - h)), cv2.FONT_HERSHEY_SIMPLEX,
# #                     1, (0, 0, 255), 2, cv2.LINE_AA)
# #     cv2.imshow('YOU', img)
# #     cv2.imshow("SIMILAR", my_similar_face)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# # cap.release()
