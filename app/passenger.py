from flask import Blueprint,render_template,redirect,url_for,request,flash

from connection import dbConnect

passenger = Blueprint("passenger",__name__,template_folder="templates",url_prefix="/passenger")

@passenger.route("/all")
def all():
    try:
        conexion = dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT TB_PASAJERO.*,TB_EQUIPAJE.* FROM TB_PASAJERO JOIN TB_EQUIPAJE ON TB_PASAJERO.IDEQUIPAJE=TB_EQUIPAJE.IDEQUIPAJE")
        pasajeros = cursor.fetchall()

        conexion.close()
        return render_template("passenger/Pasajero_Equipaje.html",pasajeros=pasajeros)
    except:
        return redirect(url_for('error'))

@passenger.route("edit/<idPasajero>")
def edit(idPasajero):
    try:
        conexion = dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT TB_PASAJERO.*, TB_EQUIPAJE.* FROM TB_PASAJERO \
                    JOIN TB_EQUIPAJE ON TB_PASAJERO.IDEQUIPAJE = TB_EQUIPAJE.IDEQUIPAJE WHERE IDPASAJERO = :idPasajero", idPasajero = idPasajero)
        
        pasajero = cursor.fetchall()
        print(pasajero)
        cursor.close()
        return render_template("passenger/Pasajero_Equipaje_edit.html", pasajero = pasajero)
    except:
        return redirect(url_for('error'))

@passenger.route ('updateEquipaje/<idPasajero>/<idEquipaje>', methods = ['GET','POST'])
def update(idPasajero, idEquipaje):
    try:
        if request.method == "POST":       
            nombre = request.form['nombre']
            ci = request.form['ci']
            telefono = request.form['telefono']
            apellido = request.form['apellido']
            correo = request.form['correo']
            CantMaletas = request.form['CantMaletas']
            peso = request.form['Peso']

            print(idPasajero, idEquipaje)
            conexion = dbConnect()
            cursor = conexion.cursor()


            datosEquipaje ={'cantMaletas':CantMaletas,'peso':peso, 'idEquipaje':idEquipaje}
            cursor.execute ("UPDATE TB_EQUIPAJE SET CANTIDADMALETAS=:CantMaletas, PESO = :peso WHERE IDEQUIPAJE =:idEquipaje ",datosEquipaje)

            conexion.commit()
            conexion.close()
            
            conexion2 = dbConnect()
            cursor2 = conexion2.cursor()
            datosPasajero ={'nombre':nombre, 'apellido':apellido, 'ci':ci,'telefono':telefono,'correo':correo, 'idPasajero':idPasajero }
            print(datosPasajero)
            cursor2.execute ("UPDATE TB_PASAJERO SET NOMBRE=:nombre ,APELLIDO=:apellido ,CIPASAJERO=:ci, CORREO=:correo , TELEFONO=:telefono WHERE IDPASAJERO =:idPasajero ", datosPasajero)

            conexion2.commit()
            cursor2.close()
            conexion2.close()
            return redirect(url_for('passenger.all'))
    except:
        return redirect(url_for('error'))

@passenger.route("delete/<idPasajero>")
def delete(idPasajero):
    try:
        conexion = dbConnect()
        cursor = conexion.cursor()
        #cambiar el estado de la tabla
        cursor.execute("UPDATE TB_PASAJERO SET ESTADO = 0 WHERE IDPASAJERO =:idPasajero",idPasajero = idPasajero)
        conexion.commit()
        conexion.close()
        return redirect(url_for('passenger.all'))
    except:
        return redirect(url_for('error'))