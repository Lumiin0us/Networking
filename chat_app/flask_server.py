from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tictactoe')
def home():
    return render_template('ut.html')

if __name__ == '__main__':
    app.run(port=8000)
