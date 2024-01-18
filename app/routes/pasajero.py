from flask import Blueprint,render_template,redirect,url_for,request
from models.aeropuerto import Aeropuerto
from models.avion import Avion
from models.equipaje import Equipaje
from utils.db import db
from models.pasajero import Pasajero

pasajero = Blueprint('pasajero', __name__, template_folder='templates',url_prefix='/pasajero')


@pasajero.route('/register',methods=['GET','POST'])
def register():
    current_equipaje = Equipaje.query.first()
    id_equipaje = current_equipaje.id
    if request.method == 'POST':
        return redirect(url_for('pasajero.register'))
    
   




@pasajero.route('/aeropuerto')
def aeropuerto_and_plane():
    aeropuertos = Aeropuerto.query.all()
    aviones = Avion.query.all()
    return render_template('views/pasajero/aeropuerto.html', aeropuertos=aeropuertos, aviones=aviones)


@pasajero.route('/aeropuerto/create')
def aeropuerto_create():
    aeropuertos = [
        {"id": "AP001", "nombre": "Aeropuerto Internacional Mariscal Sucre", "ciudad": "Quito", "pais": "Ecuador"},
        {"id": "AP002", "nombre": "Aeropuerto Internacional de Schiphol", "ciudad": "Amsterdam", "pais": "Paises Bajos"},
        {"id": "AP003", "nombre": "Aeropuerto Internacional de Jorge Chávez", "ciudad": "Lima", "pais": "Peru"},
        {"id": "AP004", "nombre": "Aeropuerto Internacional de Dubái", "ciudad": "Dubai", "pais": "Emiratos Arabes"},
        {"id": "AP005", "nombre": "Aeropuerto Internacional de Haneda", "ciudad": "Tokio", "pais": "Japon"},
        {"id": "AP006", "nombre": "Aeropuerto Internacional de Los Ángeles", "ciudad": "Los Angeles", "pais": "USA"},
        {"id": "AP007", "nombre": "Aeropuerto Internacional de Sídney", "ciudad": "Sidney", "pais": "Australia"},
        {"id": "AP008", "nombre": "Aeropuerto Internacional de Frankfurt", "ciudad": "Frankfurt", "pais": "Alemania"},
        ]
    try:
        for aeropuerto in aeropuertos:
            airports = Aeropuerto(id=aeropuerto['id'], nombre=aeropuerto['nombre'], ciudad=aeropuerto['ciudad'], pais=aeropuerto['pais'])
            db.session.add(airports,)
            
            print(f"Airport {airports.id} created")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")
    return redirect(url_for('pasajero.aeropuerto_and_plane'))


@pasajero.route('/avion/create')
def avion_create():
    aviones = [
    {"id": "AV001", "capacidad": 85, "marca": "Airbus"},
    {"id": "AV002", "capacidad": 150, "marca": "Cessna"},
    {"id": "AV003", "capacidad": 120, "marca": "Airbus"},
    {"id": "AV004", "capacidad": 300, "marca": "Boeing"},
    {"id": "AV005", "capacidad": 150, "marca": "Cessna"},
    {"id": "AV006", "capacidad": 220, "marca": "Boeing"},
    ]
    try:
        for avion in aviones:
            planes = Avion(id=avion['id'], capacidad=avion['capacidad'], marca=avion['marca'])
            db.session.add(planes,)

        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error occurred: {e}")

    return redirect(url_for('pasajero.aeropuerto_and_plane'))



  

   
# except Exception as e:  
#     db.session.rollback()
#     print(f"Error occurred: {e}")
    

  

     
    