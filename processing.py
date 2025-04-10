import csv
import argparse
import sys

def process(file):
    #Declaración de variables de balance final, contadores y transacción mayor inicializadas con valores en 0
    balance = 0
    creditCounter = 0
    debitCounter = 0
    largestTransaction = {'id':'-','tipo':'-','monto':'0'}

    #Lectura de csv 'data.csv' o 'test.csv' para pruebas
    transactionReader = csv.DictReader(file)

    #Recorrido de cada transacción
    for transaction in transactionReader:
        #Conversion del monto a float para operacion
        amount = float(transaction['monto'])

        #Operacion de la transacción e incremento del contador en base a su tipo
        if(transaction['tipo'] == 'CrÃ©dito'):
            balance += amount
            creditCounter += 1
        else:
            balance -= amount
            debitCounter += 1
        
        #Asignacion de transacción mayor si se cumple el caso (no hay montos iguales)
        largestTransaction = (transaction, largestTransaction)[ float(largestTransaction['monto']) > amount]
    
    #Generación del reporte con redondeo en valor final
    print("Reporte de Transacciones \n---------------------------------------------" )
    print("Balance Final:", round( balance, 2 ))
    print("Transacción de Mayor Monto: ID", largestTransaction['id'],"-", largestTransaction['monto'])
    print("Conteo de Transacciones: Crédito:", creditCounter, "Débito:", debitCounter)

#Lectura del nombre del archivo a utilizar
parser = argparse.ArgumentParser("argument_detection")
parser.add_argument("fileName")
args = parser.parse_args()

#Validacion de la existencia del archivo en la ubicacion ./input
try:
    csvfile = open(f'./input/{args.fileName}')
except:
    sys.exit("File not found in input folder")

process(csvfile)