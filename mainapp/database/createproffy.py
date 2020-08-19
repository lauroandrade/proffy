def createproffy(db, proffy_values, class_values, class_schedule_values):
    try:
        cursor = db.cursor()
        inserted_proffy = cursor.execute(''' INSERT INTO proffys (name, avatar, whatsapp, bio) 
        VALUES (
            ?,
            ?,
            ?,
            ?
        )
        ''', (proffy_values["name"], proffy_values["avatar"], proffy_values["whatsapp"], proffy_values["bio"]))

        proffy_id = inserted_proffy.lastrowid

        inserted_class = cursor.execute(''' INSERT INTO classes (subject, cost, proffy_id) 
        VALUES (
            ?,
            ?,
            ?
        )
        ''', (class_values["subject"], class_values["cost"], proffy_id))

        class_id = inserted_class.lastrowid

        for class_schedule_value in class_schedule_values:
            cursor.execute(''' INSERT INTO class_schedule (class_id, weekday, time_from, time_to)
            VALUES (
                ?,
                ?,
                ?,
                ?
            )
            ''', (class_id, class_schedule_value["weekday"], class_schedule_value["time_from"], class_schedule_value["time_to"]))

        db.commit()

    except db.Error as Error:
        print(Error)
    