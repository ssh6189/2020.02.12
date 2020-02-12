#개발자의 공간
from flask import Flask, render_template, request

app = Flask(__name__)

#오늘은 가능한한, 여기에 html코드가 없게 할것이다.
#브라우저 달나라
#서버 지구
#항상 데이터를 가져오는것은, request 함수이다.
listData = [{"id":0, "img":"puppy.jpg", "title":"강아지"},
            {"id":1, "img":"coffee.jpg", "title":"커피"},
            {"id":2, "img":"beer.jpg", "title":"맥주"}
           ]

@app.route('/')
def index():
    return render_template('home.html', title="my home page")

@app.route('/image')
def image():
#이름은 같더라도, 왼쪽은 템플릿 변수, 오른쪽은 파이썬 객체명이다.
    return render_template('image.html', listData = listData)

'''
@app.route('/image')
def image():
    listData = ["puppy", "coffee", "beer"
    listTitle = ["강아지", "커피", "맥주"]
'''
# /view?id=0
@app.route('/view')   # /view?id=0
def view():   
    id = request.args.get("id")
    return render_template('view.html', s = listData[int(id)] )
    
@app.route('/fileUpload', methods = ['POST'])
def fileUpload():
    f = request.files['file1']
    #여기는 URL폴더가 아니라, 실제 물리적인 폴더의 경로이다.
    f.save("./static/" + f.filename)
    title = request.form.get("title")
    id = len(listData)
    listData.append({"id":id, "img":f.filename, "title":title})
    return f'{f.filename}-제목:{title}, 파일 업로드 성공!<br><img src=/static/{f.filename}>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8890, debug=True)