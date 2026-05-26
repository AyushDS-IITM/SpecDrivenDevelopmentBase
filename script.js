const form = document.querySelector("#todo-form");
const input = document.querySelector("#todo-input");
const list = document.querySelector("#todo-list");
const emptyMessage = document.querySelector("#empty-message");

function updateEmptyMessage() {
  const hasTodos = list.children.length > 0;
  emptyMessage.classList.toggle("hidden", hasTodos);
}

function createTodo(text) {
  const item = document.createElement("li");
  item.className = "todo-item";

  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.setAttribute("aria-label", `Mark "${text}" complete`);

  const span = document.createElement("span");
  span.className = "todo-text";
  span.textContent = text;

  const deleteButton = document.createElement("button");
  deleteButton.type = "button";
  deleteButton.className = "delete-button";
  deleteButton.textContent = "Delete";

  checkbox.addEventListener("change", () => {
    item.classList.toggle("completed", checkbox.checked);
  });

  deleteButton.addEventListener("click", () => {
    item.remove();
    updateEmptyMessage();
  });

  item.append(checkbox, span, deleteButton);
  return item;
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const todoText = input.value.trim();

  if (todoText === "") {
    return;
  }

  list.append(createTodo(todoText));
  input.value = "";
  input.focus();
  updateEmptyMessage();
});

updateEmptyMessage();
