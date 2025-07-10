const signupBtn = document.getElementById("signupBtn");
const msg = document.getElementById("msg");

signupBtn.addEventListener("click", async () => {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (username.length < 3 || password.length < 4) {
        msg.innerHTML = `<p style="color:red">Username or Password too short</p>`;
        return;
    }

    const res = await fetch("/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    console.log(data.message)
    console.log(data.error)
    if (res.ok) {
        msg.innerHTML = `<p style="color:green">${data.message}. <a href="login.html">Login</a></p>`;
    } else {
        msg.innerHTML = `<p style="color:red">${data.errorr}</p>`;
    }

    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
});
