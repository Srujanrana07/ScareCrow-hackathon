// script.js
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

function submitData() {
    let values = {
        N: document.getElementById("input1").value,
        P: document.getElementById("input2").value,
        K: document.getElementById("input3").value,
        temperature: document.getElementById("input4").value,
        humidity: document.getElementById("input5").value,
        ph: document.getElementById("input6").value,
        rainfall: document.getElementById("input7").value
    };

    fetch("/predict_crop/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify(values)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Response from backend:", data);
        if (data.result) {
            document.getElementById("output").innerText = "Predicted Crop:";
            document.getElementById("output-below").innerText = data.result;
            document.getElementById("output").classList.add("visible");
            document.getElementById("output-below").classList.add("visible");
            document.getElementById("output").style.backgroundColor = "#28a745";
            document.getElementById("output-below").style.backgroundColor = "#28a745";
        } else {
            document.getElementById("output").innerText = "Error:";
            document.getElementById("output-below").innerText = data.error;
            document.getElementById("output").classList.add("visible");
            document.getElementById("output-below").classList.add("visible");
            document.getElementById("output").style.backgroundColor = "red";
            document.getElementById("output-below").style.backgroundColor = "red";
        }
        document.getElementById("output").style.display = "block";
        document.getElementById("output-below").style.display = "block";
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("output").innerText = "Error:";
        document.getElementById("output-below").innerText = "Error fetching data!";
        document.getElementById("output").classList.add("visible");
        document.getElementById("output-below").classList.add("visible");
        document.getElementById("output").style.backgroundColor = "red";
        document.getElementById("output-below").style.backgroundColor = "red";
    });
}

function redirectToIndex2() {
    window.location.href = "/index2/";
}