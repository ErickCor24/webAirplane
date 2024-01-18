from flask import Blueprint,render_template,redirect,url_for,request,flash

from connection import dbConnect




passenger = Blueprint("passenger",__name__,template_folder="templates",url_prefix="/passenger")


@passenger.route("/all")
def all():
    conexion = dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT TB_PASAJERO.*,TB_EQUIPAJE.* FROM TB_PASAJERO JOIN TB_EQUIPAJE ON TB_PASAJERO.IDEQUIPAJE=TB_EQUIPAJE.IDEQUIPAJE")
    pasajeros = cursor.fetchall()
    conexion.close()
    return render_template("passenger/Pasajero_Equipaje.html",pasajeros=pasajeros)

@passenger.route("edit/<int:id>",methods=["GET","POST"])
def edit(id):
    conexion = dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT TB_PASAJERO.*,TB_EQUIPAJE.* FROM TB_PASAJERO JOIN TB_EQUIPAJE ON TB_PASAJERO.IDEQUIPAJE=TB_EQUIPAJE.IDEQUIPAJE WHERE IDPASAJERO=%s",(id))
    pasajero = cursor.fetchone()
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        equipaje = request.form["equipaje"]
        cursor.execute("UPDATE TB_PASAJERO SET NOMBRE=%s,APELLIDO=%s,EDAD=%s,IDEQUIPAJE=%s WHERE IDPASAJERO=%s",(nombre,apellido,edad,equipaje,id))
        conexion.commit()
        conexion.close()
        return redirect(url_for("passenger.all"))
    conexion.close()

    return render_template("passenger/Pasajero_Equipaje_edit.html",pasajero=pasajero)

@passenger.route("delete/<int:id>")
def delete(id):
    conexion = dbConnect()
    cursor = conexion.cursor()
    #cambiar el estado de la tabla
    cursor.execute("UPDATE TB_PASAJERO SET ESTADO=%s WHERE IDPASAJERO=%s",(0,id))
    conexion.commit()
    conexion.close()
    return redirect(url_for("passenger.all"))