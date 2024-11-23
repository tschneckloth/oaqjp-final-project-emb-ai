let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Display the successful response
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                // Display an error message for non-200 responses
                document.getElementById("system_response").innerHTML = `<strong>${xhttp.responseText}</strong>`;
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
