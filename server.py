from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = sqlite3.connect('database/games_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Games')
        rows = cursor.fetchall()
        conn.close()
        return render_template('template.html', rows = rows)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug = True)
