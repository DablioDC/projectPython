from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/main')
def iniciaAplication():

    #Exemplo de String fixa
    #lista = ['Wellington', 'Diego', 'Cardoso', 'Farias']
    jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
    jogo2 = Jogo('Metal Gear', 'Terror', 'PS1')
    jogo3 = Jogo('Dragon Ball Heroes', 'Ação', 'PS4')
    lista = [jogo1, jogo2, jogo3]
    return render_template('main.html',
                           titulo='Pagina Inicial',
                           jogos=lista)

app.run()

