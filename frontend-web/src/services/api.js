export async function convertText(text) {
  const response = await fetch("http://localhost:5000/convert", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  return response.json();
}
