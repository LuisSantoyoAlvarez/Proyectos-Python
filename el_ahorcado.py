print('********************\nAhorcado\nVamos ajugar\n********************')
    
palabra_secreta = 'banana'.upper()
palabra_secreta = palabra_secreta.strip()
letras_acertadas = ['_','_','_','_','_','_']
print(letras_acertadas)

ahorco = False
acerto = False
errores = 0

while (not ahorco and not acerto):
    intento = input("\nDigita una letra: ")
    intento = intento.strip().upper()
    if intento in palabra_secreta:
        indice = 0
        

        for letra in palabra_secreta:
            if intento == letra:
                letras_acertadas[indice] = letra
                #print("Encontré la letra '{letra}' en la posición {indice}".format(letra, indice))
            indice += 1 
    else:
        errores += 1 
    ahorco = errores == 6  
    acerto = '_' not in letras_acertadas            
    print(letras_acertadas)
    if ahorco:
        print('\nPerdiste el juego.')
    elif acerto:
        print('\nGanaste el juego.')        

print('\nFin del Juego!') 