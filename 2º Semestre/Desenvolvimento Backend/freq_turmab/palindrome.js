function palindrome(string) {
    var reversedText = ""
    let caracteres = string.split("");

    for (let i = caracteres.length - 1; i >= 0; i--) {
        const caracter = caracteres[i];

        reversedText += caracter;
    }

    if (reversedText == string) return console.log(true)

    

    return console.log(false)
}

palindrome("CIVIC");