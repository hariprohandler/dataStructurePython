<?php
$matrix = array(
array(1,2,3,4,5),
array(16,17,18,19, 6),
array(15, 24, 25, 20, 7),
array(14, 23, 22, 21, 8 ),
array(13, 12, 11, 10, 9)
);
$finalArr = array();
$max_i = 0;
$max_j = 0;
$i =0;
$j =0; 
$r = $c = count($matrix);
while($max_i < $r){
    
    //print top to bottom
    $i = $max_i;
    $j = $max_j;
    while($i < $c){
        echo ($matrix[$i][$j])."-->";
        $i++;
    }
    
    //print left to right
    $i--;
    $j++;
    while($j < $c){
        echo ($matrix[$i][$j])."-->";
        $j++;
    }
    
    //print bottom to top
    $j--;
    $i--;
    while($i >= $max_i){
        echo ($matrix[$i][$j])."-->";
        $i--;
    }
    
    //print right to left
    $j--;
    $i++;
    while($j > $max_j){
        echo ($matrix[$i][$j])."-->";
        $j--;
    }
    
    $max_i++;
    $max_j++;
    $c--;
}

//Approach 2 => single loop
/*$mult = count($matrix);
$max_i = 4;
$max_j = 4;
$min_i = 0;
$min_j = 0;

for($i = 0, $j = 0;$i< $mult;$i++){
    
}
 * 
 */