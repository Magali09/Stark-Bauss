from data_stark import lista_personajes
from os import system
system("cls")



#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M   
def imprimir_genero_masculino(lista_personajes):
    """_summary_

    Args:
        lista_personajes (_type_): _description_
    """
    for personajes in lista_personajes:
        if personajes["genero"] == "M":
            genero = personajes["nombre"]
            print(f"{genero}")
            
def imprimir_genero_femenino(lista_personajes):
    for personajes in lista_personajes:
        if personajes["genero"] == "F":
            genero = personajes["nombre"]
            print(f"{genero}")

def imprimir_altura_maxima_masculino(lista_personajes):
    maximo_altura_masculino = 0
    bandera_mas_alto_masculino = True
    for personajes in lista_personajes:
         if personajes["genero"] == "M":  # Verificar el género
            altura = float(personajes["altura"])
            if bandera_mas_alto_masculino == True or altura > maximo_altura_masculino:
                maximo_altura_masculino = float(personajes["altura"])
                nombre_mas_alto_maculino = personajes["nombre"]
                bandera_mas_alto_masculino = False
    print(f"El masculino mas alto es: {nombre_mas_alto_maculino} y su altura es: {maximo_altura_masculino}") 

def imprimir_altura_maxima_femenino(lista_personajes):
    maxima_altura_femenino = 0
    bandera_mas_alta_femenina = True
    for personajes in lista_personajes:
        if personajes["genero"] == "F":  # Verificar el género
            altura = float(personajes["altura"])
            if bandera_mas_alta_femenina == True or altura > maxima_altura_femenino:
                maxima_altura_femenino = float(personajes["altura"])
                nombre_mas_alta_femenina = personajes["nombre"]
                bandera_mas_alta_femenina = False
            
    print(f"La femenina mas alta es: {nombre_mas_alta_femenina} y su altura es: {maxima_altura_femenino}") 
    
  
def imprimir_altura_minima_masculino(lista_personajes):    
    minimo_altura_masculino = 0
    bandera_mas_bajo_masculino = True 
    for personajes in lista_personajes:
        if personajes["genero"] == "M":  # Verificar el género
            altura = float(personajes["altura"])
            if bandera_mas_bajo_masculino == True or altura < minimo_altura_masculino:
                minimo_altura_masculino = float(personajes["altura"])
                nombre_mas_bajo_masculino = personajes["nombre"]
                bandera_mas_bajo_masculino = False
    
    print(f"El masculino mas bajo es: {nombre_mas_bajo_masculino} y su altura es: {minimo_altura_masculino}")
    
def imprimir_altura_minima_femenino(lista_personajes):
    minima_altura_femenina = 0
    bandera_menor_altura_femenina = True
    for personajes in lista_personajes:
        if personajes["genero"] == "F":  # Verificar el género
            altura = float(personajes["altura"])
            if bandera_menor_altura_femenina == True or altura < minima_altura_femenina:
                minima_altura_femenina = float(personajes["altura"])
                nombre_menor_altura_femenina = personajes["nombre"]
                bandera_menor_altura_femenina = False
            
    print(f"La femenina menos alta es: {nombre_menor_altura_femenina} y su altura es: {minima_altura_femenina}")    
    
def imprimir_altura_promedio_genero_masculino(lista_personajes):
    acumulador_masculino = 0
    contador_altura_masculino = 0   
    for personajes in lista_personajes: 
        if personajes["genero"] == "M":  # Verificar el género
            acumulador_masculino += float(personajes["altura"])
            contador_altura_masculino += 1

    promedio_altura_masculino = acumulador_masculino / contador_altura_masculino
    print(f"El promedio de altura en los superhéroes masculino es: {promedio_altura_masculino}")        

def imprimir_altura_promedio_genero_femenino(lista_personajes):
    acumulador_femenino = 0
    contador_altura_femenino = 0   
    for personajes in lista_personajes: 
        if personajes["genero"] == "F":  # Verificar el género
            acumulador_femenino += float(personajes["altura"])
            contador_altura_femenino += 1
            

    promedio_altura_femenino = acumulador_femenino / contador_altura_femenino
    print(f"El promedio de altura en los superhéroes femenino es: {promedio_altura_femenino}")    




def imprimir_tipo_color_ojos(lista_personajes):
    contador_color_ojos = {}
    for personajes in lista_personajes:
        color_ojos = personajes["color_ojos"]
        if color_ojos in contador_color_ojos:
            contador_color_ojos[color_ojos] += 1
        else:
            contador_color_ojos[color_ojos] = 1

    return contador_color_ojos


def imprimir_tipo_color_pelos(lista_personajes):
    contador_color_pelo = {}
    for personajes in lista_personajes:
        color_pelo = personajes["color_pelo"]
        if color_pelo in contador_color_pelo:
            contador_color_pelo[color_pelo] += 1
        else:
            contador_color_pelo[color_pelo] = 1

    return contador_color_pelo    
   
def imprimir_tipo_inteligencia(lista_personajes):
    contador_tipo_inteligencia = {}
    for personajes in lista_personajes:
        inteligencia = personajes["inteligencia"]
        if not inteligencia:
            inteligencia = "No tiene"
        if inteligencia in contador_tipo_inteligencia:
            contador_tipo_inteligencia[inteligencia] += 1
        else:
            contador_tipo_inteligencia[inteligencia] = 1
        
    return contador_tipo_inteligencia
def agrupacion_color_de_ojos():
    personajes_por_color = {}
   
    for personaje in lista_personajes:
        color_de_ojos = personaje["color_ojos"]

        if color_de_ojos in personajes_por_color:
            personajes_por_color[color_de_ojos].append(personaje)
      
        else:
            personajes_por_color[color_de_ojos] = [personaje]

    for color, personajes in personajes_por_color.items():
        print(f"Superheroes con ojos de color {color}: \n")
        for nombre in personajes:
            print(nombre["nombre"])
            
def agrupacion_color_de_pelo():
    personaje_color_de_pelo = {}
   
    for personaje in lista_personajes:
        color_de_pelo = personaje["color_pelo"]

        if color_de_pelo in personaje_color_de_pelo:
            personaje_color_de_pelo[color_de_pelo].append(personaje)
      
        else:
            personaje_color_de_pelo[color_de_pelo] = [personaje]

    for color, personajes in personaje_color_de_pelo.items():
        print(f"Superheroes con pelo color {color}: \n")
        for nombre in personajes:
            print(nombre["nombre"])
        
def agrupacion_tipo_inteligencia():
    personajes_por_inteligencia = {}
    for personaje in lista_personajes:
        inteligencia = personaje["inteligencia"]
        
        if inteligencia in personajes_por_inteligencia:
            personajes_por_inteligencia[inteligencia].append(personaje)
      
        else:
            personajes_por_inteligencia[inteligencia] = [personaje]
   
    for inteligencia, personajes in personajes_por_inteligencia.items():
        print(f"\n Superheroes con inteligencia {inteligencia}: \n ")
        
        for nombre in personajes:
            print(nombre["nombre"])




    
                
    


   
   


   
      

    

 
 

            
    
           
            
        

      
        


