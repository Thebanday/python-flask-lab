const button = document.getElementById("loadBtn")
const info = document.getElementById("info")


async function fetchIP() {
    const resp = await fetch("/ipinfo")
    const data = await resp.json()
    info.style.display="block"
    if (data.error) {
        info.innerHTML = `<p>Error: ${data.error}</p>`;
        return;
    }
    info.innerHTML =`
      <p><strong>IP:</strong> ${data.ip}</p>
      <p><strong>City:</strong> ${data.city}</p>
      <p><strong>Region:</strong> ${data.region}</p>
      <p><strong>Country:</strong> ${data.country}</p>
      <p><strong>Timezone:</strong> ${data.timezone}</p>
      <p><strong>Lat/Lon:</strong> ${data.latitude}, ${data.longitude}</p>
    `  

}


button.addEventListener("click", fetchIP)












