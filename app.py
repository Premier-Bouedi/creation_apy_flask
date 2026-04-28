from flask import Flask, render_template

# Initialisation de l'application
app = Flask(__name__)

# Définition de la route pour la page d'accueil
@app.route('/')
def home():
    return render_template('home.html')

# Définition de la route pour la page "À propos"
@app.route('/about')
def about():
    return render_template('about.html')

# Lancement du serveur de développement
if __name__ == '__main__':
    app.run(debug=True)