#MÉTODOS_PARA_ANALIZAR_CONEXIONES

def ConexionEntreDosObjetos(object1 , object2):
    nombre1 = object1.getNombre()
    nombre2 = object2.getNombre()

    conexionesCiclovia1 = object1.getMovimientosCiclovia()
    conexionesCiclovia2 = object2.getMovimientosCiclovia()
    conexionesPublico1 = object1.getMovimientosPublico()
    conexionesPublico2 = object2.getMovimientosPublico()
    conexionesCarro1 = object1.getMovimientosCarro()
    conexionesCarro2 = object2.getMovimientosCarro()

    for localidad in conexionesCiclovia1:
        for localidad2 in conexionesCiclovia2:
            if localidad == nombre2:
                if conexionesCiclovia1[localidad] == conexionesCiclovia2[localidad2]:
                    pass
                else:
                    cantidadTraslado = int(input('Cuántas personas se trasladan de {0} a {1} usando ciclovía'.format(nombre1 , nombre2)))
                    object1.movimientosCiclovia[localidad] = cantidadTraslado
                    object2.movimientosCiclovia[localidad2] = cantidadTraslado

    for localidad in conexionesPublico1:
        for localidad2 in conexionesPublico2:
            if localidad == nombre2:
                if conexionesPublico1[localidad] == conexionesPublico2[localidad2]:
                    pass
                else:
                    cantidadTraslado = int(input('Cuántas personas se trasladan de {0} a {1} tomando transporte público'.format(nombre1 , nombre2)))
                    object1.movimientosPublico[localidad] = cantidadTraslado
                    object2.movimientosPublico[localidad2] = cantidadTraslado

    for localidad in conexionesCarro1:
        for localidad2 in conexionesCarro2:
            if localidad == nombre2:
                if conexionesCarro1[localidad] == conexionesCarro2[localidad2]:
                    pass
                else:
                    cantidadTraslado = int(input('Cuántas personas se trasladan de {0} a {1} usando la ruta vehicular'.format(nombre1 , nombre2)))
                    object1.movimientosCarro[localidad] = cantidadTraslado
                    object2.movimientosCarro[localidad2] = cantidadTraslado
    print(object1)
    print(object2)