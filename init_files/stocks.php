<!DOCTYPE html>
<style> <?php include "__ DIR __./style/style.css"; ?> </style>
<html>
    <head>
        <link rel="stylesheet" href="../style/style.css">
        <h1>Analisador de ações</h1>
    <head>
</html>

<!-- <?php
define('style/style.css', 'template/css/'); //define CSS path 
//define('JS_PATH', 'template/js/'); //define JavaScript path 
?> -->
<!-- 
 -->
<?php
ini_set('display_errors',1);
//init_set('display_startup_erros', 1);
// ini_set('log_errors',1);
// Print a greeting if the form was submitted
if ($_POST['stock-picked']) {
print "Ação escolhida: ";print $_POST['stock-picked'];
$stock_name = $_POST['stock-picked'];
//chmod("/", 777);
print"<br> start opening";
$FileHandle = fopen("stocks/stock-picked/stock-picked.env","w");
$stock_env = "STOCK-PICKED"."=\"$stock_name\"";
fwrite($FileHandle, $stock_env);
fclose($FileHandle);
print"\n fim do bloco" ;
} else {
// Otherwise, print the form
print <<<_HTML_
<form method="post" action="$_SERVER[PHP_SELF]">
    <fieldset name="stock-picked-fds">
        <legend>Escolha uma ação da B3</legend>
        <input type="text"
        placeholder="Ex: bbas3"
        name="stock-picked">
        <button 
        type="submit"
        name="stock-picked-btn">Confirmar
        </button>
    </fieldset>
</form>
_HTML_;
}
?>







