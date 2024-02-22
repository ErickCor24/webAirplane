from flask import Blueprint,render_template
from connection import dbConnect

airport= Blueprint("airport",__name__,template_folder="templates",url_prefix="/airport")
@airport.route("/airport_and_plane")
def airport_and_plane():
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TB_AEROPUERTO")
        aeropuertos = cursor.fetchall()
        # Consulta a la segunda tabla
        cursor.execute("SELECT * FROM TB_AVION")
        aviones = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('airport/airport.html',aeropuertos=aeropuertos,aviones=aviones)
    except:
        return redirect(url_for('error'))
        