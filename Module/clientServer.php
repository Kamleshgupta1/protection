

<?php
header("Access-Control-Allow-Origin: *");
$site=$_POST['url'];
$html = file_get_contents($site);
//echo $html;
// Purpose - This file acts as a mediator between the client side popup.js and the server side test.py.
// It gets the HTML contents which acts as input to the suite of python files.

$bytes=file_put_contents('markup.txt', $html);


$decision=exec("\Python34\python test.py $site 2>&1 ");
//echo $decision;

if($decision == "PHISHING"){
    echo('Un-verified Content');
}
else{
    echo('Verified Content');
}
?>
