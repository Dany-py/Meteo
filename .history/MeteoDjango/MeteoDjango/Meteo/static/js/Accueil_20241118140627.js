
addEventListener("DOMContentLoaded", () => Ma_signature());

const input = document.querySelector("#input");

const response = document.querySelector("#req");

const button = document.querySelector("#btn");

button.addEventListener("click", () => Meteo_API());

function Meteo_API() {
  if(input.value == ""){
    alert("Veuillez saisir une ville");
  } else {
    fetch('api_request_view/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'town': input.value,
      })
    }).then((response) => {
      return response.json();
    }).then((data) => {
      const data_text = document.createElement("p");
      data_text.innerText = data.message;
      console.log(data);
      response.innerText = ""; // Assure que l'élément "response" est vidé
      response.appendChild(data_text); // Ajoute le paragraphe au DOM
    }).catch((error) => {
      console.error("Erreur lors de la requête:", error);
    });
  }
}



function Ma_signature() {
  const p =
    "Site réaliser par DEGBE Koffitsè Daniel. Contact : www.linkedin.com/in/daniel-degbe-a4078629b";
  console.log(p);
}
