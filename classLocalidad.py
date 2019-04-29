'''
LA CLASE LOCALIDAD VA A CREAR UNA LOCALIDAD DENTRO DE LA CIUDAD, LA LOCALIDAD VA A TENER HABITANTES, UN ESTRATO (DEL CUAL DEPENDE
EL PRESUPUESTO ASIGNADO A LA LOCALIDAD), EL ESTRATO Y PRESUPUESTO TIENEN LA CAPACIDAD DE INCREMENTAR/MEJORAR LAS RUTAS DE TRANSPORTE
PARA REGULAR EL EMBOTELLAMIENTO, EN ESTA CLASE SE DEFINEN LOS PRINCPIOS DE LA LOCALIDAD, ASÍ COMO SE VA A ENTENDER SU CAPACIDAD PARA
MEJORAR GENERAR UN MECANISMO DE TRANSPORTE ÓPTIMO
'''
class Localidad:

    def __init__(self):
        self.__habitantes = 120
        self.__estrato = 3
        self.__presupuesto = 1200
        self.__ciclovia = False
        self.__publico = False
        self.__carro = False

    def setHabitantes(self, habitantes=120):
        if 35 < habitantes < 500:
            self.__habitantes = habitantes
        else:
            self.__habitantes = 120
    def getHabitantes(self):
        return self.__habitantes

    def setEstrato(self, estrato=3):
        if 1 <= estrato <= 5:
            self.__estrato = estrato
        else:
            self.__estrato = 3
    def getEstrato(self):
        return self.__estrato

    def setPresupuesto(self, presupuesto=1200):
        estrato = self.getEstrato()
        presupuestoEstrato1 = 300
        presupuestoEstrato2 = 600
        presupuestoEstrato3 = 1200
        presupuestoEstrato4 = 2400
        presupuestoEstrato5 = 4800
        if estrato == 1:
            if presupuestoEstrato1-(presupuestoEstrato1/2) < presupuesto <= presupuestoEstrato1+(presupuestoEstrato1/2):
                self.__presupuesto = presupuesto
            else:
                self.__presupuesto = presupuestoEstrato1
        elif estrato == 2:
            if presupuestoEstrato2-(presupuestoEstrato2/2) < presupuesto <= presupuestoEstrato2+(presupuestoEstrato2/2):
                self.__presupuesto = presupuesto
            else:
                self.__presupuesto = presupuestoEstrato2
        elif estrato == 3:
            if presupuestoEstrato3-(presupuestoEstrato3/2) < presupuesto <= presupuestoEstrato3+(presupuestoEstrato3/2):
                self.__presupuesto = presupuesto
            else:
                self.__presupuesto = presupuestoEstrato3
        elif estrato == 4:
            if presupuestoEstrato4-(presupuestoEstrato4/2) < presupuesto <= presupuestoEstrato4+(presupuestoEstrato4/2):
                self.__presupuesto = presupuesto
            else:
                self.__presupuesto = presupuestoEstrato4
        elif estrato == 5:
            if presupuestoEstrato5-(presupuestoEstrato5/2) < presupuesto <= presupuestoEstrato5+(presupuestoEstrato5/2):
                self.__presupuesto = presupuesto
            else:
                self.__presupuesto = presupuestoEstrato5
    def getPresupuesto(self):
        return self.__presupuesto

    def setCiclovia(self, ciclovia=False):
        if ciclovia == True or ciclovia == False:
            self.__ciclovia = ciclovia
        else:
            self.__ciclovia = False
    def getCiclovia(self):
        return self.__ciclovia

    def setPublico(self, publico=False):
        if publico == True or publico == False:
            self.__publico = publico
        else:
            self.__publico = False
    def getPublico(self):
        return self.__publico

    def setCarro(self, carro=False):
        if carro == True or carro == False:
            self.__carro = carro
        else:
            self.__carro = False
    def getCarro(self):
        return self.__carro

    def __str__(self):
        Ciclovia = None
        TransportePublico = None
        RutaVehicular = None
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

        infoHabitantes = 'La localidad posee {} habitantes.\n'.format(self.getHabitantes())
        infoEstrato = 'La localidad tiene estrato {}.\n'.format(self.getEstrato())
        infoPresupuesto = 'La localidad posee un presupuesto de {} cucupesos.\n'.format(self.getPresupuesto())
        infoCiclovia = 'La localidad {} posee ciclovia.\n'.format(Ciclovia)
        infoPublico = 'La localidad {} posee trasnporte publico.\n'.format(TransportePublico)
        infoCarro = 'La localidad {} posee ruta vehicular.\n'.format(RutaVehicular)

        return infoHabitantes + infoEstrato +  infoPresupuesto + infoCiclovia + infoPublico + infoCarro
