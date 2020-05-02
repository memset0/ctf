<?php
error_reporting(0);
session_start();
include "config.php";

$username = $_POST['username'];
$password = $_POST['password'];
if (isset($username)){
    $sql = "select password from user where username=?";
    if ($stmt = $conn->prepare($sql)) {
        $stmt->bind_param("s", $username);
        $stmt->execute();
        $stmt->bind_result($dpasswd);
        $stmt->fetch();
        if ($dpasswd === $password){
            $_SESSION['login'] = 1;
            header("Location: /flag.php");
        }else{
            header("Location: /index.php?status=0");
        }
        $stmt->close();
    }
}else{
    header("Location: /index.php");
}

$conn->close();