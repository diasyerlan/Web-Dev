let ask = (question, yes, no) => {
  return (confirm(question)) ? yes()
  :no();
}
ask(
    "Do you agree?",
    () => alert("You agreed."),
    () => alert("You canceled the execution.")
  );