from flask import Flask, render_template, redirect, url_for, request, flash
from connection import dbConnect
from client import client_page

app = Flask (__name__)

app.register_blueprint(client_page)

rtnPasajero = None
vueloId = None
#app.secret_key = 'mysecretkey'

#Pagina de inicio Home
@app.route('/')
def index():
    return render_template('home.html')

#Funciones de Registrar Vuelo
@app.route('/vuelo')
def vuelo():
    return render_template('vuelo/crear_vuelo.html')

@app.route('/registro_vuelo', methods = ['GET','POST'])
def registroVuelo():
    if request.method == 'POST':
        fechaSalida = request.form ['fechaSalida']
        horaSalida = request.form ['horaSalida']
        precio = request.form ['precio']
        avionAsignado = request.form ['avionAsignado']
        aeropuertoDestino = request.form ['aeropuertoDestino']

        
        
        conexion = dbConnect()
        cursor = conexion.cursor()
        idVariable = cursor.var(int)
        datos = {'fechaS':fechaSalida , 'horaS':horaSalida, 'precio': precio, 'avionA':avionAsignado, 'aeroP': aeropuertoDestino, 'idVariable':idVariable}
        print(datos)

        
        cursor.execute ("INSERT INTO TB_VUELO (FECHASALIDA, HORASALIDA, PRECIO, ESTADO, IDAVION, IDAEROPUERTO) \
                        VALUES (TO_DATE(:fechaS,'YYYY-MM-DD'), :horaS, :precio, 1 ,:avionA, :aeroP) RETURNING IDVUELO INTO :idVariable",datos)       
        

        id_generado = idVariable.getvalue()

        print("----------")
        print (id_generado)
        
        conexion.commit()
        cursor.close() 
        conexion.close()       
        return redirect(url_for('index'))


#Funciones para registrar el cliente
'''@app.route('/cliente')
def cliente():
    return render_template('cliente/registro_cliente.html')

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

        cursor.execute ("INSERT INTO TB_CLIENTE (IDCICLIENTE, NOMBRE, APELLIDO, CORREO, TELEFONO, ESTADO) \
                        VALUES (:ci,:nombre,:apellido,:correo,:telefono, '1' )",datos)
        conexion.commit()
        cursor.close() 
        conexion.close()     

        return redirect(url_for('index'))'''


#Registro del Pasajero para ingresar a la seccion de Vuelo
@app.route('/registro')
def boleto():
    return render_template('passenger/Registro_boleto.html')

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
        global rtnPasajero

        conexion = dbConnect()
        
        cursor = conexion.cursor()
        idVariable = cursor.var(int)

        datosEquipaje ={'cantMaletas':CantMaletas,'peso':peso, 'idVariable':idVariable}

        cursor.execute ("INSERT INTO TB_EQUIPAJE(CANTIDADMALETAS, PESO) \
                        VALUES (:cantMaletas,:peso) RETURNING IDEQUIPAJE INTO :idVariable",datosEquipaje)
        id_generado = str(idVariable.getvalue()[0])
        print(type(id_generado))
        conexion.commit()
        conexion.close()
        
        conexion2 = dbConnect()
        cursor2 = conexion2.cursor()
        returnPasajero = cursor2.var(int)
        datosPasajero ={'nombre':nombre, 'apellido':apellido, 'ci':ci,'telefono':telefono,'correo':correo,'idEquipaje':id_generado,'returnPasajero':returnPasajero }
        print(datosPasajero)
        cursor2.execute ("INSERT INTO TB_PASAJERO (CIPASAJERO, NOMBRE, APELLIDO, TELEFONO, CORREO, ESTADO, IDEQUIPAJE) \
                        VALUES (:ci, :nombre, :apellido, :telefono, :correo, '1', :idEquipaje) RETURNING IDPASAJERO INTO :returnPasajero", datosPasajero)
        returnPasajero = str(returnPasajero.getvalue()[0])  
        rtnPasajero = returnPasajero
        conexion2.commit()
        cursor2.close()
        conexion2.close()
        return redirect(url_for('seleccion'))


#Funciones de regitsrar el boleto seleccionando el Vuelo registrado y clase 
@app.route ('/seleccion_vuelo')
def seleccion():
    conexion=dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TB_VUELO ")
    dataVuelo = cursor.fetchall()
    print(dataVuelo)
    cursor.close()
    
    cursor2 = conexion.cursor()
    cursor2.execute("SELECT * FROM TB_AEROPUERTO ")
    dataDestino = cursor2.fetchall()

    return render_template('ticket/flight_selection.html', data=dataVuelo, data2=dataDestino)   

@app.route('/flight_selection',methods = ['GET','POST'])
def flightSelection():
    if request.method == 'POST':
        idVuelo = request.form ['idVuelo']
        clase = request.form ['clase']          
        global vueloId
        vueloId = idVuelo
        global rtnPasajero
        idPasajero = str(rtnPasajero)
        
        datos = {'idVuelo':idVuelo , 'clase':clase , 'idPasajero':idPasajero}
        conexion = dbConnect()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO TB_BOLETO (CLASE, IDVUELO, ESTADO, IDPASAJERO)\
                       VALUES (:clase, :idVuelo, 1, :idPasajero)",datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        return redirect(url_for('pago'))
    

#Se registra el tipo de pago y el valor a pagar
@app.route("/pago")
def pago():
    return render_template('factura/registro_pago.html')

@app.route("/registro_pago", methods = ['GET','POST'])
def registroPago():
    if request.method == 'POST':
        ciCliente = request.form ['cicliente']
        valor = request.form ['valor']
        metodoPago = request.form ['metodoPago']
        global vueloId
        idVuelo = vueloId
        idFormaPago = None
        if metodoPago == 'tarjetaCredito':
            idFormaPago = 'FP01'
        elif metodoPago == 'tarjetaDebito':
            idFormaPago = 'FP02'
        elif metodoPago == 'paypal':
            idFormaPago = 'FP03'
        else :
            idFormaPago = 'FP04'

        datos = {'ciCliente':ciCliente , 'valor' :valor, 'idFormaPago' :idFormaPago , 'idVuelo':idVuelo}
        conexion = dbConnect()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO TB_FACTURA(IDCICLIENTE, IDVUELO, VALORTOTAL, IDFORMAPAGO, ESTADO)\
                       VALUES (:ciCliente, :idVuelo, :valor, :idFormaPago, 1)",datos)
        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect(url_for('index'))


'''@app.route("/factura")
def factura():
    return render_template('factura_selection.html')'''



if __name__ == '__main__':
    app.run(debug=True)
