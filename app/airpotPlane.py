from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from connection import dbConnect

airpor_plane_page = Blueprint ("aeropuetoAvion",__name__, template_folder="templates", url_prefix="/airport_plane")

@airpor_plane_page.route('/verVuelos')
def verVuelos():
    conexion = dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM TB_AVION")
    dataAvion = cursor.fetchall()

    cursor2 = conexion.cursor()
    cursor2.execute("SELECT * FROM TB_AEROPUERTO")
    dataAeropuerto = cursor2.fetchall()
    
    print (dataAvion)
    print (dataAeropuerto)

    return render_template('airportPlane/actionAP.html',dataAvion = dataAvion, dataAeropuerto = dataAeropuerto)