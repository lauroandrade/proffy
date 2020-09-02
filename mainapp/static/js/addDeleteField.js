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

    if (fieldIsEmpty) return false;

    if (schedules.length == 1) {
        const div = document.createElement('div')
        const image = document.createElement('img')

        div.classList.add('input-block', 'delete')

        image.src = '/static/images/icons/delete.svg'
        image.alt = "Delete schedule"
        image.style.cursor = "pointer"
        image.style.width = "2rem"
        image.onclick = deleteSchedule

        div.appendChild(image)
        div.style.marginTop = "1.6rem"

        newSchedule.appendChild(div)
    } else {
        newSchedule.querySelector(".input-block.delete img").onclick = deleteSchedule
    }

    document.querySelector('#schedule-items').appendChild(newSchedule)
}

function deleteSchedule(event) {
    const schedule = document.querySelectorAll('.schedule-item')
    const scheduleItem = event.target.parentElement.parentElement

    if (schedule.length !== 1) 
        scheduleItem.remove()
}
    