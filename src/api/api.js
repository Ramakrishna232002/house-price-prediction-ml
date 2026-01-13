const API_URL = "http://127.0.0.1:8000/predict";

export async function getPrediction(houseData) {
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(houseData),
    });
    if (!response.ok) {
      throw new Error("API request failed");
    }
    const data = await response.json();
    return data.predicted_price;
  } catch (error) {
    console.error("Error fetching prediction:", error);
    return null;
  }
}
