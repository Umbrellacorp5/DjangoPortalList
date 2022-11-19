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
        <div class="card" id="cardSL">
          <div class="container" id="containerSL">
            <h4><b>"${data.NombreGrupo}"</b></h4>
            <p>${data.NombreMateria}</p>
            <button id="botonSL" class="btn btn-primary">Ingresar a la Lista</button> 
          </div>
        </div>
      </form>
      `
      document.getElementById("group-list-container").innerHTML = htmlContentToAppend;
  }
}