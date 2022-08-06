import sqlite3

#from palabras import Palabras

con = sqlite3.connect(':memory:') 

c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Diccionario (
            palabra         TEXT    NOT NULL,
            significado     TEXT    NOT NULL,
            UNIQUE(palabra, significado)
        )""")    #UNIQUE(palabra, significado) para que no haya palabras ni significados duplicados dentro de la bd

def insertar(pal):
    with con:
        c.execute("INSERT INTO diccionario VALUES (:palabra, :significado)",
        {'palabra': pal.palabra, 'significado': pal.significado})

def insert_pal(pal, significado): #to add a new word to de dictionary
    with con:
        c.execute("INSERT INTO Diccionario VALUES (:palabra, :significado)",
         {'palabra': pal.palabra, 'significado': pal.significado})


def eliminar_pal(pal):
    with con:
        c.execute("""DELETE from diccionario WHERE palabra = :palabra""",
                    {'palabra': pal.palabra, 'significado': pal.significado})


def cambiar_pal(pal):
    with con:
        c.execute("""UPDATE diccionario SET palabra = :palabra
                    WHERE significado = :significado""",
                    {'palabra': pal.palabra, 'significado': pal.significado})


def edit_significado(pal, significado):
    with conn:
        c.execute("""UPDATE diccionario SET significado = :significado
                    WHERE palabra = :palabra""",
                    {'palabra': pal.palabra, 'significado': pal.significado})

def menu():
    print("""1: Elige una de las siguientes opciones escribiendo uno de los numeros:
            1: Ver listado de palabras
            2: Edita significado de una de las palabras existentes
            3: Agregar nueva palabra
            4: Editar palabra existente
            5: Buscar significado de palabra
            6: Salir del programa
            """)
    num = input("Opcion: ")
    while (num != 6):
        un = ""
        do = ""

        if num == 1: #Ver listado de palabras

            return print(c.fetchall())
            con.commit()


        if num == 2:  #Editar significado de una de las palabras
            print("Que palabra desea editar su significado?")
            un = input("Palabra: ")
            do= input("Nuevo significado: ")

            edit_significado(un, do)
            con.commit()


        if num == 3:  #Agregar nueva palabra
            print("Nueva Palabra")
            un = input("Palabra: ")
            do = input("Su Significado: ")

            insert_pal(un, do)
            con.commit()


        if num == 4:  #Editar una de las palabras
            print("Editar una de las palabras")
            un = input("Palabra: ")

            cambiar_pal(un)


        if num == 5:  #Buscar significado de palabras
            print("Buscar significado de palabra")
            un = input("Palabra: ")

            print()

menu()

con.commit()

con.exit()