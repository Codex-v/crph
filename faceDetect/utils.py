import face_recognition
import os
from django.conf import settings as s


i = 0


def handle_uploaded_file(f):
    global i
    with open(f'{s.BASE_DIR}\\faceDetect\\upload\\{f.name}.jpg',
              'wb+') as destination:
        # rest of your code

        for chunk in f.chunks():
            destination.write(chunk)

class Util:

    @staticmethod
    def handle_uploaded_file(f):
        global i
        with open(f'{s.BASE_DIR}\\faceDetect\\upload\\{f.name}', 'wb+') as destination:

            for chunk in f.chunks():
                destination.write(chunk)
    @staticmethod
    def match(fromImag,toimage):
        print("this is from image ",fromImag)
        print("this is to image ",toimage)
        items = os.listdir(f"{s.BASE_DIR}\\faceDetect\\upload")
        total_items = len(items)
        print(f"Total items are {total_items}")
        # for i in range(total_items):
        picture_of_me = face_recognition.load_image_file(f"{s.BASE_DIR}\\faceDetect\\upload\\{fromImag}")
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        unknown_picture = face_recognition.load_image_file(f"{s.BASE_DIR}\\faceDetect\\media\\{i}.jpg")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        
        return results
        
    # @staticmethod
    # def match(fromImag, toimage):
    #     try:
    #         # Load the images
    #         picture_of_me = face_recognition.load_image_file(f"{s.BASE_DIR}\\faceDetect\\upload\\{fromImag}")
    #         unknown_picture = face_recognition.load_image_file(f"{s.BASE_DIR}\\faceDetect\\media\\{toimage}")

    #         # Get face encodings if faces are detected in both images
    #         my_face_encodings = face_recognition.face_encodings(picture_of_me)
    #         unknown_face_encodings = face_recognition.face_encodings(unknown_picture)

    #         if len(my_face_encodings) > 0 and len(unknown_face_encodings) > 0:
    #             my_face_encoding = my_face_encodings[0]
    #             unknown_face_encoding = unknown_face_encodings[0]

    #             # Compare face encodings
    #             results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
    #             return results
    #         else:
    #             # Handle case where no face is detected in one or both images
    #             return [False]

    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return [False]




    @staticmethod
    def count_items_in_folder(folder_path):
        try:
            # List all items (files and folders) in the specified folder
            items = os.listdir(folder_path)

            # Count the total number of items
            total_items = len(items)
            print(f"Total items are {total_items}")
            return total_items

        except FileNotFoundError:
            print(f"The folder at {folder_path} does not exist.")
            return None



