from database.createproffy import createproffy
from database.db import init_sqlite, finish_sqlite
from data_structures import subjects, weekdays, convert_time_to_secs


def query_proffy():
    db = init_sqlite()

    proffys_query = db.execute(''' SELECT classes.*, proffys.*
        FROM proffys 
        JOIN classes ON (classes.proffy_id = proffys.id)
        WHERE classes.proffy_id = proffys.id
        ''').fetchall()

    finish_sqlite(db)
    return row_to_list(proffys_query)


def filter_proffy(subject, weekday, time):
    subject = subject
    weekday = weekday
    time = convert_time_to_secs(time)

    db = init_sqlite()
    cursor = db.cursor()

    proffys_filtered = cursor.execute(''' SELECT classes.*, proffys.*
    FROM proffys
    JOIN classes ON (classes.proffy_id = proffys.id)
    WHERE EXISTS (
        SELECT class_schedule.* 
        FROM class_schedule
        WHERE class_schedule.class_id = classes.id
        AND class_schedule.weekday = ?
        AND class_schedule.time_from <= ?
        AND class_schedule.time_to > ?
    )
    AND classes.subject = ?
    ''', (weekday, time, time, subject)).fetchall()
    
    finish_sqlite(db)

    return row_to_list(proffys_filtered)



def call_create_proffy(proffy_values, class_values, class_schedule_values):
    db = init_sqlite()

    createproffy(db = db, proffy_values = proffy_values, class_values = class_values, class_schedule_values = class_schedule_values)
    
    finish_sqlite(db)


def convert_subject(subject_index):
    return subjects[subject_index - 1]


def row_to_list(row_object):
    # row factory is able to transform the data returned in tuples into an object of a...
    # ... special class called Row, from SQLite3. This class alows treat the data as a List of Dicts ...
    # However, the class List and Dict is able to give us more control over the data
    # !!! Thus, this method transforms the Sqlite3.Row into a List of Dicts !!!
    proffys = []
    for proffy in row_object:
        proffys.append(
            {
                "name": proffy["name"],
                "avatar": proffy["avatar"],
                "whatsapp": proffy["whatsapp"],
                "bio": proffy["bio"],
                "subject": convert_subject(proffy["subject"]),   
                "cost":proffy["cost"]
            }
        ) 
    return proffys

