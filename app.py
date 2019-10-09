#-*- coding: utf-8 -*
from flask import render_template
from flask import Flask, flash, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = './files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/')
@app.route('/<name>')
def uploaded_file(name=None):
    return "upload success!"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/files/<filename>/',methods=['GET','POST'])
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)


#使用表格提交
@app.route('/WritePoem', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))

            str = "窗前明月光，疑似地上霜，举头望明月，低头思故乡"

            dict = {}
            dict['peom']=str
            dict['code']='1' #1代表没有错误 ，其它代表有错误
            dict['imgUrl']=filename
            dict['keyWord'] = '漂亮龙井'
            str1 = json.dumps(dict,ensure_ascii=False)
            print(str1)
            return str1
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type= text name=index>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/ChangePoem', methods=['GET', 'POST'])
def ChangePoem():
    keyWord = request.args.get('keyWord')
    index = request.args.get('index')
    return "keyWord:"+keyWord +" index:" +index

if __name__ == '__main__':
    app.run(host='0.0.0.0')
