const button = document.getElementById("button")
const input = document.getElementById("city")

async function fetchWeather() {
    const city=input.value.trim().toLowerCase()
    const container = document.getElementById("result")
    if (!city) {
        container.innerHTML = `<p>Please enter a valid city</p>`
        container.style.display = "block"
        return
    }

    try {
        const response = await fetch("/weather", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ city })  // send as JSON
        })

        const data = await response.json()

        if (data.error) {
            container.innerHTML = `<p>Error: ${data.error}</p>`
        } else {
            container.innerHTML = `
        <h3>Weather in ${data.city}</h3>
        <p><strong>Condition:</strong> ${data.condition}</p>
        <p><strong>Temperature:</strong> ${data.temperature_C}°C</p>
        <p><strong>Feels Like:</strong> ${data.feels_like_C}°C</p>
        <p><strong>Wind Speed:</strong> ${data.wind_kph} kph</p>
      `
        }
        container.style.display = "block"
    } catch {
        container.innerHTML = `<p>Something went wrong</p>`
        container.style.display = "block"
    }

}

button.addEventListener("click", fetchWeather)

input.addEventListener("keypress", function(e) {
  if (e.key === "Enter") {
    fetchWeather();
  }
});
