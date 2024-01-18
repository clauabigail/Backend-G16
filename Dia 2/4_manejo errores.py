numero = 10
# try (intentalo)
# y si el que falla entonces capturo el error con una except (excepcion)
try:
    print(10/'eduardo')
    
except ZeroDivisionError:
    # si el error es de tipo de division entre 0 entonces ingresara aca
    print('No se puede dividir entre 0')

except Exception as error:
    # ver que es el causante del error
    print(error.args)
    #ver
    print(type(error))
    print('operacion incorrecta')
    
print('otro codigo')

# lambda

# Crear una funcion que reciba dos numeros y devuelva cual es el mayor, si el usuario ingresa un valor que no sea un numero entonces volver a pedirselo que sea un numero.
def numeroMayor(numero1, numero2):
    pass
# pista: utilicen un while, un if y un try - except
while True:
    try:
        numero1= int(input('Ingresa el primer numero'))
        numero2= int(input('Ingresa el segundo numero'))
        resultado= numeroMayor(numero1, numero2)
        print('El numero mayor es {}'.format(resultado))
        break
    except:
        print('Tienes que ingresar solo numeros') 
               