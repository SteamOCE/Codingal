let numberButtons = document.querySelectorAll('.number')
let operatorButtons = document.querySelectorAll('.operator')
let display = document.querySelector('.display')

let currentInput = ''
let previousInput = ''
let operator = null

function updateDisplay(value){
    display.innerHTML = value
}

numberButtons.forEach(button =>{
    button.addEventListener('click',()=>{
        currentInput = currentInput + button.id
        updateDisplay(currentInput)

    })
})


operatorButtons.forEach(button =>{
    button.addEventListener('click', ()=>{
        const id = button.id
        switch(id){
            case 'clear':
                currentInput = ''
                previousInput = ''
                operator = null
                updateDisplay("")
                break

            case 'backspace':
                currentInput = currentInput.slice(0,-1)
                updateDisplay(currentInput)
                break
        }
    })
})