// Get the current domain and port
const API_BASE = window.location.origin;

async function startResearch() {
  const topic = document.getElementById("topicInput").value.trim();
  if (!topic) {
    alert("Please enter a research topic.");
    return;
  }

  document.getElementById("loading").style.display = "block";
  document.getElementById("outputSection").style.display = "none";

  try {
    const response = await fetch(`${API_BASE}/research`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ topic: topic })
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    
    if (data.filename) {
      document.getElementById("reportText").textContent = data.report;

      const download = document.getElementById("downloadLink");
      download.href = `${API_BASE}/download/${data.filename}`;
      download.style.display = "inline-block";

      document.getElementById("loading").style.display = "none";
      document.getElementById("outputSection").style.display = "block";
      
      showMessage("Research completed successfully!", "success");
    } else {
      throw new Error(data.message || "Failed to generate report");
    }

  } catch (error) {
    console.error("Error:", error);
    showMessage(`Error: ${error.message}`, "error");
    document.getElementById("loading").style.display = "none";
  }
}

function showMessage(message, type) {
  const existingMessage = document.querySelector(".message");
  if (existingMessage) {
    existingMessage.remove();
  }

  const messageDiv = document.createElement("div");
  messageDiv.className = `message ${type}`;
  messageDiv.textContent = message;
  
  const button = document.querySelector("button");
  button.parentNode.insertBefore(messageDiv, button.nextSibling);
  
  setTimeout(() => {
    if (messageDiv.parentNode) {
      messageDiv.remove();
    }
  }, 5000);
}

document.getElementById("topicInput").addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    startResearch();
  }
});
