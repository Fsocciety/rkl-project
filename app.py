import os
import database

from flask import Flask, render_template, redirect, request, url_for, send_file, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
from forms import LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fb242bacff28be0a7d2dbedfc8c9d4f9'


def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['xlsx', 'xls'])
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/izvestaj', methods=['GET', 'POST'])
def izvestaj():
    if request.method == 'GET':
        args = request.args
        if args:
            switch = -1
        else:
            switch = 0
        broj = None if 'broj' not in request.args else request.args['broj']
        posiljalac = None if 'posiljalac' not in request.args else request.args['posiljalac']
        porucilac = None if 'porucilac' not in request.args else request.args['porucilac']
        primalac = None if 'primalac' not in request.args else request.args['primalac']
        artikal = None if 'artikal' not in request.args else request.args['artikal']
        prevoznik = None if 'prevoznik' not in request.args else request.args['prevoznik']
        registracija = None if 'registracija' not in request.args else request.args['registracija']
        datumStart = None if 'datumStart' not in request.args else request.args['datumStart']
        datumEnd = None if 'datumEnd' not in request.args else request.args['datumEnd']
        return render_template('izvestaj.html', reports=database.select_from(args),
                                                posiljke=database.select_posiljalac(),
                                                porucioci=database.select_porucilac(),
                                                primaoci=database.select_primalac(),
                                                artikli=database.select_artikal(),
                                                prevoznici=database.select_prevoznik(),
                                                registracije=database.select_registracija(),
                                                broj=broj,
                                                posiljalac=posiljalac,
                                                porucilac=porucilac,
                                                primalac=primalac,
                                                artikal=artikal,
                                                prevoznik=prevoznik,
                                                registracija=registracija,
                                                datumStart=datumStart,
                                                datumEnd=datumEnd,
                                                currentDate=database.currentDate(),
                                                args=switch
                                                )

        
    


@app.route('/files', methods=['GET', 'POST'])
def files():
    if request.method == 'GET':
        return render_template('files.html', files=files())

    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            file_location = "./input/" + filename
            f.save(file_location)
            database.save(file_location)
            return redirect(url_for('files'))

@app.route('/files/<file_name>', methods=['GET', 'DELETE'])
def file_option(file_name):
    if request.method == 'GET':
        return send_file("./input/" + file_name, as_attachment=True)

    if request.method == 'DELETE':
        database.delete(file_name)
        os.remove(f"./input/{file_name}")
        return "sdaf"


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'bb' and form.password.data == 'password':
            flash('You have been loged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

def files():
    uploads = os.fsencode('./input')
    files = []
    for file in os.listdir(uploads):
        files.append(os.fsdecode(file))
    print(files)
    return files

if __name__ == "__main__":
    app.run(debug=True)


