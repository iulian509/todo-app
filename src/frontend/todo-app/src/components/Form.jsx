import React, { useState } from "react";

function Form(props) {
  const [inputTitle, setInputTitle] = useState("");
  const [inputPriority, setInputPriority] = useState("");
  const [inputTitleError, setinputTitleError] = useState("");
  const [inputPriorityError, setinputPriorityError] = useState("");

  const handleAddTodo = (event) => {
    event.preventDefault();
    if (inputTitle.length == 0 || inputPriority.length == 0) {
      setinputTitleError(inputTitle.length == 0 ? "is-invalid" : "");
      setinputPriorityError(inputPriority.length == 0 ? "is-invalid" : "");
    } else {
      fetch("/api/todos/", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: inputTitle,
          priority: Number(inputPriority),
        }),
      })
        .then((response) => response.json())
        .then((data) => props.addTask(data.id, inputTitle, inputPriority))
        .catch((error) => console.error(error));

      setInputTitle("");
      setInputPriority("");
      setinputTitleError("");
      setinputPriorityError("");
    }
  };

  const handleInputTitleChange = (event) => {
    setInputTitle(event.target.value);
  };

  const handleInputPriorityChange = (event) => {
    setInputPriority(event.target.value);
  };

  return (
    <form className="row">
      <div className="col">
        <label htmlFor="task" className="visually-hidden">
          Task
        </label>
        <input
          type="text"
          className={"form-control " + inputTitleError}
          id="task"
          placeholder="Task"
          required
          value={inputTitle}
          onChange={handleInputTitleChange}
        />
      </div>
      <div className="col">
        <label htmlFor="priority" className="visually-hidden">
          Priority
        </label>
        <input
          type="number"
          min="1"
          className={"form-control " + inputPriorityError}
          id="priority"
          placeholder="Priority"
          required
          value={inputPriority}
          onChange={handleInputPriorityChange}
        />
      </div>
      <div className="col-auto">
        <button
          type="submit"
          className="btn btn-primary mb-3"
          onClick={handleAddTodo}
        >
          Add
        </button>
      </div>
    </form>
  );
}

export default Form;
