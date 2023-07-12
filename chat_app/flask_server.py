from flask import Flask, render_template, request
from tictactoe import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route('/tictactoe', methods=['POST'])
def handle_tictactoe():
    position = int(request.form.get('position'))
    if (position - 1) % 2 == 0:
        print('[POSITION P1]', position)
    else:
        print('[POSITION P2]', position)
    response = game.tictactoe(position)
    if response: 
        return response
    return ''

@app.route('/tictactoe')
def home():
    return render_template('ut.html')

if __name__ == '__main__':
    app.run(port=8000)
