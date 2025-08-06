class Animal {
    constructor(name, size, legs, hande, nose, brain){
        this.name = name
        this.size = size
    
    }
}

const a1 = new Animal('Jaguar', 'big', 2, 2, 1, 1)

const a2 = new Animal('Lion', 'small', 2, 2, 1, 2)

console.log(a1.name)
console.log(a2.name)

class HumanBeing extends Animal{
    constructor(name, size, legs, hands, nose, brain, intelligence, population){
    super(name, size, legs, hands, nose,brain)
    this.intelligence = intelligence
    this.population = population
    }
}

const h1 = new HumanBeing('Obyda', 'Big and smart', 5390, 'high', 'very high')

console.log(h1.name)