from flask import render_template, request, redirect, url_for, flash, session, jsonify
from bson import ObjectId
from Api.services.antravision_services import SignUpService, DadosService


def init_app(app):
    
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))    
    
    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['password']
            
            user = SignUpService.validate_login(email, senha)
            if user:
                session['user_id'] = str(user['_id']) 
                session['user_name'] = user.get('nome')
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for('main'))
            else:
                flash("Email ou senha incorretos.", "danger")

        return render_template('login.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            personal_data = {
                'nome' : request.form['nome'],
                'telefone': request.form['telefone'],
                'email' : request.form['email'],
                'senha' : request.form['password'],
            }
            try:
                user = SignUpService.add_user(personal_data)
                session['user_id'] = str(user['_id'])
                session['user_name'] = user.get('nome')
                flash("Dados Pessoais Adicionados! Avançe para Cadastrar", "success")
                return redirect(url_for('signup2'))
            except Exception:
                flash(f"Erro ao salvar os dados!", "danger")
                return redirect(url_for('signup'))
        return render_template('signup.html')
    
    
    @app.route('/signup2', methods=['GET', 'POST'])
    def signup2():
        if request.method == 'POST':
            location_data = {
                'endereco': {
                'logradouro': request.form['logradouro'],
                'cidade' : request.form['cidade'],
                'estado': request.form['estado'],
                'cep': request.form['cep']
                }
            }
            try:
                user_id = session.get('user_id')
                if not user_id:
                    flash("Erro: Código do Usuário não Encontrado!", "danger")
                    return redirect(url_for('signup'))
                updated_user = SignUpService.update_user(user_id, location_data)
                flash("Cadastro realizado com Sucesso!", "success")
                return redirect(url_for('main'))
            except Exception:
                flash(f"Erro ao cadastrar!", "danger")
                return redirect(url_for('signup2'))
        return render_template('signup2.html')
    
    @app.route('/main')
    def main():
        user_name = session.get('user_name', 'Usuário')
        return render_template('main.html', user_name=user_name)
    

    @app.route('/history', methods=['GET'])
    def history():
        
        data_inicial = request.args.get('startDate')
        proper = request.args.get('owner')
        localizacao = request.args.get('location')
        
        historico = DadosService.get_dado()
        
        if data_inicial:
            historico = [d for d in historico if d['dt_analise'] == data_inicial]
        if proper:
            historico = [d for d in historico if d['proprietario'] == proper]
        if localizacao:
            historico = [d for d in historico if d['localizacao'] == localizacao]
        
        
        return render_template('history.html', historico=historico)
    
    @app.route('/history/edit/<id>', methods=['POST'])
    def edit_history(id):
        data = request.form
        try:
            updated_data = {
            "dt_analise": data['data_deteccao'], 
            "localizacao": data['localizacao'],
            "infestacao": data['nivel_infestacao'],
            "status": data['status_pupunheira'],
            "observacao": data['observacoes'],
            "proprietario": data['proprietario'],
            }
            DadosService.update_dado(ObjectId(id), updated_data) 
            return jsonify({"status": "success", "message": "Registro atualizado com sucesso!"})
        except Exception as e:
            return jsonify({"status": "error", "message": f"Erro ao atualizar: {str(e)}"})
        
    @app.route('/history/delete/<id>', methods=['POST'])
    def delete_history(id):
        try:
            DadosService.delete_dado(ObjectId(id)) 
            return redirect(url_for('history'))
        except Exception as e:
            return redirect(url_for('history'))
    
    @app.route('/perfil')
    def perfil():
        return render_template('perfil.html')
    
