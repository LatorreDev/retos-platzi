#!/usr/bin/env python3
# Retos platzi parte 1


def linea_div():
    print("\n")
    print("***************************")
    print("\n")


# Hola mundo

linea_div()

print("Hola mundo")

linea_div()

# Hola nombre y apellido
nombre = input("Cual es tu nombre?: ")
apellido = input("Cual es tu apellido?: ")
print(f"Hola, {nombre} {apellido}")

linea_div()

# Categorias Platzi
categorias = ["[Desarrollo e ingenieria]", "[Diseño y UX]", "[Marketing]",
              "[Negocios y Emprendieminto]", "[Produccion Audiovisual]",
              "[Crecimiento Profesional]"]
print(f"Platzi cuenta con cursos de: ")
for elements in categorias:
    print(elements)

linea_div()
