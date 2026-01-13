export default function PredictionResult({ price }) {
  return (
    <div>
      <h3>Predicted Price:</h3>
      <p>₹ {price.toLocaleString()}</p>
    </div>
  );
}
