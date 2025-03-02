// disease_detector\static\js\script.js
document.addEventListener("DOMContentLoaded", function () {
    const dropZone = document.getElementById("dropZone");
    const fileInput = document.getElementById("fileInput");
    const uploadButton = document.getElementById("uploadButton");
    const imagePreview = document.getElementById("imagePreview");
    const previewSection = document.getElementById("previewSection");
    const loadingIndicator = document.getElementById("loadingIndicator");
    const resultsSection = document.getElementById("resultsSection");
    const cropNameElement = document.getElementById("cropName");
    const diseaseElement = document.getElementById("disease");
    const cureElement = document.getElementById("cure");
    const chatbotSection = document.getElementById("chatbotSection");
    const messagesDiv = document.getElementById("messages");
    const userMessage = document.getElementById("userMessage");

    // ✅ Get CSRF Token Function
    function getCSRFToken() {
      let cookieValue = null;
      let cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
          cookieValue = cookie.substring("csrftoken=".length, cookie.length);
          break;
        }
      }
      return cookieValue;
    }

    // ✅ Drag & Drop Image Upload
    ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
      dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
    }

    ["dragenter", "dragover"].forEach((eventName) => {
      dropZone.addEventListener(eventName, () => dropZone.classList.add("dragover"), false);
    });

    ["dragleave", "drop"].forEach((eventName) => {
      dropZone.addEventListener(eventName, () => dropZone.classList.remove("dragover"), false);
    });

    dropZone.addEventListener("drop", handleDrop, false);

    function handleDrop(e) {
      const files = e.dataTransfer.files;
      handleFiles(files);
    }

    uploadButton.addEventListener("click", () => {
      fileInput.click();
    });

    fileInput.addEventListener("change", function () {
      handleFiles(this.files);
    });

    function handleFiles(files) {
      const file = files[0];
      if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = function (e) {
          imagePreview.src = e.target.result;
          previewSection.hidden = false;
          loadingIndicator.hidden = false;
          resultsSection.hidden = true;
          analyzeImage(file);
        };
        reader.readAsDataURL(file);
      }
    }

    // 🔥 Image Analysis API Call
    function analyzeImage(file) {
      let formData = new FormData();
      formData.append("image", file);

      fetch("/detect_disease/", {
        method: "POST",
        headers: {
          "X-CSRFToken": getCSRFToken(),
        },
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            cropNameElement.textContent = "Error";
            diseaseElement.textContent = data.error;
            cureElement.textContent = "";
          } else {
            cropNameElement.textContent = data.crop;
            diseaseElement.textContent = data.disease;
            cureElement.textContent = data.cure;
            chatbotSection.hidden = false; // Show Chatbot Only After Image Analysis ✅
          }
          loadingIndicator.hidden = true;
          resultsSection.hidden = false;
        })
        .catch((error) => {
          console.error("Error:", error);
          cropNameElement.textContent = "Error";
          diseaseElement.textContent = "Failed to analyze image.";
          cureElement.textContent = "";
          resultsSection.hidden = false;
        })
        .finally(() => {
          loadingIndicator.style.display = "none";
        });
    }

    // 🎯 Chatbot System
    async function sendMessage() {
      const message = userMessage.value.trim();
      if (!message) return;

      messagesDiv.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
      userMessage.value = "";
      messagesDiv.innerHTML += `<div><em>Scarecrow is typing...</em></div>`;
      messagesDiv.scrollTop = messagesDiv.scrollHeight;

      await fetch("/ask_question/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ question: message }),
      })
        .then((response) => response.json())
        .then((data) => {
          messagesDiv.innerHTML = messagesDiv.innerHTML.replace(`<div><em>Scarecrow is typing...</em></div>`, "");

          if (data.answer) {
            messagesDiv.innerHTML += `<div><strong>Scarecrow:</strong> ${data.answer}</div>`;
          } else {
            messagesDiv.innerHTML += `<div><strong>Scarecrow:</strong> ${data.error}</div>`;
          }
          messagesDiv.scrollTop = messagesDiv.scrollHeight;
        })
        .catch((error) => {
          console.error("Chatbot Error:", error);
          messagesDiv.innerHTML += `<div><strong>Scarecrow:</strong> Unable to generate response.</div>`;
        });
    }

    document.querySelector(".input-box button").addEventListener("click", sendMessage);
    userMessage.addEventListener("keypress", (e) => {
      if (e.key === "Enter") sendMessage();
    });
  });