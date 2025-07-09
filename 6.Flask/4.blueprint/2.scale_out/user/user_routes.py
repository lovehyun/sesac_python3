from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='../templates/user')

@user_bp.route('/')
def user_page():
    return render_template('user.html')

@user_bp.route('/profile')
def user_profile_page():
    return render_template('profile.html')
