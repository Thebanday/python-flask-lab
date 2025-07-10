const API_URL="/api/tasks";

async function fetchTasks() {
    const resp=await fetch(API_URL)
    const tasks=await resp.json()

    const list=document.getElementById("taskList")
    list.innerHTML=""

    tasks.forEach(task=>{
        const li=document.createElement("li")
        li.textContent=task.text;
        li.className=task.done ? "done":""

        const togglebtn=document.createElement("button")
        togglebtn.textContent="🔄"
        togglebtn.onclick=(e)=> {
            e.stopPropagation();
            toggleDone(task.id);
          
        }
        li.appendChild(togglebtn)
        list.appendChild(li)

        const delbtn=document.createElement("button")
        delbtn.textContent="🗑"
        delbtn.onclick=(e)=>  {
            e.stopPropagation();
            const confirmed=confirm("Are you sure want to delete this")
            if (confirmed){
                deleteTask(task.id);
            }
            
        };
        li.appendChild(delbtn)
        list.appendChild(li)



    })

    
}    

async function addTask() {
    const input=document.getElementById("taskInput")
        
    const text=input.value.trim()
    if(!text) return

    await fetch(API_URL,{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({text})
    })

    input.value="";
    fetchTasks()
}
document.getElementById("taskInput").addEventListener("keydown",function(e){
        if (e.key==="Enter"){
            addTask()
        }
})
async function deleteTask(id) {
    await fetch(`${API_URL}/${id}`,{method:"DELETE"})
    fetchTasks()


}


async function toggleDone(id) {
    await fetch(`${API_URL}/${id}/toggle`,{method:"PUT"})
    fetchTasks()
}

window.onload = fetchTasks;
