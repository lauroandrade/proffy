CREATE TABLE IF NOT EXISTS proffys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    avatar TEXT,
    whatsapp TEXT NOT NULL,
    bio TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject INTEGER,
    cost TEXT,
    proffy_id INTEGER
);

CREATE TABLE IF NOT EXISTS class_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    weekday INTEGER,
    time_from INTEGER,
    time_to INTEGER
);