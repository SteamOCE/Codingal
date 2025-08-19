var a = { email: 'obyda@gmail.com', password: 'hihello' }
console.log(a)

var b = JSON.stringify(a)
console.log(b)


var d = new Promise(function(resolve,reject){
    setTimeout(()=>resolve("hurray"), 5000)
})

d.then((x) =>console.log(x))
.catch((err) => console.log(err))

var c = JSON.parse(b)
console.log(c)

function america() {
    print("printing america haha trump everywhere")
}

function obydaRocks() {
    // doing some coding on it
    america()
    console.log("Hi this is obyda function which just ran")
}

obydarocks()
