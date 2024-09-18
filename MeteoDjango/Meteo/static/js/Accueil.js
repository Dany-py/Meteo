const entrie = document.querySelector("#put");

let recive = "";

const retour = document.querySelector("#response");

const bouton = document.querySelector("#btn");

let ville_presente = false;

addEventListener("DOMContentLoaded", () => Ma_signature());
const url =
  "https://api.meteo-concept.com/api/forecast/daily/0?token=36ef80f9b9c5e2310d624239d73726c34673d397cf14101abb5c1e8239ce23f4&insee=";

let Code_INSEE = new Object();

Code_INSEE = {
  Paris: "75056",
  Marseille: "13055",
  Lyon: "69123",
  Toulouse: "31555",
  Nice: "06088",
  Nantes: "44109",
  Montpellier: "34172",
  Strasbourg: "67482",
  Bordeaux: "33063",
  Lille: "59350",
  Rennes: "35238",
  Toulon: "83137",
  Reims: "51454",
  Saint_Etienne: "42218",
  Havre: "76351",
  Dijon: "21231",
  Grenoble: "38185",
  Angers: "49007",
  Villeurbanne: "69266",
  Saint_Denis: "93066",
  Nimes: "30189",
  Aix_en_Provence: "13001",
  Clermont_Ferrand: "63113",
  Le_Mans: "72181",
  Brest: "29019",
  Tours: "37261",
  Amiens: "80021",
  Annecy: "74010",
  Limoges: "87085",
  Metz: "57463",
  Boulogne_Billancourt: "92012",
  Perpignan: "66136",
  Besançon: "25056",
  Orléans: "45234",
  Rouen: "76540",
  Montreuil: "93048",
  Caen: "14118",
  Argenteuil: "95018",
  Mulhouse: "68224",
  Saint_Paul: "73269",
  Nancy: "54395",
  Tourcoing: "59599",
  Roubaix: "59512",
  Nanterre: "92050",
  Vitry_sur_Seine: "94081",
  Créteil: "94028",
  Avignon: "84007",
  Poitiers: "86194",
  Aubervilliers: "93001",
};

bouton.addEventListener("click", () => Meteo_API(recive));

function Meteo_API(ville) {
  ville = entrie.value;
  retour.innerText = "Un instant";
  if (Code_INSEE[ville] == undefined) {
    const re = document.createElement("p");
    alert("Saisisez une autre ville");
    re.innerText =
      "Nous sommes désolé, nous ne disposons que des informations sur les villes de France";
    retour.innerText = "";
    retour.appendChild(re);
  } else {
    fetch(url + Code_INSEE[ville])
      .then((reponse) => {
        return reponse.json();
      })
      .then((attribut) => {
        let city = new Object();
        let proprieter = new Object();
        const ptext = document.createElement("p");
        city = attribut.city;
        proprieter = attribut.forecast;
        ptext.innerText =
          "Votre ville " +
          city.name +
          ", pour aujourd'hui" +
          ", a " +
          proprieter.probafog +
          "% de risque de brouillard, " +
          proprieter.probafrost +
          "% de risque de givre, " +
          proprieter.probarain +
          "% de risque de pluie";
        retour.innerText = "";
        retour.appendChild(ptext);
      });
  }
}

function Ma_signature() {
  const p =
    "Site réaliser par DEGBE Koffitsè Daniel. Contact : www.linkedin.com/in/daniel-degbe-a4078629b";
  console.log(p);
}
