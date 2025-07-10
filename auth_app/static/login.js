button =document.getElementById("login")
display=document.getElementById("msg")

button.addEventListener("click",()=>{
    async function fetchLogin(){
        const usernameInput=document.getElementById("username")
        const passwordInput=document.getElementById("password")
        
        
        const username=usernameInput.value.trim()
        const password=passwordInput.value.trim()
        

        
        const resp=await fetch ("/api/login",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(username,password)
        })
        const data= await resp.json()
        display.innerHTML=`<p>${data.message || data.error}`
        if (resp.ok) window.location.href = "/dashboard.html";


    }
    fetchLogin()
})

