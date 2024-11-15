from flask import Flask, render_template, request, redirect, url_for, session, flash
from api.models.antravision_model import SignUp
from api.services.auth_service import authenticate_user

def init_app(app):
    
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            
            user = authenticate_user(username, password)
            
            if user:
                session['user_id'] = user.id 
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('main'))
            else:
                flash('Usuário ou senha incorretos', 'error')
    
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
    
    @app.route('/perfil')
    def perfil():
        return render_template('perfil.html')
    
