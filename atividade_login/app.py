from flask import Flask, request, render_template_string

app = Flask(__name__)


usuarios_cadastrados = {
    "lucas": "22400168",  
    "dolga": "cotemig2026",
    "janaina": "cotemig2026",
    "antonio": "cotemig2026"
}

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')


    for usuario, senha in usuarios_cadastrados.items():
        if usuario_digitado == usuario and senha_digitada == senha:
            return f"<h1>Bem-vindo(a), {usuario}!</h1>"
    

    return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)