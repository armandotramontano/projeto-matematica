function marcaACerta() {
  const alternativas = document.getElementsByClassName("alternativas");
  const resposta = document.getElementsByClassName("corretaInput")[0];
  for (let input of alternativas) {
    if (input.checked) {
      if (input.value != resposta.value) {
        input.nextElementSibling.style.backgroundColor = "red";
      }
    }
  }
  document.getElementsByClassName("corretaLabel")[0].style.backgroundColor =
    "green";
}
