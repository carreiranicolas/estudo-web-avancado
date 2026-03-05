from flask import Flask 

app = Flask(__name__)

## fase de configuração

# - Nesta fase carregamos as variaveis ambientes

app.config['FOO'] = 'bar'
app.config['DB_ADDRESS'] = '/dir_01/banco.db' or 'http://meubanco.com'
app.config['FLASK_DEBUG'] = True


# - Registrar rotas

@app.route('/')

app.add_url_rule('/', name_app = 'Delivery') #passando a variavel delivery para a rota /


# - Registrar o blueprint

app.register_blueprint('main') #

# - Inicializar extensões

admin = Admin(app)

*admin.init_app(app)

db.init_app(app)

# - Registro dos hooks (hhooks são processos de interceptação dos seus requests
# Tem o modo de interceptação antes do request ser finalizado, depois e enquanto
# está resolvendo o request)

# Interceptação de request acontece bastante em autenticação

@app.before_request
def before():
    ...

app.errorhandler(404)
def not_found(error):
    return 'Página não encontrada.', 404


# - Compor o sistema via factories secundarias

views.init_app(app)

extensions.init_app(app)

## Contexto de aplicacao (tudo que faço para o funcionamento da aplicação)


# Conceito de proxies --> ao inves de chamar app apontar para o lock de memória

current_app # Toda vez que precisarmos de uma coisa que está configurada no app

g # criar variavel global

from flask import current_app
def example():
    valor = current_app.config['FOO']

## Contexto de request

# - Cabeçalhos HTTP (GET, POST..)

# - Parametros de Url (passar parametros via url)

# - Dados de formulario

# - Objeto request

@app.route('/hello')
def hello():
    nome = request.args.get("nome")

# Sessoes (db, cookies) --> section do db add dados, salva e etc. cookies

#TODOS OS FRAMEWORKS TEM AS FASES ACIMA
