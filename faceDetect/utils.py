import face_recognition
import os


i = 0


def handle_uploaded_file(f):
    global i
    with open('D:\\police_facil_recogination\\facialReco\\faceDetect\\upload\\' + f.name + '.jpg',
              'wb+') as destination:
        # rest of your code

        for chunk in f.chunks():
            destination.write(chunk)

class Util:

    @staticmethod
    def handle_uploaded_file(f):
        global i
        with open('D:\\police_facil_recogination\\facialReco\\faceDetect\\upload\\'+f.name, 'wb+') as destination:
            # rest of your code

            for chunk in f.chunks():                destination.write(chunk)
    @staticmethod
    def match(fromImag,toimage):
        # handle_uploaded_file(f)
        picture_of_me = face_recognition.load_image_file(f"D:\\police_facil_recogination\\facialReco\\faceDetect\\upload\\{fromImag}")
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

        unknown_picture = face_recognition.load_image_file(f"D:\\police_facil_recogination\\facialReco\\faceDetect\\media\\{toimage}")
        unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        return results




    @staticmethod
    def count_items_in_folder(folder_path):
        try:
            # List all items (files and folders) in the specified folder
            items = os.listdir(folder_path)

            # Count the total number of items
            total_items = len(items)

            return total_items

        except FileNotFoundError:
            print(f"The folder at {folder_path} does not exist.")
            return None



