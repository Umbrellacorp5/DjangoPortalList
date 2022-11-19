var dictAlumnos = JSON.parse('{{dictOfAlumnos|escapejs}}');

document.addEventListener("DOMContentLoaded", function () {
  showList(dictAlumnos)
});

 function showList(dictAlumnos){
    console.log(dictAlumnos)
    let htmlContentToAppend = "";
    for(let i = 0; i < dictAlumnos.length; i++){
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
