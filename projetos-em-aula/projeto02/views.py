

def init_app(app):

    #Esse é outro factory esperado pelo flask

    @app.route('/')
    def index():
        return 'TOMA'

    @app.route('/contato')
    def contato():
        return "<button></button>"