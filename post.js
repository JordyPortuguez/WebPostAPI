const APIURL='http://127.0.0.1:8000';
const Formulario= document.querySelector("#FormularioRegistro");

Formulario.addEventListener('submit',evento => {

evento.preventDefault()

const DatosFormulario = new FormData(Formulario)

let _datos = {
    Title: document.querySelector('#Title').value,
    Content: document.querySelector('#Content').value, 
  }

  fetch(`${APIURL}/posts`, {
    method: "POST",
    body: JSON.stringify(_datos),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })
  .then(response => response.json()) 
  .then(json => {console.log(json);
    window.alert("Agregado !!")})
  .catch(err => console.log(err));
   
   


})



