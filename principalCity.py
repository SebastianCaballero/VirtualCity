import relacion
#import MetodosAnalisis
import AlgoritmoEvaluacionGeneral

#################################################  INICIO DE CLASES EJEMPLO 1 Y 2 ###############################


###CLASES DE PRUEBA PARA LOS PRIMEROS DOS EJEMPLOS
'''
c = relacion.Relacion()
c.setNombre()
c.setHabitantes(480)
c.setEstrato(5)
c.setPresupuesto(4700)
c.setCiclovia(True)
c.setPublico(True)
c.setCarro(True)

c.setComparacionCiclovia()
c.setComparacionPublico()
c.setComparacionCarro()

c.establecerMovimientosCiclovia()
c.establecerMovimientosPublico()
c.establecerMovimientosCarro()

print('\n')

v = relacion.Relacion()
v.setNombre()
v.setHabitantes(480)
v.setEstrato(5)
v.setPresupuesto(4700)
v.setCiclovia(True)
v.setPublico(True)
v.setCarro(True)

v.setComparacionCiclovia()
v.setComparacionPublico()
v.setComparacionCarro()

v.establecerMovimientosCiclovia()
v.establecerMovimientosPublico()
v.establecerMovimientosCarro()

print('\n')

j = relacion.Relacion()
j.setNombre()
j.setHabitantes(390)
j.setEstrato(2)
j.setPresupuesto(750)
j.setCiclovia(True)
j.setPublico(True)
j.setCarro(True)

j.setComparacionCiclovia()
j.setComparacionPublico()
j.setComparacionCarro()

j.establecerMovimientosCiclovia()
j.establecerMovimientosPublico()
j.establecerMovimientosCarro()


print('\n')
'''

######################################## EJEMPLO 1 ######################################

#EJEMPLO 1: FUNCIONA PARA DOS NODOS CONECTADOS EN TODAS LAS RUTAS
'''
listaDeLocalidades = [j, v]

print('El presupuesto de la ciudad es: ' + str(AlgoritmoEvaluacionGeneral.PresupuestoGeneral(listaDeLocalidades)))

print('\n')

Relaciones = [[j,v]]

saturacionCiclovia = int(input('Cuánto es el máximo peso que puede tener una viá de ciclovía?: '))
costoCiclovia = int(input('Cuánto cuesta una vía de ciclovía?: '))

saturacionPublico = int(input('Cuánto es el máximo peso que puede tener un carril de transporte público?: '))
costoPublico = int(input('Cuánto cuesta un carril de transporte público?: '))

saturacionCarro = int(input('Cuánto es el máximo peso que puede tener una vía de ruta vehicular?: '))
costoCarro = int(input('Cuánto cuesta una vía de ruta vehicular?: '))
print('\n')

AlgoritmoEvaluacionGeneral.EvaluacionCiclovia(Relaciones, saturacionCiclovia, costoCiclovia, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionPublico(Relaciones, saturacionPublico, costoPublico, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionCarro(Relaciones, saturacionCarro, costoCarro, listaDeLocalidades)
'''


############################################### EJEMPLO 2#######################################################3



#EJEMPLO2: FUNICONA PARA GRAFO DE 3 LOCALIDADES CONECTADOS POR LAS TRES RUTAS
'''
listaDeLocalidades = [j, v,c]

print('El presupuesto de la ciudad es: ' + str(AlgoritmoEvaluacionGeneral.PresupuestoGeneral(listaDeLocalidades)))

print('\n')

Relaciones = [[j,v], [j,c], [v,c]]

saturacionCiclovia = int(input('Cuánto es el máximo peso que puede tener una viá de ciclovía?: '))
costoCiclovia = int(input('Cuánto cuesta una vía de ciclovía?: '))

saturacionPublico = int(input('Cuánto es el máximo peso que puede tener un carril de transporte público?: '))
costoPublico = int(input('Cuánto cuesta un carril de transporte público?: '))

saturacionCarro = int(input('Cuánto es el máximo peso que puede tener una vía de ruta vehicular?: '))
costoCarro = int(input('Cuánto cuesta una vía de ruta vehicular?: '))
print('\n')

AlgoritmoEvaluacionGeneral.EvaluacionCiclovia(Relaciones, saturacionCiclovia, costoCiclovia, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionPublico(Relaciones, saturacionPublico, costoPublico, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionCarro(Relaciones, saturacionCarro, costoCarro, listaDeLocalidades)
'''

###########################################################################################
####################### CLASES EJEMPLO 3 ##############################################
'''
j = relacion.Relacion()
j.setNombre()
j.setHabitantes(390)
j.setEstrato(2)
j.setPresupuesto(750)
j.setCiclovia(True)
j.setPublico(True)
j.setCarro(True)

j.setComparacionCiclovia()
j.setComparacionPublico()
j.setComparacionCarro()

j.establecerMovimientosCiclovia()
j.establecerMovimientosPublico()
j.establecerMovimientosCarro()

print('\n')

v = relacion.Relacion()
v.setNombre()
v.setHabitantes(480)
v.setEstrato(5)
v.setPresupuesto(4700)
v.setCiclovia(False)
v.setPublico(True)
v.setCarro(True)

v.setComparacionCiclovia()
v.setComparacionPublico()
v.setComparacionCarro()

v.establecerMovimientosCiclovia()
v.establecerMovimientosPublico()
v.establecerMovimientosCarro()

print('\n')

c = relacion.Relacion()
c.setNombre()
c.setHabitantes(480)
c.setEstrato(5)
c.setPresupuesto(4700)
c.setCiclovia(True)
c.setPublico(False)
c.setCarro(True)

c.setComparacionCiclovia()
c.setComparacionPublico()
c.setComparacionCarro()

c.establecerMovimientosCiclovia()
c.establecerMovimientosPublico()
c.establecerMovimientosCarro()

print('\n')
'''

##################################### EJEMPLO 3 #################################
'''
listaDeLocalidades = [j, v,c]

print('El presupuesto de la ciudad es: ' + str(AlgoritmoEvaluacionGeneral.PresupuestoGeneral(listaDeLocalidades)))

print('\n')

Relaciones = [[j,v], [j,c], [v,c]]

saturacionCiclovia = int(input('Cuánto es el máximo peso que puede tener una viá de ciclovía?: '))
costoCiclovia = int(input('Cuánto cuesta una vía de ciclovía?: '))

saturacionPublico = int(input('Cuánto es el máximo peso que puede tener un carril de transporte público?: '))
costoPublico = int(input('Cuánto cuesta un carril de transporte público?: '))

saturacionCarro = int(input('Cuánto es el máximo peso que puede tener una vía de ruta vehicular?: '))
costoCarro = int(input('Cuánto cuesta una vía de ruta vehicular?: '))
print('\n')

AlgoritmoEvaluacionGeneral.EvaluacionCiclovia(Relaciones, saturacionCiclovia, costoCiclovia, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionPublico(Relaciones, saturacionPublico, costoPublico, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionCarro(Relaciones, saturacionCarro, costoCarro, listaDeLocalidades)
'''


###########################################################################################
####################### CLASES EJEMPLO 4 ##################################################
'''
j = relacion.Relacion()
j.setNombre()
j.setHabitantes(390)
j.setEstrato(2)
j.setPresupuesto(750)
j.setCiclovia(True)
j.setPublico(True)
j.setCarro(True)

j.setComparacionCiclovia()
j.setComparacionPublico()
j.setComparacionCarro()

j.establecerMovimientosCiclovia()
j.establecerMovimientosPublico()
j.establecerMovimientosCarro()

print('\n')

v = relacion.Relacion()
v.setNombre()
v.setHabitantes(480)
v.setEstrato(5)
v.setPresupuesto(4700)
v.setCiclovia(True)
v.setPublico(True)
v.setCarro(True)

v.setComparacionCiclovia()
v.setComparacionPublico()
v.setComparacionCarro()

v.establecerMovimientosCiclovia()
v.establecerMovimientosPublico()
v.establecerMovimientosCarro()

print('\n')

c = relacion.Relacion()
c.setNombre()
c.setHabitantes(480)
c.setEstrato(5)
c.setPresupuesto(4700)
c.setCiclovia(False)
c.setPublico(True)
c.setCarro(True)

c.setComparacionCiclovia()
c.setComparacionPublico()
c.setComparacionCarro()

c.establecerMovimientosCiclovia()
c.establecerMovimientosPublico()
c.establecerMovimientosCarro()

print('\n')

m = relacion.Relacion()
m.setNombre()
m.setHabitantes(480)
m.setEstrato(5)
m.setPresupuesto(4700)
m.setCiclovia(True)
m.setPublico(False)
m.setCarro(True)

m.setComparacionCiclovia()
m.setComparacionPublico()
m.setComparacionCarro()

m.establecerMovimientosCiclovia()
m.establecerMovimientosPublico()
m.establecerMovimientosCarro()

print('\n')
'''
################################## EJEMPLO 4 #######################################
'''
listaDeLocalidades = [j, v, c, m]

print('El presupuesto de la ciudad es: ' + str(AlgoritmoEvaluacionGeneral.PresupuestoGeneral(listaDeLocalidades)))

print('\n')

Relaciones = [[j,v], [j,c], [v,c], [j,m], [c,m], [v,m]]

saturacionCiclovia = int(input('Cuánto es el máximo peso que puede tener una viá de ciclovía?: '))
costoCiclovia = int(input('Cuánto cuesta una vía de ciclovía?: '))

saturacionPublico = int(input('Cuánto es el máximo peso que puede tener un carril de transporte público?: '))
costoPublico = int(input('Cuánto cuesta un carril de transporte público?: '))

saturacionCarro = int(input('Cuánto es el máximo peso que puede tener una vía de ruta vehicular?: '))
costoCarro = int(input('Cuánto cuesta una vía de ruta vehicular?: '))
print('\n')

AlgoritmoEvaluacionGeneral.EvaluacionCiclovia(Relaciones, saturacionCiclovia, costoCiclovia, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionPublico(Relaciones, saturacionPublico, costoPublico, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionCarro(Relaciones, saturacionCarro, costoCarro, listaDeLocalidades)
'''

############################ EJEMPLO PRESENTACIÓN ##########################
'''
## SE GENERAN 8 INSTANCIAS PARA QUE SEAN 8 LOCALIDADES ##

j = relacion.Relacion()
j.setNombre()
j.setHabitantes(390)
j.setEstrato(2)
j.setPresupuesto(750)
j.setCiclovia(True)
j.setPublico(True)
j.setCarro(True)

j.setComparacionCiclovia()
j.setComparacionPublico()
j.setComparacionCarro()

j.establecerMovimientosCiclovia()
j.establecerMovimientosPublico()
j.establecerMovimientosCarro()

print('\n')

v = relacion.Relacion()
v.setNombre()
v.setHabitantes(480)
v.setEstrato(5)
v.setPresupuesto(4700)
v.setCiclovia(True)
v.setPublico(True)
v.setCarro(True)

v.setComparacionCiclovia()
v.setComparacionPublico()
v.setComparacionCarro()

v.establecerMovimientosCiclovia()
v.establecerMovimientosPublico()
v.establecerMovimientosCarro()

print('\n')

c = relacion.Relacion()
c.setNombre()
c.setHabitantes(480)
c.setEstrato(5)
c.setPresupuesto(4700)
c.setCiclovia(False)
c.setPublico(True)
c.setCarro(True)

c.setComparacionCiclovia()
c.setComparacionPublico()
c.setComparacionCarro()

c.establecerMovimientosCiclovia()
c.establecerMovimientosPublico()
c.establecerMovimientosCarro()

print('\n')

m = relacion.Relacion()
m.setNombre()
m.setHabitantes(480)
m.setEstrato(5)
m.setPresupuesto(4700)
m.setCiclovia(True)
m.setPublico(True)
m.setCarro(True)

m.setComparacionCiclovia()
m.setComparacionPublico()
m.setComparacionCarro()

m.establecerMovimientosCiclovia()
m.establecerMovimientosPublico()
m.establecerMovimientosCarro()

print('\n')

n = relacion.Relacion()
n.setNombre()
n.setHabitantes(480)
n.setEstrato(5)
n.setPresupuesto(4700)
n.setCiclovia(False)
n.setPublico(True)
n.setCarro(True)

n.setComparacionCiclovia()
n.setComparacionPublico()
n.setComparacionCarro()

n.establecerMovimientosCiclovia()
n.establecerMovimientosPublico()
n.establecerMovimientosCarro()

print('\n')

k = relacion.Relacion()

k.setNombre()
k.setHabitantes(480)
k.setEstrato(5)
k.setPresupuesto(4700)
k.setCiclovia(True)
k.setPublico(True)
k.setCarro(True)

k.setComparacionCiclovia()
k.setComparacionPublico()
k.setComparacionCarro()

k.establecerMovimientosCiclovia()
k.establecerMovimientosPublico()
k.establecerMovimientosCarro()

print('\n')

z = relacion.Relacion()
z.setNombre()
z.setHabitantes(480)
z.setEstrato(5)
z.setPresupuesto(4700)
z.setCiclovia(False)
z.setPublico(True)
z.setCarro(False)

z.setComparacionCiclovia()
z.setComparacionPublico()
z.setComparacionCarro()

z.establecerMovimientosCiclovia()
z.establecerMovimientosPublico()
z.establecerMovimientosCarro()

print('\n')

w = relacion.Relacion()
w.setNombre()
w.setHabitantes(480)
w.setEstrato(5)
w.setPresupuesto(4700)
w.setCiclovia(True)
w.setPublico(False)
w.setCarro(False)

w.setComparacionCiclovia()
w.setComparacionPublico()
w.setComparacionCarro()

w.establecerMovimientosCiclovia()
w.establecerMovimientosPublico()
w.establecerMovimientosCarro()

print('\n')
'''
### INICIO DEL ALGORIMTO ###
'''

listaDeLocalidades = [j, v, c, m, n, k, z, w]

print('El presupuesto de la ciudad es: ' + str(AlgoritmoEvaluacionGeneral.PresupuestoGeneral(listaDeLocalidades)))

print('\n')

Relaciones = [[j,w] , [j,m] , [j,v] , [w,m] , [m,v] , [m,k] , [v,k] , [v,c] , [v,n] , [k,n] , [c,n] , [c,z] , [z,n]]

saturacionCiclovia = int(input('Cuánto es el máximo peso que puede tener una viá de ciclovía?: '))
costoCiclovia = int(input('Cuánto cuesta una vía de ciclovía?: '))

saturacionPublico = int(input('Cuánto es el máximo peso que puede tener un carril de transporte público?: '))
costoPublico = int(input('Cuánto cuesta un carril de transporte público?: '))

saturacionCarro = int(input('Cuánto es el máximo peso que puede tener una vía de ruta vehicular?: '))
costoCarro = int(input('Cuánto cuesta una vía de ruta vehicular?: '))
print('\n')

AlgoritmoEvaluacionGeneral.EvaluacionCiclovia(Relaciones, saturacionCiclovia, costoCiclovia, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionPublico(Relaciones, saturacionPublico, costoPublico, listaDeLocalidades)
print('\n')
AlgoritmoEvaluacionGeneral.EvaluacionCarro(Relaciones, saturacionCarro, costoCarro, listaDeLocalidades)
'''