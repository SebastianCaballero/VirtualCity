import relacion
import MetodosAnalisis

'''EL ALGORITMO A CONTINUACIÓN VA A EVALUAR UNA LISTA DE OBJETOS DONDE VA A COMPARAR, SUMAR Y 
OBTENER TODOS LOS PESOS DE LAS RUTAS ENTRE LOCALIDADES PARA LAS DIFERENTES POSIBILIDADES DE MOVILIDAD, 
LO PRINCIPAL DEL ALGORITMO ES RETORNAR TODOS LOS VALORES IMPORTENTES PARA DAR UNA SOLUCIÓN'''

def PresupuestoGeneral(listaDeLocalidades):
    presupuesto = 0
    contador = 0
    for localidad in listaDeLocalidades:
        presupuesto += listaDeLocalidades[contador].presupuesto
        contador += 1
    return presupuesto

def EvaluacionCiclovia(listaRelacion, saturacionCiclovia, costeDeCiclovia, listaDeLocalidades):
    presupuesto = PresupuestoGeneral(listaDeLocalidades)

    for localidad1 in listaRelacion:
        nombre1 = localidad1[0].nombre
        nombre2 = localidad1[1].nombre
        if localidad1[0].ciclovia == False:
            print('Las localidades {} y {} no se conectan por ciclovía'.format(nombre1,nombre2))
        else:
            Peso = MetodosAnalisis.ConexionEntreDosObjetosCiclovia(localidad1[0], localidad1[1])
            if Peso == None:
                pass
            elif Peso == 0:
                print('No exixte peso en ciclovia debido a que {} y {} no se conectan mediante ciclovia'.format(nombre1, nombre2))
            else:
                cad1= 'El peso entre ' + nombre1 + ' y '  + nombre2 + ' en ciclovia es: '
                print(cad1 + str(Peso))
                if int(Peso) < saturacionCiclovia:
                    print('En el caso de la conexión entre {} y {} en ciclovia no hay embotellamiento.'.format(nombre1, nombre2))

                elif Peso == saturacionCiclovia:
                    print('La conexión entre {} y {} por ciclovia no tiene embotellamiento pero está muy cerca.'.format(nombre1, nombre2))

                else:
                    print('La conexión entre {} y {} por ciclovia tiene embotellamiento.'.format(nombre1, nombre2))
                    sobre = Peso - saturacionCiclovia
                    # POR CADA NUEVA RUTA DE CICLOVIA, CABEN 5 CIUDADANOS
                    cantidadDeVias = int(sobre / 5) + 1
                    precioDeVias = (cantidadDeVias * costeDeCiclovia)
                    print('Es necesario que se compren ' + str(cantidadDeVias) + ' vías. Esto le costaría al presupuesto de la ciudad ' + str(precioDeVias) + 'cucupesos.')
                    print('Embotellamiento de {} a {} por ciclovia solucionado.'.format(nombre1, nombre2))
                    presupuesto -= precioDeVias
                    print('Quedan {} cucupesos de presupuesto.'.format(presupuesto))
    print('\n')


def EvaluacionPublico(listaRelacion, saturacionPublico, costeCarrilPublico, listaDeLocalidades):
    presupuesto = PresupuestoGeneral(listaDeLocalidades)

    for localidad1 in listaRelacion:
        nombre1 = localidad1[0].nombre
        nombre2 = localidad1[1].nombre
        if localidad1[0].publico == False:
            print('Las localidades {} y {} no se conectan por transporte publico'.format(nombre1,nombre2))
        else:
            Peso = MetodosAnalisis.ConexionEntreDosObjetosPublico(localidad1[0], localidad1[1])
            if Peso == None:
                pass
            elif Peso == 0:
                print('No exixte peso en transporte público debido a que {} y {} no se conectan mediante transporte publico'.format(nombre1, nombre2))
            else:
                cad1 = 'El peso entre ' + nombre1 + ' y ' + nombre2 + ' en transporte publico es: '
                print(cad1 + str(Peso))
                if Peso < saturacionPublico:
                    print('En el caso de la conexión entre {} y {} en transporte público no hay embotellamiento.'.format(nombre1, nombre2))

                elif int(Peso) == saturacionPublico:
                    print('La conexión entre {} y {} mediante transporte publico no tiene embotellamiento pero está muy cerca.'.format(nombre1, nombre2))
                else:
                    print('La conexión entre {} y {} mediante Transporte público tiene embotellamiento.'.format(nombre1, nombre2))
                    sobre = Peso - saturacionPublico
                    # POR CADA NUEVA VÍA DE TRANSPORTE PUBLICO, CABEN 25 CIUDADANOS
                    cantidadDeVias = int(sobre / 25) + 1
                    precioDeVias = cantidadDeVias * costeCarrilPublico
                    print('Es necesario que se compren ' + str(cantidadDeVias) + ' vías. Esto le costaría al presupuesto de la ciudad ' + str(precioDeVias) + ' cucupesos.')
                    print('Embotellamiento de {} a {} de transporte público solucionado.'.format(nombre1, nombre2))
                    presupuesto -= precioDeVias
                    print('Quedan {} cucupesos de presupuesto.'.format(presupuesto))
    print('\n')


def EvaluacionCarro(listaRelacion, saturacionCarro, costeViaVehicular, listaDeLocalidades):
    presupuesto = PresupuestoGeneral(listaDeLocalidades)

    for localidad1 in listaRelacion:
        nombre1 = localidad1[0].nombre
        nombre2 = localidad1[1].nombre
        if localidad1[0].publico == False:
            print('Las localidades {} y {} no se conectan por ciclovía'.format(nombre1, nombre2))
        else:
            Peso = MetodosAnalisis.ConexionEntreDosObjetosCarro(localidad1[0], localidad1[1])
            if Peso == None:
                pass
            elif Peso == 0:
                print('No exixte peso en ruta vehicular debido a que {} y {} no se conectan mediante ruta vehicular'.format(nombre1, nombre2))
            else:
                cad1 = 'El peso entre ' + nombre1 + ' y ' + nombre2 + ' en ruta vehicular es: '
                print(cad1 + str(Peso))
                if int(Peso) < saturacionCarro:
                    print('En el caso de la conexión entre {} y {} en ruta vehicular no hay embotellamiento.'.format(nombre1, nombre2))

                elif Peso == saturacionCarro:
                    print('La conexión entre {} y {} por ruta vehicular no tiene embotellamiento pero está muy cerca.'.format(nombre1, nombre2))
                else:
                    print('La conexión entre {} y {} por ruta vehicular tiene embotellamiento.'.format(nombre1, nombre2))
                    sobre = Peso - saturacionCarro
                    # POR CADA NUEVA VÍA DE TRANSPORTE PUBLICO, CABEN 8 AUTOS ELÉCTRICOS DE 1 PERSONA
                    cantidadDeVias = int(sobre / 8) + 1
                    precioDeVias = cantidadDeVias * costeViaVehicular
                    print('Es necesario que se compren ' + str(cantidadDeVias) + ' vías. Esto le costaría al presupuesto de la ciudad ' + str(precioDeVias) + ' cucupesos.')
                    print('Embotellamiento de {} a {} de transporte público solucionado.'.format(nombre1, nombre2))
                    presupuesto -= precioDeVias
                    print('Quedan {} cucupesos de presupuesto.'.format(presupuesto))
    print('\n')



