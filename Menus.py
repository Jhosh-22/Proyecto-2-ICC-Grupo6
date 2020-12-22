import  json
#Colores que se usa en el texto
blanco = '\033[1m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
magenta = '\033[35m'
verde2 = '\033[36m'
blanco2 = '\033[37m'
reset = '\033[39m'

# Función en Bucle representa el menu principal donde se encuentran los modulos siguientes

def MenuPrincipal():
    while True:
        print(blanco+verde2,"MENU PRINCIPAL")

        print(azul +"[1] Ingresar Matrices",end="          ")
        print("[2] Operar Matrices")
        print("[3] Mostrar Matrices",end="           ")
        print("[4] Salir")
        opcion = input(blanco+blanco2+"Seleccione opción: ")
        if opcion in ["1","2","3","4"]:
            return opcion
        else:
            print(rojo+"Opción no válida!!! Vuelva a intentarlo")

# Función en Bucle representan las opciones donde se ingresan las matrices

def IngresarMatrices():
    while True:
        #MENÚ 1
        print(verde2,"INGRESAR MATRICES")
        print(azul +"[1] Ingresar una Matriz a una de memoria de matriz especificada ",end="   ")
        print("[2] Ingresar una matriz a una memoria libre")
        print("[3] Salir")
        opcion = input(blanco+blanco2+"Seleccione opción: ")
        if opcion in ["1","2","3"]:
            return opcion
        else:
            print(rojo+"Opción no válida!!! Vuelva a intentarlo")

# Función que crea matrices cuando si existen otras matrices

def crearMatriz(MM, a,opcion1):
    if a == 0:
        return MM
    else:
        m = IngresoNumeroValido(blanco+blanco2+"Filas: ", "Error!!!! El valor ingresado es incorrecto")
        n = IngresoNumeroValido(blanco+blanco2+"Columnas: ", "Error!!!! El valor ingresado es incorrecto")
        matriz = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                matriz[i][j] = IngresoNumeroValido(blanco+blanco2+f"M[{i}][{j}] = ", "El valor ingreso no es permitido")
        if opcion1 == "1":
            posi = int(IngresoNumeroValido(blanco+blanco2+"Ingrese posicion de matriz: ", "Posicion no permitida")) - 1
            while posi+1 > len(MM) or posi == -1:
                print(rojo + "no existe la posición dada intentelo otra vez:")
                posi = int(IngresoNumeroValido(blanco + blanco2 + "Ingrese posicion de matriz: ", "Posicion no permitida")) - 1

            MM[posi] = matriz

        if opcion1 == "2":
            MM.append(matriz)
        return crearMatriz(MM, a - 1,opcion1)

#Funcion que crea matriz cuando no hay memoria.json

def adiciona_matrices(MM,MM1,a):
    if a==0:
        MM=MM1
        return MM
    else:

        m = IngresoNumeroValido(blanco+blanco2+"Filas1: ", "Error!!!! El valor ingresado es incorrecto")
        n = IngresoNumeroValido(blanco+blanco2+"Columnas1: ", "Error!!!! El valor ingresado es incorrecto")
        matriz = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                matriz[i][j] =IngresoNumeroValido(blanco+blanco2+f"M[{i}][{j}] = ","El valor ingreso no es permitido")
        posi = int(IngresoNumeroValido("Ingrese posicion de matriz: ", "Posicion no permitida")) - 1

        while posi + 1 > len(MM1) or posi == -1:
            print(rojo + "no existe la posición dada intentelo otra vez:")
            posi = int(IngresoNumeroValido(blanco + blanco2 + "Ingrese posicion de matriz: ", "Posicion no permitida")) - 1

        MM1[posi] = matriz

        return adiciona_matrices(MM,MM1,a-1)

# Funcion en bucle donde se encuentran las opciones para poder operar las matrices

def operarMatrices ():
    while True:
        print(verde2+"OPERAR MATRICES")
        print(azul +"[1] Suma de matrices",end="         ")
        print("[2] Resta de matrices",end="                ")
        print("[3] Multiplicacion de matrices")
        print("[4] Trasposición de matriz",end="   ")
        print("[5] Multiplicar matriz por escalar",end="   ")
        print("[6] Resolver laberinto",end="           ")
        print("[7] Salir")
        opcion = input(blanco+blanco2+"Seleccione opción: ")
        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
            return opcion
        else:
            print(rojo+"Opción no válida!!! Vuelva a intentarlo")

# Funcion bucle donde se muestran todas las matrices o una matriz especifica

def MostrarMatrices ():
    while True:
        print(verde2+"MOSTRAR MATRICES ")
        print(azul +"[1] Lista de matrices guardadas",end="   ")
        print("[2] Mostrar contenido de una matriz ",end="   ")
        print("[3] Salir")
        opcion = input(blanco+blanco2+"Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print(rojo+"Opción no válida!!! Vuelva a intentarlo")

# Funcion que valida que un caracter sea un numero entero

def IngresoNumeroValido(mensajeUsuario, mensajeError):
    while(not (numero:=input(mensajeUsuario)).isdigit()):
        print(mensajeError)
    return int(numero)
# Funcion que agrega matrices al archivo json
def mandar_a_memoria(matriz):
    archivo2 = open("memoria.json", "w")
    archivo2.write(json.dumps(matriz))
    archivo2.write("\n")
    archivo2.close()
# Funcion que corre el archivo .json para que se puedan leer las matrices guardadas
def cargar_memoria():
        archivo = open("memoria.json", "r")
        mm=[]
        for linea in archivo:
            x = json.loads(linea)
            for matriz in range(len(x)):
                mm.append(x[matriz])
        return mm
#Guarda temporalmente las matrices y cuando se cierra se guardan la matrices en el archivo .json
def memori_de_matrices():
    n =IngresoNumeroValido(blanco+blanco2+"Por favor ingrese el numero de matrices que quiere añadir en la memoria:",
                                  "Error!!!! El valor ingresado es incorrecto")
    MemoriaMatrices = [[]] * n
    return MemoriaMatrices
#Funcion que muestra la lista de matrices ordenadas
def matriz_ordenada_listado(matriz):
    for k in matriz:
        print("\n")
        b=""
        for i in range(len(k)):
            for j in range(len(k[0])):
                b +=str(k[i][j])+"\t"
            print(b)
            b=""
    return b
#Funcion que muestra una sola matriz ordenada
def matriz_ordenada_solo(matriz):
    b = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            b += str(matriz[i][j]) + "\t"
        print(b)
        b = ""
    return b
