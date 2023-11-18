import mysql.connector
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

db = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              port='3307',
                              database='db_tennis')
@app.route('/')
def index():


        

    return render_template('index.html')

@app.route('/terrains', methods=["GET"])
def terrains():


        

    return render_template('terrains.html')


@app.route('/ecole', methods=["GET"])
def ecole():


    return render_template('ecole.html')



@app.route('/formulaire', methods=["GET","POST"])
def formulaire():
    if request.method == 'POST':
        prenom = request.form['prenom'].capitalize()
        nom = request.form['nom'].upper()
        date_naissance = request.form['date_naissance']
        sexe = request.form['sexe']
        adresse = request.form['adresse'].upper()
        email = request.form['email']
        tel = request.form['tel']
        zip = request.form['zip']
        ville = request.form['ville'].upper()
        age = request.form['age']

        cursor = db.cursor()
        cursor.execute("INSERT INTO adherants (prenom, nom, age, tel, email, adresse, ville, zip, date_naissance, sexe, date_inscription) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())", (prenom, nom, age, tel, email, adresse, ville, zip, date_naissance, sexe))
        db.commit()
        cursor.close()

        return redirect("/validation")

    return render_template('formulaire.html')

@app.route('/validation', methods=["GET"])
def validation():


    return render_template('validation.html')



@app.route('/contact', methods=["GET"])
def contact():
    
    
    
    return render_template('contact.html')

