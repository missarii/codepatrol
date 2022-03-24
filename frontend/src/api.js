// Remove the full URL, use empty string so requests go through Vite proxy
const API_URL = "";

export async function submitCode(username, code) {
  const form = new FormData();
  form.append("username", username); // optional, backend ignores it
  const file = new Blob([code], { type: "text/plain" });
  form.append("file", file, "code.txt");

  const response = await fetch(`${API_URL}/submit`, {
    method: "POST",
    body: form,
