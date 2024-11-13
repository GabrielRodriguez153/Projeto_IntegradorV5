from flask import render_template, request, url_for, redirect, jsonify

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
    
    @app.route('/perfil')
    def perfil():
        return render_template('perfil.html')
    
    @app.route('/data')
    def data():
        chart_data = {
            "labels": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"],
            "datasets": [{
                "label": "Casos de Antracnose",
                "data": [65, 59, 80, 81, 56, 55],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }
        return jsonify(chart_data)