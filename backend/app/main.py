from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from flask_cors import CORS

# Carregando o modelo treinado e o scaler
with open('modelo/modelo.pkl', 'rb') as f:
    model = pickle.load(f)

with open('modelo/scaler.pkl', 'rb') as f:  # Supondo que você tenha salvo o scaler em um arquivo
    scaler = pickle.load(f)

# Definindo as colunas categóricas processadas
regions = ['region_northwest', 'region_southeast', 'region_southwest']

app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Recebe os dados do usuário em JSON

    try:
        # Extraindo os dados do JSON
        age = data['age']
        bmi = data['bmi']
        children = data['children']
        smoker_yes = 1 if data['smoker'].lower() == 'yes' else 0  # Alterado para usar "smoker_yes"
        region = data['region'].lower()
        sex = 1 if data['sex'].lower() == 'male' else 0  # Calculando sex_male

        # Validação da região
        if region not in ['northwest', 'southeast', 'southwest']:
            return jsonify({'error': 'Região inválida! Use uma das seguintes: northwest, southeast, southwest'}), 400

        # Criando as colunas booleanas para a região
        region_encoded = [1 if region == 'northwest' else 0, 
                          1 if region == 'southeast' else 0, 
                          1 if region == 'southwest' else 0]

    except KeyError as e:
        return jsonify({'error': f'Campo ausente: {str(e)}'}), 400

    # Preparar os dados na ordem correta, agora incluindo sex_male e smoker_yes
    input_data = np.array([[age, bmi, children, smoker_yes, sex] + region_encoded])

    # Transformar em DataFrame para corresponder ao modelo
    input_data_df = pd.DataFrame(input_data, columns=model.feature_names_in_)

    # Normalizar as variáveis 'age', 'bmi' e 'children'
    input_data_df[['age', 'bmi', 'children']] = scaler.transform(input_data_df[['age', 'bmi', 'children']])

    # Garantir que o número de features está correto
    if input_data_df.shape[1] != len(model.feature_names_in_):
        return jsonify({'error': f'Número de features incorreto. Esperado: {len(model.feature_names_in_)}, mas recebido: {input_data_df.shape[1]}'}), 400

    # Faz a previsão
    prediction = model.predict(input_data_df)[0]

    return jsonify({'estimated_charge': prediction})

if __name__ == '__main__':
    print("Servidor Flask iniciado na porta 5000")
    app.run(debug=True)  # Inicia o servidor Flask
