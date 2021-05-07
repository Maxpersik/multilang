<?php
$aR = $argv;
$S = 0;

for ($r = 1; $r < count($aR); $r++)
{
    $S += 1/$aR[$r];
}

$R = 1/$S;
echo "Общее сопротивление равно: ".round($R, 2)." Ом";  
?>  
