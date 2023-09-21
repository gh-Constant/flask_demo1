from flask import Flask, request, render_template, redirect, url_for, abort  # application WSGI

import datetime

liste_etudiants = [
    {'id':1,'nom':'tom', 'groupe':'A1'},
    {'id':2,'nom':'enzo', 'groupe':'A1'},
    {'id':3,'nom':'laurence', 'groupe':'A2'},
    {'id':4,'nom':'theo', 'groupe':'A2'},
    {'id':5,'nom':'mehdi', 'groupe':'B1'}
]

# (interface de serveur web python)
# comportements et méthodes d'un serveur web


app = Flask(__name__)    # instance de classe Flask (en paramètre le nom du module)

@app.route('/')
@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!<a href="hello">lien hello</a>  &nbsp; <a href="/heure"> heure </a>'

@app.route('/heure')
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template('index_demo.html', h=h,min=m,sec=s )

@app.route('/etudiant/show')
def show_etudiants():
    return render_template('etudiant/show_etudiants.html', etudiants=liste_etudiants )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
