<!DOCTYPE html>
<html>
<head>
    <title>Indian Express Sentiment Analysis</title>
    <link rel="stylesheet" type="text/css" href="stylephp.css">
    <meta http-equiv="refresh" content="15">
</head>
<body style='background-color:grey;background-image: url("https://ak5.picdn.net/shutterstock/videos/19404958/thumb/11.jpg");'>

<?php 
    
    echo shell_exec("python analyser.py");
    ?>
    <h1 style="background-color:pink; color:grey; padding: 3%;text-align: center; ">INDIAN EXPRESS REAL TIME NEWS ANALYSIS</h1>
    <ul>
    <?php
    
    $positiveCount=1;
    $positive = fopen("positive-news.txt","r") or die("Unable to open the file positive-news.txt");
    $negative=fopen("negative-news.txt","r") or die("Unable to open the file negative-news.txt");
    $neutral=fopen("neutral-news.txt","r") or die ("Unable to open the file neutral-news.txt")
    ?> <h1 style="background-color: lightgreen; padding:2%;"> <txt style="color:darkviolet;text-decoration:underline;">Postive News</txt></h1>
    <?php
    while(!feof($positive))
    {
        ?><h2 style="background-color: lightyellow; padding:1%"><?php echo fgets($positive);
        ?><br>
        <?php
        $positiveCount+=1;

    }
    ?><h1 style="background-color: red;padding:2%;text-decoration: underline;">Negative News</h1><?php
    while(!feof($negative))
    {
        ?><h2 style="background-color: darkorange; padding:1%"><?php echo fgets($negative);
        ?><br>
        <?php
    } 
    ?><h1 style="background-color: blue;padding: 2%">Neutral News</h1><?php

    while(!feof($neutral))
    {
        ?><h2 style="background-color: lightblue; padding:1%"><?php echo fgets($neutral);
        ?><br>
        <?php
    } 

    #$postiveText=fread($positive,filesize('positive-news.txt'));
    #$negativeText=fread($negative,filesize('negative-news.txt'));

    

    fclose($positive);

    $Color="yellow";
    

 ?>




</body>
</html>