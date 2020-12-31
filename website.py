from flask import Flask, url_for, render_template, request, redirect
import json
from Vision import Detector
import os
from PIL import Image
from pathlib import Path
from Food import Food

app = Flask(__name__)

@app.route('/')
def base():
	return render_template('upload.html')

@app.route('/Main',  methods = ["POST", "GET"])
def process_image():
    if request.method == 'POST':
        input_image = request.form['camera--output']
        current_working_directory = Path(Path.cwd())
        folder_path = current_working_directory.joinpath('Nutrution_App\\pictures')
        picture_path = folder_path + "\\" + input_image
        img.save("picture_path")
        new_detector = Detector()
        name_food = new_detector.detect_labels(picture_path)
        food_obj = Food(name_food)
        food_obj.start()
        results = sorted(food_obj.nutrition.items())
        return render_template('display.html', result = results)  #, results = results

if __name__ == "__main__":
	app.run(debug=True)
