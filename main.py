from route.login import fetch
from config import app, db, login_manager

app.config['SECRET_KEY'] = 'test'
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(fetch)

if __name__ == "__main__":
    app.run(debug=True)
