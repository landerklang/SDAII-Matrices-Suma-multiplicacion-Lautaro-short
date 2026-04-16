from flask import Blueprint, request, jsonify
from services.matrix_service import sumar_matrices, multiplicar_matrices

matrix_bp = Blueprint("matrix", __name__)

@matrix_bp.route("/suma", methods=["POST"])
def suma():
    data = request.json

    matriz1 = data.get("matriz1")
    matriz2 = data.get("matriz2")

    resultado = sumar_matrices(matriz1, matriz2)

    return jsonify({
        "resultado": resultado
    })


@matrix_bp.route("/multiplicacion", methods=["POST"])
def multiplicacion():
    data = request.json

    matriz1 = data.get("matriz1")
    matriz2 = data.get("matriz2")

    resultado = multiplicar_matrices(matriz1, matriz2)

    return jsonify({
        "resultado": resultado
    })