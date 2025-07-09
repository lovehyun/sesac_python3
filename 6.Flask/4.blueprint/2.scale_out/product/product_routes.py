from flask import Blueprint, render_template

product_bp = Blueprint('product', __name__, template_folder='../templates/product')

@product_bp.route('/')
def user_page():
    return render_template('product.html')

@product_bp.route('/fruit')
def user_page():
    return render_template('fruit.html')

@product_bp.route('/drink')
def user_page():
    return render_template('drink.html')
