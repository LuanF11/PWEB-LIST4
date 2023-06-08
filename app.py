from flask import Flask, render_template, request, redirect

app = Flask(__name__)


funcionarios = [
     {'nome': 'João', 'endereco': 'Rua A', 'telefone': '11'},
    {'nome': 'Maria', 'endereco': 'Rua B', 'telefone': '22'}
]



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/funcionarios')
def listar_funcionarios():
    if len(funcionarios) == 0:
        mensagem_erro = "Nenhum funcionário cadastrado."
        return render_template('funcionarios.html', funcionarios=[], mensagem_erro=mensagem_erro)
    else:
        return render_template('funcionarios.html', funcionarios=funcionarios)


@app.route('/cadastrar-funcionario', methods=['GET', 'POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        funcionario = {'nome': nome, 'endereco': endereco, 'telefone': telefone}
        funcionarios.append(funcionario)
        return redirect('/funcionarios')
    return render_template('cadastrar_funcionario.html')

@app.route('/ver-funcionario/<int:id>')
def ver_funcionario(id):
    funcionario = funcionarios[id]
    return render_template('ver_funcionario.html', funcionario=funcionario)


@app.route('/editar-funcionario/<int:id>', methods=['GET', 'POST'])
def editar_funcionario(id):
    if request.method == 'POST':
        funcionario = funcionarios[id]
        funcionario['nome'] = request.form['nome']
        funcionario['endereco'] = request.form['endereco']
        funcionario['telefone'] = request.form['telefone']
        funcionarios[id] = funcionario
        return redirect('/funcionarios')
    else:
        funcionario = funcionarios[id]
        funcionario['id'] = id
        return render_template('editar_funcionario.html', funcionario=funcionario)




@app.route('/excluir-funcionario/<int:id>')
def excluir_funcionario(id):
    funcionarios.pop(id)
    return redirect('/funcionarios')

if __name__ == '__main__':
    app.run()
