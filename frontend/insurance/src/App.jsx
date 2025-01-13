import React, { useState } from "react";
import axios from "axios"
import './App.css'; // Importando o CSS


function App() {
  const [formData, setFormData] = useState({
    age: "",
    bmi: "",
    children: "",
    smoker: "no",
    region: "northwest",
    sex: "male"  // Adicionando o campo 'sex' ao estado
  });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict", formData);
      setResult(response.data.estimated_charge);
    } catch (error) {
      console.error("Erro ao fazer a previsão:", error);
    }
  };

  return (
    <div style={{ margin: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Calculadora de Seguro</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Idade:
            <input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
            />
          </label>
        </div>
        <div>
          <label>
            BMI:
            <input
              type="number"
              step="0.1"
              name="bmi"
              value={formData.bmi}
              onChange={handleChange}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Número de filhos:
            <input
              type="number"
              name="children"
              value={formData.children}
              onChange={handleChange}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Fumante:
            <select name="smoker" value={formData.smoker} onChange={handleChange}>
              <option value="no">Não</option>
              <option value="yes">Sim</option>
            </select>
          </label>
        </div>
        <div>
          <label>
            Região:
            <select name="region" value={formData.region} onChange={handleChange}>
              <option value="northwest">Northwest</option>
              <option value="southeast">Southeast</option>
              <option value="southwest">Southwest</option>
            </select>
          </label>
        </div>
        <div>
          <label>
            Sexo:
            <select name="sex" value={formData.sex} onChange={handleChange}>
              <option value="male">Masculino</option>
              <option value="female">Feminino</option>
            </select>
          </label>
        </div>
        <button type="submit">Calcular</button>
      </form>

      {result !== null && (
        <div style={{ marginTop: "20px" }}>
          <h2>Resultado:</h2>
          <p>O valor estimado do seguro é: ${result.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
