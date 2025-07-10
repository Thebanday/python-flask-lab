const button = document.getElementById("button")
const display = document.getElementById("msg")
test=document.getElementById("see")

async function signUp(event) {
    event.preventDefault()
    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password");
    const emailInput=document.getElementById("email")
    const cpasswordInput=document.getElementById("cpassword")
        

    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();
    const email=emailInput.value.trim()
    const cpassword=cpasswordInput.value.trim()

    body={
            username:username,
            email:email,
            password:password,
            cpassword:cpassword
        }

    const hasNumber = /[0-9]/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>_\-+=~`[\]\\;'\/]/.test(password);
    if(!hasNumber || !hasSpecialChar){
        display.innerHTML=`<p>Password should contain at least one number and special character</p>`
        return
    }

    // if (password.length<10){
    //     display.innerHTML=`<p>Password length should be atleast 10</p>`
    //     return
    // }

    resp = await fetch("/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    })
    const data = await resp.json()
    if (resp.ok) {
        test.innerHTML=""
        display.innerHTML = `
    <p>
        <strong>${data.message}</strong>
        &nbsp;
        <a href="/login.html" style="color: blue; text-decoration: underline;" title="Go to Login Page">Login here</a>
    </p>
  
`;
        


    }
    else {
        display.innerHTML=`<p style="color:red;">${data.error}</p>`;
        
    }

    usernameInput.value = ""
    passwordInput.value = ""
}
button.addEventListener("click", signUp)