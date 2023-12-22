from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector
from datetime import datetime

# Connexion à la base de données MySQL
conn = mysql.connector.connect(
    user='root',
    password='',
    host='127.0.0.1',
    port='3307',
    database='db_tennis'
)
cursor = conn.cursor()

# Interroger la base de données pour récupérer le nom et le prénom
cursor.execute("SELECT prenom, nom, age, tel, email, adresse, ville, zip, date_naissance, sexe, date_inscription, adherant_id FROM adherants")

# Récupérer les données pour chaque personne et générer une facture individuelle
for row in cursor:
    prenom, nom, age, tel, email, adresse, ville, zip, date_naissance, sexe, date_inscription, adherant_id = row
    filename = f"{nom}_{prenom}_facture.pdf"
    date_du_jour = datetime.now()
    date_du_jour = date_du_jour.strftime("%Y-%m-%d")

    # Créer un objet Canvas pour générer le PDF
    c = canvas.Canvas(filename, pagesize=letter)

    # Informations de la facture
    c.drawString(225, 760, f"FACTURE N°2023-000-0{adherant_id}")
    c.drawString(50, 700, "UNION SPORTIVE D’IVRY")
    c.drawString(50, 680, "69, Av. Danielle Casanova")
    c.drawString(50, 665, "94200 Ivry sur Seine")
    c.drawString(50, 645, "01 45 15 07 90")
    c.drawString(50, 625, "N° SIRET 785 721 473 00029")
    c.drawString(50, 605, "APE : 9312Z")
    c.drawString(405, 700, f"{nom}")
    c.drawString(405, 680, f"{prenom}")
    c.drawString(405, 660, f"{adresse}")
    c.drawString(405, 640, f"{zip} {ville}")
    c.rect(400, 610, 200, 120)
    c.drawImage("tampon.jpg", 400, 110, width=200, height=100)

    # Informations de la facture
    c.drawString(50, 550, "FACTURE 2023-10-003")
    c.drawString(50, 520, f"Date de facture : {date_du_jour}")
    c.drawString(50, 500, f"Prénom : {prenom}")

    # Enregistrez le PDF
    c.save()

# Fermer la connexion à la base de données
conn.close()
