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