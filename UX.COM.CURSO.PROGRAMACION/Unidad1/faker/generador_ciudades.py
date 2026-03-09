from faker import Faker
fake = Faker('es_MX')

#1. Declaración de un vector vacío
ciudades_la = []

#2.Operación de llenado(ciclo)
for _ in range (5):
    ciudades_la.append(fake.city())

#3.Escritura de arreglos (Mostrar resultados)
print("\n--- DATASET DE CIUDADES GENERADO ---")
for i in range(len(ciudades_la)):
    print(f"Registro {i+1}: {ciudades_la[i]}")