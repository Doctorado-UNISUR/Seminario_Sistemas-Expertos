#Mandamos llamar a la libreria de experta 
#para utilizar sus opalabras clave para el desarrollo del sistema de reglas basado en reglas
from experta import *

# Definición de una clase que hereda de 'Fact', que es una estructura de datos
# utilizada para almacenar hechos en el sistema experto. En este caso, los hechos
# serán las respuestas proporcionadas por el usuario.
class RespuestaTEA(Fact):
    """Información de las respuestas"""
    pass

# Definición de la clase 'SistemaExpertoTEA' que hereda de 'KnowledgeEngine',
# la cual es responsable de procesar las reglas y los hechos en el sistema experto.
class SistemaExpertoTEA(KnowledgeEngine):

    # Definición de varias reglas (usando decoradores) que especifican condiciones
    # bajo las cuales ciertos hechos deben ser declarados en el sistema. En este caso,
    # las reglas especifican combinaciones de respuestas que indican la ausencia de rasgos de TEA.
    
    @Rule(RespuestaTEA(A6=0, A7=0, A2=0, A3=0))
    @Rule(RespuestaTEA(A9=0, A2=0, A6=0, A4=0, A7=0))
    @Rule(RespuestaTEA(A5=0, A2=0, A6=0, A10=0, A3=0))
    @Rule(RespuestaTEA(A9=0, A1=0, A5=0, A4=0, A2=0))
    @Rule(RespuestaTEA(A9=0, A7=0, A10=0))
    @Rule(RespuestaTEA(A6=0, A7=0, A1=0, A4=0))
    @Rule(RespuestaTEA(A6=0, A9=0, A2=0, A3=0))
    @Rule(RespuestaTEA(A9=0, A1=0, A5=0, A10=0))
    def rasgos_presentes(self):
        # Si alguna de las reglas anteriores es verdadera, se declara un hecho (Fact) indicando 
        # que el usuario no presenta rasgos de TEA.
        self.declare(Fact(TEA=True))

    # Esta regla se activa cuando se ha declarado el hecho 'TEA=True', lo que indica que 
    # el diagnóstico es "No Existen rasgos de TEA".
    @Rule(Fact(TEA=True))
    def diagnostico_negativo(self):
        self.resultado = "No Existen rasgos de TEA"

    # Esta regla se activa si no se ha declarado el hecho 'TEA=True', lo que implica que
    # el diagnóstico es "Existen rasgos de TEA".
    @Rule(NOT(Fact(TEA=True)))
    def diagnostico_positivo(self):
        self.resultado = "Existen rasgos de TEA"
   
    # Método para ejecutar el sistema experto. Recibe las respuestas del usuario, 
    # resetea el motor de inferencia, declara los hechos (las respuestas) y 
    # ejecuta las reglas para obtener el diagnóstico.
    def ejecutar(self, respuestas):
        self.reset()  # Resetea la máquina de inferencia para eliminar hechos previos.
        self.declare(RespuestaTEA(**respuestas))  # Declara los hechos basados en las respuestas.
        self.run()  # Ejecuta las reglas para generar un diagnóstico.
        return self.resultado  # Retorna el resultado del diagnóstico.
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
