# take picture on phone to website 
# API call to google vision 
# search for food type
# search for calorie count on google
# track macros and micro nutrients
from google.cloud import vision
import os, io
from pathlib import Path
API_key = "my_key"
credential_path = Path(Path.cwd())
credential_path = credential_path.joinpath('Nutrution_App\\Account_Credentials.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(credential_path)





class Detector:
    def detect_labels(self, path):
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        client = vision.ImageAnnotatorClient()
        response = client.label_detection(image=image)
        labels = response.label_annotations
        data = labels[0]
        food_item = data.description
        if response.error.message:
            raise Exception("error")
        return food_item
        
        





if __name__ == "__main__":
    new_object = Detector()
    current_working_directory = Path(Path.cwd())
    path1 = current_working_directory.joinpath('Nutrution_App\\test_hotdog.jpg')
    food_name = new_object.detect_labels(path1)
