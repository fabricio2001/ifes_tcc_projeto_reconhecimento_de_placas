from flask import Flask, render_template, jsonify, request
from db.db import session
from db.db import Pessoa, Carro, Registro, Cor, Marca, Modelo, Cargo
import json
from datetime import datetime
from flask_cors import CORS
import base64
import os

app = Flask(__name__, template_folder="view")
CORS(app)

@app.route("/", methods=['GET'])
def index():

    session.add(
        Carro(placa="teste", modelo="teste",marca="teste",cor="teste",pessoa=1)
    )
    session.commit()

    template = render_template('index.html', titulo="Controle e Monitoramento")
    return template

@app.route("/Pessoas", methods=['GET'])
def GetPessoas():
    lista_pessoas = []
    pessoas = session.query(Pessoa).all()
    for c in pessoas:
        lista_pessoas.append({"id": c.id, "cpf": c.cpf, "nome": c.nome, "telefone": c.telefone, "email": c.email, "cargo": c.cargo})
    response = jsonify(lista_pessoas)
    return AddHeaders(response)

@app.route("/Pessoas", methods=['POST'])
def PostPessoas():
    values = json.loads(request.values.get('values'))

    session.add(
        Pessoa(cpf=values["cpf"], nome=values["nome"], telefone=values["telefone"], email=values["email"], cargo=values["cargo"]),
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Pessoas", methods=['PUT'])
def PutPessoas():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("cpf")):
        session.query(Pessoa).filter(Pessoa.id == key).update(
            {"cpf": values["cpf"]}
        )

    if(values.get("nome")):
        session.query(Pessoa).filter(Pessoa.id == key).update(
            {"nome": values["nome"]}
        )

    if(values.get("telefone")):
        session.query(Pessoa).filter(Pessoa.id == key).update(
            {"telefone": values["telefone"]}
        )

    if(values.get("email")):
        session.query(Pessoa).filter(Pessoa.id == key).update(
            {"email": values["email"]}
        )
    
    if(values.get("cargo")):
        session.query(Pessoa).filter(Pessoa.id == key).update(
            {"cargo": values["cargo"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Pessoas", methods=['DELETE'])
def DeletePessoas():
    key = json.loads(request.values.get('key'))

    session.query(Pessoa).filter(Pessoa.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)



@app.route("/Carros", methods=['GET'])
def GetCarros():
    lista_carros = []
    carros = session.query(Carro).all() 
    
    for c in carros:
        lista_carros.append({"id": c.id, "placa": c.placa, "modelo": c.modelo, "marca": c.marca, "cor": c.cor, "pessoa": c.pessoa})
    response = jsonify(lista_carros)
    return AddHeaders(response)

@app.route("/Carros", methods=['POST'])
def PostCarros():
    values = json.loads(request.values.get('values'))

    session.add(
        Carro(placa=values["placa"], modelo=values["modelo"], marca=values["marca"], cor=values["cor"],pessoa=values["pessoa"])
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Carros", methods=['PUT'])
def PutCarros():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("placa")):
        session.query(Carro).filter(Carro.id == key).update(
            {"placa": values["placa"]}
        )

    if(values.get("modelo")):
        session.query(Carro).filter(Carro.id == key).update(
            {"modelo": values["modelo"]}
        )

    if(values.get("marca")):
        session.query(Carro).filter(Carro.id == key).update(
            {"marca": values["marca"]}
        )

    if(values.get("cor")):
        session.query(Carro).filter(Carro.id == key).update(
            {"cor": values["cor"]}
        )
    
    if(values.get("pessoa")):
        session.query(Carro).filter(Carro.id == key).update(
            {"pessoa": values["pessoa"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Carros", methods=['DELETE'])
def DeleteCarros():
    key = json.loads(request.values.get('key'))

    session.query(Carro).filter(Carro.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)



@app.route("/Registros", methods=['GET'])
def GetRegistros():
    lista_registro = []
    registro = session.query(Registro).all() 
    
    for c in registro:
        lista_registro.append({"id": c.id, "placa": c.placa, "direcao": c.direcao, "data": c.data, "tipo": c.tip})
    response = jsonify(lista_registro)
    return AddHeaders(response)

@app.route("/Registros", methods=['POST'])
def PostRegistros():
    
    values = json.loads(request.values.get('values'))
    # values = request.get_json()
    
    session.add(
        Registro(placa=values["placa"], direcao=values["direcao"], data=datetime.strptime(values["data"], '%Y/%m/%d %H:%M:%S'), tip = 1)
        # Registro(placa=values["placa"], direcao=values["direcao"], data=datetime.strptime(values["data"], '%Y-%m-%dT%H:%M:%S.%fZ'), tip = 1)

    )
    session.commit()

    response = jsonify({"status": "true"})
    return response

@app.route("/Registros/App", methods=['POST'])
def PostRegistrosApp():
    print('requisicao')
    
    # values = json.loads(request.values.get('values'))
    # values = request.get_json()
    # if 'image' in request.files:
    #     print('arquivo recebido')
    #     file = request.files['image']

    #     save_path = os.path.join('app\static\img', file.filename)
        
    #     # Salve o arquivo
    #     file.save(save_path)

    #     print('arquivo salvo')
    fileName = 'roi.jpg'
    if 'json_field' in request.form:
        # carregue o json a partir da string
        values = json.loads(request.form['json_field'])
        # você pode manipular os dados conforme necessário
        fileName = values[0]['placa'] + '.jpg'

        

    if 'image' in request.files:
        file = request.files['image']
        print("Image")
        # você pode salvar o arquivo ou manipulá-lo conforme necessário
        save_path = os.path.join('static\img', fileName)
        file.save(save_path)

    # Verifique se o campo JSON está presente
    print('Verifique se o campo JSON está presente')
    #print(values[0]["placa"])# < esta dand erro
    # session.add(
    #     Registro(placa=values[0]["placa"], direcao=values[0]["direcao"], data=parse_date(values[0]["data"]), tip = 2)
    # )
    # session.commit()

    response = jsonify({"status": "true"})
    return response

@app.route("/Dados/Cor", methods=['GET'])
def GetCor():
    lista_carros = []
    carros = session.query(Cor).all() 
    
    for c in carros:
        lista_carros.append({"id": c.id, "nome": c.nome})
    response = jsonify(lista_carros)
    return AddHeaders(response)

@app.route("/Dados/Cor", methods=['POST'])
def PostCor():
    values = json.loads(request.values.get('values'))

    session.add(
        Cor(nome=values["nome"])
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Cor", methods=['PUT'])
def PutCor():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("nome")):
        session.query(Cor).filter(Cor.id == key).update(
            {"nome": values["nome"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Cor", methods=['DELETE'])
def DeleteCor():
    key = json.loads(request.values.get('key'))

    session.query(Cor).filter(Cor.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Marca", methods=['GET'])
def GetMarca():
    lista_carros = []
    carros = session.query(Marca).all() 
    
    for c in carros:
        lista_carros.append({"id": c.id, "nome": c.nome})
    response = jsonify(lista_carros)
    return AddHeaders(response)

@app.route("/Dados/Marca", methods=['POST'])
def PostMarca():
    values = json.loads(request.values.get('values'))

    session.add(
        Marca(nome=values["nome"])
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Marca", methods=['PUT'])
def PutMarca():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("nome")):
        session.query(Marca).filter(Marca.id == key).update(
            {"nome": values["nome"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Marca", methods=['DELETE'])
def DeleteMarca():
    key = json.loads(request.values.get('key'))

    session.query(Marca).filter(Marca.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Modelo", methods=['GET'])
def GetModelo():
    lista_carros = []
    carros = session.query(Modelo).all() 
    
    for c in carros:
        lista_carros.append({"id": c.id, "nome": c.nome})
    response = jsonify(lista_carros)
    return AddHeaders(response)

@app.route("/Dados/Modelo", methods=['POST'])
def PostModelo():
    values = json.loads(request.values.get('values'))

    session.add(
        Modelo(nome=values["nome"])
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Modelo", methods=['PUT'])
def PutModelo():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("nome")):
        session.query(Modelo).filter(Modelo.id == key).update(
            {"nome": values["nome"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Modelo", methods=['DELETE'])
def DeleteModelo():
    key = json.loads(request.values.get('key'))

    session.query(Modelo).filter(Modelo.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Cargo", methods=['GET'])
def GetCargo():
    lista_carros = []
    carros = session.query(Cargo).all() 
    
    for c in carros:
        lista_carros.append({"id": c.id, "nome": c.nome})
    response = jsonify(lista_carros)
    return AddHeaders(response)

@app.route("/Dados/Cargo", methods=['POST'])
def PostCargo():
    values = json.loads(request.values.get('values'))

    session.add(
        Cargo(nome=values["nome"])
    )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Cargo", methods=['PUT'])
def PutCargo():
    values = json.loads(request.values.get('values'))
    key = json.loads(request.values.get('key'))

    if(values.get("nome")):
        session.query(Cargo).filter(Cargo.id == key).update(
            {"nome": values["nome"]}
        )
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)

@app.route("/Dados/Cargo", methods=['DELETE'])
def DeleteCargo():
    key = json.loads(request.values.get('key'))

    session.query(Cargo).filter(Cargo.id == key).delete()   
    session.commit()

    response = jsonify({"status": "true"})
    return AddHeaders(response)


@app.route("/Chart/Entrada", methods=['GET'])
def GetChart():
    # lista_registro = []
    # registro = session.query(Registro).all() 
    
    dic1 = {"arg": 'Segunda', "val": 25, "parentID": '' }
    dic2 = {"arg": 'Terça', "val": 20, "parentID": '' }
    dic3 = {"arg": 'Quarta', "val": 28, "parentID": '' }
    dic4 = {"arg": '1h', "val": 28, "parentID": 'Segunda' }
    dic5 = {"arg": '2h', "val": 28, "parentID": 'Terça' }
    dic6 = {"arg": '3h', "val": 28, "parentID": 'Quarta' }
    list = [dic1, dic2, dic3, dic4, dic5, dic6]
    # for c in registro:
    #     lista_registro.append({"id": c.id, "placa": c.placa, "direcao": c.direcao, "data": c.data, "tipo": c.tip})
    response = jsonify(list)
    return AddHeaders(response)

def AddHeaders(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Max-Age', '86400')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def parse_date(date_str):
    for fmt in ('%Y/%m/%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S.%fZ'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')