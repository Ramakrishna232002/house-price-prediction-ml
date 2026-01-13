const BASE_URL = "http://127.0.0.1:8000"; // Your FastAPI backend URL

export const predictHousePrice = async (houseData) => {
  try {
    const response = await fetch(`${BASE_URL}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(houseData),
    });
    const data = await response.json();
    return data.predicted_price;
  } catch (error) {
    console.error("Error fetching prediction:", error);
    return null;
  }
};
