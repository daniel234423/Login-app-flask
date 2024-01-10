#este archivo sera el archivo principal en el cual llamaremos la funcion create app y le daremos para que entorno se debe configurar si produccion o development
#luego definiremos un contexto de la applicacion y crearemos todads las tablas de la base de dato y un usuario de prueba
from app import create_app, db
from app.auth.models import User

flask_scappy_app = create_app("prod")
with flask_scappy_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name="test").first():
        User.create_user(
        user="test",
        email="test-testing@test.com",
        password="test**123"
    )
flask_scappy_app.run()