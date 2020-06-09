from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'inventory'

mysql = MySQL()
mysql.init_app(app)

# URL Pages


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/add_product')
def productUI():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT * FROM marcas')
    marca = cur.fetchall()
    cur.execute('SELECT * FROM tipos')
    tipo = cur.fetchall()
    return render_template('addProduct.html', marcas=marca, tipos=tipo, title='Inicio', back=True)

# METHODS


@app.route('/api/add_product', methods=['POST'])
def add_product():
    if request.method == 'POST':
        json = request.get_json(silent=True)
        data = json['data']
        nombre = data['nombre']
        marca = data['marca']
        tipo = data['tipo']
        precio = data['precio']
        costo = data['costo']
        stock = data['stock']
        descripcion = data['descripcion']
        imagen = ""
        print(data)
        cur = mysql.get_db().cursor()
        cur.execute('INSERT INTO productos (nombre, id_marca, id_tipo, precio, costo, stock, descripcion, imagen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                    (nombre, marca, tipo, precio, costo, stock, descripcion, imagen))
        mysql.get_db().commit()
        return redirect('/')


@app.route('/api/edit')
def edit_product():
    return 'Edit product'


@app.route('/api/delete')
def delete_contact():
    return 'Delete product'


if __name__ == '__main__':
    app.run(port=3000, debug=True)
