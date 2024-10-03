from flask import render_template, request, url_for, redirect

def init_app(app):
    
    @app.route('/')
    def login():
        return render_template('login.html')
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')