from data_stark import  lista_personajes
from os import system
system("cls")



def imprimir_nombres(lista_personajes):

    for personajes in lista_personajes:
        print(personajes["nombre"])
         
    
def imprimir_altura_nombres(lista_personajes):
    
    for personajes in lista_personajes:
        print(f"{personajes['nombre']} - Altura: {personajes['altura']} cm")
      
    

def mayor_altura(lista_personajes):
    bandera_mas_alto = True
    maximo_altura = 0  
    for personajes in lista_personajes:
        altura = float(personajes["altura"])
        if bandera_mas_alto == True or altura > maximo_altura:
                maximo_altura = float(personajes["altura"])
                nombre_mas_alto = personajes["nombre"]
                bandera_mas_alto = False
    print(f"El mas alto es: {nombre_mas_alto}y si altura es: {maximo_altura}")
    
def menor_altura(lista_personajes):
    bandera_mas_bajo = True
    minimo_altura = 0  
    for personajes in lista_personajes:
        altura = float(personajes["altura"])
        if bandera_mas_bajo == True or altura < minimo_altura:
                minimo_altura = float(personajes["altura"])
                nombre_menos_alto = personajes["nombre"]
                bandera_mas_bajo = False
    print(f"El menos alto es: {nombre_menos_alto} y su altura es: {minimo_altura}")

def calcular_promedio(lista_personajes):
  
    acumulador_altura = 0
    contador_altura = 0
    for personajes in lista_personajes:
        acumulador_altura += float(personajes["altura"])
        contador_altura += 1
    promedio_altura = acumulador_altura / contador_altura
    print(f"El promedio altura es: {promedio_altura}")
    

def mas_menos_pesado(lista_personajes):
    bandera_mas_pesado = True
    bandera_menos_pesado = True
    mas_pesado = 0
    menos_pesado = 0
    for personajes in lista_personajes:
        peso = float(personajes["peso"])
        if peso > mas_pesado or bandera_mas_pesado == True:
            mas_pesado = float(personajes["peso"])
            nombre_mas_pesado = personajes["nombre"]
            bandera_mas_pesado = False
        if peso < menos_pesado or bandera_menos_pesado == True:
            menos_pesado = float(personajes["peso"])
            nombre_menos_peso = personajes["nombre"]
            bandera_menos_pesado = False
    print(f"El super con mas peso es: {mas_pesado} y su nombre es: {nombre_mas_pesado}")
    print(f"El super con menos peso es: {menos_pesado} y su nombre es: {nombre_menos_peso}") 
   
