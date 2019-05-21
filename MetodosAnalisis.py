#MÉTODOS_PARA_ANALIZAR_CONEXIONES

def ConexionEntreDosObjetosCiclovia(object1 , object2): #RETORNA EL PESO ENTRE OBJETO 1 Y 2 EN CICLOVIA
    nombre1 = object1.getNombre()
    nombre2 = object2.getNombre()

    conexionesCiclovia1 = object1.getMovimientosCiclovia()
    conexionesCiclovia2 = object2.getMovimientosCiclovia()

    for localidad in conexionesCiclovia1:
        for localidad2 in conexionesCiclovia2:
            if localidad == nombre2:
                    return object1.movimientosCiclovia[localidad] + object2.movimientosCiclovia[nombre1]
            else:
                pass


def ConexionEntreDosObjetosPublico(object1, object2): #RETORNA EL PESO ENTRE OBJETO 1 Y 2 EN TRANSPORTE PUBLICO
    nombre1 = object1.getNombre()
    nombre2 = object2.getNombre()

    conexionesPublico1 = object1.getMovimientosPublico()
    conexionesPublico2 = object2.getMovimientosPublico()

    for localidad in conexionesPublico1:
        for localidad2 in conexionesPublico2:
            if localidad == nombre2:
                return object1.movimientosPublico[localidad] + object2.movimientosPublico[nombre1]
            else:
                pass


def ConexionEntreDosObjetosCarro(object1, object2): #RETORNA EL PESO ENTRE OBJETO 1 Y 2 EN RUTA VEHICULAR
    nombre1 = object1.getNombre()
    nombre2 = object2.getNombre()

    conexionesCarro1 = object1.getMovimientosCarro()
    conexionesCarro2 = object2.getMovimientosCarro()

    for localidad in conexionesCarro1:
        for localidad2 in conexionesCarro2:
            if localidad == nombre2:
                return object1.movimientosCarro[localidad] + object2.movimientosCarro[nombre1]
            else:
                pass

