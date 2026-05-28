import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados=""
        )

    num2 = float(num2_valor)

    if operacao == "bhaskara":
        num3_valor = request.form.get("num3", "").strip()
        if not num3_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o terceiro número (c) para a fórmula de Bhaskara.",
                resultados=""
            )
        num3 = float(num3_valor)
        a, b, c = num1, num2, num3
        
        if a == 0:
            return render_template("calculadora.html", etapas="O coeficiente 'a' não pode ser zero.", resultados="Erro")
        
        delta = b**2 - 4*a*c
        if delta < 0:
            etapas = f"Δ = {delta} (Δ < 0)"
            resultado = "Não existem raízes reais"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            etapas = f"Δ = {delta}"
            resultado = f"x1 = {x1}, x2 = {x2}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    if operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = "O logaritmando deve ser maior que zero."
        elif num2 <= 0 or num2 == 1:
            resultado = "Erro"
            etapas = "A base do logaritmo deve ser maior que zero e diferente de 1."
        else:
            resultado = math.log(num1, num2)
            etapas = f"log_{num2}({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} * {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            resultado = "Erro: Divisão por zero"
            etapas = "Não é possível dividir por zero."
        else:
            resultado = num1 / num2
            etapas = f"{num1} / {num2} = {resultado}"
    elif operacao == "**":
        resultado = num1 ** num2
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        resultado = "Erro"
        etapas = "Operação inválida"

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)