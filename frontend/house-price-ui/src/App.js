// src/App.js
import { useState } from "react";
import "./App.css";

const fields = [
  { name: "area", label: "Area (sq ft)", type: "number" },
  { name: "bedrooms", label: "Bedrooms", type: "number" },
  { name: "bathrooms", label: "Bathrooms", type: "number" },
  { name: "stories", label: "Stories", type: "number" },
  { name: "parking", label: "Parking", type: "number" },
  { name: "mainroad", label: "Main Road", type: "select", options: ["yes", "no"] },
  { name: "guestroom", label: "Guest Room", type: "select", options: ["yes", "no"] },
  { name: "basement", label: "Basement", type: "select", options: ["yes", "no"] },
  { name: "hotwaterheating", label: "Hot Water Heating", type: "select", options: ["yes", "no"] },
  { name: "airconditioning", label: "Air Conditioning", type: "select", options: ["yes", "no"] },
  { name: "prefarea", label: "Preferred Area", type: "select", options: ["yes", "no"] },
  { name: "furnishingstatus", label: "Furnishing Status", type: "select", options: ["unfurnished", "semi-furnished", "furnished"] }
];

function App() {
  const [formData, setFormData] = useState(
    Object.fromEntries(fields.map(f => [f.name, ""]))
  );
  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const predictPrice = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...Object.fromEntries(
            Object.entries(formData).map(([k, v]) => [
              k,
              isNaN(v) ? v : Number(v)
            ])
          )
        })
      });
      const data = await response.json();
      setPrice(data.predicted_price);
    } catch (err) {
      console.error(err);
      alert("Backend not reachable or API error");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🏠 House Price Prediction</h1>
      <div className="form">
        {fields.map((field) => (
          <div key={field.name} className="form-group">
            <label>{field.label}</label>
            {field.type === "select" ? (
              <select name={field.name} value={formData[field.name]} onChange={handleChange}>
                <option value="">Select</option>
                {field.options.map(opt => <option key={opt} value={opt}>{opt}</option>)}
              </select>
            ) : (
              <input
                type={field.type}
                name={field.name}
                value={formData[field.name]}
                onChange={handleChange}
              />
            )}
          </div>
        ))}
        <button onClick={predictPrice} disabled={loading || Object.values(formData).some(v => v === "")}>
          {loading ? "Predicting..." : "Predict Price"}
        </button>
      </div>
      {price && <h2 className="result">Predicted Price: ₹ {price}</h2>}
    </div>
  );
}

export default App;
