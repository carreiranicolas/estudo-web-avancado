from flask import Flask
from views import init_app

def create_app():

    #Isso é um factory, o flask espera isso para criar o app adequadamente

    app = Flask(__name__)

    init_app(app) #As views só serão criadas quando fizermos isso (pois é um callable),
    #dessa forma, ele só criaá as views, ao criar o app
    
    return app




