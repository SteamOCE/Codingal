let numberButtons = document.querySelectorAll('.number')
let operatorButtons = document.querySelectorAll('.operator')
let display = document.querySelector('.display')

let currentInput = ''
let previousInput = ''
let operator = null

function updateDisplay(value) {
    display.innerHTML = value
}

numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        currentInput = currentInput + button.id
        updateDisplay(currentInput)

    })
})


operatorButtons.forEach(button => {
    button.addEventListener('click', () => {
        const id = button.id
        switch (id) {
            case 'clear':
                currentInput = ''
                previousInput = ''
                operator = null
                updateDisplay("")
                break

            case 'backspace':
                currentInput = currentInput.slice(0, -1)
                updateDisplay(currentInput)
                break
            case 'equals':
                if (operator && previousInput && currentInput) {
                    const result = calculate(parseFloat(previousInput),
                        parseFloat(currentInput), operator)
                    updateDisplay(result.toString())
                    previousInput = ''
                    operator = null
                }
                break

            case 'divide':
            case 'multiply':
            case 'subtract':
            case 'sum':
                if (currentInput) {
                    if (previousInput && operator) {
                        const result = calculate(parseFloat
                            (previousInput), parseFloat(currentInput),
                            operator)

                        previousInput = result.toString()
                        updateDisplay(result)
                    }
                    else {
                        previousInput = currentInput
                    }
                    currentInput = ''
                    operator = id
                }
        }

    })
})
function calculate(p, c, o) {
    switch (o) {
        case "sum":
            return p + c
        case 'subtract':
            return p - c
        case 'divide':
            return p / c
        case 'multiply':
            return p * c
        default:
            return c
    }
}