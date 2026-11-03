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

charadas = [
    "O que é, o que é? Quanto mais se tira, maior fica? Um buraco.",
    "O que é, o que é? Tem dentes, mas não morde? Um pente.",
    "O que é, o que é? Cai em pé e corre deitado? A chuva.",
    "O que é, o que é? Tem cabeça e tem dente, mas não é gente? O alho.",
    "O que é, o que é? Quanto mais seca, mais molhada fica? A toalha."
]

riddles = [
    "What has a hole that gets bigger the more you take away? A hole.",
    "What has teeth but cannot bite? A comb.",
    "What falls standing up and runs lying down? Rain.",
    "What has a head and teeth but isn't human? Garlic.",
    "What gets wetter the more it dries? A towel."
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>\n <a href="/random_facts">Check out a random fact!</a>\n <a href="/riddles">Check out these riddles in English!</a>'

@app.route("/pt")
def ola_mundo():
    return '<h1>Olá, Mundo!</h1>\n <a href="/random_facts">Veja um fato aleatório!</a>\n <a href="/charadas">Veja essas charadas em português!</a>'

@app.route("/random_facts")
def facts_en():
    return f'<h1>Here is some random facts! F5 to reload and get a new fact!</h1>\n <h2>{random.choice(facts_list_en)}</h2>\n <a href="/fatos_aleatorios_pt">Check out a random fact in portuguese!</a>\n <a href="/">Get back to home</a>'

@app.route("/fatos_aleatorios_pt")
def facts_pt():
    return f'<h1>Aqui está alguns fatos aleatórios! F5 para recarregar a página e ganhar um novo fato!</h1>\n <h2>{random.choice(facts_list_pt)}</h2>\n <a href="/random_facts">Veja alguns fatos aleatórios em inglês!</a>\n <a href="/pt">Voltar para a página inicial</a>'

@app.route("/charadas")
def charada():
    return f'<h1>Veja essa charada aleatória! Você consegue adivinhar?</h1>\n <h2>{random.choice(charadas)}</h2>\n <a href="/riddles">Veja essas charadas em inglês!</a>\n <a href="/pt">Voltar para página inicial</a>'

@app.route("/riddles")
def riddle():
    return f'<h1>Check out this random riddle! Can you guess it?</h1>\n <h2>{random.choice(riddles)}</h2>\n <a href="/charadas">Check out these riddles in Portuguese!</a>\n <a href="/">Get back to home</a>'

app.run(debug=True)