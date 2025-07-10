const msg =document.getElementById("msg")


async function fetchData(){
    const resp=await fetch("/api/user")
    const data=await resp.json()
        msg.innerText = "Hello, " + data.username;
}    

fetchData()


const button=document.querySelector(".btn")

async function logout(e){
    e.preventDefault()
    const resp=await fetch("/api/logout",{
        method:"POST"
    });
    const data = await resp.json();
    if (resp.ok){
         window.location.href = "/login";
    }
    

}

button.addEventListener("click",logout)


