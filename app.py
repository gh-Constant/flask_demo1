#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

                                    ## à ajouter
from flask import session, g
import pymysql.cursors



def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",                 # à modifier
            user="constant",                     # à modifier
            password="password",                # à modifier
            database="main",        # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/etudiant/show')
def show_etudiants():
    mycursor = get_db().cursor()
    sql='''   SELECT id_etudiant AS id, nom_etudiant AS nom, groupe_etudiant AS groupe FROM etudiant ORDER BY nom;   '''
    mycursor.execute(sql)
    liste_etudiants = mycursor.fetchall()
    return render_template('etudiant/show_etudiants.html', etudiants=liste_etudiants )


@app.route('/etudiant/add', methods=['GET'])
def add_etudiant():
    return render_template('etudiant/add_etudiant.html')

@app.route('/etudiant/add', methods=['POST'])
def valid_add_etudiant():
    nom = request.form.get('nom')
    groupe = request.form.get('groupe')
    
    mycursor = get_db().cursor()
    sql = '''INSERT INTO etudiant(id_etudiant, nom_etudiant, groupe_etudiant) VALUES (NULL, %s, %s);'''
    mycursor.execute(sql, (nom, groupe))
    get_db().commit()
    
    flash('Etudiant ajouté avec succès')
    return redirect('/etudiant/show')

@app.route('/etudiant/delete')
def delete_etudiant():
    print('''suppression d'un étudiant''')
    print(request.args)
    print(request.args.get('id'))
    id=request.args.get('id')
    mycursor = get_db().cursor()
    sql='''   DELETE FROM etudiant WHERE id_etudiant = %s;   '''
    mycursor.execute(sql, (id))
    get_db().commit()
    flash('Etudiant supprimé avec succès')
    return redirect('/etudiant/show')

@app.route('/etudiant/edit', methods=['GET'])
def edit_etudiant():
    print('''affichage du formulaire pour modifier un étudiant''')
    print(request.args.get('id'))
    id=request.args.get('id')
    if id != None and id.isnumeric():
        indice = int(id)

        mycursor = get_db().cursor()
        sql = '''   SELECT id_etudiant AS id, nom_etudiant AS nom, groupe_etudiant AS groupe FROM etudiant WHERE id_etudiant = %s;   '''
        
        mycursor.execute(sql, (id))
        etudiant = mycursor.fetchone()

    else:
        etudiant=[]
    return render_template('etudiant/edit_etudiant.html', etudiant=etudiant)


@app.route('/etudiant/edit', methods=['POST'])
def valid_edit_etudiant():
    id = request.form.get('id')
    nom = request.form.get('nom')
    groupe = request.form.get('groupe')
    
    mycursor = get_db().cursor()
    sql = '''UPDATE etudiant SET nom_etudiant = %s, groupe_etudiant = %s WHERE id_etudiant = %s'''
    mycursor.execute(sql, (nom, groupe, id))
    get_db().commit()
    
    flash('Etudiant modifié avec succès')
    return redirect('/etudiant/show')

if __name__ == '__main__':
    app.run(debug=True, port=5000)