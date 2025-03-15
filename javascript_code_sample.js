function greetRobot(name) {
  let exampleString = "example string";

  document.getElementById("output").innerHTML = "Hello, " + name;
}

document.getElementById("btn").addEventListener("click", function () {
  let userInput = document.getElementById("inputName").value;
  greetRobot(userInput);
});
