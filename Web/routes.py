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
        user_name = session.get('user_name')
        user_id = session["user_id"]
<<<<<<< HEAD
        
        
        try:
            total = DadosService.get_casos_recentes() 
            hectares_afetados = DadosService.get_hectares_afetados()  
            nivel_severidade = DadosService.get_nivel_severidade_mais_frequente() 
            grafico_dados = DadosService.get_dados_grafico() 
        except Exception as e:
            casos_recentes = 0
            grafico_dados = []
        return render_template("main.html", user_name=user_name, user_id=user_id, total=total, 
                           hectares_afetados=hectares_afetados,
                           nivel_severidade=nivel_severidade,
                           grafico_dados=grafico_dados)
        
    @app.route('/dados-grafico', methods=['GET'])
    def dados_grafico():
        try:
            dados = DadosService.get_dados_grafico()
            response = {
                "labels": [dado["_id"] for dado in dados],
                "data": [dado["totalPlantacoes"] for dado in dados],
            }
            return jsonify(response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
=======
        return render_template("main.html", user_name=user_name, user_id=user_id)
>>>>>>> 864d1789d32cc6490f5c0994c14fe9a5db322346
    

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
    
    @app.route('/history/edit', methods=['POST'])
    def edit_history():
        try:
            data = request.form 
        
            item_id = data.get('id')
            if not item_id:
                return jsonify({"status": "error", "message": "ID do registro não fornecido"}), 400

            try:
                item_id = ObjectId(item_id)
            except Exception:
                return jsonify({"status": "error", "message": "ID inválido"}), 400
        
            updated_data = {
                "dataDeteccao": data.get('data_deteccao'),
                "localizacao": data.get('localizacao'),
                "nivelInfestacao": data.get('nivel_infestacao'),
                "status": data.get('status_pupunheira'),
                "observacoes": data.get('observacoes'),
                "proprietario": data.get('proprietario'),
                "hectares": data.get('hectares')
            }
        
            if not all(updated_data.values()):
                return jsonify({"status": "error", "message": "Campos obrigatórios estão faltando"}), 400

        
            resultado = DadosService.update_dado(item_id, updated_data)
        
            if resultado:
                return redirect(url_for('history'))
            else:
                return jsonify({"status": "error", "message": "Não foi possível atualizar os dados"}), 500

        except Exception as e:
            return jsonify({"status": "error", "message": f"Erro ao atualizar: {str(e)}"}), 500
        
    @app.route('/history/delete/<id>', methods=['POST'])
    def delete_history(id):
        try:
            DadosService.delete_dado(ObjectId(id)) 
            return redirect(url_for('history'))
        except Exception as e:
            return redirect(url_for('history'))
    
    @app.route('/perfil')
    def perfil():
        user_id = request.args.get('user_id') 
        if not user_id:
            user_id = session["user_id"]
        user_data = SignUpService.get_user_by_id(user_id)
        
        return render_template('perfil.html', user_data=user_data)
    
    @app.route('/perfil/edit', methods=['GET', 'POST'])
    def edit_perfil():
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('login'))

        if request.method == 'POST':
            nome = request.form['nome']
            telefone = request.form['telefone']
            email = request.form['email']
            senha = request.form['password']  

            logradouro = request.form['logradouro']
            cidade = request.form['cidade']
            estado = request.form['estado']
            cep = request.form['cep']

            updated_data = {
                'nome': nome,
                'telefone': telefone,
                'email': email,
            }

            if senha:
                updated_data['senha'] = senha
        

            location_data = {
                'endereco': {
                    'logradouro': logradouro,
                    'cidade': cidade,
                    'estado': estado,
                    'cep': cep
                }
            }

            try:
                resultado_pessoal = SignUpService.update_user(user_id, updated_data)
                resultado_localizacao = SignUpService.update_user(user_id, location_data)

                if resultado_pessoal and resultado_localizacao:
                    return redirect(url_for('perfil'))
            except Exception as e:
                flash(f"Erro ao atualizar o perfil: {str(e)}", "danger")

        user_data = SignUpService.get_user_by_id(user_id)

        return redirect(url_for('perfil'))
