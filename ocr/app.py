# import os

# import cv2
# import numpy as np
from flask import Flask, jsonify, request

# from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = 'D:/learn/py/project-akhir-backend/ocr/uploads' # direktori untuk menyimpan file yang diupload
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# mengecek apakah file yang diupload memiliki ekstensi yang diperbolehkan
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1) [1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to OCR API, send some image in post request with file as the key to Localhost/media/uploads'

@app.route('/media/upload', methods=['POST'])
def upload_media():
    data = request.get_json()
    token = data['token']

    if token != '#@<!3c8e_237bc+v)ps;*&er':
        return jsonify({'error': 'unauthorized'}), 401
    if 'image' not in request.files:
        return jsonify({'error': 'media not provided'}), 400
    file= request.files['image']
    if file.filename == '':
        return jsonify({'error': 'no file selected'}), 400
    if file and allowed_file(file.filename):
        # TODO: get image as variable in cv2
        img = request.files['image'].stream
        # img = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_COLOR)
        return jsonify({'msg':'success'}),200



        # filename = secure_filename (file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # TODO: use file as the image that we will process, like pre processing, ocr, recog, etcetera
    return jsonify({ 'msg': f'media uploaded successfully{file.filename}'})

if __name__ == '__main__':
    app.run(debug=True)