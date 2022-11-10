  
  document.addEventListener("DOMContentLoaded", function () {
    showLista(alumnosData);
  });
  
  function showLista(data){
    let htmlContentToAppend = "";
    for(let i = 0; i < data.length; i++){
        let alumnos = data[i];
  
        htmlContentToAppend += `
              <tr >
                <td><img src="${alumnos.foto}" width="50" height="60"> </td>
                <td>${alumnos.nombre}</td>
                <td>${alumnos.apellido}</td>
                <td>${alumnos.CI}</td>
                <td>
                  <select name=" optionlist " onChange="combo(this, 'falta')">
                  <option selected="true">${alumnos.falta}</option>
                  <option>${alumnos.falta}</option>
                  </select></td>
              </tr>
            `
  
        document.getElementById("AlumnoTable").innerHTML = htmlContentToAppend;
    }
  }


  alumnosData = [
    {
        "foto": "123456789.jpg",
        "nombre": "Jose",
        "apellido": "Gomez",
        "CI": "123456789",
        "falta": "True",
    },
    {
        "foto": "1223456789.jpg",
        "nombre": "Franco",
        "apellido": "Gomez",
        "CI": "223456789",
        "falta": "False",
    },
    {
      "foto": "323456789.jpg",
      "nombre": "Juan",
      "apellido": "Gomez",
      "CI": "523456789",
      "falta": "True",
    },
    {
      "foto": "423456789.jpg",
      "nombre": "Pedro",
      "apellido": "Gomez",
      "CI": "623456789",
      "falta": "True",
    },
    {
      "foto": "523456789.jpg",
      "nombre": "Renzo",
      "apellido": "Gomez",
      "CI": "823456789",
      "falta": "True",
    },
    {
      "foto": "123456789.jpg",
      "nombre": "Julio",
      "apellido": "Gomez",
      "CI": "923456789",
      "falta": "True",
    },
  ]