import random
def jugar():
    print('********************\nAdivina el número de 1 a 100\n********************')
    print('Elige el nivel de dificultad')
    print('********************')
    print('(1)Novato\n(2)Intermedio\n(3)Avanzado')
    

    nivel = int(input('Nivel: '))

    if nivel == 1:
        total_intentos = 20
    elif nivel == 2:
        total_intentos = 10
    else:
        total_intentos = 5    


    #numero = int(random.random() *100)
    numero = random.randint(1,100)
    puntos = 1000

    round(numero)
    intento = 1


    for intento in range(1,total_intentos+1):
        
        print(f'Intento {intento} de {total_intentos}')
        entrada = int(input('Digita un número: '))

        if (entrada < 1 or entrada > 100):
            print('Digita un número mayor a 0 y menor o igual a 100')

        acierto = entrada == numero
        mayor = entrada > numero
        menor = entrada < numero

        if(acierto):
            print(f'El número ', entrada, ' es correcto.\nAdivinaste el número.\nTu puntajes es de: ', puntos, 'puntos')
            break
        else:
            if(mayor):
                print('El número es mayor.')
            elif(menor):
                print('El número es menor.')
            puntos_perdido = abs(numero - entrada)  
            puntos = puntos - puntos_perdido  
            print('No acertaste, intenta de nuevo.')
    print('Fin del juego.')    

if(__name__=="__main__"):
    jugar()            