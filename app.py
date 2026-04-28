from flask import Flask, render_template

# Initialisation de l'application
app = Flask(__name__)

# Définition de la route pour la page d'accueil
@app.route('/')
def home():
    return render_template('home.html', title="Accueil")

# Définition de la route pour la page "À propos"
@app.route('/about')
def about():
    return render_template('about.html', title="À Propos")

# Définition de la route pour la page "Jeux Vidéo"
@app.route('/games')
def games():
    games_list = [
        "The Legend of Zelda: Tears of the Kingdom",
        "Super Mario Odyssey",
        "Red Dead Redemption 2",
        "Elden Ring",
        "God of War Ragnarök",
        "Cyberpunk 2077"
    ]
    return render_template('games.html', title="Mes Jeux Préférés", games=games_list)

# Lancement du serveur de développement
if __name__ == '__main__':
    app.run(debug=True)