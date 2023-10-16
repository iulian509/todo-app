import React, { useState } from "react";

function Todo(props) {
  const [isEditing, setEditing] = useState(false);
  const [newTitle, setNewTitle] = useState(props.title);
  const [newPriority, setnewPriority] = useState(props.priority);

  const handleDeleteTask = (event) => {
    event.preventDefault();

    fetch("/api/todos/" + props.id, {
      method: "DELETE",
    })
      .then((response) => response.json())
      .catch((error) => console.error(error));

    props.deleteTask(props.id);
  };

  const handleInputTitleChange = (event) => {
    setNewTitle(event.target.value);
  };

  const handleInputPriorityChange = (event) => {
    setnewPriority(event.target.value);
  };

  function handleUpdateTask(e) {
    e.preventDefault();

    fetch("/api/todos/" + props.id, {
      method: "PUT",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: newTitle,
        priority: Number(newPriority),
      }),
    })
      .then((response) => response.json())
      .catch((error) => console.error(error));

    props.editTask(props.id, newTitle, newPriority);
    setEditing(false);
  }

  const editingTemplate = (
    <form className="row mb-2">
      <div className="col">
        <label htmlFor={"task" + props.id} className="visually-hidden">
          Task
        </label>
        <input
          type="text"
          className="form-control"
          id={"task" + props.id}
          placeholder={props.title}
          value={newTitle}
          onChange={handleInputTitleChange}
        />
      </div>
      <div className="col">
        <label htmlFor={"priority" + props.id} className="visually-hidden">
          Priority
        </label>
        <input
          type="number"
          min="1"
          className="form-control"
          id={"priority" + props.id}
          placeholder={props.priority}
          value={newPriority}
          onChange={handleInputPriorityChange}
        />
      </div>
      <div className="col-auto">
        <button
          type="button"
          className="btn btn-secondary col-auto"
          onClick={() => setEditing(false)}
        >
          Cancel
        </button>
      </div>
      <div className="col-auto">
        <button
          type="button"
          className="btn btn-primary"
          onClick={handleUpdateTask}
        >
          Save
        </button>
      </div>
    </form>
  );

  const viewTemplate = (
    <div className="row">
      <div className="col mt-1">
        <span className="badge bg-warning text-dark rounded-pill align-middle">
          {props.priority}
        </span>
        <span className="align-middle m-1">{props.title}</span>
      </div>
      <div className="col-auto">
        <button
          type="button"
          className="btn btn-secondary col-auto"
          onClick={() => setEditing(true)}
        >
          Update
        </button>
      </div>
      <div className="col-auto">
        <button
          type="button"
          className="btn btn-danger"
          onClick={handleDeleteTask}
        >
          Delete
        </button>
      </div>
    </div>
  );

  return (
    <li className="list-group-item">
      {isEditing ? editingTemplate : viewTemplate}
    </li>
  );
}

export default Todo;
