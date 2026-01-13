export default function Result({ price }) {
  return (
    <div>
      <h2>Predicted House Price:</h2>
      <p>{price ? `₹ ${price.toLocaleString()}` : "No prediction yet"}</p>
    </div>
  );
}
