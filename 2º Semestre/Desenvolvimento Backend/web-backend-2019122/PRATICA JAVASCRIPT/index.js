function orderArrayNumbers(array) {
    let arraySorted = array.sort((a,b)=>{return a - b});
    return console.log(arraySorted);
}

function orderArrayStrings(array) {
    let arraySorted = array.sort((a,b)=>{return a.localeCompare(b)});
    return console.log(arraySorted);
}

let array = [8,3,5,1,2,3,9,4,7,0];
let arrayNames = ["Jacky", "Saul", "Miguel", "Roberto", "Nick", "Sara", "Hemily", "Gonçalo"];


orderArrayNumbers(array);
orderArrayStrings(arrayNames);