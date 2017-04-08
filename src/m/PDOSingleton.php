<?php

    class PDOSingleton {
        public static $_instance;
        public $_pdo;

        private function __construct() {
             $this->$_pdo = new PDO('mysql:host=cse345.carrio.me;dbname=project','tlcarrio','By$RLLupf#');
        }

        public static function init(){
            if(self::$_instance == null){
                self::$_instance = new self();
            }
            return self::$_instance;
        }

        public function getPDO(){
            return $this->$_pdo;
        }
    }

    class PDOConnection {
        private $_pdo;

        public function __construct() {
            $this->$_pdo = new PDO('mysql:host=cse345.carrio.me;dbname=project','tlcarrio','By$RLLupf#');
        }

        public function getPDO(){
            return $this->$_pdo;
        }

    }

?>