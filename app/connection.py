import cx_Oracle

def dbConnect():
    try:
        connect = cx_Oracle.connect(
        user = 'JOHAN123',
        password = 'david123',
        dsn = 'localhost/xe')
        return connect
    
    except Exception as err:
        print("Error en la conexion a la DB", err)

    else:
        print("Conectado a la DB", connect.version)
    #connection.close()
