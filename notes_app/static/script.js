const API_URL="/api/notes";

async function fetchnotes() {
    const res=await fetch(API_URL)
    const notes=await res.json();

    const list=document.getElementById("notesList")
    list.innerHTML=""

    notes.forEach(note=>{
        const li =document.createElement("li")
        li.textContent=note.content;
        const deletebtn=document.createElement("button")
        deletebtn.textContent="🗑️"
        deletebtn.onclick= () => deleteNote(note.id);
        li.appendChild(deletebtn)
        list.appendChild(li)

    })

}

async function addNote(){
    const input=document.getElementById("noteInput")
    const content=input.value.trim()

    if (!content) return;

    await fetch(API_URL,{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({content})
    })

    input.value=""

    fetchnotes()
}


async function deleteNote(id){
    await fetch(`${API_URL}/${id}`,{
        method:"DELETE"
    })
    fetchnotes()
}

window.onload=fetchnotes