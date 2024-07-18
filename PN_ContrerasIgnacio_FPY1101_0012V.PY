# Examen Transversal FPY1101
import random
import csv

# Listas de nombres y apellidos
nombres = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Miguel", "Isabel", "Francisco", "Elena"]
apellidos = ["Perez", "Garcia", "Lopez", "Martinez", "Rodriguez", "Hernandez", "Sanchez", "Gomez", "Diaz", "Fernandez"]

# Generar 10 empleados con nombres y apellidos aleatorios
empleados = [f"{random.choice(nombres)} {random.choice(apellidos)}" for _ in range(10)]


sueldos = {empleado: random.randint(300000, 2500000) for empleado in empleados}

def clasificar_sueldos():
    clasificados = sorted(sueldos.items(), key=lambda x: x[1], reverse=True)
    for i, (nombre, sueldo) in enumerate(clasificados, start=1):
        print(f"{i}. {nombre}: ${sueldo}")

def ver_estadisticas():
    for nombre, sueldo in sueldos.items():
        clasificacion = "Alto" if sueldo > 1500000 else "Medio" if sueldo > 750000 else "Bajo"
        print(f"{nombre}: ${sueldo} - Clasificación: {clasificacion}")

def reporte_sueldos_csv():
    with open('reporte_sueldos.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Sueldo Base', 'Desc. Salud', 'Desc. AFP', 'Sueldo Liquido'])
        for nombre, sueldo_base in sueldos.items():
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            escritor.writerow([nombre, sueldo_base, desc_salud, desc_afp, sueldo_liquido])
    print("Reporte de sueldos , exportados.")

def mostrar_mensaje_final():
    print("Programa finalizado.")
    print("Desarrollado por Ignacio Contreras")
    print("RUT : 21.352.995-1")

def menu():
    while True:
        print("\nMenú:")
        print("1. Clasificar sueldos")
        print("2. Ver estadísticas")
        print("3. Reporte de sueldos")
        print("4. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clasificar_sueldos()
        elif opcion == "2":
            ver_estadisticas()
        elif opcion == "3":
            reporte_sueldos_csv()
        elif opcion == "4":
            mostrar_mensaje_final()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()