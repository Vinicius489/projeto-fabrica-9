from flask import Flask, request, jsonify

app = Flask(__name__)

itens = [
    {
        "id": 1,
        "nome": "Arroz 5kg",
        "quantidade": 2,
        "categoria": "Alimentos",
        "prioridade": "alta",
        "comprado": False
    }
]

@app.route("/items", methods=["GET"])
def listar_itens():
    return jsonify(itens)

@app.route("/items/<id>", methods=["GET"])
def buscar_item(id):
    item = next((i for i in itens if i ["id"] == id), None)
    if not item:
        return jsonify({"erro": "Item não encontrado!"}), 404

@app.route("/items", methods=["POST"])
def add_item():
    dados = request.get_json()
    novo_item = {
        "id": len(itens) + 1,
        "nome": dados["nome"],
        "quantidade": dados["quantidade"],
        "categoria": dados["categoria"],
        "prioridade": dados["prioridade"],
        "comprado": dados["comprado"]
    }
    itens.append(novo_item)
    return jsonify(novo_item), 201



@app.route("/items/<id>", methods=['PU'])
def ayualizar_item(id):
    item = next((i for i in itens if i ["id"] == id), None) 
    if not item:
        return jsonify({"erro:" "Item não Encontrado!"}), 404
    dados = request.get_json()
    item["nome"] = dados.get('nome', dados["nome"])
    item["quantidade"] = dados.get('quantidade', dados["quantidade"])
    item["categoria"] = dados.get('categoria', dados["categoria"])
    item["prioridade"] = dados.get('prioridade', dados["prioridade"])
    item["comprado"] = dados.get('comprado', dados["comprado"])


    return jsonify(item)

@app.route("/items/<id>", methods=['DELETE'])
def excluir_item(id):
    global itens
    item = next((i for i in itens if i["id"] == id), None)
    if not item:
        return jsonify({"erro": "Item não Encontrado!"}), 404

    itens = [i for i in itens if i ["id"] != id]
    return jsonify({"mensagem": "Item excluido com Sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)