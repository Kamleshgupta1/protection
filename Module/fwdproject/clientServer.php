

<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = file_get_contents($site);
//echo $html;
$bytes=file_put_contents('markup.txt', $html);


$decision=exec("\Python27\python test.py $site 2>&1 ");

if($decision == "PHISHING"){
    echo('Un-verified Content');
}
else{
    echo('Verified Content');
}
?>
