from conexion.conexion import insert_row, read_rows, read_product_by_id, insert_usuario
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
    
    
    return render_template('crear_producto.html')  # Muestra el formulario para agregar un producto

@app.route('/usuario/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        gmail = request.form['gmail']
        fecha_nacimiento = request.form['fecha_nacimiento']
        
        # Manejo del archivo de imagen para la foto de perfil
        foto_perfil = request.files['foto_perfil']
        if foto_perfil:
            # Guardar el archivo de imagen de manera segura
            filename = secure_filename(foto_perfil.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            foto_perfil.save(filepath)
            foto_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
        else:
            foto_path = None
        
        # Insertar el nuevo usuario en la base de datos
        insert_usuario(nombre, contraseña, gmail, fecha_nacimiento, foto_path)
        
        # Redirigir a la página de productos o a cualquier otra página
        return redirect(url_for('ver_productos'))  # Puedes cambiar la redirección a donde necesites

    return render_template('crear_usuario.html')

@app.route('/comprar', methods=['POST'])
def comprar_producto():
    producto_id = request.form.get('producto_id')
    if producto_id:
        producto = read_product_by_id(producto_id)  # Obtener el producto por su ID
        return render_template('ver_productos.html', producto=producto)
    return redirect(url_for('ver_productos'))
@app.route('/agregar_comentario', methods=['POST'])
def agregar_comentario():
    comentario = request.form['comentario']
    # Aquí deberías agregar el comentario a la base de datos o procesarlo.
    # Luego, puedes redirigir al usuario o renderizar una nueva página.
    return redirect(url_for('ver_productos'))  # O cualquier página que quieras mostrar después

if __name__ == '__main__':
    app.run(debug=True)
