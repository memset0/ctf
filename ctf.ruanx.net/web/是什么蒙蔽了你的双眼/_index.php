<?php
/*
 * https://www.cnblogs.com/embedded-linux/p/12638906.html
 * Date: 2016-12-20 23:26
 */
error_reporting(E_ALL || ~E_NOTICE);


header('content-type:text/html;charset=utf-8');
if(!isset($_GET['jpg'])){
    header('Refresh:0;url=./index.php?jpg=V20xNGFGcDVOWEZqUjJNOQ==');
}
$file = base64_decode(base64_decode(base64_decode($_GET['jpg'])));
echo '<title>'.$_GET['jpg'].'</title>';
$file = preg_replace("/[^a-zA-Z0-9.]+/","", $file);
echo $file.'</br>';
$file = str_replace("config","!", $file);
echo $file.'</br>';
$txt = base64_encode(file_get_contents($file));

echo "<img src='data:image/gif;base64,".$txt."'></img>";
/*
 * Can you find the flag file?
 *
 */

?>