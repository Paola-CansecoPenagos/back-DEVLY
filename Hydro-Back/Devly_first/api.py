from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pymongo import DESCENDING
from pdf_generator import generar_pdf
from calculator import statistical_calculator
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="Public", static_url_path="/Public")
app.config['MONGO_URI'] = 'mongodb+srv://sensorsDevly:devly1@sensorsdevly.wnv4cc4.mongodb.net/Sensors'
app.config['SECRET_KEY'] = 'b99878292951aa53e17598417a4a0a0121fcd0808ef8ae13f76a786a09bdaa4f'
mongo = PyMongo(app)

CORS(app)

@app.route("/login", methods=["POST"])
@cross_origin(origin="http://localhost:3000", headers=["Content-Type"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Buscar al usuario en la base de datos MongoDB
    user = mongo.db.users.find_one({"username": username})

    if user and check_password_hash(user["password"], password):
        # Generar el token JWT
        token = jwt.encode(
            {"username": username}, app.config["SECRET_KEY"], algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"message": "Credenciales inválidas"}), 401


@app.route("/register", methods=["POST", "OPTIONS"])
@cross_origin(origin="http://localhost:3000", headers=["Content-Type"])
def register():
    email = request.json.get("email")
    username = request.json.get("username")
    password = request.json.get("password")

    # Verificar si el email ya existe en la base de datos
    existing_email = mongo.db.users.find_one({"email": email})
    if existing_email:
        return jsonify({"message": "El email ya está en uso"}), 400

    # Verificar si el usuario ya existe en la base de datos
    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"message": "El nombre de usuario ya está en uso"}), 400

    # Generar un hash de la contraseña
    password_hash = generate_password_hash(password)

    # Crear un nuevo usuario en la base de datos
    new_user = {"email": email, "username": username, "password": password_hash}
    mongo.db.users.insert_one(new_user)

    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@app.route('/api/calcular', methods=['GET'])
def obtener_documentos():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token faltante'}), 401

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = payload['username']
        documentos = mongo.db.datos.find().sort("_id", DESCENDING).limit(50)
        campo1_output = []
        campo2_output = []
        campo3_output = []
        campo4_output = []
        campo5_output = []
        campo6_output = []
        for documento in documentos:
            campo1_output.append(documento['temperature'])
            campo2_output.append(documento['humedity'])
            campo3_output.append(documento['waterTem'])
            campo4_output.append(documento['light'])
            campo5_output.append(documento['pH'])
            campo6_output.append(documento['conduc'])
        pdf_filename = 'ReporteSensores.pdf'
        # Realizar la operación
        arr_sorted_campo1 = campo1_output[:50] if len(campo1_output) >= 50 else campo1_output
        arr_sorted_campo2 = campo2_output[:50] if len(campo2_output) >= 50 else campo2_output
        arr_sorted_campo3 = campo3_output[:50] if len(campo3_output) >= 50 else campo3_output
        arr_sorted_campo4 = campo4_output[:50] if len(campo4_output) >= 50 else campo4_output
        arr_sorted_campo5 = campo5_output[:50] if len(campo5_output) >= 50 else campo5_output
        arr_sorted_campo6 = campo6_output[:50] if len(campo6_output) >= 50 else campo6_output
        #Temperatura
        desviacion_media_campo1, media_campo1, varianza_campo1, desviacion_estandar_campo1, arr_ordenate_campo1,table_frecuency_campo1,moda_campo1 = statistical_calculator(
            arr_sorted_campo1)
        #Humedad
        desviacion_media_campo2, media_campo2, varianza_campo2, desviacion_estandar_campo2, arr_ordenate_campo2, table_frecuency_campo2,moda_campo2 = statistical_calculator(
            arr_sorted_campo2)
        #waterTemperature
        desviacion_media_campo3, media_campo3, varianza_campo3, desviacion_estandar_campo3, arr_ordenate_campo3, table_frecuency_campo3,moda_campo3= statistical_calculator(
            arr_sorted_campo3)
        #Luz
        desviacion_media_campo4, media_campo4, varianza_campo4, desviacion_estandar_campo4, arr_ordenate_campo4, table_frecuency_campo4,moda_campo4= statistical_calculator(
            arr_sorted_campo4)
        #pH
        desviacion_media_campo5, media_campo5, varianza_campo5, desviacion_estandar_campo5, arr_ordenate_campo5, table_frecuency_campo5,moda_campo5= statistical_calculator(
            arr_sorted_campo5)
        #Conductivity
        desviacion_media_campo6, media_campo6, varianza_campo6, desviacion_estandar_campo6, arr_ordenate_campo6, table_frecuency_campo6,moda_campo6= statistical_calculator(
            arr_sorted_campo6)

        #Generar pdf
        generar_pdf(pd.DataFrame(table_frecuency_campo2),pd.DataFrame(table_frecuency_campo1),pd.DataFrame(table_frecuency_campo3),
        pd.DataFrame(table_frecuency_campo4),pd.DataFrame(table_frecuency_campo5),arr_sorted_campo2, desviacion_media_campo2, varianza_campo2, media_campo2,
        desviacion_estandar_campo2,arr_sorted_campo1, arr_ordenate_campo2, arr_ordenate_campo1,
        desviacion_media_campo1, media_campo1, varianza_campo1, desviacion_estandar_campo1,pdf_filename,
        desviacion_media_campo3, media_campo3, varianza_campo3, desviacion_estandar_campo3, arr_ordenate_campo3,
        arr_sorted_campo3,desviacion_media_campo4, media_campo4, varianza_campo4, desviacion_estandar_campo4, arr_ordenate_campo4,
        arr_sorted_campo4,desviacion_media_campo5, media_campo5, varianza_campo5, desviacion_estandar_campo5,arr_ordenate_campo5,arr_sorted_campo5,moda_campo1,moda_campo2
                ,moda_campo3,moda_campo4,moda_campo5,desviacion_media_campo6, media_campo6, varianza_campo6, desviacion_estandar_campo6, arr_ordenate_campo6, table_frecuency_campo6,moda_campo6,arr_sorted_campo6)


        return jsonify("http://localhost:400/Public/ReporteSensores.pdf")


    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 401



@app.route('/api/documentos/<id>', methods=['DELETE'])
def eliminar_documento(id):
    documento = mongo.db.Datos.find_one({'_id': id})
    if documento:
        mongo.db.Datos.delete_one({'_id': id})
        return jsonify({'mensaje': 'Documento eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'Documento no encontrado'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=400)