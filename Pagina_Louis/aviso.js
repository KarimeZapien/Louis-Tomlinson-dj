/* La variable usuario tiene la respuesta */ 
usuario= window.confirm("¿Estás seguro de que deseas ingresar a esta página?");
if (!usuario)  /*Esto significa que si esto es falso*/ {
    // Si el usuario hace clic en "Cancelar", regresar a la página anterior
    window.history.back();
}
