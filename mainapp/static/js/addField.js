// Button event listener
document.querySelector('#add-time')
.addEventListener('click', cloneField)

// Event Listener action
function cloneField() {
    // Selecting all schedules itens
    const schedules = document.querySelectorAll('.schedule-time')
    // Cloning the last schedule
    const newSchedule = schedules[schedules.length - 1].cloneNode(true)
    // Getting the fields of the last schedule
    const fields = newSchedule.querySelectorAll('input')

    let fieldIsEmpty = false

    fields.forEach(function(field){
        if (!field.value) 
            fieldIsEmpty = true
        field.value = ""
    })

    if (fieldIsEmpty) {
        return false;
    }

    document.querySelector('#schedule-items').appendChild(newSchedule)
}
    