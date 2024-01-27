from flask import Flask, request
#request > Donde se almacenara toda la informacion de la poeticion actual del cliente
# cada vez que el cliente realice una peticion toda esa informacion se almacenara en el request

# __name__ > variable de python que sirve para indicar si el archivo que estamos utilizando es el archivo principal del proyecto esto sirve para que la instancia de Flask solamente corra en el archivo principal y asi evitar instancias de Flask en archivos secundarios del proyecto

app = Flask(__name__)

# si el archivo es el archivo principal el valor de __name__ sera __main__

#Decoradores
# Sirve para utilizar un metodo sin la necesidad de modificarlo desde la clase en la cual estamos hacioendo la referencia
# GET > Devolver
# POST > Creaciones
# PUT > Actualizaciones
@app.route('/', methods=['GET', 'POST', 'PUT'])
def inicio():
    # request.method > devolvera el metodo HTTP que esta realizando el cliente
    if request.method == 'PUT' :
        return {
            'message' : ' Actualizacion exitosa'
        }, 200 # estado de respuesta http (OK)
        
    elif request.method == 'GET':
         return {
            'message' : ' Devolucion exitosa'
        }, 200 # OK
         
    elif request.method == 'POST':
         return {
            'message' : ' Creacion exitosa'
        }, 201 # Created

# levantamos nuestro servidor flask
app.run(debug=True)
