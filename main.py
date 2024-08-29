# Importa la clase SistemaExpertoTEA del módulo correspondiente.
from expert_system import SistemaExpertoTEA

# Función para capturar las respuestas del usuario a una serie de preguntas.
def capturar_respuestas():
    # Diccionario que mapea cada pregunta con su clave identificadora (A1, A2, etc.)
    preguntas = {
        "A1": "A1 ¿Su hijo lo mira cuando lo llama por su nombre?",
        "A2": "A2 ¿Qué tan fácil es para usted tener contacto visual con su hijo?",
        "A3": "A3 ¿Su hijo señala para indicar que quiere algo? (por ejemplo, un juguete que está fuera de alcance)",
        "A4": "A4 ¿Su hijo señala compartir interés con usted? (p. ej., punteando en una vista interesante)",
        "A5": "A5 ¿Su hijo finge? (por ejemplo, cuidar muñecas, hablar por un teléfono de juguete)",
        "A6": "A6 ¿Su hijo sigue hacia donde usted está mirando?",
        "A7": "A7 Si usted u otra persona de la familia está visiblemente molesta, ¿su hijo muestra signos de decaimiento para consolarlo? (por ejemplo, acariciar el cabello, abrazarlos)",
        "A9": "A9 ¿Tu hijo utiliza gestos sencillos? (por ejemplo, decir adiós con la mano)",
        "A10": "A10 ¿Su hijo mira fijamente a la nada sin un propósito aparente?"
    }

    respuestas = {}  # Diccionario para almacenar las respuestas del usuario.
    
    # Itera sobre cada pregunta en el diccionario.
    for key, pregunta in preguntas.items():
        while True:  # Bucle para asegurar que la respuesta sea válida ('Si' o 'No').
            # Solicita al usuario que responda la pregunta.
            respuesta = input(f"{pregunta} (Si/No): ").strip().lower()
            # Verifica si la respuesta es 'si' o 'no'.
            if respuesta in ["si", "no"]:
                # Almacena la respuesta en el diccionario con 1 para 'si' y 0 para 'no'.
                respuestas[key] = 1 if respuesta == "si" else 0
                break  # Sale del bucle si la respuesta es válida.
            else:
                # Solicita una respuesta válida si el usuario no ingresó 'si' o 'no'.
                print("Por favor, responde con 'Si' o 'No'.")

    return respuestas  # Retorna el diccionario con todas las respuestas capturadas.

# Función principal que ejecuta el test de detección de rasgos TEA.
def ejecutar_test():
    while True:  # Bucle principal que permite repetir el test si el usuario lo desea.
        print("\nPor favor, responde las siguientes preguntas:")
        respuestas = capturar_respuestas()  # Captura las respuestas del usuario.
        sistema = SistemaExpertoTEA()  # Crea una instancia del sistema experto.
        resultado = sistema.ejecutar(respuestas)  # Ejecuta el sistema experto con las respuestas capturadas.
        print(f"\nResultado: {resultado}\n")  # Muestra el resultado del diagnóstico.

        # Pregunta al usuario si desea realizar el test nuevamente.
        repetir = input("¿Quieres realizar el test de nuevo? (Si/No): ").strip().lower()
        if repetir != "si":  # Si la respuesta no es 'si', se sale del bucle y finaliza el programa.
            print("Gracias por utilizar el sistema experto.")
            break  # Sale del bucle y termina el programa.

# Punto de entrada del programa. Ejecuta la función 'ejecutar_test' cuando el script es ejecutado directamente.
if __name__ == "__main__":
    ejecutar_test()
