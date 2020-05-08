# Escribir un programa que pida ingresar la coordenada de un punto en el plano
# , es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
#  (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.) 
a=int(input('Valor a:'))
b=int(input('Valor b:'))
if a>0 and b>0:
    print('Se encuentra en el primer cuadrante')
elif a<0 and b<0:
    print('Se encuentra en el segundo cuadrante')
else:
    print('Se encuentra en el tercer cuadrante')
