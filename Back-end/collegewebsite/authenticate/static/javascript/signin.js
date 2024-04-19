function change1(){
    let i,j = 0;
    
    var elementList = document.getElementsByClassName('change');
    for(i; i<elementList.length; i++){
        elementList[i].innerHTML = "Sign-Up";
    };
    
    var elementList = document.getElementsByClassName('hide');
    for(j; j<elementList.length; j++){
        elementList[j].style.display = 'block';
    };

    document.getElementById('form').setAttribute("action", "/signin");

    document.getElementById('password').setAttribute('type','text');

    document.getElementById('changer').innerHTML = "Already have an account? Sign-in!!";
    document.getElementById('changer').setAttribute("onclick", "change2();");
}

function change2(){
    let i,j = 0;
    
    var elementList = document.getElementsByClassName('change');
    for(i; i<elementList.length; i++){
        elementList[i].innerHTML = "Sign-In";
    };

    var elementList = document.getElementsByClassName('hide');
    for(j; j<elementList.length; j++){
        elementList[j].style.display = "none";
    };

    document.getElementById('form').setAttribute("action", "/login");

    document.getElementById('password').setAttribute('type','password');
                                                    
    document.getElementById('changer').innerHTML = "Don't have an account? Create Now!!";
    document.getElementById('changer').setAttribute("onclick", "change1();");
}

function dismiss(){
    document.getElementById('close').style.display = 'none';
}