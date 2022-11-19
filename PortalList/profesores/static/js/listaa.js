var dictAlumnos = JSON.parse("{{dictOfAlumnos|escapejs}}");
console.log(dictAlumnos)
document.addEventListener("DOMContentLoaded", function () {

});


function showList(dictAlumnos){
  console.log(dictAlumnos)
  let htmlContentToAppend = "";
  for(let i = 0; i < dictAlumnos.length; i++){
      let infoAlumnos = dictAlumnos[i];

      htmlContentToAppend += `
            <tr >
              <p>{{alumno}}</p>
              <td><img src="" width="50" height="60"> </td>
              <td>${dictAlumnos.alumno1}</td>
              <td>${dictAlumnos.alumno1}</td>
              <td>${dictAlumnos.alumno1}</td>
                
            </tr>
          `

      document.getElementById("AlumnoTable").innerHTML = htmlContentToAppend;
  }
}



{% comment %} function checkList(alumno){
  if (alumno.falta == 1){
    document.getElementById("data.CI").checked = true;
  }
  if (alumno.falta == 2){
    document.getElementById("data.CI").checked = true;
  }
  if (alumno.falta == 3){
    document.getElementById("data.CI").checked = false;
  }
} {% endcomment %}