from flask import Flask
import random

facts_list = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",            
              "De acordo com um estudo realizado em 2018, mais de 50 por cento das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.", 
              "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.", 
              "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/fatos")
def fatos():
    fatos = random.choice(facts_list)
    return f'<h1>{fatos}</h1>'

app.run(debug=True)