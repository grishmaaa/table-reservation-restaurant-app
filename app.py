from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS reservations (id INTEGER PRIMARY KEY, name TEXT, date DATE, time TIME, status TEXT)')
    conn.close()

init_db()

# Routes
@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservations')
    reservations = cursor.fetchall()
    conn.close()
    return render_template('index.html', reservations=reservations)

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    status = 'Reserved'
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO reservations (name, date, time, status) VALUES (?, ?, ?, ?)', (name, date, time, status))
    conn.commit()
    conn.close()
    
    flash('Reservation created successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/cancel/<int:reservation_id>')
def cancel(reservation_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE reservations SET status=? WHERE id=?', ('Cancelled', reservation_id))
    conn.commit()
    conn.close()
    
    flash('Reservation canceled successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/update/<int:reservation_id>', methods=['POST'])
def update(reservation_id):
    new_date = request.form['new_date']
    new_time = request.form['new_time']
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE reservations SET date=?, time=? WHERE id=?', (new_date, new_time, reservation_id))
    conn.commit()
    conn.close()
    
    flash('Reservation updated successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
