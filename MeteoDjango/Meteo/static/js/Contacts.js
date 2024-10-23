addEventListener("DOMContentLoaded", () => Ma_signature());

const mail = document.querySelector("#exampleFormControlInput1");

const content = document.querySelector("#exampleFormControlTextarea1")

const button =  document.querySelector("#btn");

button.addEventListener("click", () => Send_contact_message());

function Send_contact_message() {
  if(mail.value == "" || content.value == "" ){
    alert("fill in all fields");
  }else{
    fetch('send_contact_message/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',        
      },
      body : JSON.stringify({
        'email' : mail.value,
        'message' : content.value
      })
    }).then((response) =>  {
      return response.json()
    }).then((data) => {
      alert(data.message)
    })
  }
}


function Ma_signature() {
  const p =
    "Site réaliser par DEGBE Koffitsè Daniel. Contact : www.linkedin.com/in/daniel-degbe-a4078629b";
  console.log(p);
}
