from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name': 'MyName', 'id': 'user', 'pw': 'password'}
]

items = [
    {'id': 'prod-001', 'name': '사과', 'price': 1000},
    {'id': 'prod-002', 'name': '딸기', 'price': 2000},
    {'id': 'prod-003', 'name': '바나나', 'price': 3000},
]

@app.route('/cart')
def view_cart():
    user = session.get('user')
    if not user:
        return render_template("cart.html", user=None, items=items, error="로그인 후 사용할 수 있습니다.")
    
    cart = session.get("cart", {}) # 카트가 없으면 {} 빈 dict를 반환하겠다.
    
    cart_items = []
    for item_id, item_qty in cart.items():
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            a_item = item.copy()
            a_item["qty"] = item_qty
            cart_items.append(a_item)
    
    return render_template("cart.html", user=user, cart=cart_items)

@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user, items=items)

@app.route('/add_to_cart', methods=["POST"])
def add_to_cart():
    user = session.get('user')
    if not user:
        return render_template("product.html", user=None, items=items, error="로그인 후 사용할 수 있습니다.")
    
    item_id = request.form.get('item_id')
    print("담기요청한 상품코드: ", item_id)
    
    if "cart" not in session:
        # session["cart"] = []  # prod-001, prod-002, prod-001, prod-001
        session["cart"] = {}  # key, value  {"prod-001": 1}
        
    cart = session["cart"] # 빈 카트를 가져오거나, 이전에 담은 카드...
    
    if item_id in cart:  # 이전에 내 카트에 이 상품이 있어??
        cart[item_id] += 1
    else:
        cart[item_id] = 1
        
    session["cart"] = cart
    
    return render_template("product.html", user=user, items=items, message=f"{item_id} 가 담겼습니다.")

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))  # 어디로 보낼지, 뭐라고 출력할지, 내맘임..

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_submit():
    input_id = request.form.get('id')
    input_pw = request.form.get('password')
    
    user = next((u for u in users if u['id'] == input_id and u['pw'] == input_pw), None)
    if user: # 성공
        session['user'] = user  # 사용자 정보를 모두다 저장함.
        return redirect(url_for("user"))
    else: # 실패
        return render_template('login.html', error="ID 또는 비밀번호가 올바르지 않습니다.")

@app.route('/logout')
def logout():
    session.pop('user', None)  # user가 없으면 KeyError 가 날 수 있음.. 그래서 없을때 None 반환..
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
