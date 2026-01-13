import { useState } from "react";
import "./App.css";

// Dynamic form fields configuration
const fieldsConfig = [
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
  { 
    name: "furnishingstatus", 
    label: "Furnishing Status", 
    type: "select", 
    options: ["semi-furnished", "unfurnished", "furnished"] 
  },
];

function App() {
  const [formData, setFormData] = useState(
    fieldsConfig.reduce((acc, field) => {
      acc[field.name] = field.type === "select" ? field.options[0] : "";
      return acc;
    }, {})
  );

  const [price, setPrice] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const predictPrice = async () => {
    setLoading(true);
    try {
      const payload = { ...formData };
      // convert number fields to Number
      fieldsConfig.forEach(f => {
        if (f.type === "number") payload[f.name] = Number(payload[f.name]);
      });

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await response.json();
      setPrice(data.predicted_price || null);
    } catch (err) {
      console.error(err);
      alert("Backend not running or API error");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🏠 House Price Prediction</h1>
      <div className="form">
        {fieldsConfig.map((field) => (
          <div key={field.name}>
            <label>{field.label}</label>
            {field.type === "select" ? (
              <select name={field.name} value={formData[field.name]} onChange={handleChange}>
                {field.options.map((opt) => (
                  <option key={opt} value={opt}>{opt}</option>
                ))}
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

        <button onClick={predictPrice} disabled={loading}>
          {loading ? "Predicting..." : "Predict Price"}
        </button>
      </div>

      {price && <h2 className="result">Predicted Price: ₹ {price}</h2>}
    </div>
  );
}

export default App;
