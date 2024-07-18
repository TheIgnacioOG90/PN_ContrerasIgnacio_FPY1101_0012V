# Examen Transversal FPY1101

import ramdon 
import csv

#Listas de nombres y apellidos
nombres = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Miguel", "Isabel", "Francisco", "Elena"]
apellidos = ["Perez", "Garcia", "Lopez", "Martinez", "Rodriguez", "Hernandez", "Sanchez", "Gomez", "Diaz", "Fernandez"]

# Generar 10 empleados con nombre y apellido aleatorio
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