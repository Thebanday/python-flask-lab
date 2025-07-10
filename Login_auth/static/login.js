const button=document.querySelector(".btn")


async function login(event){
    event.preventDefault()
    const emailInput=document.getElementById("email")
    const passInput=document.getElementById("pass")

    const email=emailInput.value.trim()
    const password=passInput.value.trim()

    const display=document.getElementById("message")
    const body={
        "email":email,
        "password":password
    }

    if (!email || !password){
        display.innerHTML="Please fill the details"
        display.style.color="red"
    }else{
        const resp=await fetch("/api/login",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(body)
        })

        const data=await resp.json()

        if(resp.ok){
            display.innerHTML=data.message
            display.style.color="green"
            window.location.href = "/";
        }else{
            display.innerHTML=data.error
            display.style.color="red"
        }
    }    

}


button.addEventListener("click",login)




