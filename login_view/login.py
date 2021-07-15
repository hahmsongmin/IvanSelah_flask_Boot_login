from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user, logout_user
from login_control.user_control import User
from datetime import datetime

my_login = Blueprint('login', __name__)

@my_login.route('/set_login', methods=['POST'])
def set_login():
    try:
        if request.method == 'POST':
            user = User.find(request.form['user_email'], request.form['user_password'])
            print(request.form['user_email'], request.form['user_password'])
            login_user(user)
            return redirect(url_for('login.mytving'))
    except:
        return render_template('index_A.html')

@my_login.route('/set_join', methods=['POST'])
def set_join():
    user = User.find(request.form['user_email'], request.form['user_password'])
    if user == None:
        print(request.form['user_email'], request.form['user_password'])
        user = User.create(request.form['user_email'], request.form['user_password'])

    login_user(user)
    return render_template('index_A.html')

@my_login.route('/del_logout', methods=['POST'])
def del_logout():
    user = User.find(request.form['user_email'], request.form['user_password'])
    if user == None:
        return render_template('index_del_logout_msg.html', message="일치하는회원정보가없습니다.")
    else:
        User.delete(user.id)
        logout_user()
        return render_template('index_A.html')

@my_login.route('/login')
def login():
    return render_template('index_A.html')

@my_login.route('/join')
def join():
    return render_template('index_join.html')

@my_login.route('/delete')
def delete():
    return render_template('index_del_logout.html')
    


@my_login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.mytving'))

@my_login.route('/mytving')
def mytving():
    if current_user.is_authenticated:
        return render_template('index_B.html', user_email=current_user.user_email)
    else:
        return render_template('index_A.html')

