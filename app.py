from flask import Flask, request,render_template, url_for
import os

from model_actions import predict_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'static/uploads'

@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        
        if 'image' not in request.files:
            return render_template('index.html', txt = 'No file part', image_path = '', rslt = '')
        image = request.files['image']
        if image.filename == '':
            return render_template('index.html', txt = 'No selected file', image_path = '',rslt = '')
        
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok = True)
        path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(path)

        img_url = url_for('static', filename = 'uploads/' + image.filename)

        return render_template('index.html', txt = 'File successfully uploaded', image_path = img_url, rslt = predict_image(path))

    return render_template('index.html', txt = 'No data Recieved',image_path = '', rslt = '')

if __name__ == '__main__':
    app.run(debug = True)
