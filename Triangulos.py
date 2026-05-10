lado_1 = float(input('Ingrese la medida del primer lado: '))
lado_2 = float(input('Ingrese la medida del segundo lado: '))
lado_3 = float(input('Ingrese la medida del tercer lado: '))

if (lado_1 + lado_2 > lado_3) and (lado_2 + lado_3 > lado_1) and (lado_3 + lado_1 > lado_2):
    print('Tú triangulo es: ')
    if (lado_1 == lado_2) and (lado_2 == lado_3):
        print('Equilatero.')
    elif (lado_1 == lado_2) or (lado_2 == lado_3):
        print('Isoceles') 
    elif (lado_1 != lado_2 != lado_3):
        print('Escaleno')
else:
    print ('Ingrese datos correctos de un triangulo, teniendo en cuenta que: Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero.')    