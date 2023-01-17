<!DOCTYPE html>
<style> <?php include "__ DIR __./style/style.css"; ?> </style>
<html>
    <head>
        <link rel="stylesheet" href="../style/style.css">
        <h1>ola</h1>
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
// init_set('display_startup_erros', 1);
ini_set('log_errors',1);
// Print a greeting if the form was submitted
if ($_POST['stock']) {
print "Ação escolhida: ";print $_POST['stock'];
$stock_name = $_POST['stock'];
//chmod("/", 777);
print"<br> start opening";
$FileHandle = fopen("$stock_name .txt", w); print"\n try to open";
fclose($FileHandle);
print"\n fim do bloco" ;
} else {
// Otherwise, print the form
print <<<_HTML_
<form method="post" action="$_SERVER[PHP_SELF]">
    <fieldset name="stock-picked">
     <legend>Escolha uma ação da B3</legend>
     <input type="text"
      placeholder="Ex: bbas3">
     <button type="submit"  class="button medium-btn" name="stock-picked"></button>
    </fieldset>
</form>
_HTML_;

}
?>







