let getTodoItems = () => {

    let items = document.getElementById('todos');
    let itemsHTML = ''

    fetch("/api/todo")
        .then((response) => response.json())
        .then((data) => {
            for (const item of data) {
                itemsHTML += `
                    <li
                        class="list-group-item d-flex justify-content-between align-items-center
                                border-start-0 border-top-0 border-end-0 border-bottom rounded-0 mb-2">
                        <div class="d-flex align-items-center" id="item-${item.id}" data-value="${item.task}">
                            ${item.task}
                        </div>
                        <div class="float-end">
                            <i class="fas fa-pen text-primary" style="margin-right: 30px" data-mdb-toggle="modal"
                             data-mdb-target="#exampleModal" onclick='updateTodoItem(${item.id})'></i>
                            <i class="fas fa-times text-primary" onclick='deleteTodoItem(${item.id})'></i>
                        </div>
                    </li>
                `
            }
            items.innerHTML = itemsHTML;
        })
        .catch(console.error);
}

getTodoItems();


let createTodoItem = (e) => {

    e.preventDefault();
    todoTask = document.getElementById('todoTask').value;
    const data = { task: todoTask };

    fetch('/api/todo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            getTodoItems();
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    // reset form
    document.getElementById('todo-from').reset();
}


let updateTodoItem = (id) => {
    let modalInput = document.getElementById('todo-text');
    let updateTodoBtn = document.getElementById("update-todo")
    let todoItem = document.getElementById(`item-${id}`).getAttribute('data-value');
    modalInput.value = todoItem
    
    updateTodoBtn.addEventListener('click', () => {
        const data = { task: modalInput.value };
        fetch(`/api/todo/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                getTodoItems();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }, { once: true })
}


let deleteTodoItem = (id) => {

    fetch(`/api/todo/${id}`, {
        method: 'DELETE',
    })
        .then((response) => response.json())
        .then((data) => {
            getTodoItems();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
