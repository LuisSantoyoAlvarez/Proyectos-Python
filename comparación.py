numero_1 = float(input('ingrese un número: '))
numero_2 = float(input('ingrese un segundo número: '))

if numero_1 < numero_2:
    print(f'El número mas grande es:  {numero_2}')
elif numero_2 < numero_1:
    print(f'El número mas grande es:  {numero_1}')
else:
    print('Los números son iguales.')    