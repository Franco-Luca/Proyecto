#Franco Luca 31790135
#Tulio Franco 31748581

import re
import string

def calcular_puntaje_seguridad(password, patrones):
    puntaje = len(password)
    # existencia de letras minúsculas
    if any(char.islower() for char in password):
        puntaje += 1
    # existencia de números
    if any(char.isdigit() for char in password):
        puntaje += 1
    # existencia de letras mayúsculas
    if any(char.isupper() for char in password):
        puntaje += 1
    # existencia de símbolos
    if any(char in string.punctuation for char in password):
        puntaje += 3
    # símbolo adicional al primero
    puntaje += 2 * (len([char for char in password if char in string.punctuation]) - 1)
    # secuencia o patrón obvio
    for patron in patrones:
        if re.search(patron, password):
            puntaje -= 5
    return puntaje

def clasificar_seguridad(puntaje):
    if puntaje <= 15:
        return "Debil"
    if puntaje <= 20:
        return "Moderada"
    if puntaje <= 35:
        return "Buena"
    if puntaje <= 100:
        return "Excelente"
    return "Impenetrable"

def ordenamiento_burbuja_descendente(lista_tupla):
    n = len(lista_tupla)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_tupla[j][1] < lista_tupla[j+1][1]:
                lista_tupla[j], lista_tupla[j+1] = lista_tupla[j+1], lista_tupla[j]
    return lista_tupla

def ordenar_seguridad(passwords, patrones):
    passwords_puntajes = [(password, calcular_puntaje_seguridad(password, patrones)) for password in passwords]
    passwords_puntajes = ordenamiento_burbuja_descendente(passwords_puntajes)
    return passwords_puntajes

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read().splitlines()

def exportar_archivo(passwords_puntajes, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for password, puntaje in passwords_puntajes:
            archivo.write(f'{password} | {clasificar_seguridad(puntaje)} | {puntaje}\n')

def main():
    passwords = leer_archivo('contraseñas.txt')
    patrones = leer_archivo('patrones.txt')
    passwords_puntajes = ordenar_seguridad(passwords, patrones)
    exportar_archivo(passwords_puntajes, 'resultados.txt')

def pedir_contraseña(patrones):
    nueva_contraseña = input("Ingrese una contraseña: ")
    puntaje = calcular_puntaje_seguridad(nueva_contraseña, patrones)
    print(f'{nueva_contraseña} | {clasificar_seguridad(puntaje)} | {puntaje}\n')

pedir_contraseña("patrones.txt")

if __name__ == '__main__':
    main()

# Importar el módulo subprocess
import subprocess

# Especificar el nombre del archivo a ejecutar y leer
archivo = "resultados.txt"

# Ejecutar el archivo usando subprocess.run()
subprocess.run(["python", archivo])

# Abrir el archivo en modo de lectura
f = open(archivo, "r")

# Leer el contenido del archivo
contenido = f.read()

# Cerrar el archivo
f.close()

# Imprimir el contenido del archivo
#print(contenido)
