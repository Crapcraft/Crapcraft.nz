fetch("../version.json")
    .then(response => response.json())
    .then(data => {
      document.getElementById("version").textContent = data.Version;
    });
    //does the exact same thing as stats.js but for version.json so that all webpages have their versions updated dynamicly