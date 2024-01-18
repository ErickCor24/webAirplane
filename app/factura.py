from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from connection import dbConnect

factura_page = Blueprint ("factura",__name__, template_folder="templates", url_prefix="/factura")


@factura_page.route("/ver_factura")
def verFactura ():
    conexion=dbConnect()
    cursor = conexion.cursor()
    cursor.execute("SELECT TB_FACTURA.*, TB_VUELO.*, TB_FORMA_PAGO.*, TB_CLIENTE.* \
                   FROM TB_FACTURA JOIN TB_VUELO ON TB_FACTURA.IDVUELO = TB_VUELO.IDVUELO \
                   JOIN TB_FORMA_PAGO ON TB_FACTURA.IDFORMAPAGO= TB_FORMA_PAGO.IDFORMAPAGO \
                   JOIN TB_CLIENTE ON TB_FACTURA.IDCICLIENTE = TB_CLIENTE.IDCICLIENTE")
    dataFacturas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('factura/factura_selection.html',dataFactura=dataFacturas)

@factura_page.route('/eliminar_factura/<idFactura>')
def deleteFactura (idFactura):
    conexion=dbConnect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM TB_FACTURA WHERE IDFACTURA = :idFactura",idFactura = idFactura)
    conexion.commit()
    cursor.close()
    conexion.close()
    print (idFactura)
    return redirect(url_for('factura.verFactura'))

    