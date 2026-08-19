const API_URL = "https://ai-adoption-rag-core.onrender.com/ask";
const queryInput = document.getElementById("query");
const askBtn = document.getElementById("ask-btn");
const statusDiv = document.getElementById("status");
const resultDiv = document.getElementById("result");
const answerP = document.getElementById("answer");
const sourcesDiv = document.getElementById("sources");

askBtn.addEventListener("click", async () => {
  const query = queryInput.value.trim();
  if (!query) { statusDiv.textContent = "Enter a question first."; return; }

  askBtn.disabled = true;
  resultDiv.classList.add("hidden");
  statusDiv.innerHTML = '<span class="spinner"></span> Checking, may take a few seconds...';

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query, n_results: 3 }),
    });
    if (!response.ok) throw new Error("Server returned " + response.status);
    const data = await response.json();

    const escaped = data.answer
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\*\*(.+?)\*\*/g, "<strong>\</strong>");
    answerP.innerHTML = escaped;
    sourcesDiv.innerHTML = "";
    data.sources.forEach((s) => {
      const chip = document.createElement("span");
      chip.className = "source-chip" + (s.status.includes("draft") ? " draft" : "");
      chip.textContent = s.title.length > 40 ? s.title.slice(0, 40) + "..." : s.title;
      sourcesDiv.appendChild(chip);
    });

    resultDiv.classList.remove("hidden");
    statusDiv.textContent = "";
  } catch (err) {
    statusDiv.innerHTML = '<div class="error-box">Couldn\'t reach the service. Please try again in a moment.</div>';
  } finally {
    askBtn.disabled = false;
  }
});
