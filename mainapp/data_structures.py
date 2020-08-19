def convert_time_to_secs(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])

def define_proffy_values(name, avatar, whatsapp, bio):
    return {
        "name": name,
        "avatar": avatar,
        "whatsapp": whatsapp,
        "bio": bio
    }


def define_class_values(subject, cost):
    return {
        "subject": subject,
        "cost": cost
    }


def define_class_schedule_values(weekday, time_from, time_to):
    values = [] # creates the class schedule list 
    class_schedule_values_size = len(weekday) # check how many "Horários" the proffy added

    for index in range (class_schedule_values_size): 
        # puts each "Horário" in the list 
        values.append(
            {
                "weekday": weekday[index],
                "time_from": convert_time_to_secs(time_from[index]),
                "time_to": convert_time_to_secs(time_to[index])
            }
        )

    return values # returns the list that will be sent to database


subjects = [
    "Artes",
    "Biologia",                             
    "Ciências",
    "Educação física",
    "Física",
    "Geografia",
    "História",
    "Matemática",
    "Português",
    "Química",
]

weekdays = [
    "Domingo",
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]