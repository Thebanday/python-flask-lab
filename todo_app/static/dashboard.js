const taskList = document.getElementById("task-list");
const addBtn = document.getElementById("addBtn");

const userId = localStorage.getItem("user_id");
if (!userId) {
    alert("Please login first");
    window.location.href = "login.html";
}

async function loadTasks() {
    const res = await fetch(`/api/tasks/${userId}`);
    const tasks = await res.json();

    taskList.innerHTML = "";
    tasks.forEach(task => {
        const div = document.createElement("div");
        div.innerHTML = `
            <p><strong>${task.Title}</strong>: ${task.Description}</p>
            <p>Status: ${task.status ? "✅" : "❌"}</p>
            <button onclick="deleteTask(${task.Id})">Delete</button>
            <button onclick="toggleStatus(${task.Id}, ${task.status})">Toggle Status</button>
            <hr>
        `;
        taskList.appendChild(div);
    });
}

async function deleteTask(taskId) {
    await fetch(`/api/tasks/${taskId}`, { method: "DELETE" });
    loadTasks();
}

async function toggleStatus(taskId, currentStatus) {
    await fetch(`/api/tasks/${taskId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: !currentStatus })
    });
    loadTasks();
}

addBtn.addEventListener("click", async () => {
    const title = document.getElementById("title").value.trim();
    const description = document.getElementById("description").value.trim();
    if (!title || !description) return;

    await fetch("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description, user_id: userId })
    });

    document.getElementById("title").value = "";
    document.getElementById("description").value = "";
    loadTasks();
});

loadTasks();
