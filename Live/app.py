from flask import (
    Flask,
    request,
    render_template,
    send_from_directory,
    url_for,
    jsonify 
)
from werkzeug import secure_filename
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
from ssd import getCount    

basedir = os.path.abspath(os.path.dirname(__file__))
updir = os.path.join(basedir, 'upload/')
mem=[]
priority=[]
f=1
app = Flask(__name__)

from logging import Formatter, FileHandler
handler = FileHandler(os.path.join(basedir, 'log.txt'), encoding='utf8')
handler.setFormatter(
    Formatter("[%(asctime)s] %(levelname)-8s %(message)s", "%Y-%m-%d %H:%M:%S")
)
app.logger.addHandler(handler)


app.config['ALLOWED_EXTENSIONS'] = set(['mp4', '3gp'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'js_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/js', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    elif endpoint == 'css_static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     'static/css', filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(app.root_path + '/static/css/', filename)


@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(app.root_path + '/static/js/', filename)

@app.route('/<path:filename>')
def img_statt(filename):
    return send_from_directory(app.root_path + '/', filename)

@app.route('/file/<path:filename>')
def upload_static(filename):
    return send_from_directory(app.root_path + '/upload/', filename)


@app.route('/')
def index():
    global f
    f=1
    return render_template('index.html')

@app.route('/image')
def ima():
    return render_template('image.html')


def FrameCapture(num,path): 
    vidObj = cv2.VideoCapture(path)
    success, image = vidObj.read()
    return getCount(num,image)
    # cv2.imwrite("frame%d.jpg" % num, image)

def calcFront(ar):
    global f
    i = f - 1
    l1 = ar[0][0] + (ar[0][1] * 2) + (ar[0][2] * 3)
    l2 = ar[1][0] + (ar[1][1] * 2) + (ar[1][2] * 3)
    l3 = ar[2][0] + (ar[2][1] * 2) + (ar[2][2] * 3)
    l4 = ar[3][0] + (ar[3][1] * 2) + (ar[3][2] * 3)
    
    print(f)
    if(f%4==1):
        mem.clear()

        q = [l1,l2,l3,l4]
        for x in range(0,4):
            priority.append(0)
        maximum = max(q)
        lane = q.index(maximum)
        mem.append(lane)
        time = maximum * 2.5

        if (time<10):
            time = 10
            rem = 0
        elif (time>60):
            time = 60
            rem = maximum - (60/2.5)
        else:
            rem = 0
        for j in range(0,4):
            priority[j] = priority[j] + 1
        priority[lane] = 0
        print (mem)
        
        # print("Lane chosen : ",(lane+1))
        # print("Count before signal : ",maximum)
        # print("Count after signal : ",rem)
        # print("Timer length : ",time)
        f+=1
        return {"a" : lane+1 , "b" : maximum , "c" : rem , "d" : int(time),"res":ar,"f":int(f)  }
    if((int(f)%4)==2) or ((int(f)%4)==3) or ((int(f)%4)==0):
        q = [l1,l2,l3,l4]
        maximum = -1
        for j in range(0, 4):
            if j in mem:
                continue
            else:
                if q[j]>maximum:
                    maximum = q[j]
                    lane = j
        time = maximum * 2.5
        mem.append(lane)
        if (time<10):
            time = 10
            rem = 0
        elif (time>60):
            time = 60
            rem = maximum - (60/2.5)
        else:
            rem = 0
        for j in range(0,4):
            print(j)
            priority[j] = priority[j] + 1
        priority[lane] = 0
        
        if(i%4 == 3):
            priority[i] = 0

        # print("Lane chosen : ",(lane+1))
        # print("Count before signal : ",maximum)
        # print("Count after signal : ",rem)
        # print("Timer length : ",time)
        f+=1
        return {"a" : lane+1 , "b" : maximum , "c" : rem , "d" : int(time),"res":ar}       




@app.route('/getdata',methods=['POST'])
def getTime():
    global f
    ct=[0,float(request.form['v1']),float(request.form['v2']),float(request.form['v3']),float(request.form['v4'])]
    et=[0,float(request.form['v1e']),float(request.form['v2e']),float(request.form['v3e']),float(request.form['v4e'])]
    # ct=[0,float(request.form['v1'])]
    # et=[0,float(request.form['v1e'])]
    # ffmpeg_extract_subclip(os.path.join(updir,'vid1.mp4'), ct[1], min(ct[1]+0.05,et[1]), targetname=os.path.join(updir,'cut1.mp4'))
    # ffmpeg_extract_subclip(os.path.join(updir,'vid2.mp4'), ct[2], min(ct[2]+0.05,et[2]), targetname=os.path.join(updir,'cut2.mp4'))
    # ffmpeg_extract_subclip(os.path.join(updir,'vid3.mp4'), ct[3], min(ct[3]+0.05,et[3]), targetname=os.path.join(updir,'cut3.mp4'))
    # ffmpeg_extract_subclip(os.path.join(updir,'vid4.mp4'), ct[4], min(ct[4]+0.05,et[4]), targetname=os.path.join(updir,'cut4.mp4'))
    var=[FrameCapture(1,os.path.join(updir,'vid1.mp4')),FrameCapture(2,os.path.join(updir,'vid2.mp4')),FrameCapture(3,os.path.join(updir,'vid3.mp4')),FrameCapture(4,os.path.join(updir,'vid4.mp4'))]
    print(var)
    data = calcFront(var)
    # print(data)
    return jsonify(data=data)

@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        files = request.files['file']
        if files and allowed_file(files.filename):
            filename = request.form['name']+'.'+secure_filename(files.filename).split('.')[-1]
            app.logger.info('FileName: ' + filename)
            updir = os.path.join(basedir, 'upload/')
            files.save(os.path.join(updir, filename))
            file_size = os.path.getsize(os.path.join(updir, filename))
            return jsonify(name=filename, size=file_size)



if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')