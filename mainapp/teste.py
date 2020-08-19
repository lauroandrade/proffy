from database.createproffy import createproffy
from database.db import init_sqlite, finish_sqlite

proffy_values = {
    'name': 'Diego Fernandes',
    'avatar': 'https://avatars2.githubusercontent.com/u/2254731?s=460&amp;u=0ba16a79456c2f250e7579cb388fa18c5c2d7d65&amp;v=4',
    'whatsapp': '31984354946',
    'bio': 'Entusiasta das melhores tecnologias de química avançada.<br><br>Apaixonado por explodir coisas em laboratório e por mudar a vida das pessoas através de experiências. Mais de 200.000 pessoas já passaram por uma das minhas explosões.'
}

class_values = {
    'subject': 1,   
    'cost':'20',
}

class_schedule_values = [
    {
        'weekday': 0,
        'time_from': 720,
        'time_to': 1220
    },
    {
        'weekday': 1,
        'time_from': 520,
        'time_to': 1220
    }
]

try:
    # INITIALIZING SQL
    db = init_sqlite()
    cursor = db.cursor()

    # CREATING PROFFY
    createproffy(db, proffy_values, class_values, class_schedule_values)

    # CONSULTING PROFFY DATA
    selected_proffys = cursor.execute("SELECT * FROM proffys").fetchall()
    print(selected_proffys)

    # CLOSING THE DB
    finish_sqlite(db)
except:
    print('Error while initializing or finishing SQLite')

# [] = list / {} = dictionary)

