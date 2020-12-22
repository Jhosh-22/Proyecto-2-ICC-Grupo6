import Menus
import Matrices

negrita = '\033[1m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
verde2 = '\033[36m'
blanco = '\033[37m'
reset = '\033[39m'

print(azul+"HOLA QUERIDO USUARIO, BIENVENIDO")
archivocargado=Menus.cargar_memoria()
MemoriaMatrices=[]

while (opcion := Menus.MenuPrincipal()) != "4":
    if opcion == "1":
        while (opcion1 := Menus.IngresarMatrices()) != "3":
            opcion=opcion1
            if opcion1 == "1":
                #Acciones para ingresar matriz en posicion existente

                a = Menus.IngresoNumeroValido(negrita+blanco+
                    "Por favor ingrese el numero de matrices que quiere añadir en la memoria:",
                    "Error!!!! El valor ingresado es incorrecto")
                if len(archivocargado)==0:
                    MM1 = [[0]] * a

                    A=Menus.adiciona_matrices(MemoriaMatrices,MM1,a)
                    for i in A:
                        MemoriaMatrices.append(i)
                else:
                    print(MemoriaMatrices)
                    Menus.crearMatriz(archivocargado,a,opcion)


            elif opcion1 == "2":
                #Acciones para ingresar matriz en posicion libre
                n = Menus.IngresoNumeroValido(blanco+"Por favor ingrese el numero de matrices que quiere añadir en la memoria:",
                                        "Error!!!! El valor ingresado es incorrecto")

                Menus.crearMatriz(MemoriaMatrices,n,opcion)
    elif opcion == "2":
        MemoriaMatrices1 = archivocargado + MemoriaMatrices
        while (opcion := Menus.operarMatrices()) != "7":
            if opcion == "1":
                # función que suma matrices
                a1 = Menus.IngresoNumeroValido(blanco+"Elige la primera matriz que desea sumar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                a2 = Menus.IngresoNumeroValido(blanco+"Elige la segunda matriz que desea sumar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                b1 = a1 - 1
                b2 = a2 - 1
                if b1 < len(MemoriaMatrices1) and b2 < len(MemoriaMatrices1):
                    matriz1 = MemoriaMatrices1[b1]
                    matriz2 = MemoriaMatrices1[b2]
                    if len(matriz1) == 0 or len(matriz2) == 0:
                        print("Error las matrices no se pueden sumar por que están vacías, intento de nuevo")
                    else:
                        print(blanco + "Este es la primera matriz")
                        print(verde + Menus.matriz_ordenada_solo(matriz1))
                        print(blanco + "Este es la segunda matriz")
                        print(verde + Menus.matriz_ordenada_solo(matriz2))
                        if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
                            a = Matrices.sumamatriz(matriz1, matriz2)
                            print(blanco + "La matriz resultante es: ")
                            Menus.matriz_ordenada_solo(a)
                            MemoriaMatrices.append(Matrices.sumamatriz(matriz1, matriz2))
                        else:
                            print(rojo + "Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n")
                else:
                    print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")

            elif opcion == "2":
                #La función que resta matrices
                a1 = Menus.IngresoNumeroValido(blanco+"Elige la primera matriz que desea restar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                a2 = Menus.IngresoNumeroValido(blanco+"Elige la segunda matriz que desea restar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                b1 = a1 - 1
                b2 = a2 - 1
                if b1 < len(MemoriaMatrices1) and b2 < len(MemoriaMatrices1):
                    matriz1 = MemoriaMatrices1[b1]
                    matriz2 = MemoriaMatrices1[b2]
                    if len(matriz1) == 0 or len(matriz2) == 0:
                        print("Error las matrices no se pueden sumar por que están vacías, intento de nuevo")
                    else:
                        print(blanco+"Este es la primera matriz")
                        print(verde+Menus.matriz_ordenada_solo(matriz1))
                        print(blanco+"Este es la segunda matriz")
                        print(verde+Menus.matriz_ordenada_solo(matriz2))
                        if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
                            print(blanco + "La matriz resultante es: ")
                            print(verde + Menus.matriz_ordenada_solo(Matrices.restamatriz(matriz1, matriz2)))

                            MemoriaMatrices.append(Matrices.restamatriz(matriz1, matriz2))
                        else:
                            print(rojo + "Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n")
                else:
                    print(rojo+"Querido Usuario!!! La matriz que ingreso no existe!!!!!")


            elif opcion == "3":
                #Función que multiplica matrices
                a1 = Menus.IngresoNumeroValido(blanco+"Elige la primera matriz que desea multiplicar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                a2 = Menus.IngresoNumeroValido(blanco+"Elige la segunda matriz que desea multiplicar: ",
                                               "Error!!!! El valor ingresado es incorrecto")
                b1 = a1 - 1
                b2 = a2 - 1
                if b1 < len(MemoriaMatrices1) and b2 < len(MemoriaMatrices1):
                    matriz1 = MemoriaMatrices1[b1]
                    matriz2 = MemoriaMatrices1[b2]
                    if len(matriz1) == 0 or len(matriz2) == 0:
                        print("Error las matrices no se pueden multiplicar por que están vacías, intenta de nuevo")
                    else:
                        print("Este es la primera matriz: ")
                        print(verde + Menus.matriz_ordenada_solo(matriz1))
                        print(blanco + "Este es la segunda matriz: ")
                        print(verde + Menus.matriz_ordenada_solo(matriz2))
                        if len(matriz1[0]) == len(matriz2):
                            print(blanco + "La matriz resultante es: ")
                            print(verde + Menus.matriz_ordenada_solo(Matrices.multiplicacion(matriz1, matriz2)))
                            MemoriaMatrices.append(Matrices.multiplicacion(matriz1, matriz2))
                        else:
                            print(rojo + "Alerta!!!!! Querido usuario recuerde que las matrices deben de ser m*n y n*p")

                else:
                    print(rojo+"Querido Usuario!!! La matriz que ingreso no existe!!!!!")



            elif opcion == "4":
                #"Función que traspone una matriz")
                a = Menus.IngresoNumeroValido(blanco+"Elige la matriz que desea trasponer: ",
                                              "Error!!!! El valor ingresado es incorrecto")
                b = a - 1
                if b < len(MemoriaMatrices1):
                    Matriz3 = MemoriaMatrices1[b]
                    print("Matriz a trasponer: ")
                    print( verde+Menus.matriz_ordenada_solo(Matriz3))
                    if len(Matriz3) == 0:
                        print("Error la matriz no se puede trasponer por que está vacía, intenta de nuevo")
                    else:
                        matriztraz = Matrices.trasponerMatrices(Matriz3)
                        MemoriaMatrices.append(matriztraz)
                        print(blanco+"La matriz traspuesta es: ")
                        print( verde+Menus.matriz_ordenada_solo(matriztraz))
                else:
                    print(rojo+"La matriz no existe en la memoria")

            elif opcion == "5":
                #"Funcion que multiplica un escalar por una matriz")
                a = Menus.IngresoNumeroValido(blanco+"Elige la matriz que desea multiplicar por el escalar: ",
                                              "Error!!!! El valor ingresado es incorrecto")
                b = a - 1
                # numero = int(input("Ingrese el numero que quiere multiplicar a la matriz: "))
                numero = Menus.IngresoNumeroValido(blanco+"Ingrese un numero: ",
                                                   "Error!! El valor ingresado no es un numero: ")
                if b < len(MemoriaMatrices1):
                    matrizz = MemoriaMatrices1[b]
                    if len(matrizz) == 0:
                        print(blanco+"Error la matriz no se puede multiplicar por que está vacía, intenta de nuevo")
                    else:
                        MemoriaMatrices.append(Matrices.escalar_matriz(numero, matrizz))
                        print(blanco+"Matriz a multiplicar")
                        print(verde+Menus.matriz_ordenada_solo(matrizz))

                        print(blanco+"Matriz multiplicada por el escalar" )
                        print(verde+Menus.matriz_ordenada_solo(Matrices.escalar_matriz(numero, matrizz)))
                else:
                    print("Querido Usuario!!! La matriz que ingreso no existe!!!!!")



            elif opcion == "6":
                print(verde2 + "RESOLVER LAVERINTO ")
                print(blanco + "Opciones disponibles: ")
                print(azul + "[1] Desarrollar un laberinto planteado aleatoriamente:   ")
                print("[2] Desarrollar un laberinto planteado por el usuario: ")
                opcion2 = Menus.IngresoNumeroValido(blanco + "Ingrese la opcion que desea desarrollar: ",
                                                    "Error!! Valor no valido")
                if opcion2 == 1:
                    N = Menus.IngresoNumeroValido(blanco + "Ingrese el tamaño que quiere que sea su laberinto: ",
                                                  "Error el valor ingresado no es un numero")

                    labo = Matrices.crear_laberinto_aleatorio(N)
                    print(labo)
                    print(" ")
                    print(azul + "laberinto planteado aleatoriamente: ")
                    print(Matrices.mostrar_lab_planteado(labo))
                    Matrices.solve_laberinto(labo, N)
                    print(" ")
                if opcion2 == 2:
                    N = Menus.IngresoNumeroValido(blanco + "Ingrese el tamaño que quiere que sea su laberinto: ",
                                                  "Error el valor ingresado no es un numero")
                    matriz_lab = Matrices.crear_laberinto_ingresado_por_usuario(N)
                    print(matriz_lab)
                    print(" ")
                    print(azul + "Laberinto planteado por el usuario")
                    print(Matrices.mostrar_lab_planteado(matriz_lab))
                    print(" ")
                    Matrices.solve_laberinto(matriz_lab, N)


    elif opcion == "3":
        MemoriaMatrices1 = archivocargado + MemoriaMatrices
        while (opcion := Menus.MostrarMatrices()) != "3":

            if opcion == "1":

                if len(MemoriaMatrices1)==0:
                    print(rojo+"la memoria de matrices está vacia")
                else:
                    print(verde2+"LISTADO DE MATRICES ", MemoriaMatrices1)
                    print(verde+Menus.matriz_ordenada_listado(MemoriaMatrices1))
            elif opcion == "2":

                a = Menus.IngresoNumeroValido(blanco+"Ingrese el orden de la matriz que desea ver en la memoria: ",
                                              "Error!!!! El valor ingresado es incorrecto")
                if a - 1 < len(MemoriaMatrices1):

                    print(verde2+Menus.matriz_ordenada_solo(MemoriaMatrices1[a - 1]))
                else:
                    print(rojo+"La matriz no existe en la memoria")
MemoriaMatrices2=archivocargado+ MemoriaMatrices
Menus.mandar_a_memoria(MemoriaMatrices2)


print("GRACIAS POR ESTAR AQUÍ ")



print(azul+negrita+"ºººººººººº       ºººººººººº       ºººº               ºººº          ººººººººººººº","\n"
    "ºººººººººº       ºººººººººº       ºººº               ºººº          ºººººººººººº","\n"
    "ºººº             ºººº             ºººº               ºººº                ººººº","\n"
    "ºººººººººº       ºººººººººº       ºººº               ºººº              ººººº","\n"
    "ºººººººººº       ºººººººººº       ºººº               ºººº             ººººº","\n"
    "ºººº             ºººº             ºººº               ºººº           ººººº","\n"
    "ºººº             ºººººººººº       ºººººººººººº       ºººº          ºººººººººººº","\n"
    "ºººº             ºººººººººº       ºººººººººººº       ºººº         ººººººººººººº","\n")

print("ºººººººº      ºººº            ºººººººº     ºººº              ºººº     ºººº     ºººººººººººº                 ºººººººº            ººººººººººººº","\n"
      "ººººººººº     ºººº           ºººº  ºººº     ºººº            ºººº      ºººº     ºººººººººººººº              ºººº  ºººº           ºººººººººººººº","\n"
      "ºººº ººººº    ºººº          ºººº    ºººº     ºººº          ºººº       ºººº     ºººº        ººººº          ºººº    ºººº          ºººº        ººººº","\n"
      "ºººº  ººººº   ºººº         ºººº      ºººº     ºººº        ºººº        ºººº     ºººº         ººººº        ºººº      ºººº         ºººº         ººººº","\n"
      "ºººº   ººººº  ºººº        ºººººººººººººººº     ºººº      ºººº         ºººº     ºººº         ººººº       ºººººººººººººººº        ºººº         ººººº","\n"       
      "ºººº    ººººº ºººº       ºººººººººººººººººº     ºººº    ºººº          ºººº     ºººº       ººººº        ºººººººººººººººººº       ºººº       ººººº","\n"
      "ºººº     ººººººººº      ºººº            ºººº     ºººº  ºººº           ºººº     ºººººººººººººº         ºººº            ºººº      ºººººººººººººº","\n"
      "ºººº      ºººººººº     ºººº              ºººº     ºººººººº            ºººº     ºººººººººººº          ºººº              ºººº     ºººººººººººº")

