import classLocalidad

class Relacion(classLocalidad.Localidad):
    def __init__(self):
        self.nombre = ''

        self.conexionesCiclovia = []  #LISTA DE LOCALIDAD ...
        self.conexionesPublico = []   #CON LAS QUE ESTA ...
        self.conexionesCarro = []     #LOCALIDAD CONECTA.

        self.movimientosCiclovia = {} #DICCIONARIOS CON EL ...
        self.movimientosPublico = {}  #NOMBRE Y PESO DE LAS ...
        self.movimientosCarro = {}    #LOCALIDADES CON QUE CONECTA.

        self.trasladoDeCiclovia = 0  #CANTIDAD DE PERSONAS ...
        self.trasladoDePublico = 0   #QUE SE TRASLADAN A TRAVES ...
        self.trasladoDeCarro = 0     #DE CADA VIA.

        self.trasladoTotal = self.trasladoDeCiclovia + self.trasladoDePublico + self.trasladoDeCarro


    def setNombre(self): #SETEA EL NOMBRE DE LA LOCALIDAD
        nombre = input('Cual es el nombre de la Localidad?: ')
        self.nombre = nombre

    def getNombre(self): #DEVUELVE EL NOMBRE DE LA LOCALIDAD
        return self.nombre



    def setComparacionCiclovia(self): #CREA UNA LISTA DE LAS LOCALIDADES CON LAS QUE SE CONECTA LA LOCALIDAD POR CICLOVIA.
        if self.ciclovia == False:
            print('La localidad no posee ciclovía.')
        else:
            numeroConexionesCiclovia = int(input('Cuántas conexiones de ciclovia posee la localidad?: '))
            numero = 1
            for x in range(numeroConexionesCiclovia):
                localidadConectada = input('Localidad Nº{} qué conecta a {} por Ciclovía?: '.format(numero , self.getNombre()))
                numero += 1
                self.conexionesCiclovia.append(localidadConectada)

    def getConexionesCiclovia(self): #DEVUELVE LA LISTA DE LOCALIDADES CON LAS QUE SE CONECTA POR CICLOVIA
        return self.conexionesCiclovia



    def setComparacionPublico(self): #CREA UNA LISTA DE LAS LOCALIDADES CON LAS QUE SE CONECTA LA LOCALIDAD USANDO TRANSPORTE PUBLICO.
        if self.publico == False:
            print('La localidad no posee sistema de transporte público.')
        else:
            numeroConexionesPublico = int(input('Cuántas conexiones de Transporte Público posee la localidad?: '))
            numero = 1
            for x in range(numeroConexionesPublico):
                localidadConectada = input('Localidad Nº{} qué conecta a {} por Ciclovía?: '.format(numero, self.getNombre()))
                numero += 1
                self.conexionesPublico.append(localidadConectada)

    def getConexionesPublico(self):  #DEVUELVE LA LISTA DE LOCALIDADES CON LAS QUE SE CONECTA MEDIANTE TRANSPORTE PUBLICO
        return self.conexionesPublico



    def setComparacionCarro(self):  #CREA UNA LISTA DE LAS LOCALIDADES CON LAS QUE SE CONECTA LA LOCALIDAD POR RUTA VEHICULAR.
        if self.carro == False:
            print('La localidad no posee ruta vehicular.')
        else:
            numeroConexionesCarro = int(input('Cuántas conexiones por ruta vehicular posee la localidad?: '))
            numero = 1
            for x in range(numeroConexionesCarro):
                localidadConectada = input('Localidad Nº{} qué conecta a {} por ruta vehicular?: '.format(numero, self.getNombre()))
                numero += 1
                self.conexionesCarro.append(localidadConectada)

    def getConexionesCarro(self): #DEVUELVE LA LISTA DE LOCALIDADES CON LAS QUE SE CONECTA POR RUTA VEHICULAR
        return self.conexionesCarro



    def establecerMovimientosCiclovia(self): #Establece un diccionario de la forma {'localidadConLaQueCOnecta':Personas que van}
        if self.ciclovia == False:
            pass
        else:
            print('Va a establecer el peso de {}, o sea la cantidad de habitantes que se mueven por ciclovía.'.format(str(self.getNombre())))
            print('Recuerde que el peso también depende de los habitantes que se trasladen de otra localidad a {}.'.format(self.getNombre()))
            movimientos = int(input('¿Cuántos habitantes se mueven usando bicicleta?: '))
            self.trasladoDeCiclovia = movimientos
            for n in self.conexionesCiclovia:
                habitantesALocalidad = int(input('¿Cuántos habitantes se mueven de {0} a {1}?: '.format(self.getNombre() , n)))
                self.movimientosCiclovia[n] = habitantesALocalidad

    def getMovimientosCiclovia(self): #Retorna el diccionario de las personas que se van a n localidad usando Ciclovía
        return self.movimientosCiclovia



    def establecerMovimientosPublico(self):#Establece un diccionario de la forma {'localidadConLaQueCOnecta':Personas que van}
        if self.publico == False:
            pass
        else:
            print('Va a establecer el peso de {}, o sea la cantidad de habitantes que se mueven usando transporte publico.'.format(str(self.getNombre())))
            print('Recuerde que el peso también depende de los habitantes que se trasladen de otra localidad a {}.'.format(self.getNombre()))
            movimientos = int(input('¿Cuántos habitantes se mueven tomando transporte público?: '))
            self.trasladoDePublico = movimientos
            for n in self.conexionesPublico:
                habitantesALocalidad = int(input('¿Cuántos habitantes se mueven de {0} a {1}?: '.format(self.getNombre() , n)))
                self.movimientosPublico[n] = habitantesALocalidad

    def getMovimientosPublico(self): #Retorna el diccionario de las personas que se van a n localidad usando transporte publico.
        return self.movimientosPublico



    def establecerMovimientosCarro(self):
        if self.carro == False:
            pass
        else:
            print('Va a establecer el peso de {}, o sea la cantidad de habitantes que se mueven usando carro.'.format(str(self.getNombre())))
            print('Recuerde que el peso también depende de los habitantes que se trasladen de otra localidad a {}.'.format(self.getNombre()))
            movimientos = int(input('¿Cuántos habitantes se mueven usando carro?: '))
            self.trasladoDeCarro = movimientos
            for n in self.conexionesCarro:
                habitantesALocalidad = int(input('¿Cuántos habitantes se mueven de {0} a {1}?: '.format(self.getNombre() , n)))
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

        Traslado = self.trasladoTotal
        TrasladosTotales = 'De {} habitantes, se trasladan {} '.format(self.getHabitantes() , str(Traslado))
        INFOBASICA = nombre  + '\n'+ infoHabitantes + infoEstrato +  infoPresupuesto + infoCiclovia + infoPublico + infoCarro
        INFOAVANZADA = infoMovimientosCiclovia + '\n' + infoMovimientosPublico + '\n' + infoMovimientosCarro + '\n' + TrasladosTotales
        return INFOBASICA + INFOAVANZADA