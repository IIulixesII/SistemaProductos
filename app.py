from conexion.conexion import insert_row, read_rows, read_product_by_id
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configura la carpeta donde se guardarán las imágenes subidas
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def ver_productos():
    productos = read_rows()  # Obtener todos los productos
    return render_template('ver_productos.html', productos=productos)

@app.route('/producto/crear', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        categoria = request.form['categoria']
        
        # Manejo del archivo de imagen
        imagen = request.files['img']
        if imagen:
            filename = secure_filename(imagen.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(filepath)
            img_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
            insert_row(nombre, precio, categoria, img_path)
        
        return redirect(url_for('ver_productos'))
    
    return render_template('crear_producto.html')

@app.route('/comprar', methods=['POST'])
def comprar_producto():
    producto_id = request.form.get('producto_id')
    if producto_id:
        producto = read_product_by_id(producto_id)  # Obtener el producto por su ID
        return render_template('ver_productos.html', producto=producto)
    return redirect(url_for('ver_productos'))

if __name__ == '__main__':
    app.run(debug=True)
