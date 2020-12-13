function revisar(elemento){
    if(elemento.value==''){ //si el campo está vacío
        elemento.className='error';
    }else{
        elemento.className='input';
    }
}

function revisarEmail(elemento){
    if(elemento.value!==''){
        var data = elemento.value
        var exp = /\w+@\w+\.+[a-z]/ //expresión de email
        if(!exp.test(data)){ //si no cumple la expresión
            elemento.className='error';
        }else{
            elemento.className='input';
        }
    }
}
function revisarNombre(elemento){
    if(elemento.value!==''){
        var data = elemento.value;
        var exp = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s[a-zA-ZÀ-ÿ\u00f1\u00d1]+)*$/; //expresión para nombre simple o compuesto
        if(!exp.test(data)){
            elemento.className='error';
        }else{
            elemento.className='input';
        }
    }
}
function revisarApellidos(elemento){
    if(elemento.value!==''){
        var data = elemento.value;
        var exp = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s[a-zA-ZÀ-ÿ\u00f1\u00d1]+)*$/; //expresión para uno o varios apellidos
        if(!exp.test(data)){
            elemento.className='error';
        }else{
            elemento.className='input';
        }
    }
}

function validar()
{
    var nombre,apellidos,correo,expresionnombre,expresionemail;
    nombre = document.getElementById("nombre").value;
    apellidos = document.getElementById("apellidos").value;
    correo = document.getElementById("correo").value;
    expresionemail = /\w+@\w+\.+[a-z]/;
    expresionnombre = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s[a-zA-ZÀ-ÿ\u00f1\u00d1]+)*$/;

    if(nombre === "" || !expresionnombre.test(nombre)){
        document.getElementById("nombre").className ='error';
        document.getElementById("nombre").value  = "";
        return false;
    }
    else if(apellidos === "" || !expresionnombre.test(apellidos)){
        document.getElementById("apellidos").className='error';
        document.getElementById("apellidos").value  = "";
        return false;
    }
    else if(correo === "" || !expresionemail.test(correo)){
        document.getElementById("correo").className='error';
        document.getElementById("correo").value  = "";
        return false;
    }
    else if(usuario === ""){
        document.getElementById("usuario").className='error';
        document.getElementById("usuario").value="";
        return false;
    }

    else
        return true;

}
function Registro(){

    console.log(validar()); //comprobamos si todos los datos son correctos

}