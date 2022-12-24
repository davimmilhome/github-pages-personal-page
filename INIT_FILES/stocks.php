<?php
// Print a greeting if the form was submitted
if ($_POST['stock']) {
print "Ação escolhida: ";print $_POST['stock'];
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







