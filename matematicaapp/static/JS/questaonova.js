var elementohtml = document.getElementById("howmany");
elementohtml.onchange = numerodealternativas();
function makeajax(bola, carro) {
  const request = new Request("", { headers: { "X-CSRFToken": carro } });
  fetch(request, {
    method: "POST",
    mode: "same-origin", // Do not send CSRF token to another domain.
  }).then(function (response) {
    alert("FOI CARAJOOOOO");
  });

  /*  $.ajax({
    method: "POST",
    url: "",
    data: { howMany: bola },
    success: function (data) {
      alert("FOI CARAJOOOOO");
    },
    error: function (data) {
      console.log(data);
      alert("NAO TA FUNCIONANDO MDS VC EH BURRO");
    },
  }); */
}
function numerodealternativas() {
  var howmany = elementohtml.value;
  console.log(howmany);
  const csrftoken = Cookies.get("csrftoken");
  $(document).ready(makeajax(howmany));
}
