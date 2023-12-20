# import face_recognition



# class Util:
#     @staticmethod
#     def match(fromImag,toimage):
#         picture_of_me = face_recognition.load_image_file(f"{fromImag}.jpg")
#         my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

#         unknown_picture = face_recognition.load_image_file(f"{toimage}.jpg")
#         unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
#         results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

#         if results[0] == True:
#             print("It's a picture of me!")
#         else:
            # print("It's not a picture of me!")


