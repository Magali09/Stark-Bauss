from stark00 import *


while True:
    opcion = int(input("""
                    \n 1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de genero M:
                    \n 2.Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
                    \n 3.Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
                    \n 4.Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
                    \n 5.Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
                    \n 6.Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
                    \n 7.Calcular e informar cual es el superhéroe más y menos pesado.
                    \n 8.Elija una opcion..."""))
                    
                    
    
    
    match opcion:
        case 1:
            imprimir_nombres(lista_personajes)
           
        case 2:
            imprimir_altura_nombres(lista_personajes)
            
        case 3:
           mayor_altura(lista_personajes)
            
        case 4:
           menor_altura(lista_personajes)
            
        case 5:
           
           calcular_promedio(lista_personajes)
           
        case 6:
            mayor_altura(lista_personajes)
            menor_altura(lista_personajes)
    
            
        case 7:
            mas_menos_pesado(lista_personajes)
            
        case 8:
            break
       
         
  
            

    
            
            
            
        
            
     
                