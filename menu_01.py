from stark01 import *


while True:
    opcion = int(input("""
                    \n 1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
                    \n 2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
                    \n 3.Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
                    \n 4.Recorrer la lista y determinar cuál es el superhéroe más alto de género F
                    \n 5.Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
                    \n 6.Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
                    \n 7.Recorrer la lista y determinar la altura promedio de los superhéroes de género M
                    \n 8.Recorrer la lista y determinar la altura promedio de los superhéroes de género F
                    \n 9.Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 6)
                    \n 10.Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                    \n 11.Determinar cuántos superhéroes tienen cada tipo de color de pelos.
                    \n 12.Determinar cuántos superhéroes tienen cada tipo de inteligencia
                    \n 13.Listar todos los superhéroes agrupados por color de ojos.
                    \n 14.Listar todos los superhéroes agrupados por color de pelo.
                    \n 15.Listar todos los superhéroes agrupados por tipo de inteligencia
                    \n 16. salir
                    \n 17.Elija una opcion..."""))
                            
                    
                    
    
    
    match opcion:
        case 1:
            imprimir_genero_masculino(lista_personajes)
           
        case 2:
            imprimir_genero_femenino(lista_personajes)
            
        case 3:
            imprimir_altura_maxima_masculino(lista_personajes)
            
        case 4:
            imprimir_altura_maxima_femenino(lista_personajes)
            
        case 5:
            imprimir_altura_minima_masculino(lista_personajes)
           
        case 6:
            imprimir_altura_minima_femenino(lista_personajes)
           
        case 7:
            imprimir_altura_promedio_genero_masculino(lista_personajes)
            
        case 8:
            imprimir_altura_promedio_genero_femenino(lista_personajes)
            
        case 9:
            imprimir_altura_maxima_masculino(lista_personajes)  
            imprimir_altura_maxima_femenino(lista_personajes)
            imprimir_altura_minima_masculino(lista_personajes)
            imprimir_altura_minima_femenino(lista_personajes)
        case 10:
            
            respuesta = imprimir_tipo_color_ojos(lista_personajes)
            print(f"La cantidad de colores de ojos que hay es: \n{respuesta}")
            
        case 11:
            respuesta = imprimir_tipo_color_pelos(lista_personajes)
            print(respuesta)
            
        case 12:
            tipo_inteligencia = imprimir_tipo_inteligencia(lista_personajes)   
            print(f"Número de superhéroes con cada tipo de inteligencia: {tipo_inteligencia}")
        case 13:
            print(agrupacion_color_de_ojos())   
        case 14:
            print(agrupacion_color_de_pelo())
        case 15:
            print(agrupacion_tipo_inteligencia())
        case 16:
            break
       
         
  
            

    
            
            
            
        
            
     
                