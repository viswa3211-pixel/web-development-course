function validateForm() {
  let name = document.getElementById("name").value;
  let age = document.getElementById("age").value;
  let message = document.getElementById("message");

  // Check if name is empty
  if (name === "") {
    message.innerHTML = "Name cannot be empty!";
    message.style.color = "red";
    return false;
  }

  // Check if age is empty or less than 18
  if (age === "" || age < 18) {
    message.innerHTML = "You must be at least 18 years old.";
    message.style.color = "red";
    return false;
  }

  // If everything is valid
  message.innerHTML = "Login successful!";
  message.style.color = "green";
  return false; // keep false to prevent actual form submission (for projects)
}
