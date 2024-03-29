from flask import Flask, render_template, redirect, url_for, request, flash, Blueprint
from connection import dbConnect

client_page = Blueprint ("cliente",__name__, template_folder="templates", url_prefix="/client")

@client_page.route("/cliente_ver")
def clienteVer():
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TB_CLIENTE ")
        dataCliente = cursor.fetchall()
        print(dataCliente)
        cursor.close()
        conexion.close()
        return render_template('client/accion_cliente.html',dataCliente=dataCliente)
    except:
        return redirect(url_for('error'))

@client_page.route("/editClient")
def clienteEditDelete():
    return redirect(url_for('cliente.clienteVer'))

@client_page.route("/deleteClient/<idCliente>")
def clienteDelete(idCliente):
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("UPDATE TB_CLIENTE SET ESTADO = '0' WHERE idCiCliente = :idCliente ",idCliente = idCliente)
        conexion.commit()
        conexion.close()
        return redirect(url_for('cliente.clienteVer'))
    except:
        return redirect(url_for('error'))

@client_page.route("/editCliente/<idCliente>")
def clienteEdit(idCliente):
    try:
        conexion=dbConnect()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TB_CLIENTE WHERE idCiCliente = :idCliente ",idCliente = idCliente)
        data = cursor.fetchall()
        conexion.close()
        return render_template('client/edit_cliente.html', data=data)
    except:
        return redirect(url_for('error'))

@client_page.route("/update_client/<idCliente>", methods = ['GET','POST'])
def clienteUpdate(idCliente):
    
    try:
        if request.method == 'POST':
            nombre = request.form ['nombre']
            ci = request.form ['ci']
            telefono = request.form ['telefono']
            apellido = request.form ['apellido']
            correo = request.form ['correo']
            
            datos = {'nombre':nombre, 'ci':ci,'telefono':telefono, 'apellido':apellido, 'correo':correo}

            conexion=dbConnect()
            cursor = conexion.cursor()
            print (datos)
            cursor.execute ("UPDATE TB_CLIENTE SET NOMBRE=:nombre, APELLIDO=:apellido, CORREO=:correo, TELEFONO=:telefono WHERE IDCICLIENTE =:ci",datos)

            conexion.commit()
            conexion.close()
    
            return redirect(url_for('cliente.clienteVer'))
    except:
        return redirect(url_for('error'))

@client_page.route('/cliente')
def cliente():
    return render_template('client/registro_cliente.html')

@client_page.route('/registro_cliente', methods = ['GET','POST'])
def registroCliente():
    try:
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
            return redirect(url_for('index'))  
    except:
        return redirect(url_for('error'))




