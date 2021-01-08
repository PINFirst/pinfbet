function validate()
{
    var name,surnames,email,user,nameexpression,emailexpression,password1,password2;
    name = document.getElementById("id_name").value;
    surnames = document.getElementById("id_surnames").value;
    email = document.getElementById("id_email").value;
    password1 = document.getElementById("id_password").value;
    password2 = document.getElementById("id_confirm").value;
    user = document.getElementById("id_username").value;
    emailexpression = /[a-z]+\.[a-z]+@alum\.uca\.es/;
    nameexpression = /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s[a-zA-ZÀ-ÿ\u00f1\u00d1]+)*$/;

    if(name === "" || !nameexpression.test(name)){
        document.getElementById("id_name").className ='error';
        document.getElementById("id_name").value  = "";
        return false;
    }
    else{
        document.getElementById("id_name").className ='input';
        if(surnames === "" || !nameexpression.test(surnames)){
            document.getElementById("id_surnames").className='error';
            document.getElementById("id_surnames").value  = "";
            return false;
        }
        else{
            document.getElementById("id_surnames").className='input';
            if(user === ""){
                document.getElementById("id_username").className='error';
                document.getElementById("id_username").value="";
                return false;
            }
            else{

                document.getElementById("id_username").className='input';
                if(email === "" || !emailexpression.test(email)){
                    document.getElementById("id_email").className='error';
                    document.getElementById("id_email").value  = "";
                    return false;
                }

                else{
                    document.getElementById("id_email").className='input';
                    if(password1 === "" || password2 === "" || password1 !== password2){
                        document.getElementById("id_password").className='error';
                        document.getElementById("id_password").value="";
                        document.getElementById("id_confirm").className='error';
                        document.getElementById("id_confirm").value="";
                        return false;
                    }
                    else{
                        document.getElementById("id_password").className='input';
                        document.getElementById("id_confirm").className='input';
                        return true;
                    }
                }
            }

        }
    }
}