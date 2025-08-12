var a = [60, 2, 4, 90, 50, 10, 230, 403]

console.log(a)
console.log(a[0])
console.log(a.length)
console.log(a[7])
console.log(a[8])

// arrange the code in decending order

a.sort(function (a, b) { return a - b })

console.log(a)

// arrange the array in decending order

a.sort(function (a, b) { return b - a })

console.log(a)

a.sort(function(a,b){return b - a})
a.sort((a , b)=> b - a)

console.log(a)

var b = a.map(function(e){return e*10})
console.log(b)

// using the arrow function to map through every element for array a

var c = a.map(a=>a*100)
console.log(c)
console.log(a)