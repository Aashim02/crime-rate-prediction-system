async function predictCrime() {
  const crime_type = document.getElementById("crime_type").value;
  const area = document.getElementById("area").value;
  const time = document.getElementById("time").value;
  const month = document.getElementById("month").value;

  const response = await fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      crime_type: parseInt(crime_type),
      area: parseInt(area),
      time: parseInt(time),
      month: parseInt(month)
    })
  });

  const data = await response.json();

  document.getElementById("result").innerText =
    "Prediction: " + data.prediction;
}
