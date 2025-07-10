button = document.getElementById("logout")




    async function logOut() {
        const resp = await fetch("/api/logout",{
            method:"POST"
        })
        window.location.href="/login.html"
    }
button.addEventListener("click",logOut)

async function fetchUser() {
    const resp = await fetch("/api/user")
    const data = await resp.json()
    if (resp.ok) {
    document.getElementById("username").innerText = data.username;
  } else {
    alert("Please login first");
    window.location.href = "/login.html";
  }
}

fetchUser();