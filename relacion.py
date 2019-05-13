import classLocalidad

class Relacion(classLocalidad.Localidad):
    def __init__(self):
        self.nombre = None
        self.conexionesCiclovia = []
        self.conexionesPublico = []
        self.conexionesCarro = []

        self.movimientosCiclovia = {}
        self.movimientosPublico = {}
        self.movimientosCarro = {}

        self.trasladoDeCiclovia = None
        self.trasladoDePublico = None
        self.trasladoDeCarro = None

    def setNombre(self):
        nombre = input('Cual es el nombre de la Localidad?: ')
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setComparacionCiclovia(self):
        if self.ciclovia == False:
            print('La localidad no posee ciclovía.')
        else:
            numeroConexionesCiclovia = int(input('Cuántas conexiones de ciclovia posee la localidad? '))
            for x in range(numeroConexionesCiclovia):
                localidadConectada = input('Localidad qué conecta por Ciclovía?: ')
                self.conexionesCiclovia.append(localidadConectada)

    def setComparacionPublico(self):
        if self.publico == False:
            print('La localidad no posee sistema de transporte público.')
        else:
            numeroConexionesPublico = int(input('Cuántas conexiones de transporte público posee la localidad? '))
            for x in range(numeroConexionesPublico):
                localidadConectada = input('Localidad qué conecta por Transporte Público?: ')
                self.conexionesPublico.append(localidadConectada)

    def setComparacionCarro(self):
        if self.carro == False:
            print('La localidad no posee ruta vehicular.')
        else:
            numeroConexionesCarro = int(input('Cuántas conexiones de ruta vehicular posee la localidad? '))
            for x in range(numeroConexionesCarro):
                localidadConectada = input('Localidad qué conecta por Ruta Vehicular?: ')
                self.conexionesCarro.append(localidadConectada)

    def getConexionesCiclovia(self):
        return self.conexionesCiclovia
    def getConexionesPublico(self):
        return self.conexionesPublico
    def getConexionesCarro(self):
        return self.conexionesCarro

    def establecerMovimientosCiclovia(self):
        if self.ciclovia == False:
            pass
        else:
            print('Considere que la localidad posee {} habitantes, menos los que ya se han establecido para moverse.'.format(str(self.getHabitantes())))
            movimientos = int(input('De los {0} habitantes de {1}, ¿Cuántos se mueven usando bicicleta?: '.format(str(self.getHabitantes()), self.getNombre())))
            self.trasladoDeCiclovia = movimientos
            for n in self.conexionesCiclovia:
                habitantesALocalidad = int(input('Cuántos habitantes se mueven de {0} a {1}'.format(self.getNombre() , n)))
                self.movimientosCiclovia[n] = habitantesALocalidad
    def getMovimientosCiclovia(self):
        return self.movimientosCiclovia

    def establecerMovimientosPublico(self):
        if self.publico == False:
            pass
        else:
            print('Considere que la localidad posee {} habitantes, menos los que ya se han establecido para moverse.'.format(str(self.getHabitantes())))
            movimientos = int(input('De los {0} habitantes de {1}, ¿Cuántos se mueven usando Transporte Público?: '.format(str(self.getHabitantes()), self.getNombre())))
            self.trasladoDePublico = movimientos
            for n in self.conexionesPublico:
                habitantesALocalidad = int(input('Cuántos habitantes se mueven de {0} a {1}'.format(self.getNombre() , n)))
                self.movimientosPublico[n] = habitantesALocalidad
    def getMovimientosPublico(self):
        return self.movimientosPublico

    def establecerMovimientosCarro(self):
        if self.carro == False:
            pass
        else:
            print('Considere que la localidad posee {} habitantes, menos los que ya se han establecido para moverse.'.format(str(self.getHabitantes())))
            movimientos = int(input('De los {0} habitantes de {1}, ¿Cuántos se mueven en carro?: '.format(str(self.getHabitantes()), self.getNombre())))
            self.trasladoDeCarro = movimientos
            for n in self.conexionesCarro:
                habitantesALocalidad = int(input('Cuántos habitantes se mueven de {0} a {1}'.format(self.getNombre() , n)))
                self.movimientosCarro[n] = habitantesALocalidad
    def getMovimientosCarro(self):
        return self.movimientosCarro

    def __str__(self):

        if self.getCiclovia() == True:
            Ciclovia = 'si'
        else:
            Ciclovia = 'no'
        if self.getPublico() == True:
            TransportePublico = 'si'
        else:
            TransportePublico = 'no'
        if self.getCarro() == True:
            RutaVehicular = 'si'
        else:
            RutaVehicular = 'no'

        nombre = 'El nombre de la localidad es: {}.'.format(self.getNombre())

        infoHabitantes = 'La localidad posee {} habitantes.\n'.format(self.getHabitantes())
        infoEstrato = 'La localidad es de estrato {}.\n'.format(self.getEstrato())
        infoPresupuesto = 'La localidad posee un presupuesto de {} cucupesos.\n'.format(self.getPresupuesto())
        infoCiclovia = 'La localidad {} posee ciclovia.\n'.format(Ciclovia)
        infoPublico = 'La localidad {} posee trasnporte publico.\n'.format(TransportePublico)
        infoCarro = 'La localidad {} posee ruta vehicular.\n'.format(RutaVehicular)

        movsCiclovia = str(self.getMovimientosCiclovia())
        movsPublico = str(self.getMovimientosPublico())
        movsCarro = str(self.getMovimientosCarro())
        if movsCiclovia == '{}':
            infoMovimientosCiclovia = 'La localidad no se conectaa por ciclovía.'
        else:
            infoMovimientosCiclovia = 'La localidad se conecta por ciclovía con {}'.format(movsCiclovia)
        if movsPublico == '{}':
            infoMovimientosPublico = 'La localidad no se conecta usando transporte público'
        else:
            infoMovimientosPublico = 'La localidad se conecta a través de Transporte público con {}'.format(movsPublico)
        if movsCarro == {}:
            infoMovimientosCarro = 'La localidad no se conecta mediante ruta vehicular.'
        else:
            infoMovimientosCarro = 'La localidad se conecta con ruta vehicular con {}'.format(movsCarro)
        trasladoCiclovia = self.trasladoDeCiclovia
        if self.trasladoDeCiclovia == None:
            trasladoCiclovia = 0
        trasladoPublico = self.trasladoDePublico
        if self.trasladoDePublico == None:
            trasladoPublico = 0
        trasladoCarro = self.trasladoDeCarro
        if self.trasladoDeCiclovia == None:
            trasladoCarro = 0
        Traslado = trasladoCiclovia + trasladoPublico + trasladoCarro
        TrasladosTotales = 'De {} habitantes, se trasladan {} '.format(self.getHabitantes() , str(Traslado))
        INFOBASICA = nombre  + '\n'+ infoHabitantes + infoEstrato +  infoPresupuesto + infoCiclovia + infoPublico + infoCarro
        INFOAVANZADA = infoMovimientosCiclovia + '\n' + infoMovimientosPublico + '\n' + infoMovimientosCarro + '\n' + TrasladosTotales
        return INFOBASICA + INFOAVANZADA