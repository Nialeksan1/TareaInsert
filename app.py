from flask import Flask, request, render_template_string
import pymysql
import os

app = Flask(__name__)

# Configuracion de la base de datos
db_config = {
    'host': 'localhost',
    'user': os.getenv('DB_USER').strip(),
    'password': os.getenv('DB_PASSWORD').strip(),
    'database': 'tarea_insert'
}

# Funcion para obtener la conexion a la base de datos
def get_db_connection():
    conn = pymysql.connect(**db_config)
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Conectar a la base de datos y realizar la insercion
        conn = get_db_connection();
        cursor = conn.cursor();
        cursor.execute('INSERT INTO insert_tabla (data) VALUES (%s)', (user_input,)) # Es un tupla de un solo elemento, por eso la coma
        conn.commit()
        cursor.close()
        conn.close()

        return 'Dato insertado correctamente'
    
    # Formulario HTML para ingresar datos
    form_html = '''
    <form method="post">
        <label for="user_input">Ingrese un dato:</label>
        <input type="text" id="user_input" name="user_input">
        <input type="submit" value="Enviar">
    </form>
    '''
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True)