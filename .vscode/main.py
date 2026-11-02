from flask import Flask
import random

facts_list_pt = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",            
              "De acordo com um estudo realizado em 2018, mais de 50 por cento das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.", 
              "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.", 
              "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."]

facts_list_en = ["Elon Musk says that social media is designed to keep us on the platform, so we spend as much time as possible looking at content.",
                 "According to a study conducted in 2018, more than 50 percent of people between 18 and 34 consider themselves dependent on their smartphones.",
                 "Social media has its ups and downs, and we should be aware of both when using it.",
                 "The study of technological dependence is one of the most relevant areas of modern scientific research."]


app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>\n <a href="/random_facts">Check out a random fact!</a>'

@app.route("/pt")
def ola_mundo():
    return '<h1>Olá, Mundo!</h1>\n <a href="/random_facts">Veja um fato aleatório!</a>'

@app.route("/random_facts")
def facts_en():
    return f'<h1>Here is some random facts! F5 to reload and get a new fact!</h1>\n <h2>{random.choice(facts_list_en)}</h2>\n <a href="/fatos_aleatorios_pt">Check out a random fact in portuguese!</a>'

@app.route("/fatos_aleatorios_pt")
def facts_pt():
    return f'<h1>Aqui está alguns fatos aleatórios! F5 para recarregar a página e ganhar um novo fato!</h1>\n <h2>{random.choice(facts_list_pt)}</h2>\n <a href="/random_facts">Veja alguns fatos aleatórios em inglês!</a>'

app.run(debug=True)