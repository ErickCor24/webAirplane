from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from connection import dbConnect

boleto_page = Blueprint ("boleto",__name__, template_folder="templates", url_prefix="/ticket_passenger")

rtnPasajero = None
vueloId = None

@boleto_page.route('/registro')
def boleto():
    return render_template('passenger/Registro_boleto.html')

@boleto_page.route('/registro_pasajero', methods = ['GET','POST'])
def registro():
    try:
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
            return redirect(url_for('boleto.seleccion'))
    except:
        return redirect(url_for('error'))

#Funciones de regitsrar el boleto seleccionando el Vuelo registrado y clase 
@boleto_page.route ('/seleccion_vuelo')
def seleccion():
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TB_VUELO ")
        dataVuelo = cursor.fetchall()
        cursor.close()
        
        cursor2 = conexion.cursor()
        cursor2.execute("SELECT * FROM TB_AEROPUERTO ")
        dataDestino = cursor2.fetchall()
        conexion.close()

        return render_template('ticket/flight_selection.html', data=dataVuelo, data2=dataDestino)   
    except:
        return redirect(url_for('error'))

@boleto_page.route("/boleto_ver")
def boleto_ver():
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TB_BOLETO ")
        dataBoleto = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('ticket/boleto_selection.html',dataBoleto=dataBoleto)
    except:
        return redirect(url_for('error'))

@boleto_page.route('/flight_selection',methods = ['GET','POST'])
def flightSelection():
    try:
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
            return redirect(url_for('boleto.pago'))
    except:
        return redirect(url_for('error'))
    

#Se registra el tipo de pago y el valor a pagar
@boleto_page.route("/pago")
def pago():
    return render_template('factura/registro_pago.html')

@boleto_page.route("/registro_pago", methods = ['GET','POST'])
def registroPago():
    try:
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
    except:
        return redirect(url_for('error'))
