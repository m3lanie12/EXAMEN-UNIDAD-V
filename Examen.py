estudiantes = int(input("¿Cuántos estudiantes hay? "))
materias = int(input("¿Cuántas materias tiene el grupo? "))

matriz = []

print("\n--- Captura de calificaciones ---")
for i in range(estudiantes):
    fila = []
    print(f"\nEstudiante {i+1}:")
    for j in range(materias):
        cal = float(input(f"  Calificación en materia {j+1}: "))
        while cal < 0 or cal > 100:
            print("  Error: ingrese una calificación entre 0 y 100.")
            cal = float(input(f"  Calificación en materia {j+1}: "))
        fila.append(cal)
    matriz.append(fila)

prom_estudiantes = []
for fila in matriz:
    prom_estudiantes.append(sum(fila) / materias)

prom_materias = []
for col in range(materias):
    suma = 0
    for fila in matriz:
        suma += fila[col]
    prom_materias.append(suma / estudiantes)

max_cal = max([max(fila) for fila in matriz])
min_cal = min([min(fila) for fila in matriz])

print("\n--- Matriz de calificaciones ---")
for fila in matriz:
    print(fila)

print("\n--- Resultados ---\n")

print("Promedio por estudiante:")
for i, prom in enumerate(prom_estudiantes, start=1):
    print(f"  Estudiante {i}: {prom:.2f}")

print("\nPromedio por materia:")
for j, prom in enumerate(prom_materias, start=1):
    print(f"  Materia {j}: {prom:.2f}")

print(f"\nCalificación más alta: {max_cal}")
print(f"Calificación más baja: {min_cal}")

print("\nFin del programa.")
