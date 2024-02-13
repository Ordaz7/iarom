import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Definir respuestas a saludos
respuestas_saludos = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "¿cómo estás?": "Estoy bien, gracias. ¿Y tú?",
    "buenos días": "¡Buenos días!",
    "buenas tardes": "¡Buenas tardes!",
    "buenas noches": "¡Buenas noches!",
    "¿qué tal?": "Hola, ¿cómo estás?",
    "saludos": "Saludos. ¿En qué puedo ayudarte hoy?",
    "¿hay alguien ahí?": "¡Hola! Sí, estoy aquí para ayudarte.",
    "¿qué hay de nuevo?": "No mucho, ¿en qué puedo asistirte?",
    "¡hey!": "¡Hola! ¿Cómo puedo ayudarte?",
    "¿cómo va todo?": "Todo va bien, gracias. ¿En qué puedo ayudarte?"
}

# Definir respuestas a otras preguntas
respuestas_otras_preguntas = {
    "¿quién eres?": "Soy un programa de inteligencia artificial creado para ayudarte.",
    "¿cuál es tu propósito?": "Mi propósito es asistirte proporcionando información y ayuda en diversos temas.",
    "¿cómo puedo aprender programación?": "Puedes comenzar aprendiendo un lenguaje como Python y practicando con proyectos pequeños.",
    "¿qué tiempo hace hoy?": "Lo siento, no tengo acceso a información en tiempo real. Te recomiendo consultar un servicio meteorológico en línea.",
    "¿cuál es tu creador?": "Mi creador se llama Ricardo Ordaz.",
    "¿cómo te llamas?": "Puedes llamarme Asistente AI.",
    "¿en qué año fuiste creado?": "Fui creado en 2021.",
    "¿cuál es tu color favorito?": "No tengo preferencias de color, ya que soy un programa de software.",
    "¿puedes decir chistes?": "Sí, aquí tienes uno: ¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿cuántos dedos tienes?": "No tengo dedos, ya que soy un programa de computadora.",
    "¿puedes aprender de mí?": "Actualmente, mi capacidad de aprendizaje es limitada. Puedo proporcionar información y ayuda en función de mi programación inicial.",
    "¿eres humano?": "No, soy una inteligencia artificial creada por humanos."
}

# Función para procesar la entrada del usuario y dar una respuesta
def procesar_entrada(entrada):
    # Convertir a minúsculas y tokenizar
    tokens = word_tokenize(entrada.lower())

    # Eliminar stopwords
    stop_words = set(stopwords.words('spanish'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]

    # Buscar respuesta
    respuesta = respuestas_saludos.get(' '.join(tokens), None)
    if respuesta is None:
        respuesta = respuestas_otras_preguntas.get(' '.join(tokens), None)

    if respuesta is None:
        respuesta = procesar_operaciones(tokens)

    return respuesta if respuesta else "Lo siento, no entiendo la pregunta. ¿Puedes ser más específico?"

# Función para procesar operaciones matemáticas
def procesar_operaciones(tokens):
    if 'sumar' in tokens or 'restar' in tokens:
        numeros = [int(token) if token.isdigit() or (token[0] == '-' and token[1:].isdigit()) else None for token in tokens]
        numeros = [numero for numero in numeros if numero is not None]

        if 'sumar' in tokens:
            return f"La suma de los números es: {sum(numeros)}" if numeros else "No ingresaste números para sumar."
        elif 'restar' in tokens:
            return f"La resta de los números es: {numeros[0] - sum(numeros[1:])}" if len(numeros) >= 2 else "No ingresaste suficientes números para restar."

    return None

# Ejecutar el programa
if __name__ == "__main__":
    print("Bienvenido al Asistente de Inteligencia Artificial.")
    print("Escribe 'adiós' en cualquier momento para salir.")

    while True:
        entrada_usuario = input("Usuario: ")

        # Salir del bucle si el usuario escribe "adiós"
        if entrada_usuario.lower() == 'adiós':
            print("Hasta luego. ¡Que tengas un buen día!")
            break

        # Procesar entrada y dar respuesta
        respuesta_ia = procesar_entrada(entrada_usuario)
        print("IA:", respuesta_ia)
