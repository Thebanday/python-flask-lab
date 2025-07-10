const button = document.querySelector(".btn")


async function signUp(e){
    e.preventDefault()
    const usernameInput=document.getElementById("user")
    const passwordInput=document.getElementById("pass")
    const emailInput=document.getElementById("email")

    const username=usernameInput.value.trim()
    const password=passwordInput.value.trim()
    const email=emailInput.value.trim()

    const display=document.getElementById("message")

    const body={
        "username":username,
        "email":email,
        "password":password
    }
    const resp=await fetch("/api/signup",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify(body)
        
    })

    const data=await resp.json()
    

    if(resp.ok){
        display.innerHTML = data.message;
        display.style.color = "green";
    }else{
        display.innerHTML = data.error;
        display.style.color = "red";
        
    }
    usernameInput.value = "";
    emailInput.value = "";
    passwordInput.value = "";
    

}

button.addEventListener("click",signUp)