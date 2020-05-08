# Realizar un programa que pida cargar una fecha cualquiera,
#  luego verificar si dicha fecha corresponde a Navidad.
dia=input('Introduce el dia:')
mes=input('Introduce el mes:')
data=dia+'/'+mes
print(data)
if data=='25/12':
    print('Es dia navidad')
else:
    print('No es dia navidad')