from flask import Flask, jsonify, request
import requests, re

app = Flask(__name__)

@app.route('/consultar-cnpj', methods=['GET'])
def consultar_cnpj():
    cnpj = request.args.get('cnpj')
    
    if not cnpj:
        return jsonify({"erro": "CNPJ é obrigatório"}), 400
    
    # Remove tudo que não for número
    cnpj = re.sub(r'\D', '', cnpj)

    if len(cnpj) != 14:
        return jsonify({"erro": "CNPJ inválido"}), 400
    
    try:
        url = f"https://open.cnpja.com/office/{cnpj}"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"erro": "Erro ao consultar API externa"}), response.status_code

        data = response.json()

        razao_social = data.get("company", {}).get("name")

        if not razao_social:
            return jsonify({"erro": "Razão social não encontrada"}), 404

        return jsonify({
            "Razão Social": razao_social
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run()
    

