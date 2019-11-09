nombre=" ELMER SANDOVAL DE LA CRUZ"
print(" ESTUDIANTE:", nombre)

numero=" BOLETA 01"
print("NRO :", numero)

# INPUT
cliente=input("nombre del cliente:")
pedido01=int(input("Nro de camisas:"))
pedido02=int(input("Nro de pantalones:"))
pedido03=int(input("Nro de corbatas:"))
pu1=float(input("precio unitario camisas:"))
pu2=float(input("precio unitario pantalones:"))
pu3=float(input("precio unitario corbatas:"))
IGV=8.8

# PROCESSING
total_camisas=pedido01*pu1
total_pantalones=pedido02*pu2
tolal_corbatas=pedido03*pu3
total=(total_camisas+total_pantalones+tolal_corbatas)*IGV

# VERIFICADOR
comprobar=(total>=894)

# OUTPUT
print("######################################")
print("    BOLETA DE VENTA : TIENDA JOSE             ")
print("###########################################")
print("#")
print("# cliente:              ",cliente,"    ")
print("##################################################")
print("   DATOS:        CANTIDAD:     PU:       TOTAL:")
print("# camisas:         ",pedido01,"      ",pu1,"       ",total_camisas,"  ")
print("# pantalones:      ",pedido02,"      ",pu2,"       ",total_pantalones,"")
print("# corbatas:        ",pedido03,"      ",pu3,"       ",tolal_corbatas,"")
print("# IGV:             ",IGV,"          ")
print("# total:           ",total,"      ")
print("###########################################")
print(" comprovar:", comprobar)

numero=" BOLETA 02"
print("NRO:", numero)

# INPUT
cliente=input("cliente:")
paga=int(input("monto:"))
interes=float(input("interes:"))
dia=input("Dia:")

# PROCESSING
total_a_pagar=paga+interes*paga

# VERIFICADOR
comprobando_total=(total_a_pagar<465)

# OUTPUT
print("#####################################")
print("  BOLETA ELECTRONICA            ")
print("#")
print(" cliente:      ",cliente,"      ")
print("#")
print("# Dia:           ",dia,"        ")
print("# pagar:         ",paga,"       ")
print("# interes:       ",interes,"    ")
print("# total a pagar:  ",total_a_pagar," ")
print("#################################")
print(" comprobando :" , comprobando_total)


numero=("BOLETA 3")
print("NRO:", numero)

# INPUT
nombre=input("nombre:")
cargo=input("cargo:")
sueldo=int(input("sueldo mensual:"))
descuento=float(input("descuento del AFP:"))

# PROCESSING
total_salario_mensual=sueldo-(descuento*sueldo)

# VERIFICADOR
comprobar_el_sueldo=(total_salario_mensual<45.85)

# OUTPUT
print("##########################################")
print("       BOLETA DE PAGO                 ")
print("#########################################")
print("#")
print("# Nombre:                  ",nombre,"    ")
print("# Cargo:                   ",cargo,"     ")
print("# sueldo mensual:          ",sueldo,"    ")
print("# descuento del AFP:       ",descuento," ")
print("# total de recibo mensual: ",total_salario_mensual," ")
print("#############################################")
print("comprobando:"   ,comprobar_el_sueldo)


numero=(" BOLETA 04")
print("NRO:", numero)

# INPUT
masa=int(input("Masa:"))
volumen=int(input("volumen:"))

# PROCESSING
Densidad=masa/volumen

# VERIFICADOR
comprobador=(Densidad>=80)

# OUTPUT
print("#####################################")
print("#      DENSIDAD DE UN CUERPO      ")
print("######################################")
print("#")
print("# DATOS:             VALOR:   ")
print("# masa:             ",masa,"     ")
print("# volumen:          ",volumen,"   ")
print("# densidad:         ",Densidad,"   ")
print("######################################")
print(" comprobar la densida del cuerpo:", comprobador)

numero=(" BOLETA 05")
print("NRO:", numero)

# INPUT
densidad=int(input("Densidad:"))
altura=int(input("Altura:"))
gravedad=float(input("Gravedad:"))

# PROCESSING
presion=densidad*altura*gravedad

# VERIFICADOR
comprobar=(presion<42.3)

# OUTPUT
print("#################################")
print("#    PRESION DE UN CUERPO         ")
print("###################################")
print("#")
print("#  DATOS:             VALOR:      ")
print("# densidad:          ",densidad," ")
print("# altura:            ",altura,"   ")
print("# gravedad:          ",gravedad,"  ")
print("# presion:           ",presion,"  ")
print("###################################")
print("comprobar la presion:", comprobar)


numero=(" BOLETA 06")
print("NRO:", numero)

# INPUT
Radio=int(input("Radio:"))
Pi=float(input("Pi:"))

# PROCESSING
area=((Radio**2)*Pi)

# VERIFICADOR
comprobador=(area>=145)

# OUTPUT
print("####################################")
print("#      AREA DEL CIRCULO          ")
print("######################################")
print("#")
print("#  DATOS:                 VALOR:   ")
print("# radio:                ",Radio,"   ")
print("# Pi:                   ",Pi,"      ")
print("# Area:                 ",area,"    ")
print("#####################################")
print("comprobar el area del circulo:", comprobador)

numero=("BOLETA 07")
print("NRO:", numero)


# INPUT
velocidad_inicial=int(input("Velocidad inicial:"))
velocidad_final=int(input("Velocidad final:"))
tiempo=int(input("Tiempo:"))

# PROCESSING
altura=((velocidad_inicial+velocidad_final)/2)*tiempo

# VERIFICADOR
comprobador=(altura>=80)

# OUTPUT
print("##################################")
print("# ALTURA DE UN CUERPO EN CAIDA LIBRE  ")
print("####################################")
print("#")
print("# DATOS:                   VALOR:           ")
print("# velocidad inicial:      ",velocidad_inicial,"  ")
print("# velocidad final:        ",velocidad_final,"   " )
print("# tiempo:                 ",tiempo,"             ")
print("# altura:                 ",altura,"             ")
print("##################################################")
print("comprobar la altura:", comprobador)


numero=(" BOLETA 08")
print("Nro:", numero)

# INPUT
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))

# PROCESSING
E=A+B-C

# VERIFICADOR
comprobando=(E>=50.84)

# OUTPUT
print("#############################")
print("#   CALCULAR   E   ")
print("#############################")
print("#")
print("# VARIABLES:         VALOR:")
print("#   A:              ",A,"  ")
print("#   B:              ",B,"  ")
print("#   C:              ",C,"  ")
print("#   E:              ",E,"  ")
print("#############################")
print(" comprobando E :", comprobando)

numero=(" BOLETA 08")
print(" Nro:", numero)

# INPUT
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))

# PROCESSING
E=A+B-C
print("E:",E)

# VERIFICADOR
comprobando=(E>=50.84)

# OUTPUT
print("#############################")
print("#   CALCULAR   E   ")
print("#############################")
print("#")
print("# VARIABLES:         VALOR:")
print("#   A:              ",A,"  ")
print("#   B:              ",B,"  ")
print("#   C:              ",C,"  ")
print("#   E:              ",E,"  ")
print("#############################")
print(" comprobando E :", comprobando)


numero=("BOLETA 09")
print("Nro:", numero)

# INPUT
Masa=int(input("Masa:"))
Aceleracion=int(input("Aceleracion:"))

# PROCESSING
Fuerza=Masa*Aceleracion
print("Fuerza:", Fuerza)

# VERIFICADOR
comprobar=(Fuerza<=80)

# OUTPUT
print("################################################")
print("  LA FUEZA QUE APLICA UNA PERSONA A UNA PIEDRA  ")
print("################################################")
print("#")
print("# DATOS:                 VALOR:                ")
print("# Masa:                 ", Masa , "            ")
print("# Aceleracion:         ", Aceleracion , "      ")
print("# Fuerza:              ",Fuerza ,"             ")
print("###############################################")
print("comprobar la fuerza:" , comprobar              )


numero=(" BOLETA 10")
print("Nro:", numero)

# INPUT
base_mayor=int(input("base mayor:"))
base_menor=int(input("base menor:"))
altura=int(input("altura:"))

# PROCESSING
area_del_trapecio=((base_mayor+base_menor)*altura)/2
print("area del trapecio:", area_del_trapecio)

# VERIFICADOR
comprobar_area=(area_del_trapecio>=546)

# OUTPUT
print("###############################")
print("    AREA DEL TRAPECIO           ")
print("####################################")
print("#")
print("#  DATOS:                VALOR:      ")
print("#  Base mayor:         ",base_mayor," ")
print("#  Base menor:         ",base_menor," ")
print("#  Altura:             ",altura,"     ")
print("#  Area trapecio:      ",area_del_trapecio," ")
print("#######################################")
print("comprobar el area del trapecio:",comprobar_area)


nombre=(" JACK SUYON RIOJAS")
print("ESTUDIANTE:", nombre)

# boleta 1: calcular el valor M
# INPUT
N=int(input("N:"))
P=int(input("P:"))
R=int(input("R:"))

# PROCESSING
M=(N*P)/3+R
print("M:", M)

# VERIFICADOR
comprobar=(M>=456)

# OUTPUT
print("####################################")
print("       CALCULAR  M            ")
print("####################################")
print("#")
print("#  VARIABLES:           VALOR:")
print("#   N:                  ",N," ")
print("#   P:                  ",P," ")
print("#   R:                  ",R," ")
print("#   M:                  ",M," ")
print("###################################")
print("comprobando el valor de E:",comprobar)

#boleta 2 :calcular el numero de electrones
#input
numero_de_protones=int(input("ingre el numero de protones:"))
carga=int(input("ingrese la carga:"))

#processing
numero_de_electrones=(numero_de_protones + carga)

#verificador
verificador=(numero_de_electrones>47)

#output
print("###########################################")
print("#      BOLETA DE NUMERO DE ELECTRONES     #")
print("###########################################")
print("#   datos  ")
print("#numero de protones:",numero_de_protones)
print("#carga:",carga)
print("#numero de elctrones es:",numero_de_electrones)
print("###########################################")
print("#el numero de elctrones>47:",verificador)


#boleta 3 : calcular la densidad

#input
cuerpo=input("ingrese el cuerpo: ")
masa=int(input("ingrese la masa:"))
volumen=float(input("ingrese el volumen:"))

#processing
densidad=masa/volumen

#verificador
verificador=(densidad==45)

#output
print("#####################################")
print("#     BOLETA FORMULA DENSIDAD        #")
print("######################################")
print("#   datos")
print("#tipo de cuerpo:  ",cuerpo            )
print("#masa: ",masa                         )
print("#volumen:  ",volumen                  )
print("#densidad:   ",densidad               )
print("#######################################")
print("#densidad==45:   ",verificador        )


#boleta 4: calcular el area lateral de un cono
#input
pi=3.1416
radio=float(input("mostrar el radio:"))
generatriz=int(input("mostrar generatriz:"))

#processing
area_lateral_cono=(pi*radio*generatriz)
verificador=(area_lateral_cono<=65)

#output
print("###########################################")
print("#       BOLETA DEL AREA LATERAL DEL CONO   #" )
print("############################################" )
print("#    datos:"                                     )
print("#pi:   ",pi,"                                " )
print("#radio:  ",radio ,"                           ")
print("#generatriz:  ",generatriz ,"                 " )
print("#area lateral del cono:  ",area_lateral_cono)
print("###########################################")
print("#area lateral del cono<=65:",verificador)


#boleta 5: calcular el area total de la piramide
#input
area_lateral_piramide=int(input("ingrese el area lateral de la piramide:"))
area_base_piramide=int(input("ingrese el area de la base de la piramide:"))

#processing
area_total_piramide= area_lateral_piramide + area_base_piramide

#verificador
verificador=(area_total_piramide!=62)

#output
print("#################################################")
print("#        BOLETA DEL AREA TOTAL DE LA PIRAMIDE    #")
print("#################################################")
print("# datos  "                                        )
print("#area lateral de la piramide:    ",area_lateral_piramide," ")
print("#area de la base de la piramide:    ",area_base_piramide," ")
print("#area total de la piramide     ",area_total_piramide,"")
print("###################################################")
print("#area total de la piramide=!62",verificador)

#boleta 6: calcular el volumen de la piramide
#input
area_base_de_la_piramide=int(input("ingrese el area de la base:"))
altura=float(input("ingrese la altura:"))

#processing
volumen_piramide=(area_base_de_la_piramide*altura)/3

#verificador
verificador=(volumen_piramide>36)

#output
print("##################################################")
print("#       BOLETA DEL VOLUMEN DE UNA PIRAMIDE   #")
print("##################################################")
print("#datos")
print("#area de la base de la piramide:",area_base_de_la_piramide)
print("#altura:",altura)
print("#volumen de la piramide:",volumen_piramide)
print("###################################################")
print("#volumen de la piramide>36",verificador)


#boleta 7: clacular el area lateral del cilindro
#input
pi=3.1416
radio1=float(input("ingrese el radio:"))
generatriz1=int(input("ingrese la generatriz:"))

#processing
area_lateral_cilindro=(2*pi*radio1*generatriz1)

#verificador
verificador=(area_lateral_cilindro>=29)

#output
print("###############################################")
print("#         BOLETA DEL AREA DEL CILINDRO        #")
print("###############################################")
print("#   datos")
print("#pi:  ",pi                                       )
print("#radio1:    ",radio1)
print("#generatriz1:    ",generatriz1)
print("#area latera del cilindro:    ",area_lateral_cilindro)
print("#################################################")
print("#area lateral del cilindro>=29",verificador)



#boleta 8: calcular el tiempo de enuentro
#input
distancia=float(input("ingrese distancia:"))
velocidad1=int(input("ingrese velocidad:"))
velocidad2=int(input("ingrese velocidad 2"))
#processing
tiempo_encuentro=(distancia)/(velocidad1 + velocidad2)

#verificador
verificador=(tiempo_encuentro<=30)

#output
print("########################################################")
print("#     BOLETA DE LA FORMULA DE TIEMPO DE ENCUENTRO      #")
print("########################################################")
print("#  datos")
print("#distancia:   ",distancia                                )
print("#velocidad:   ",velocidad1                               )
print("#velocidad:    ",velocidad2                              )
print("#tiempo de encuentro:   ",tiempo_encuentro               )
print("########################################################")
print("#tiempo de encuentro<=30",verificador)


#boleta 9: calcular tiempo de alcance
#input
distancia=float(input("ingrese distancia:"))
velocidad1=int(input("ingrese velocida1:"))
velocidad2=int(input("ingrese velocidad2:"))

#processing
tiempo_alcance=(distancia)/(velocidad1 - velocidad2)

#verificador
verificador=(tiempo_alcance==90)

#output
print("#########################################")
print("#     BOLETA DE TIEMPO DE ALCANCE       #")
print("#########################################")
print("# datos                                  ")
print("#distancia :   ",distancia)
print("#velocidad 1:   ",velocidad1)
print("#velocidad 2:   ",velocidad2)
print("#tiempo alcance:   ",tiempo_alcance)
print("#########################################")
print("#tiempo de alcance==90:   ",verificador)


#boleta 10: calcular la presion hidrostatica
#input
densidad=float(input("ingrese la densidad:"))
gravedad=int(input("ingrese la gravedad:"))
altura=float(input("ingrese la altura:"))

#processing
presion_hidrostatica=densidad*gravedad*altura

#verificador
verificador=(presion_hidrostatica>=32)
#output
print("#########################################################")
print("#    BOLETA DE LA FORMULA DE LA PRESION HIDROSTATICA    #")
print("#########################################################")
print("#    datos")
print("#densidad0:   ",densidad)
print("#gravedad0:   ",gravedad)
print("#altura0:   ",altura)
print("#presion hidrostatica:   ",presion_hidrostatica)
print("##########################################################")
print("#presion hidrostatica>=32:   ",verificador)


