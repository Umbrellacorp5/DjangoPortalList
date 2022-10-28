-- SQLite


DELETE FROM administracion_administrador WHERE codAdministrador = 1;

INSERT INTO administracion_administrador (codAdministrador, email, contraseña)
VALUES (5, 'quinto@gmail.com', '12345'); 

INSERT INTO administracion_usuario (cedula, email, nombre, apellido, contraseña, codAdministrador_id)
VALUES (5555,'quinto@gmail.com','nombre','password','5');

