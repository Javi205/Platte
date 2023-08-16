<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = $_POST["usuario"];
    $contrasena = $_POST["contrasena"];

    // Realiza aquí la validación de usuario y contraseña
    // Ejemplo básico (¡NO RECOMENDADO para uso real!):
    if ($usuario === "usuario" && $contrasena === "contrasena") {
        header("Location: bienvenido.php"); // Redirige a la página de bienvenida
        exit();
    } else {
        echo "Usuario o contraseña incorrectos";
    }
}
?>
