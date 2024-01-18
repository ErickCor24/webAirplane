from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from connection import dbConnect

vuelo_page = Blueprint ("vuelo",__name__, template_folder="templates", url_prefix="/flight")

@vuelo_page.route('/vuelo')
def vuelo():
    conexion = dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TB_AVION")
    aviones = cursor.fetchall()
    cursor.close()
    cursor3 = conexion.cursor()
    cursor3.execute("SELECT * FROM TB_AEROPUERTO")
    aeropuertos = cursor3.fetchall()
    cursor3.close()

    return render_template('flight/crear_vuelo.html', aviones = aviones, aeropuertos = aeropuertos)

@vuelo_page.route('/registro_vuelo', methods = ['GET','POST'])
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

        cursor.execute ("INSERT INTO TB_VUELO (FECHASALIDA, HORASALIDA, PRECIO, ESTADO, IDAVION, IDAEROPUERTO) \
                        VALUES (TO_DATE(:fechaS,'YYYY-MM-DD'), :horaS, :precio, 1 ,:avionA, :aeroP) RETURNING IDVUELO INTO :idVariable",datos)       
        
        id_generado = idVariable.getvalue()       
        conexion.commit()
        cursor.close() 
        conexion.close()       
        return redirect(url_for('index'))
    
@vuelo_page.route('/ver_vuelo', methods = ['GET','POST'])
def verVuelo():
    conexion=dbConnect()
    cursorVuelo = conexion.cursor()
    cursorVuelo.execute("SELECT TB_VUELO.*, TB_AVION.*, TB_AEROPUERTO.* FROM TB_VUELO JOIN TB_AVION ON TB_VUELO.IDAVION = TB_AVION.IDAVION JOIN TB_AEROPUERTO ON TB_VUELO.IDAEROPUERTO = TB_AEROPUERTO.IDAEROPUERTO ")
    dataVuelo = cursorVuelo.fetchall()      
    conexion.close()
    return render_template('flight/consultar_vuelo.html', dataVuelo=dataVuelo)


@vuelo_page.route('/editarVuelo/<idVuelo>')
def editarVuelo(idVuelo):
    conexion=dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TB_VUELO WHERE idVuelo = :idVuelo ",idVuelo = idVuelo)
    datos = cursor.fetchall()
    cursor.close()


    cursor2 = conexion.cursor()
    cursor2.execute("SELECT * FROM TB_AVION")
    aviones = cursor2.fetchall()
    cursor2.close()

    cursor3 = conexion.cursor()
    cursor3.execute("SELECT * FROM TB_AEROPUERTO")
    aeropuertos = cursor3.fetchall()
    cursor3.close()
    conexion.close()

    return render_template('flight/editarVuelo.html', data=datos, aviones = aviones, aeropuertos = aeropuertos)

@vuelo_page.route("/update_vuelo/<idVuelo>", methods = ['GET','POST'])
def vueloUpdate(idVuelo):
    
    if request.method == 'POST':
        fechaSalida = request.form ['fechaSalida']
        horaSalida = request.form ['horaSalida']
        precio = request.form ['precio']
        avionAsignado = request.form ['avionAsignado']
        aeropuertoDestino = request.form ['aeropuertoDestino']
    
        conexion = dbConnect()
        cursor = conexion.cursor()
        idVariable = cursor.var(int)
        datos = {'fechaS':fechaSalida , 'horaS':horaSalida, 'precio': precio, 'avionA':avionAsignado, 'aeroP': aeropuertoDestino, 'idVuelo':idVuelo }
        print(datos)
        cursor.execute ("UPDATE TB_VUELO SET FECHASALIDA =(TO_DATE(:fechaS,'YYYY-MM-DD')), HORASALIDA =:horaS, PRECIO = :precio, IDAVION = :avionA, IDAEROPUERTO = :aeroP WHERE IDVUELO =:idVuelo  ",datos)       

        conexion.commit()
        cursor.close() 
        conexion.close()       
        return redirect(url_for('vuelo.verVuelo'))
    
@vuelo_page.route ("/eliminarVuelo/<idVuelo>")
def eliminarVuelo (idVuelo):
    conexion=dbConnect()
    cursor = conexion.cursor()
    cursor.execute("UPDATE TB_VUELO SET ESTADO = '0' WHERE IDVUELO = :idVuelo ",idVuelo = idVuelo)
    conexion.commit()
    conexion.close()
    return redirect(url_for('vuelo.verVuelo'))
