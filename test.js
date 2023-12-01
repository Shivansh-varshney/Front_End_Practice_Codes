roll = 7
nme = "Shiva123"
if(roll == 7){
    for (let char of nme){
        char = char.toLowerCase();
        if(("a".charCodeAt() <= char.charCodeAt() || char.charCodeAt() >= "z".charCodeAt()) == false) {
            console.log(char)
            console.log("<h2>Invalid Input: Name field must have alphabets only.</h2>")
            break
        }
    console.log("<h2>All the details were correct and the form has been submitted successfully.</h2>")
    }
}
else{
    console.log("<h2>Roll number must have 7 digits.</h2>")
}

// console.log("a".charCodeAt())
// console.log("b".charCodeAt())
// console.log("c".charCodeAt())
// console.log("d".charCodeAt())
// console.log("w".charCodeAt())
// console.log("x".charCodeAt())
// console.log("y".charCodeAt())
// console.log("z".charCodeAt())