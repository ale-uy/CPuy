import sqlite3


def postales(x):
    if x.lower() == "si":
        c = input("\nEscriba un Codigo Postal: ")
        while not isinstance(c, int):
            try:
                c = int(c)
                cp = (c,)
                database = sqlite3.connect("db")
                cursor = database.cursor()
                cursor.execute("SELECT Departamento, Localidad FROM Localidades WHERE CodigoPostal = ?", cp)
                log = cursor.fetchall()
                if len(log) > 0:
                    print("\nEl Codigo postal es del departamento de:\n")
                    print(f"* {log[0][0]}\n")
                    print("En las localidades/barrios:\n")
                    for l in log:
                        print(f"* {l[-1]}")
                else:
                    print("\nEl codigo postal introducido no existe...")
                x = input("\nDesea buscar otro Codigo Postal? -> (si/no): ")
                postales(x)
            except ValueError:
                c = input("\nEscriba el Codigo Postal de nuevo: ")
            except Exception as e:
                print(e)
                postales()
    elif x.lower() == "no":
        print("\nGracias por usar el buscador\n")
    else:
        x = input("\nSolo escriba SI o NO por favor: ")
        postales(x)
        
postales("si")        

input("ENTER para salir")
