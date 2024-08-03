import os
import platform

from laboratorio_poo import (
    Paper,
    Ponencia,
    GestionInvestigaciones,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print("<<<<<<<<<<<<<<<< Bienvenid@ al SiGIn >>>>>>>>>>>>>>>>")
    print("<<<<<<< Sistema de Gestión de Investigaciones >>>>>>>")
    print("======================================================")
    print('1. Agregar Paper')
    print('2. Agregar Ponencia')
    print('3. Buscar Investigacion por Título') #Podría hacerse también por autor, tema o año
    print('4. Eliminar Investigacion por Título')
    print('5. Mostrar Todas las Investigaciones')
    print('6. Salir')
    print('======================================================')

def agregar_investigacion(gestion, tipo_investigacion):
    try:
        autor = input('Ingrese nombre y apellido del autor de la investigación: ')
        titulo = input('Ingrese título de la investigación: ')
        ciudad = input('Ingrese ciudad de la investigación: ')
        año = int(input('Ingrese año de la investigación: '))
        url = input('Ingrese url de la investigación: ')

        if tipo_investigacion == '1':
            revista_libro = input('Ingrese Revista o Libro en el que se publicó la investigación: ')
            editorial = input('Ingrese editorial en la que se publica la investigación: ')
            investigacion = Paper(autor, titulo, ciudad, año, url, revista_libro, editorial)
        elif tipo_investigacion == '2':
            evento = input('Ingrese evento en que se expuso la investigación: ')
            investigacion = Ponencia(autor, titulo, ciudad, año, url, evento)
        else:
            print('Opción inválida')
            return

        gestion.crear_investigacion(investigacion)
        input('Presione ENTER para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')

def buscar_investigacion_por_titulo(gestion):
    titulo = input('Ingrese el titulo a buscar: ')
    gestion.leer_investigacion(titulo)
    input('Presione enter para continuar...')

def eliminar_investigacion_por_titulo(gestion):
    titulo = input('Ingrese el titulo de la investigación a eliminar: ')
    gestion.eliminar_investigacion(titulo)
    input('Presione enter para continuar...')

def mostrar_todas_las_investigaciones(gestion):
    print('=============== Listado completo de Investigaciones ==============')
    for investigacion in gestion.leer_datos().values():
        if 'editorial' in investigacion:
            print(f"{investigacion['titulo']} de {investigacion['autor']} | Publicado en {investigacion['revista_libro']}")
        else:
            print(f"{investigacion['titulo']} de {investigacion['autor']} | Expuesto en {investigacion['evento']}")
    print('==================================================================')
    input('Presione enter para continuar...')

if __name__ == "__main__":
    archivo_investigaciones = 'investigaciones_db.json'
    gestion = GestionInvestigaciones(archivo_investigaciones)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1' or opcion == '2':
            agregar_investigacion(gestion, opcion)
        
        elif opcion == '3':
            buscar_investigacion_por_titulo(gestion)

        elif opcion == '4':
            eliminar_investigacion_por_titulo(gestion)

        elif opcion == '5':
            mostrar_todas_las_investigaciones(gestion)

        elif opcion == '6':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-6)')
        

