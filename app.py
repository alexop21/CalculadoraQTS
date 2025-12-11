from flask import Flask, request, jsonify
from calculadora_notas import CalculadoraNotas

app = Flask(__name__)
calc = CalculadoraNotas()

def get_lista(param):
    try:
        return [float(x) for x in param.split(",")]
    except:
        return None

@app.route("/media-aritmetica")
def media_aritmetica():
    notas = get_lista(request.args.get("notas", ""))
    if not notas:
        return jsonify({"erro": "notas deve ser lista de números"}), 400
    return jsonify({"media": calc.media_aritmetica(notas)})

@app.route("/media-ponderada")
def media_ponderada():
    notas = get_lista(request.args.get("notas", ""))
    pesos = get_lista(request.args.get("pesos", ""))
    if not notas or not pesos or len(notas) != len(pesos):
        return jsonify({"erro": "notas e pesos inválidos"}), 400
    return jsonify({"media": calc.media_ponderada(notas, pesos)})

@app.route("/maior-nota")
def maior_nota():
    notas = get_lista(request.args.get("notas", ""))
    if not notas:
        return jsonify({"erro": "notas inválidas"}), 400
    return jsonify({"maior": calc.maior_nota(notas)})

@app.route("/menor-nota")
def menor_nota():
    notas = get_lista(request.args.get("notas", ""))
    if not notas:
        return jsonify({"erro": "notas inválidas"}), 400
    return jsonify({"menor": calc.menor_nota(notas)})

if __name__ == "__main__":
    app.run(debug=True)