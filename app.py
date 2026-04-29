from flask import Flask, render_template, request

# Initialisation de l'application
app = Flask(__name__)

# Route racine
@app.get('/')
def home():
    return render_template('home.html', title="Accueil")

# Route À propos
@app.get('/about')
def about():
    return render_template('about.html', title="À Propos")

# Route Jeux Vidéo
@app.get('/games')
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

# Route Connexion (GET pour afficher, POST pour traiter)
@app.get('/login')
def login_get():
    return render_template('login.html', title="Connexion")

@app.post('/login')
def login_post():
    # Simulation de traitement de connexion
    username = request.form.get('username')
    return f"Tentative de connexion pour l'utilisateur : {username}"

# Gestion de l'erreur 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Non Trouvée"), 404

# Lancement du serveur de développement
if __name__ == '__main__':
    app.run(debug=True)