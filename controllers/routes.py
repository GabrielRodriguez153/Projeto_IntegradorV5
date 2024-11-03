from flask import render_template, request, url_for, redirect

def init_app(app):
    
    @app.route('/')
    def login():
        return render_template('login.html')
    
    @app.route('/signup')
    def signup():
        return render_template('signup.html')
    
    @app.route('/signup2')
    def signup2():
        return render_template('signup2.html')
    
    @app.route('/main')
    def main():
        return render_template('main.html')

    @app.route('/history')
    def history():
        return render_template('history.html')