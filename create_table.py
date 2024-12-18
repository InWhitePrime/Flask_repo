import pandas as pd
import sqlite3

# Создаем файл базы данных
connection = sqlite3.connect('database/games_database.db')

# Объект курсора используется для выполнения запросов к базе данных и получения результатов этих запросов
cursor = connection.cursor()

# Удаление таблицы, если она уже существует
cursor.execute('DROP TABLE IF EXISTS Games')

# Создание таблицы
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Games (
    Game TEXT,
    Genre TEXT,
    Date DATE,
    Status TEXT
)'''
)

# Заполнение таблицы данными
cursor.execute(
    '''INSERT INTO Games VALUES ('Cyberpunk 2077', 'Action-RPG', '10-12-2020', 'Не пройдена'),
                                           ('Metro Exodus', 'Action-RPG', '14-02-2019', 'Пройдена'),
                                           ('Forza Horizon 5', 'Racing', '01-11-2021', 'Пройдена'),
                                           ('Disciples 2', 'Strategy', '23-01-2002', 'Пройдена'),
                                           ('Tekken 8', 'Fighting', '25-01-2024', 'Не пройдена'),
                                           ('Baldurs gate 3', 'RPG', '03-08-2023', 'Не пройдена'),
                                           ('Star Wars Jedi Fallen Order', 'Action-RPG', '11-11-2019', 'Пройдена'),
                                           ('Atomic Heart', 'Action-RPG', '21-02-2023', 'Не пройдена'),
                                           ('Black Myth: Wukong', 'Action-RPG', '19-08-2024', 'Не пройдена'),
                                           ('Ori and the Blind Forest', 'Platformer', '10-03-2015', 'Пройдена')'''
)

# Вывод содержимого таблицы
sql = '''SELECT * FROM Games'''
print(pd.read_sql(sql, connection))

# Завершение работы
connection.commit()
cursor.close()
connection.close()
