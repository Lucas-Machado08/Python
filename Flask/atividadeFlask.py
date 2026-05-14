from flask import Flask

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return "Para ver a explicação do conceito de decorator vá para o navegador /decorator"

@app.route('/decorator')
def explicacao():
    
    return """
    <h1>Explicação de Decorator</h1>
   
    <h3>O que é um Decorator?</h3>
    <p>Um decorator (decorador) em Python é uma função que recebe outra função como parâmetro, adiciona alguma funcionalidade a ela e retorna uma nova função, tudo isso sem modificar o código original da função decorada.\n
    Eles são amplamente utilizados para "envolver" (wrapper) funções com lógica extra, como registro de logs, verificação de autorização (autenticação), medição de tempo de execução ou cache.</p>
   
    <h3>Qual sua utilidade?</h3>
    <p>Reutilização de Código: Aplica a mesma lógica a múltiplas funções sem repeti-las.\n
    Separação de Responsabilidades: Separa a lógica principal da função de tarefas transversais (log, segurança).\n
    Limpeza: Mantém o código mais elegante, legível e Pythônico.</p>
   
    <h3>Como é usado no Flask?</h3>
    <p>No Flask, o @app.route é um decorator usado para registrar rotas. Ele diz ao Flask qual URL deve acionar a função que está logo abaixo dele.\n
    Quando o Flask inicia, ele lê o código e o decorator @app.route('/') pega a função home() e a mapeia no sistema interno do Flask. Quando uma requisição HTTP GET chega na raiz (/), o Flask sabe que deve executar a função home().</p>
    """

if __name__ == '__main__':
    app.run(debug=True)


