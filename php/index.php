 <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<div>
    <button id="1"> A</button>
    <button ="2"> B</button>
</div>
 <script>
 $('div button').on('click', function(ele){
     console.log(ele);
     if($(ele).children().length ==0 ){
         console.log($(ele).parent());
     }
 })
 </script>
<?php




exit;
function getLen($str=""){
    $count = 0;
    while($str[$count]){
        $count++;
    }
    return $count;
}
$str = "Hari Prasad Sharma";

$cnt =getLen($str);
for($i= $cnt-1;$i>=0;$i--){
    $revStr = "";
}

$arr = array(1,2,2,3,4,4,4);
$count = array();
$finalArr = array();
//single loop 
//remove unique values & keep duplicate
for($i=0;$i<count($arr);$i++){
    if(!$count[$arr[$i]]){
        $count[$arr[$i]] = 0;
    }   
    $count[$arr[$i]]++;
    if($count[$arr[$i]] > 1){
        $finalArr[] = $arr[$i];
        while($count[$arr[$i]] > 1){
            $finalArr[] = $arr[$i];
            $count[$arr[$i]]--;
        }
    }
}
print_r($finalArr);
exit;


//remove unique values & keep duplicate
for($i=0;$i<count($arr);$i++){
    if(!$count[$arr[$i]]){
        $count[$arr[$i]] = 0;
    }
    $count[$arr[$i]]++;
}
$arr = [];
foreach ($count as $key => $value) {
    if($value > 1){
        $arr[] = $key;
    }
}

print_r($arr);


?>