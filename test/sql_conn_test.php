<?php

include_once('../src/m/PDOSingleton.php');
try {
    //$pdo = new PDO('mysql:host=cse345.carrio.me;dbname=project','tlcarrio','By$RLLupf#');
    $pdo = PDOSingleton::init()->getPDO();
    //$statement = $pdo->prepare("SELECT * FROM TEST_TABLE");
    $statement = $pdo->query("SELECT * FROM TEST_TABLE");
    
    while( $row = $statement->fetch(PDO::FETCH_ASSOC)){
        print(join(" | ",$row)."\n");    
    }
    print("Oh shit, that mysql connection string DID work!\n");

    } catch(PDOException $ex){
    die("Well fuck, that mysql connection string did NOT work!");
}
