# def > definition
# toda funcion puede recibir parametros
# toda funcion puede devolver un resultado
def saludar():
    print('Hola buenas noches!')

# si la funcion esta definida pero no esta siendo implementa (llamada) el codigo dentro de la funcion nunca se ejecutara

saludar()

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print('La suma es', resultado)

sumar (10 , 20)

def multiplicar(numero1 , numero2):
    resultado = numero1 * numero2
    #return sirve para devolver el resultado de la ejecucion de la funcion
    return resultado,2000


resultado_multiplicacion = multiplicar(50 , 20)
print(resultado_multiplicacion)

# si queremos colocar un parametro por defecto entonces los parametros por defecto SIEMPRE van al final
def saludarCordialmente(nombre, cargo='Siñorsh'):
    return 'Buenas noches {} {}'.format(cargo, nombre)

print(saludarCordialmente('Juancito'))
print(saludarCordialmente('Sofia', 'Damicela'))

print(saludarCordialmente(cargo='Gerente', nombre='Raul'))

# el * al momento de definir una funcion indicaremos que esta puede recibir n valores
# args > arguments
def sumaNumeros(*args):
    resultado = 0
    #devolver la sumatoria de todos los valores que recibe args
    for numero in args:
        resultado = resultado + numero
        # resultado += numero
    return resultado

resultado = sumaNumeros(10, 20, 30, 40, 50, 60, 70, 80, 90, 110)
print(resultado)
    


# ** sirve para recibir un numero ilimitado de parametros
#vkwargs > keyboard arguments
def capturarPersona(**kwargs):
    return kwargs

resultado = capturarPersona (nombre='Eduardo',
                 apellido='De Rivero', 
                 correo='ederiveroman@gmail.com',
                 estatura=1.87)
print(resultado)

data = {'nombre':'Eduardo',
    'apellido':'De Rivero', 
    'correo':'ederiveroman@gmail.com',
    'estatura':1.87}
# en el metodo .get sollo sirve para devolver informacion mas no para asignar nuevos valores
print (data.get('apellido'))
data['edad']= 30
# no se puede usar el metodo .get para cuestiones de asignacion, netamente para la lectura
# data.get('nacionalidad')='Peruano'
print('hola')