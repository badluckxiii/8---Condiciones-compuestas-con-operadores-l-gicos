#Se ingresan por teclado tres números, si al menos uno de los valores ingresados 
# es menor a 10, imprimir en pantalla la leyenda "Alguno de los números es menor 
# a diez". 
a=int(input('Valor a:'))
b=int(input('Valor b:'))
c=int(input('Valor c:'))
if a<10 or b<10 or c<10:
    print('Algunos de tus numeros es menor a 10')
else:
    print('No hay ningun numero menor a 10')