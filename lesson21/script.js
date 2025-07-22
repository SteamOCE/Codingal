var aus = {
    cities: ['Perth', 'Sydney', 'Melbourne'], population:
        26600000, greet: function () { return 'hello buddy' }
}
console.log(aus.greet())
console.log(aus.population)

var a = 'obyda from perth australia'
console.log(a.toUpperCase())
console.log(a.toLowerCase())

console.log(Math.random())
console.log(Math.floor(5.789))

let i
for (i = 0; i < 6; i++) {
    console.log('Obyda')
}

let day
day = 7

switch(day){
    case 0:
        console.log('Sunday office ')
        break;
        case 1:
            console.log('Monday office')
            break;
            case 2:
                console.log('Tuesday')
                break;
                default:
                    console.log('default case running')
                    break;

}