
var datajs = JSON.parse("{{datajs|escapejs}}");

document.addEventListener("DOMContentLoaded", function (e) {
showGrupos(datajs);

});

function showGrupos(data){
let htmlContentToAppend = "";
for(var x in data){
    htmlContentToAppend += `
    <form method="POST">
      {% csrf_token %}
      <div class="card">
        <div class="container">
          <h4><b>"${data.NombreGrupo}"</b></h4>
          <p>${data.NombreMateria}</p>
          <button class="btn btn-primary" type="sumbit">Ingresar a la Lista</button> 
        </div>
      </div>
    </form>
    `
    document.getElementById("group-list-container").innerHTML = htmlContentToAppend;
}
}

GruposData = [
  {
      "name": "3BK",
      "materia": "math"
  },
  {
      "name": "2BA",
      "materia": "programacion"
  },
  {
      "name": "2BB",
      "materia": "programacion"
  },
  {
    "name": "1A",
    "materia": "programacion"
},
{
      "name": "1B",
      "materia": "programacion"
  },
  {
    "name": "1C",
    "materia": "programacion"
}
]