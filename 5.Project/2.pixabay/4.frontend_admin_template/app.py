from flask import Flask, jsonify, redirect, url_for, render_template, request
import os

app = Flask(__name__)

# 글로벌 변수
images = [
    {"filename":"cat1.jpg", "keywords": ["cat", "animal", "cute"]},
    {"filename":"cat2.jpg", "keywords": ["cat", "pet", "cute"]},
    {"filename":"cat3.jpg", "keywords": ["cat", "kitty", "cute"]},
    {"filename":"dog1.jpg", "keywords": ["dog", "pet", "park"]},
    {"filename":"panda1.jpg", "keywords": ["panda", "zoo", "bear"]}
]

@app.route('/')
def index():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        # pythonic하게 한줄로...
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    
    return render_template("index.html", query=query, results=results)

@app.route('/admin')
def admin():
    return render_template("admin.html", images=images)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('image')
    keywords = request.form.get('keywords')
    print(keywords)
    
    if file:
        filename = file.filename
        filepath = os.path.join('static', 'img', filename)
        file.save(filepath)
        images.append({'filename': filename, "keywords": keywords.lower().split(',')})
    
    return redirect(url_for('admin'))

@app.route('/update/<filename>', methods=['POST'])
def update_keywords(filename):
    new_keywords = request.form.get('keywords')
    for i in images:
        if i["filename"] == filename:
            i["keywords"] = [word.strip() for word in new_keywords.lower().split(',') if len(word.strip())]
            break
        
    return redirect(url_for('admin'))

@app.route('/delete/<filename>')
def delete_image(filename):
    print('삭제할파일: ', filename)
    global images   # 우리의 글로벌 변수를 읽어갈때는 문제가 없음. 단, 수정할꺼면 global로 설정해줘야지만, 해당 변수안의 내용을 수정할 수 있음.
    
    # 삭제할거 빼고 나머지를 다시 채움
    images = [
        img 
        for img in images 
        if img["filename"] != filename
    ]
    
    # 실제로 이미지를 지울거면??
    filepath = os.path.join('static', 'img', filename)
    if os.path.exists(filepath):
        # os.remove(filepath)
        print(f'{filepath} 지웠다고 치자...')
    
    return redirect(url_for('admin'))

if __name__ == "__main__":
    app.run(debug=True)
    