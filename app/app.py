from flask import Flask, render_template, redirect, url_for, request
from connection import dbConnect

app = Flask (__name__)


#Pagina de inicio Home
@app.route('/')
def index():
    return render_template('home.html')

#Funciones de Registrar Vuelo
@app.route('/vuelo')
def vuelo():
    return render_template('crear_vuelo.html')

@app.route('/registro_vuelo', methods = ['GET','POST'])
def registroVuelo():
    if request.method == 'POST':
        fechaSalida = request.form ['fechaSalida']
        horaSalida = request.form ['horaSalida']
        precio = request.form ['precio']
        avionAsignado = request.form ['avionAsignado']
        aeropuertoDestino = request.form ['aeropuertoDestino']

        datos = {'fechaS':fechaSalida , 'horaS':horaSalida, 'precio': precio, 'avionA':avionAsignado, 'aeroP': aeropuertoDestino}
        print(datos)
        
        conexion = dbConnect()
        cursor = conexion.cursor()

        cursor.execute ("INSERT INTO TB_VUELO (FECHASALIDA, HORASALIDA, PRECIO, ESTADO, IDAVION, IDAEROPUERTO) \
                        VALUES (TO_DATE(:fechaS,'YYYY-MM-DD'), :horaS, :precio, 1 ,:avionA, :aeroP)",datos)
        conexion.commit()
        cursor.close() 
        conexion.close()       
        return redirect(url_for('index'))


#Funciones para registrar el cliente
@app.route('/cliente')
def cliente():
    return render_template('registro_cliente.html')

@app.route('/registro_cliente', methods = ['GET','POST'])
def registroCliente():
    if request.method == 'POST':
        nombre = request.form ['nombre']
        ci = request.form ['ci']
        telefono = request.form ['telefono']
        apellido = request.form ['apellido']
        correo = request.form ['correo']

        datos = {'nombre':nombre, 'ci':ci,'telefono':telefono, 'apellido':apellido, 'correo':correo}
        print (datos)
        conexion = dbConnect()
        cursor = conexion.cursor()

        cursor.execute ("INSERT INTO TB_CLIENTE (IDCICLIENTE, NOMBRE, APELLIDO, CORREO, TELEFONO) \
                        VALUES (:ci,:nombre,:apellido,:correo,:telefono )",datos)
        conexion.commit()
        cursor.close() 
        conexion.close()     

        return redirect(url_for('index'))


#Registro del Pasajero para ingresar a la seccion de Vuelo
@app.route('/registro')
def boleto():
    return render_template('Registro_boleto.html')

@app.route('/registro_pasajero', methods = ['GET','POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ci = request.form['ci']
        telefono = request.form['telefono']
        apellido = request.form['apellido']
        correo = request.form['correo']
        CantMaletas = request.form['CantMaletas']
        peso = request.form['Peso']
        print (peso)
        return redirect(url_for('seleccion'))


#Funciones de regitsrar el boleto seleccionando el Vuelo registrado y clase 
@app.route ('/seleccion_vuelo')
def seleccion():
    return render_template('flight_selection.html')   

@app.route('/flight_selection',methods = ['GET','POST'])
def flightSelection():
    if request.method == 'POST':
        idVuelo = request.form ['idVuelo']
        clase = request.form ['clase']   
        print (idVuelo, clase)
        return redirect(url_for('pago'))
    

#Se registra el tipo de pago y el valor a pagar
@app.route("/pago")
def pago():
    return render_template('registro_pago.html')

@app.route("/registro_pago", methods = ['GET','POST'])
def registroPago():
    if request.method == 'POST':
        ciCliente = request.form ['cicliente']
        valor = request.form ['valor']
        metodoPago = request.form ['metodoPago']
        print (ciCliente, metodoPago, valor)

        return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)

