denuncias = []
tipos = []        
gravedades = []   
base_verdadera=[]
base_falsas=[]
contador_de_denuncia=0
contador_denuncias_falsas=0
contador=0
sistema=False
fin_de_dia=False
contraseña_autoridad="123456789"

ROJO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"

while fin_de_dia == False:

    print ("_____________________________".center(80,' '))
    print (("\033[1m" +"Unidad Educativa Cerro Verde"+"\033[0m").center(85,' ')) 
    print ("CREANDO FUTUROS PROFESIONALES".center(80,' '))
    print ("_____________________________".center(80,' '))
    print ("Esperamos te encuentres muy bien".center(80,' '))
    print ()
    print (("\033[1m" +"Bienvenido al sistema de Denuncias anonimas"+"\033[0m").center(90,' '))
    print ()
    print ("¿En que podemos ayudarte?")
    print ()
    print ("1. Denunciar Acoso")
    print ("2. Denunciar Bullying")
    print ("3. Denunciar Inconformidad con calificaciones")
    print ("4. Otras Denuncias")
    print ("5. Administración")
    print ("6. Salir del sistema")

    var = input("\nIngrese el literal de la opcion deseada: ")
    if not var.isdigit():
        print (ROJO+"Solo puede ingresar números"+ RESET)
        continue
    var = int (var)
    if var < 1 or var > 6 :
        print (ROJO +"Elija un numeral válido"+ RESET)
        continue

    if var == 6:
        print("Saliendo del sistema...")
        fin_de_dia = True
        continue

    intentos = 0
    while intentos < 3:
        print ()
        print ("\033[1m""Ingese su fecha del dia Actual/Hoy""\033[0m")
        print ()
        fecha = input("\033[1mIngresa una fecha (DD/MM/AAAA):\033[0m").strip()
        if fecha == "":
            print(ROJO +"La fecha no puede estar vacía.\n"+RESET)
            intentos += 1
            continue
        partes = fecha.split("/")
        if len(partes) != 3:
            print(ROJO + "Formato incorrecto. Usa DD/MM/AAAA.\n"+ RESET)
            intentos += 1
            continue
        dia, mes, año = partes

        if not (dia.isdigit() and mes.isdigit() and año.isdigit()):
            print(ROJO + "La fecha debe contener solo números.\n"+ RESET)
            intentos += 1
            continue

        dia = int(dia)
        mes = int(mes)
        año = int(año)

        if mes < 1 or mes > 12:
            print(ROJO+ "Mes inválido.\n"+ RESET)
            intentos += 1
            continue

        if dia < 1 or dia > 31:
            print(ROJO + "Día inválido.\n"+ RESET)
            intentos += 1
            continue

        if mes in [4, 6, 9, 11] and dia > 30:
            print(ROJO + "Ese mes solo tiene 30 días.\n" +RESET)
            intentos += 1
            continue

        if mes == 2:
            bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

            if bisiesto and dia > 29:
                print(ROJO + "Febrero en año bisiesto solo tiene 29 días.\n"+ RESET)
                intentos += 1
                continue
            elif not bisiesto and dia > 28:
                print(ROJO +"Febrero solo tiene 28 días.\n" +RESET)
                intentos += 1
                continue

        print("Fecha válida:", fecha)

        if año != 2025 :
            print (ROJO +"Año no valido"+ RESET)
            intentos += 1
            continue

        break

    if intentos == 3:
        print(ROJO + "Se excedieron los intentos. Programa finalizado."+ RESET)
        continue

    if var != 5 and var != 6 :
        print ()
        print("Escriba que nivel de gravedad es su decuncia, esto nos ayuda a poder resolver el problema de manera inmediata y de la mejor forma.")
        print ("\033[1m" +"Que nivel de gravedad es su denuncia"+"\033[0m" )
        print ()
        print (" Alto : Muy grave necesito ayuda ahora mismo  ")
        print (" Medio : Puedo esperar un poco para que me ayuden inmediatamente")
        print (" Bajo : Puedo esperar la ayuda.")
        print ()
   
        while True:
            nivel_de_denuncia = input("Ingrese gravedad (alto/medio/bajo): ").lower()
            if nivel_de_denuncia in ["alto","medio","bajo"]:
                break
            else:
                print(ROJO + "Gravedad inválida. Use solo sin espacios: alto, medio o bajo." + RESET)

        print ()
        print ("\033[1m" "Detalle su denuncia con la siguiente guia:""\033[0m")
        print ()
        print ("-Explique que sucedio, quien fue el causante si no sabe su nombre describa su aspecto fisico.")
        print ()
        print ("-Puede añadir en que lugar de la institucion ocurrio o si ocurrio fuera de la misma.")
        print ()
        print ("-Si ocurrio ciber acoso, de el nombre de la aplicacion, puede dar detalles del suceso.")
        print ()
        texto = input("Ingrese detalles de su denuncia (minimo 50 caracteres): ").lower()
        print ()
        print ("Muchas gracias por tu decuncia espera pronto la resolucion de tu caso.")
        print ()
        print ("\033[1m"+"SI SU DENUNCIA NO FUE ATENDIDA EN UN PLAZO DE 5 DIAS IR A LAS OFICINAS DE LA INSTITUCION"+"\033[0m")
        print ()
        print ("Ten un buen dia FUTURO PROFESIONAL...")
        tipos.append(var)
        gravedades.append(nivel_de_denuncia)

        palabras_clave_falso=["xd", "casi", "a veces", "asd"]
        tipo_denuncia=["acoso", "bullying", "calificaciones", "otros"]

        if len(texto)>=50:
            for palabra in texto.split():
                if palabra in palabras_clave_falso:
                    contador+=1

            if contador <=5:
                base_verdadera.append([contador_de_denuncia, tipo_denuncia[var-1], nivel_de_denuncia, texto])
                contador_de_denuncia+=1
            else:
                base_falsas.append([contador_denuncias_falsas, tipo_denuncia[var-1], nivel_de_denuncia, texto])
                contador_denuncias_falsas+=1
        else:
            base_falsas.append([contador_denuncias_falsas, tipo_denuncia[var-1], nivel_de_denuncia, texto])
            contador_denuncias_falsas+=1

    elif var == 5:
        intentos_admin = 0
        while intentos_admin < 3:
            clave = input("ingrese la contraseña de acceso")
            if clave == contraseña_autoridad :
                print ("Acceso concedido")
                sistema = True
                break
            else :
                print ("Contraseña incorrecta")
                sistema = False

        while sistema == True:
            print ()
            print (("\033[1m" +"Bienvenido al Sistema de Administrativo de la institucion"+"\033[0m").center(80,' ') )
            print ()
            print ("¿En que podemos ayudarte?")
            print ()
            print ("1. Ver denuncias")
            print ("2. Ver denuncias falsas")
            print ("3. Ver estadisticas")
            print ("4. Terminar dia")
            print ()

            desicion=input("Ingrese el literal de la opcion deseada: ")
            if desicion == "1":
                print("1. Ver todas las denuncias")
                print("2. Filtrar por tipo")
                print("3. Filtrar por gravedad")
                print("4. Filtrar por fecha")

                opcion_control = input("Elija una opción: ")

                if opcion_control == "1":
                    if len(base_verdadera) == 0:
                        print ("No existen denuncias registradas aun")
                    else :   
                        for d in base_verdadera:
                            print("-----")
                            print(d)

                elif opcion_control == "2":
                    tipo_filtro = input("Ingrese el tipo (acoso/bullying/calificaciones/otros): ")

                    for d in base_verdadera:
                        if d[1] == tipo_filtro:
                            print("-----")
                            print(d)

                elif opcion_control == "3":
                    gravedad_filtro = input("Ingrese la gravedad (Alto/Medio/Bajo): ").lower()

                    for d in base_verdadera:
                        if d[2] == gravedad_filtro:
                            print("-----")
                            print(d)

                elif opcion_control == "4":
                    fecha_filtro = input("Ingrese la fecha: ")

                    for d in base_verdadera:
                        if fecha_filtro in d[3]:
                            print("-----")
                            print(d)

            elif desicion == "2":
                print("Denuncias detectadas como falsas:", contador_denuncias_falsas)

            elif desicion == "3":
                print("Total de denuncias registradas:", len(tipos))
                print("------------------------------------")

                print("Denuncias por tipo")
                print("Tipo 1:", tipos.count(1))
                print("Tipo 2:", tipos.count(2))
                print("Tipo 3:", tipos.count(3))
                print("Tipo 4:", tipos.count(4))

                total = len(tipos)
                print("------------------------------------")
                print("Porcentajes")

                if total > 0:
                    print("Tipo 1:", tipos.count(1) * 100 // total, "%")
                    print("Tipo 2:", tipos.count(2) * 100 // total, "%")
                    print("Tipo 3:", tipos.count(3) * 100 // total, "%")
                    print("Tipo 4:", tipos.count(4) * 100 // total, "%")

            else:
                print ()
                print("\033[1m""ha declarado fin de la jornada, gracias por usar nuestro programa, hasta mañana""\033[0m")
                fin_de_dia = True
                sistema = False

