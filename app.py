#Se importa de la libreria Flask para crear una instancia de la aplicación web en Flask.
#render_template se usa para renderizar plantillas HTML. 
#Permite pasar datos desde el backend (Python) a las plantillas HTML.
#request contiene la información de la solicitud HTTP realizada por el cliente. 
#Permite acceder a los datos del formulario enviado, así como a otros detalles de la solicitud.

from flask import Flask, render_template, request
from expert_system import SistemaExpertoTEA

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta principal de la aplicación
@app.route('/', methods=['GET', 'POST'])
def index():
	# Maneja la solicitud cuando se envía el formulario
    if request.method == 'POST':
        # Inicializa un diccionario de respuestas con valores predeterminados de 0.
        respuestas = {
            'A1': 0,
            'A2': 0,
            'A3': 0,
            'A4': 0,
            'A5': 0,
            'A6': 0,
            'A7': 0,
            'A9': 0,
            'A10': 0,
        }

        # Actualiza el diccionario con las respuestas del formulario, si están presentes
        for key in respuestas.keys():
            if key in request.form:
                respuestas[key] = int(request.form[key]) # Convierte la respuesta a entero

        # Crea una instancia del sistema experto TEA
        sistema = SistemaExpertoTEA()
        # Ejecuta el sistema experto con las respuestas proporcionadas y obtiene el resultado
        resultado = sistema.ejecutar(respuestas)
        # Renderiza la plantilla 'resultado.html' con el resultado del sistema experto
        return render_template('resultado.html', resultado=resultado)
    # Renderiza la plantilla 'index.html' para solicitudes GET (o POST si no hay datos)
    return render_template('index.html')

# Ejecuta la aplicación Flask en modo de depuración si este archivo es el principal
if __name__ == '__main__':
    app.run(debug=True)
