// al darle al botón, si los datos coínciden redirecciona a página asistí, en caso de que los datos estén incorrectos poner un mensaje de error

const usuario ="a";
const contra = "a";

document.getElementById("btnLoginIP").addEventListener("click", function iniciarSesion() {
     if(usuario === document.getElementById("inputUsuarioIP").value && contra === document.getElementById("inputContraseñaIP").value){
        window.location.replace ("/templates/asistencia.html");
        document.getElementById("correctoIP").innerHTML = "Has ingresado correctamente.";
      }
      else{
        document.getElementById("incorrectoIP").innerHTML = "El usuario ingresado no existe.";
      }
})

// JavaScript de Admin //

document.getElementById("btnCrearAlumno").addEventListenerEventListener("click", function IngresarCrearAlumno () {
  document.getElementById("btnCA").innerHTML = "Has ingresado correctamente."

// JavaScript de Registrar Alumno //

const NombreRA = "a";
const ApellidoRA = "a"; 
const CedulaRA = "a";
const NumeroPadreRA = "a";
const FotoRA = "a";
const GrupoRA = "a";
const EmailRA = "a";
const UsuarioCiRA = "a";
const ContraseñaRA = "a";

document.getElementById("btnRegistrarAlumno").addEventListener("click", function RegistrarAlumno() {
  if (NombreRA === document.getElementById("inputNombreRA").value){                                    //&& ApellidoRA === document.getElementById("inputApellidoRA").value && CedulaRA === document.getElementById("inputCedulaRA").value && NumeroPadreRA === document.getElementById("inputNumeroPadreRA").value && FotoRA === document.getElementById("inputFotoRA").value && GrupoRA === document.getElementById("inputGrupoRA").value && EmailRA === document.getElementById("inputEmailRA").value && UsuarioCiRA === document.getElementById("inputUsuarioCiRA").value && ContraseñaRA === document.getElementById("inputContraseñaRA").value){
    window.location.replace("//templates/ingresarAlumno.html");
    document.getElementById("correctoRA").innerHTML = "Te has registrado correctamente.";
    }
    else{
      document.getElementById("incorrectoRA").innerHTML = "No has podido registrarte correctamente."
    }
})})


