import cx_Oracle

def dbConnect():
    try:
        connect = cx_Oracle.connect(
        user = 'UsuarioProyecto',
        password = '1234',
        dsn = 'localhost/xe')
        return connect
    
    except Exception as err:
        raise err
        print("Error en la conexion a la DB", err)


    #connection.close()
