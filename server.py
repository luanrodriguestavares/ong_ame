from flask import Flask, render_template

app = Flask(__name__)


#Rota raiz
@app.route('/')
def inicio():
    return render_template('index.html')


#Rota para "Cadastrar Empresas"
@app.route('/cadastrar-empresas')
def cadastrarEmpresas():
    return render_template('cadastrar-empresas.html')


#Rota para página "Cadastrar Pessoas"
@app.route('/cadastrar-pessoas')
def cadastrarPessoas():
    return render_template('cadastrar-pessoas.html')


#Rota para página "Empresas Parceiras"
@app.route('/empresas-parceiras')
def empresasParceiras():
    return render_template('empresas-parceiras.html')


#Rota para página "Pessoas Atendidas"
@app.route('/pessoas-atendidas')
def pessoasAtendidas():
    return render_template('pessoas-atendidas.html')


if __name__ == '__main__':
    app.run(debug=True)
