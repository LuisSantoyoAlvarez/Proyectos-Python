#En este programa, nos piden que si un número es divisible entre 15, se coloque la palabra "FizzBuzz", pero si es divisible entre 3, se imprima "Buzz" y si es divisible entre 5, "Fizz".

def fizzBuzz(n):
   #Varibles para decidir cuando dice una palabra u otra
    if n<=0 or n>=200000:
        print(f'error: {n} fuera del rango')
    for i in range(1,n+1):
        if i%15 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Buzz')
        elif i%5 == 0:
            print('Fizz')
        else:
            print(i)           
        
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
