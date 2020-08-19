// Procurar o botão 
document.querySelector('#add-time')
.addEventListener('click', cloneField)
// Quando clicar no botão 

// Executar uma ação
function cloneField() {
    // Duplicando o campo
    const newFieldContainer = document.querySelector('.schedule-time').cloneNode(true)

    // Limpando os campos
    const fields = newFieldContainer.querySelectorAll('input')

    fields.forEach(function(field){
        field.value = ""
    })

    document.querySelector('#schedule-items').appendChild(newFieldContainer)
}
    