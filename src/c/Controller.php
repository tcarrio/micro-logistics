<?php
    session_start();
    include_once("m/Model.php");

    class Controller {
        public $model;

        public function __construct(){
            $this->model = new Model();
        }

        public function invoke(){
            if(isset($_POST["login"])){
                if(isset($_POST["pass"])){
                    // check password and return correct page/error
                    
                } else {
                    // no password given, return error and go to
                    include 'v/login.php';
                }   
            } else if(isset($_SESSION['login'])){
                // user is logged in and ready to go
                include 'v/customer.php';
            } else {
                // main login page, no login attempt / error
                include 'v/login.php';
            }
        }
    }