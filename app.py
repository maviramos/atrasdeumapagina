from flask import Flask, render_template, request

app = Flask(__name__)

# Dados de exemplo
posts = [
    {
        'autor': 'João',
        'titulo': 'Post 1',
        'conteudo': 'Conteúdo do post 1. Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'data_postagem': '10 de janeiro de 2024'
    },
    {
        'autor': 'Maria',
        'titulo': 'Post 2',
        'conteudo': 'Conteúdo do post 2. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
        'data_postagem': '15 de janeiro de 2024'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_results = None
    if request.method == 'POST':
        query = request.form['query']
        # Aqui você pode adicionar lógica para buscar os resultados com base na consulta
        # Por enquanto, vamos apenas retornar a consulta inserida
        search_results = f"Você pesquisou por: {query}"
    return render_template('index.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)