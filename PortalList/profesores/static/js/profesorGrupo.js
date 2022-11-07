GruposData = '{"name":"John", "materia":Matematicas}'



document.addEventListener("DOMContentLoaded", function (e) {
    console.log('document')
    getJSONData(GruposData).then(function(resultObj){
        if (resultObj.status === "ok"){
            console.log('resultadosOK')
            showGrupos(resultObj.data);
            
        }
    });
});


function showGrupos(data){
    console.log('funcion')
    let htmlContentToAppend = "";
    for(let i = 0; i < data.length; i++){
        let grupos = data[i];

        htmlContentToAppend += `
          <div class="col-md-4">
            <a href="product-info.html" class="card mb-4 shadow-sm custom-card">
              <img class="bd-placeholder-img card-img-top" src="${data.name}" alt="${data.materia}">
              <h3 class="m-3">${data.name}</h3>
              <div class="card-body">
                <p class="card-text">${data.materia}</p>
              </div>
        
            </a>
          </div>
            `

        document.getElementById("group-list-container").innerHTML = htmlContentToAppend;
    }
}