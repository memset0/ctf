<?php
include('config.php');
$k = 'flag!flag!';
extract($_GET);
if(isset($t))
{
    $content=trim(file_get_contents($k));
    if($t==$content)
    {
        echo $flag;
    }
    else
    {
        echo'flag!flag!';
    }
}
?>