// 미션1. /api/todo 에 CRUD 하기 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}

document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const textInput = document.getElementById('text-input');

    todoForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = textInput.value.trim();
        if (!text) return;
        textInput.value = ''; // 입력값 지우기

        // try catch 로 감싸서 예외처리해야함.
        // 여기는 퉁쳐서 두가지 다른 일을 하나로 잡았지만, 진짜 좋은 코드는 각각의 목적에 맞게 분리하는게 좋은거다. 하지만, "진짜 좋은" 의 정의가 무엇이냐?? 를 생각해 볼것...
        try {
            const response = await fetch('/api/todo', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text})
            });
            const data = await response.json()
            console.log(data);
        } catch (err) {
            console.error('백엔드 요청에 실패하였음: ', err);
        }

        loadTodos(); // 데이터 요청하기
    });

    // 최초 로딩 - 시작시 일단 현재 목록 불러오기
    loadTodos();
});

async function loadTodos() {
    const todoList = document.getElementById('todo-list');
    const res = await fetch('/api/todo');
    const data = await res.json();

    console.log(data);
    todoList.innerHTML = ''; // 현재 있는거 초기화
    data.forEach((task) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span class="${task.done ? 'done': ''}" onclick="toggleTodo(${task.id})">
                ${task.task}
            </span>
            <a onclick="deleteTodo(${task.id})"><i class="bi bi-trash"></i></a>
        `;
        todoList.appendChild(li);
    })
}

async function toggleTodo(id) {
    // 여기도 try catch 해야함.
    const response = await fetch(`/api/todo/${id}`, {
        method: 'PUT'     
    });
    const data = await response.json();
    console.log(data);
    loadTodos(); 
}

async function deleteTodo(id) {
    // 여기도 try catch 해야함.
    const response = await fetch(`/api/todo/${id}`, {
        method: 'DELETE'     
    });
    const data = await response.json();
    console.log(data);
    loadTodos(); 
}
