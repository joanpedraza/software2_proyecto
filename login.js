const nombre=document.getElementById("nombre");
const apellidos=document.getElementById("apellidos");
const usuario=document.getElementById("nusuario");
const password=document.getElementById("contrasena");
const Vpassword=document.getElementById("confirmar_contrasena");
const form=document.getElementById("form");
const parrafo=document.getElementById("warnings");

form.addEventListener("submit", e => {
    e.preventDefault();
    let warnings=" ";
    let entrar=false;
    let tieneNumeros = /[0-9]/.test(password.value);
    let tieneCaracteresEspeciales = /[#%&/_]/.test(password.value);
    //Expresion regular para verificar si un correo es valido
    let email_Exp = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;

    parrafo.innerHTML=" ";

    if(!/[a-zA-Z]/.test(nombre.value)){
        warnings+='El nombre sólo debe contener caracteres alfabeticos. <br>';
        entrar=true;
    }

    if(!/[a-zA-Z]/.test(apellidos.value)){
        warnings+='Los apellidos sólo debe contener caracteres alfabeticos. <br>';
        entrar=true;
    }

    if(!email_Exp.test(usuario.value)){
        warnings+='Correo Electronico No valido. <br>';
        entrar=true;
    }


    if(password.value.length<8){
        warnings+='La contraseña debe tener más de 8 caracteres. <br>'
        entrar=true;
    }

    if (!(tieneNumeros && tieneCaracteresEspeciales)) {
        switch (true) {
            case !tieneNumeros:
                warnings += 'La contraseña debe contener al menos un número.<br>';
            case !tieneCaracteresEspeciales:
                warnings += 'La contraseña debe contener al menos un carácter especial (#, %, /, &, _).<br>';
            default:
                warnings += 'La contraseña no es válida.<br>';
        }
    
        entrar = true;
    }

    if(password.value!==Vpassword.value){
        warnings+='Las contraseñas tienen que ser iguales. <br>'
        entrar=true;
    }

    if(entrar==true){
        parrafo.innerHTML=warnings;
    } else{
        alert("Bienvenido" + " " + nombre.value + " " + apellidos.value + " " + "al sistema");
    }



});

  
