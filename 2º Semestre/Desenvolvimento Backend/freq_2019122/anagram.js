function verificaAnagrama(string1, string2) {
    var splittedText = string1.split("")
    var boolean = true;;

    for (let i = 0; i < string2.length; i++) {
        for (let j = 0; j < splittedText.length; j++) {
            
            if ( string2.includes(splittedText[j]) != true) {
                boolean = false;
            }
        }
    }
    console.log(boolean);
}

verificaAnagrama("CARE", "RACE");