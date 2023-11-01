function check(){
    var roll = '5684263';
    roll = roll.split('')
    var nme = "Shivansh Varshney";

    if(roll.length == 7 && typeof nme == 'string'){
        console.log("<h2>All the details were correct and the form has been submitted successfully.</h2>")
    }
    else{
        console.log("Something went wrong.")
    }

}
check()