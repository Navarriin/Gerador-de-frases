from flask import Flask, request, render_template
from random import choice

# comando padrao para startar um app flask
app = Flask(__name__)

# lista com frases e autores
frases = [
    '“Os problemas são oportunidades para se mostrar o que sabe”.',

    '“Nossos fracassos, às vezes, são mais frutíferos do que os êxitos”.',

    '“Tente de novo. Fracasse de novo. Mas fracasse melhor”.',

    '“É costume de um tolo, quando erra, queixar-se dos outros. É costume de um sábio queixar-se de si mesmo”.',

    '“O verdadeiro heroísmo consiste em persistir por mais um momento, quando tudo parece perdido”.',

    '“Mesmo que já tenhas feito uma longa caminhada, há sempre um novo caminho a fazer”.',

    '“Na prosperidade, nossos amigos nos conhecem; na adversidade, nós é que conhecemos nossos amigos”.',

    '“A felicidade não está em fazer o que a gente quer, e sim querer o que a gente faz”.',

    '“Nada acontece a menos que sonhemos antes”.',
    
    '“É sempre divertido fazer o impossível”.',
]

# roteando 
@app.route('/', methods=['GET', 'POST'])
def index():
    variavel = choice(frases)
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return render_template('index.html', variavel=variavel)


app.run(port=5000,host='localhost',debug=True)