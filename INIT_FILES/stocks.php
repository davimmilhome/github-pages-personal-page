<?php
ini_set('display_errors',0);
ini_set('log_errors',1);
echo whoami;
// Print a greeting if the form was submitted
if ($_POST['stock']) {
print "Ação escolhida: ";print $_POST['stock'];
$stock_name = $_POST['stock'];
//chmod("/", 777);
print"\n start opening open";
$FileHandle = fopen("1.txt", w); print"try to open";
$FileHandle = fopen("1.txt", w) or die("can't open file");
fclose($FileHandle);
print"\n fim do bloco" ;
} else {
// Otherwise, print the form
print <<<_HTML_
<form method="post" action="$_SERVER[PHP_SELF]">
Escolha uma ação da B3: <input type="text" name="stock" />
<span><button type="submit">confirmar</button></span>
</form>
_HTML_;
}
?>







