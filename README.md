🧮 Calculadora de Seguro de Saúde (Machine Learning)

Este projeto consiste em uma aplicação completa com Flask (backend) e React + Vite (frontend) que estima o custo de seguro de saúde com base em variáveis como idade, IMC, número de filhos, tabagismo, região e sexo.

O backend carrega um modelo de Machine Learning treinado, aplica normalização e retorna o valor estimado.
O frontend envia os dados via API e exibe o resultado ao usuário.

🚀 Tecnologias Utilizadas
Backend (API – Flask)

Python

Flask

Scikit-learn

Pickle (modelo e scaler)

Pandas / NumPy

Flask-CORS

Frontend

React

Vite

Axios

CSS simples

📌 Funcionalidades

Formulário para entrada dos dados do usuário.

Normalização das variáveis pelo scaler treinado.

Previsão do valor do seguro via modelo ML carregado no backend.

Exibição do resultado no frontend.

Troca dinâmica entre opções de região, sexo e tabagismo.

🔗 Fluxo da Aplicação

Usuário preenche o formulário.

O frontend envia os dados para POST /predict.

O backend:

Monta o vetor de entrada

Aplica o scaler

Executa o modelo

Retorna estimated_charge

O valor estimado é exibido na tela.
