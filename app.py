from flask import Flask, render_template

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