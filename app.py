from flask import Flask, render_template, request, jsonify, send_file;
from flask_cors import CORS, cross_origin
import os
from utils import *

app = Flask(__name__);
folder_path = './src/uploads'
processed_path = './src/processed_image'
CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'

@app.after_request
def after_request_func(response):
    schedule_deletion(folder_path)
    schedule_deletion(processed_path)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
    
@app.route("/")
@app.route("/<name>")
def index(name="Ibrahim"):
    return render_template('index.html', name=name)


@app.route("/api/v1/image", methods=['POST'])
# @cross_origin()
def enhance_image():
    if 'file' not in request.files:
        return jsonify({
            'success': False,
            'message': 'No file to upload'
        }), 500
        
    else:
        upload = upload_image(request.files['file'])
        if(upload != False):
            path, name = upload
            isUploaded, file_path, file_name = features(request.form['action'], path, name)
            if(isUploaded):
                return jsonify({
                        'success': True,    
                        'message': 'success',
                        'data': {
                            'path': os.getenv('PROCESSED_URL') + file_name,
                            'name': 'image'
                        }
            })   
            return jsonify({
                'success': False,
                'message': 'Unable to Process update',                
            }), 500

        return jsonify({
                    'success': False,    
                    'message': 'Cannot upload this file type',  
        }), 500     

@app.route("/check")
def check():
    return "<h1>Hello World! Hello Main We are checking</h1>"


@app.route('/processed_image/<filename>')
def serve_image(filename):
    return send_file(f'src/processed_image/{filename}', mimetype='image/png')


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)
    app.run(host='0.0.0.0')

