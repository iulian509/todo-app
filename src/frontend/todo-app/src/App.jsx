import React, { useState, useEffect } from "react";
import Todo from "./components/Todo";
import Form from "./components/Form";

function App() {
  const [todos, setTodos] = useState([]);

  function sortItems(items) {
    return items.sort((i1, i2) => i1.priority - i2.priority);
  }

  function addTask(id, title, priority) {
    const newTask = { id: id, title: title, priority: priority };
    setTodos([...todos, newTask]);
  }

  function editTask(id, newTitle, newPriority) {
    const editedTaskList = todos.map((todo) => {
      if (id === todo.id) {
        return { ...todo, title: newTitle, priority: newPriority };
      }
      return todo;
    });
    setTodos(editedTaskList);
  }

  function deleteTask(id) {
    const remainingTasks = todos.filter((todo) => id !== todo.id);
    setTodos(remainingTasks);
  }

  useEffect(() => {
    fetch("/api/todos/")
      .then((response) => response.json())
      .then((data) => setTodos(data))
      .catch((error) => console.error(error));
  }, []);

  const taskList = sortItems(todos).map((task) => (
    <Todo
      id={task.id}
      title={task.title}
      priority={task.priority}
      key={task.id}
      deleteTask={deleteTask}
      editTask={editTask}
    />
  ));

  return (
    <div className="container">
      <div className="card mt-5">
        <h3 className="card-header text-center">TodoApp</h3>
        <div className="card-body">
          <Form addTask={addTask} />
          <h2>Tasks:</h2>
          <ul className="list-group list-group-flush">{taskList}</ul>
        </div>
      </div>
    </div>
  );
}

export default App;
