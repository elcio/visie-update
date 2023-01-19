<?php

$pessoa = json_decode(file_get_contents('php://input'));
echo "<p>Olá {$pessoa->nome}, você tem {$pessoa->idade} anos</p>";

