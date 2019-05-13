'''
LA CLASE LOCALIDAD VA A CREAR UNA LOCALIDAD DENTRO DE LA CIUDAD, LA LOCALIDAD VA A TENER HABITANTES, UN ESTRATO (DEL CUAL DEPENDE
EL PRESUPUESTO ASIGNADO A LA LOCALIDAD), EL ESTRATO Y PRESUPUESTO TIENEN LA CAPACIDAD DE INCREMENTAR/MEJORAR LAS RUTAS DE TRANSPORTE
PARA REGULAR EL EMBOTELLAMIENTO, EN ESTA CLASE SE DEFINEN LOS PRINCPIOS DE LA LOCALIDAD, ASÍ COMO SE VA A ENTENDER SU CAPACIDAD PARA
MEJORAR GENERAR UN MECANISMO DE TRANSPORTE ÓPTIMO
'''
class Localidad:

    def __init__(self):
        self.habitantes = 120
        self.estrato = 3
        self.presupuesto = 1200
        self.ciclovia = False
        self.publico = False
        self.carro = False

    def setHabitantes(self, habitantes=120):
        if 35 < habitantes < 500:
            self.habitantes = int(habitantes)
        else:
            self.habitantes = 120
    def getHabitantes(self):
        return self.habitantes

    def setEstrato(self, estrato=3):
        if 1 <= estrato <= 5:
            self.estrato = estrato
        else:
            self.estrato = 3
    def getEstrato(self):
        return self.estrato

    def setPresupuesto(self, presupuesto=1200):
        estrato = self.getEstrato()
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
    def getPresupuesto(self):
        return self.presupuesto

    def setCiclovia(self, ciclovia=False):
        if ciclovia == True or ciclovia == False:
            self.ciclovia = ciclovia
        else:
            self.ciclovia = False
    def getCiclovia(self):
        return self.ciclovia

    def setPublico(self, publico=False):
        if publico == True or publico == False:
            self.publico = publico
        else:
            self.publico = False
    def getPublico(self):
        return self.publico

    def setCarro(self, carro=False):
        if carro == True or carro == False:
            self.carro = carro
        else:
            self.carro = False
    def getCarro(self):
        return self.carro
