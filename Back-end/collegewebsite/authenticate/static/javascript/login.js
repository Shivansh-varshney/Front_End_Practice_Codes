function change1(){
    let i = 0;
    
    var elementList = document.getElementsByClassName('change');
    for(i; i<elementList.length; i++){
        elementList[i].innerHTML = "Sign-Up";
    }

    document.getElementById('emaildiv').style.display = 'block';
    document.getElementById('form').setAttribute("action", "/signup");

    document.getElementById('changer').innerHTML = "Already have an account? Sign-in!!";
    document.getElementById('changer').setAttribute("onclick", "change2();");
}

function change2(){
    let i = 0;
    
    var elementList = document.getElementsByClassName('change');
    for(i; i<elementList.length; i++){
        elementList[i].innerHTML = "Sign-in";
    }

    document.getElementById('emaildiv').style.display = 'none';
    document.getElementById('form').setAttribute("action", "/login");
                                                    
    document.getElementById('changer').innerHTML = "Don't have an account? Create Now!!";
    document.getElementById('changer').setAttribute("onclick", "change1();");
}

function dismiss(){
    document.getElementById('close').style.display = 'none';
}