import { useState } from "react";

export default function HouseForm({ onSubmit }) {
  const [formData, setFormData] = useState({
    area: "",
    bedrooms: "",
    bathrooms: "",
    stories: "",
    parking: "",
    mainroad: "yes",
    guestroom: "no",
    basement: "no",
    hotwaterheating: "no",
    airconditioning: "no",
    prefarea: "no",
    furnishingstatus: "furnished"
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="number" name="area" placeholder="Area" onChange={handleChange} required />
      <input type="number" name="bedrooms" placeholder="Bedrooms" onChange={handleChange} required />
      <input type="number" name="bathrooms" placeholder="Bathrooms" onChange={handleChange} required />
      <input type="number" name="stories" placeholder="Stories" onChange={handleChange} required />
      <input type="number" name="parking" placeholder="Parking" onChange={handleChange} required />
      
      {/* Example for yes/no dropdown */}
      <select name="mainroad" value={formData.mainroad} onChange={handleChange}>
        <option value="yes">Yes</option>
        <option value="no">No</option>
      </select>

      {/* Add other dropdowns similarly: guestroom, basement, hotwaterheating, airconditioning, prefarea, furnishingstatus */}

      <button type="submit">Predict Price</button>
    </form>
  );
}
