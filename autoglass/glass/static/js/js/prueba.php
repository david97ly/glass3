<?php
  
$con = mysql_connect("localhost","dcrexploradores","dcr1276512");
mysql_select_db("regionlacosta",$con);
 $sql ="Select * from noticias";
 $q = mysql_query($sql,$con);
$re = mysql_fetch_array($q);

####################################################################

function saludo(){

	echo "<strong>David cortez</strong>";
}


class DB_mysql { 

  /* variables de conexión */ 
	 var $BaseDatos;
	 var $Servidor; 
	 var $Usuario; 
	 var $Clave; 
	     /* identificador de conexión y consulta */ 
	 var $Conexion_ID = 0; 
	 var $Consulta_ID = 0;   
	     /* número de error y texto error */ 
	 var $Errno = 0;
	 var $Error = "";   
	 var $consulta;

	 /* Método Constructor: Cada vez que creemos una variablede esta clase, se ejecutará esta función */ 
function DB_mysql($bd = "regionlacosta", $host = "localhost", $user = "dcrexploradores", $pass = "dcr1276512") { 
 $this->BaseDatos = $bd;
 $this->Servidor = $host; 
 $this->Usuario = $user; 
 $this->Clave = $pass; 
} 
  /*Conexión a la base de datos*/
   function conectar(){   

// Conectamos al servidor
 $this->Conexion_ID = mysql_connect($this->Servidor, $this->Usuario, $this->Clave); 
 if (!$this->Conexion_ID) { 
$this->Error = "Ha fallado la conexión."; 
return 0; 
} 

//seleccionamos la base de datos 
if (!@mysql_select_db($this->BaseDatos, $this->Conexion_ID)) { 
} 
$this->Error = "Imposible abrir ".$this->BaseDatos ; 
return 0; 

  /* Si hemos tenido éxito conectando devuelve  el identificador de la conexión, sino devuelve 0 */ 
  return $this->Conexion_ID; 
}  
 /* Ejecuta un consulta */ 
function consulta($sql = ""){   
if ($sql == "") { 
 $this->Error = "No ha especificado una consulta SQL";
  return 0; 
}   

  //ejecutamos la consulta 
$this->Consulta_ID = @mysql_query($sql, $this->Conexion_ID);  
 if (!$this->Consulta_ID) { 
$this->Errno = mysql_errno(); 
$this->Error = mysql_error(); 
}
 /* Si hemos tenido éxito en la consulta devuelve  el identificador de la conexión, sino devuelve 0 */ 
return $this->Consulta_ID; 
} 
  /* Devuelve el número de campos de una consulta */
 function numcampos() { 
return mysql_num_fields($this->Consulta_ID); 
}  
 /* Devuelve el número de registros de una consulta */ 
 function numfilas(){ 
return mysql_num_rows($this->Consulta_ID);
 } 

 /* Devuelve el nombre de un campo de una consulta */ 
 function nombrecampo($numcampo) { 
return mysql_field_name($this->Consulta_ID, $numcampo); 
}  
 /* Muestra los datos de una consulta */
 function getconsulta() {   
   return  $this->consulta = mysql_fetch_array($this->Consulta_ID);
}    
 } 
 //fin de la Clse DB_mysql 
?>