'''
DESAFÍO 1: Sistema de Gestión de un Repositorio de Investigaciones Académicas

OBJETIVO: Desarrollar un sistema para gestionar un repositorio de investigaciones académicas.

REQUISITOS:
    • Crear una clase base Investigacion con los siguientes atributos:
        - Autor
        - Título
        - ciudad
        - Año
        - URL
    • Definir clases derivadas para diferentes tipos de investigaciones con atributos y métodos específicos:
        - Paper: Editorial, Revista/Libro
        - Ponencia: Evento
    • Implementar operaciones CRUD para gestionar las investigaciones.
    • Manejar errores con bloques try-except para validar entradas y gestionar excepciones (por ejemplo, url negativo, longitud autor, etc).
    • Persistir los datos en archivo JSON.
'''
import json

class Investigacion:
    def __init__(self, autor, titulo, ciudad, año, url):
        self.__autor = autor
        self.__titulo = titulo
        self.__ciudad = ciudad
        self.__año = self.validar_año(año)
        self.__url = url

    @property
    def autor(self):
        return self.__autor.capitalize()
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ciudad(self):
        return self.__ciudad.capitalize()
    
    @property
    def año(self):
        return self.__año
    
    @property
    def url(self):
        return self.__url

    def validar_año(self, año):
        try:
            año_num = int(año)
            if len(str(año)) != 4:
                raise ValueError("ERROR: El año debe tener 4 dígitos")
            if año_num <= 0:
                raise ValueError("ERROR: El año debe ser un número positivo")
            return año_num
        except ValueError:
            raise ValueError("ERROR: El año debe ser un número positivo y estar compuesto por 4 dígitos")

    def to_dict(self):
        return {
            "autor": self.autor,
            "titulo": self.titulo,
            "ciudad": self.ciudad,
            "año": self.año,
            "url": self.url
        }

    def __str__(self):
        return f"{self.autor} {self.titulo}"

class Paper(Investigacion):
    def __init__(self, autor, titulo, ciudad, año, url, revista_libro, editorial):
        super().__init__(autor, titulo, ciudad, año, url)
        self.__revista_libro = revista_libro
        self.__editorial = editorial

    @property
    def revista_libro(self):
        return self.__revista_libro
    
    @property
    def editorial(self):
        return self.__editorial

    def to_dict(self):
        data = super().to_dict()
        data["revista_libro"] = self.revista_libro
        data["editorial"] = self.editorial
        return data

    def __str__(self):
        return f"{super().__str__()} - Revista/Libro: {self.revista_libro}"

class Ponencia(Investigacion):
    def __init__(self, autor, titulo, ciudad, año, url, evento):
        super().__init__(autor, titulo, ciudad, año, url)
        self.__evento = evento

    @property
    def evento(self):
        return self.__evento

    def to_dict(self):
        data = super().to_dict()
        data["evento"] = self.evento
        return data

    def __str__(self):
        return f"{super().__str__()} - Evento: {self.evento}"

class GestionInvestigaciones:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_investigacion(self, investigacion):
        try:
            datos = self.leer_datos()
            titulo = investigacion.titulo
            if not str(titulo) in datos.keys():
                datos[titulo] = investigacion.to_dict()
                self.guardar_datos(datos)
                print(f"Investigacion cargada correctamente")
            else:
                print(f"Ya existe investigacion con el titulo '{titulo}'.")
        except Exception as error:
            print(f'Error inesperado al crear investigacion: {error}')

    def leer_investigacion(self, titulo):
        try:
            datos = self.leer_datos()
            if titulo in datos:
                investigacion_data = datos[titulo]
                if 'revista_libro' in investigacion_data:
                    investigacion = Paper(**investigacion_data)
                else:
                    investigacion = Ponencia(**investigacion_data)
                print(f'Investigacion encontrada con el título {titulo}')
            else:
                print(f'No se encontró investigación con el título {titulo}')

        except Exception as e:
            print('Error al leer investigacion: {e}')

    def eliminar_investigacion(self, titulo):
        try:
            datos = self.leer_datos()
            if str(titulo) in datos.keys():
                 del datos[titulo]
                 self.guardar_datos(datos)
                 print(f'La investigación titulada {titulo} ha sido eliminada correctamente')
            else:
                print(f'No se encontró una investigacion con el título:{titulo}')
        except Exception as e:
            print(f'Error al eliminar la investigacion: {e}')