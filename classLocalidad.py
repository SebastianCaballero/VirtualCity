'''
LA CLASE LOCALIDAD VA A CREAR UNA LOCALIDAD DENTRO DE LA CIUDAD, LA LOCALIDAD VA A TENER HABITANTES, UN ESTRATO (DEL CUAL DEPENDE
EL PRESUPUESTO ASIGNADO A LA LOCALIDAD), EL ESTRATO Y PRESUPUESTO TIENEN LA CAPACIDAD DE INCREMENTAR/MEJORAR LAS RUTAS DE TRANSPORTE
PARA REGULAR EL EMBOTELLAMIENTO, EN ESTA CLASE SE DEFINEN LOS PRINCPIOS DE LA LOCALIDAD, ASÍ COMO SE VA A ENTENDER SU CAPACIDAD PARA
MEJORAR GENERAR UN MECANISMO DE TRANSPORTE ÓPTIMO
'''
class Localidad:
    def __init__(self):
        self.__habitantes = None
        self.__estrato = None
        self.__presupuesto = None
        self.__ciclovia = False
        self.__publico = False
        self.__carro = False

    def setHabitantes(self, habitantes=100):
        self.__habitantes = habitantes
    def getHabitantes(self):
        return self.__habitantes

    def setEstrato(self, estrato=3):
        self.__estrato = estrato
    def getEstrato(self):
        return self.__estrato

    def setPresupuesto(self, presupuesto=400):
        self.__presupuesto = presupuesto
    def getPresupuesto(self):
        return self.__presupuesto

    def setCiclovia(self, ciclovia=False):
        self.__ciclovia = ciclovia
    def getCiclovia(self):
        return self.__ciclovia

    def setPublico(self, publico=False):
        self.__publico = publico
    def getPublico(self):
        return self.__publico

    def setCarro(self, carro=False):
        self.__carro = carro
    def getCarro(self):
        return self.__carro

    def __str__(self):
        infoHabitantes = 'La localidad posee {} habitantes.\n'.format(self.getHabitantes())
        infoEstrato = 'La localidad posee {} habitantes.\n'.format(self.getEstrato())
        infoPresupuesto = 'La localidad posee {} habitantes.\n'.format(self.getPresupuesto())
        infoCiclovia = 'La localidad posee {} habitantes.\n'.format(self.getCiclovia())
        infoPublico = 'La localidad posee {} habitantes.\n'.format(self.getPublico())
        infoCarro = 'La localidad posee {} habitantes.\n'.format(self.getCarro())
        return infoHabitantes + infoEstrato +  infoPresupuesto +  infoCiclovia + infoPublico + infoCarro