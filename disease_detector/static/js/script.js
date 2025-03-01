document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');
    const imagePreview = document.getElementById('imagePreview');
    const previewSection = document.getElementById('previewSection');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const resultsSection = document.getElementById('resultsSection');
    const cropNameElement = document.getElementById('cropName');
    const diseaseElement = document.getElementById('disease');
    const cureElement = document.getElementById('cure');

    function getCSRFToken() {
        let cookieValue = null;
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith("csrftoken=")) {
                cookieValue = cookie.substring("csrftoken=".length, cookie.length);
                break;
            }
        }
        return cookieValue;
    }

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, unhighlight, false);
    });

    function highlight(e) {
        dropZone.classList.add('dragover');
    }

    function unhighlight(e) {
        dropZone.classList.remove('dragover');
    }

    dropZone.addEventListener('drop', handleDrop, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }

    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', function(e) {
        handleFiles(this.files);
    });

    function handleFiles(files) {
        const file = files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                previewSection.hidden = false;
                loadingIndicator.hidden = false;
                resultsSection.hidden = true;
                analyzeImage(file);
            }
            reader.readAsDataURL(file);
        }
    }

    function analyzeImage(file) {
        let formData = new FormData();
        formData.append("image", file);

        fetch("/detect_disease/", {
            method: "POST",
            headers: {
                "X-CSRFToken": getCSRFToken()
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                cropNameElement.textContent = "Error";
                diseaseElement.textContent = data.error;
                cureElement.textContent = "";
            } else {
                cropNameElement.textContent = data.crop;
                diseaseElement.textContent = data.disease;
                cureElement.textContent = data.cure;
            }
            loadingIndicator.hidden = true;
            resultsSection.hidden = false;
        })
        .catch(error => {
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
});