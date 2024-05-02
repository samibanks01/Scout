function scanPort() {
    const hostname = document.getElementById("hostname").value;
    const port = parseInt(document.getElementById("port").value);
  
    // Use Fetch API to send an HTTP request to the server
    fetch(`/scan?host=${hostname}&port=${port}`)
      .then(response => response.text())
      .then(data => {
        // Update the UI with the scan result
        document.getElementById("result").textContent = data;
      })
      .catch(error => console.error(error));
  }
  