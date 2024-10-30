from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Contador de cliques
click_count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def button_click():
    global click_count
    click_count += 1  # Incrementa o contador de cliques
    return jsonify({'message': 'Botão clicado!', 'click_count': click_count})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
