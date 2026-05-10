import horca
import adivina_un_numero

print('********************\nJuegos de Python\n********************')
print("(1) Juego de la Horca\n(2) Juego de adivinar el número")
juego = int(input("Selecciona el juego que deseas: "))
if juego == 1:
    print("Juego de la horca")
    horca.jugar()
elif juego ==2:
    print("Juego de adivinar el número")
    adivina_un_numero.jugar()