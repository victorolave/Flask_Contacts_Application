from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'victor1131'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()

    return render_template('index.html', contacts = data)

@app.route('/addContact', methods=['POST'])
def addContact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)', (name,phone,email))
        mysql.connection.commit()

        flash('Contact Added')
        return redirect(url_for('Index'))

@app.route('/edit')
def editContact():
    return 'Edit Contact'

@app.route('/delete/<string:id>')
def deleteContact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacts WHERE idcontacts = {0}'.format(id))
    mysql.connection.commit()

    flash('Contact Deleted')
    return redirect(url_for('Index'))
    

if __name__ == '__main__':
    app.run(port = 3000, debug = True)