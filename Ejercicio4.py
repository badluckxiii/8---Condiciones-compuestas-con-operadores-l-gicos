#  Se ingresan tres valores por teclado, si todos son iguales se imprime la
#  suma del primero con el segundo y a este resultado se lo multiplica 
# por el tercero. 
a=int(input('Valor a:'))
b=int(input('Valor b:'))
c=int(input('Valor c:'))
if a==b and b==c:
    print(a+b)
    print((a+b)*c)
else:
    print('No son iguales')