'''
LA CLASE LOCALIDAD VA A CREAR UNA LOCALIDAD DENTRO DE LA CIUDAD, LA LOCALIDAD VA A TENER HABITANTES, UN ESTRATO (DEL CUAL DEPENDE
EL PRESUPUESTO ASIGNADO A LA LOCALIDAD), EL ESTRATO Y PRESUPUESTO TIENEN LA CAPACIDAD DE INCREMENTAR/MEJORAR LAS RUTAS DE TRANSPORTE
PARA REGULAR EL EMBOTELLAMIENTO, EN ESTA CLASE SE DEFINEN LOS PRINCPIOS DE LA LOCALIDAD, ASÍ COMO SE VA A ENTENDER SU CAPACIDAD PARA
MEJORAR GENERAR UN MECANISMO DE TRANSPORTE ÓPTIMO
'''
class Localidad:

    def __init__(self):
        self.habitantes = 120       #CANTIDAD DE HABITANTES DE LA LOCALIDAD
        self.estrato = 3            #ESTRATO DE LA LOCALIDAD
        self.presupuesto = 1200     #PRESUPUESTO DE LA LOCALIDAD
        self.ciclovia = False       #BOOLEANO QUE DEFINE SI LA LOCALIDAD POSEE CICLOVIA O NO
        self.publico = False        #BOOLEANO QUE DEFINE SI LA LOCALIDAD POSEE TRANSPORTE PUBLICO O NO
        self.carro = False          #BOOLEANO QUE DEFINE SI LA LOCALIDAD POSEE RUTA VEHICULAR O NO

    def setHabitantes(self, habitantes=120):  #SETEA LOS HABITANTES. SI NO CUMPLEN LO DEJA EN 120
        if 35 < habitantes < 500:
            self.habitantes = int(habitantes)
        else:
            self.habitantes = 120

    def getHabitantes(self): #RETORNA LOS HABITANTES
        return self.habitantes



    def setEstrato(self, estrato=3): #SETEA EL ESTRATO DE 1 A 5. SI NO CUMPLE LO VALE A 3
        if 1 <= estrato <= 5:
            self.estrato = estrato
        else:
            self.estrato = 3

    def getEstrato(self): #RETORNA EL ESTRATO
        return self.estrato



    def setPresupuesto(self, presupuesto=1200):  #SETEA EL PRESUPUESTO DEPENDIENDO DEL ESTRATO, SI NO ES VALIDO VA
        estrato = self.getEstrato()              #A SER EVALUADO EN 1200
        presupuestoEstrato1 = 300
        presupuestoEstrato2 = 600
        presupuestoEstrato3 = 1200
        presupuestoEstrato4 = 2400
        presupuestoEstrato5 = 4800
        if estrato == 1:
            if presupuestoEstrato1-(presupuestoEstrato1/2) < presupuesto <= presupuestoEstrato1+(presupuestoEstrato1/2):
                self.presupuesto = presupuesto
            else:
                self.presupuesto = presupuestoEstrato1
        elif estrato == 2:
            if presupuestoEstrato2-(presupuestoEstrato2/2) < presupuesto <= presupuestoEstrato2+(presupuestoEstrato2/2):
                self.presupuesto = presupuesto
            else:
                self.presupuesto = presupuestoEstrato2
        elif estrato == 3:
            if presupuestoEstrato3-(presupuestoEstrato3/2) < presupuesto <= presupuestoEstrato3+(presupuestoEstrato3/2):
                self.presupuesto = presupuesto
            else:
                self.presupuesto = presupuestoEstrato3
        elif estrato == 4:
            if presupuestoEstrato4-(presupuestoEstrato4/2) < presupuesto <= presupuestoEstrato4+(presupuestoEstrato4/2):
                self.presupuesto = presupuesto
            else:
                self.presupuesto = presupuestoEstrato4
        elif estrato == 5:
            if presupuestoEstrato5-(presupuestoEstrato5/2) < presupuesto <= presupuestoEstrato5+(presupuestoEstrato5/2):
                self.presupuesto = presupuesto
            else:
                self.presupuesto = presupuestoEstrato5

    def getPresupuesto(self): #RETORNA EL PRESUPUESTO
        return self.presupuesto



    def setCiclovia(self, ciclovia=False): #RECIBE EL FACTOR DE SI HAY CICLOVIA O NO
        if ciclovia == True or ciclovia == False:
            self.ciclovia = ciclovia
        else:
            self.ciclovia = False

    def getCiclovia(self): #RETORNA SI HAY O NO CICLOVIA
        return self.ciclovia



    def setPublico(self, publico=False):  #RECIBE EL FACTOR DE SI HAY TRANSPORTE PUBLICO O NO
        if publico == True or publico == False:
            self.publico = publico
        else:
            self.publico = False

    def getPublico(self):  #RETORNA SI HAY O NO TRANSPORTE PUBLICO
        return self.publico



    def setCarro(self, carro=False):  #RECIBE EL FACTOR DE SI HAY RUTA VEHICULAR O NO
        if carro == True or carro == False:
            self.carro = carro
        else:
            self.carro = False

    def getCarro(self): #RETORNA SI HAY O NO RUTA VEHICULAR
        return self.carro