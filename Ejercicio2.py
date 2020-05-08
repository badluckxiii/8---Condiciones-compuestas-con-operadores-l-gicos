#  Se ingresan por teclado tres números, si todos los valores ingresados son 
# menores a 10, imprimir en pantalla la leyenda "Todos los números son menores 
# a diez". 
a=int(input('Valor a:'))
b=int(input('Valor b:'))
c=int(input('Valor c:'))
if a<10 and b<10 and c<10:
    print('Todos los numeros son menores de 10')
else:
    print('No todos los numeros son menores de 10')