import relacion
import MetodosAnálisis

#MONTERREY
Monterrey = relacion.Relacion()
Monterrey.setNombre()
Monterrey.setHabitantes(350)
Monterrey.setEstrato(4)
Monterrey.setPresupuesto(2750)
Monterrey.setCiclovia(False)
Monterrey.setPublico(True)
Monterrey.setCarro(True)

Monterrey.setComparacionCiclovia()
Monterrey.setComparacionPublico()
Monterrey.setComparacionCarro()

Monterrey.establecerMovimientosCiclovia()
Monterrey.establecerMovimientosPublico()
Monterrey.establecerMovimientosCarro()


#COLINA
Colina = relacion.Relacion()
Colina.setNombre()
Colina.setHabitantes()
Colina.setEstrato()
Colina.setPresupuesto()
Colina.setCiclovia(True)
Colina.setPublico(True)
Colina.setCarro(True)

Colina.setComparacionCiclovia()
Colina.setComparacionPublico()
Colina.setComparacionCarro()

Colina.establecerMovimientosCiclovia()
Colina.establecerMovimientosPublico()
Colina.establecerMovimientosCarro()


# #TEOREMA7
# Teorema7 = relacion.Relacion()
# Teorema7.setNombre()
# Teorema7.setHabitantes(400)
# Teorema7.setEstrato(1)
# Teorema7.setPresupuesto(500)
# Teorema7.setCiclovia(True)
# Teorema7.setPublico(True)
# Teorema7.setCarro(False)
#
# Teorema7.setComparacionCiclovia()
# Teorema7.setComparacionPublico()
# Teorema7.setComparacionCarro()
#
# Teorema7.establecerMovimientosCiclovia()
# Teorema7.establecerMovimientosPublico()
# Teorema7.establecerMovimientosCarro()
# print(Teorema7)
#
# #LAVICTORIA
# LaVictoria = relacion.Relacion()
# LaVictoria.setNombre()
# LaVictoria.setHabitantes(480)
# LaVictoria.setEstrato(5)
# LaVictoria.setPresupuesto(4700)
# LaVictoria.setCiclovia(True)
# LaVictoria.setPublico(True)
# LaVictoria.setCarro(True)
#
# LaVictoria.setComparacionCiclovia()
# LaVictoria.setComparacionPublico()
# LaVictoria.setComparacionCarro()
#
# LaVictoria.establecerMovimientosCiclovia()
# LaVictoria.establecerMovimientosPublico()
# LaVictoria.establecerMovimientosCarro()
# print(LaVictoria)

# #JUGUETE
# Juguete = relacion.Relacion()
# Juguete.setNombre()
# Juguete.setHabitantes(390)
# Juguete.setEstrato(2)
# Juguete.setPresupuesto(750)
# Juguete.setCiclovia(True)
# Juguete.setPublico(True)
# Juguete.setCarro(True)
#
# Juguete.setComparacionCiclovia()
# Juguete.setComparacionPublico()
# Juguete.setComparacionCarro()
#
# Juguete.establecerMovimientosCiclovia()
# Juguete.establecerMovimientosPublico()
# Juguete.establecerMovimientosCarro()
# print(Juguete)

MetodosAnálisis.ConexionEntreDosObjetos(Monterrey,Colina)