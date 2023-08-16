<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];
    $correo = $_POST["correo"];
    $contrasena = $_POST["contrasena"];

    // Realiza aquí la validación y almacenamiento de la información del usuario
    // Ejemplo básico (¡NO RECOMENDADO para uso real!):
    // Aquí podrías insertar los datos en una base de datos, encriptar la contraseña, etc.
    echo "Usuario registrado exitosamente";
}
?>
