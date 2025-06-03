# ---------------------------------------------
#           TheoryBot - Tu Compañero Musical
#           Desarrollado por Santiago Tigreros
# ---------------------------------------------

"""
TheoryBot es un chatbot diseñado para ayudarte a crear tus propias canciones. 
Con este asistente musical, podrás explorar tonalidades, progresiones armónicas, 
y estructuras de canciones para transmitir emociones o sensaciones específicas.

Funciones principales de TheoryBot:
1. Sugerencias de tonalidades:
   - Escoge la tonalidad ideal para tu canción según la emoción que desees transmitir.

2. Progresiones armónicas:
   - Genera progresiones de acordes que encajen con el sentimiento o estilo que buscas.

3. Estructuras de canciones:
   - Proporciona posibles estructuras para organizar tu canción (verso, coro, puente, etc.).

4. Personalización emocional:
   - Adapta las recomendaciones de acordes y estructuras basándote en la emoción o género musical.


Nota importante:
Para usar TheoryBot correctamente y aprovechar al máximo sus funciones, 
es necesario tener conocimientos básicos de teoría musical, como:
- Qué son las escalas y tonalidades.
- Cómo se forman los acordes.
- La relación entre acordes y progresiones.
- Como se estructuran las canciones.

Notas:
- Hay linas que no tienen comentario porque previamente se explicaron y repetir lo mismo cada vez que sale no es eficiente a la hora de programar, si hay alguna duda, comuniquese conmigo.
¡Comienza a crear música con TheoryBot!
"""

############################################################################################################################################################

def progresiones_emociones():
    """
    # Progresiones de acordes y emociones asociadas
    """
    # Hacemos unas listas con progresiones y sus sentimientos asociados
    progresiones_tristes = ["i - VI - III - VII", "i - III - VII - iv", "i - VII - VI - V", "i - VI - III -V", "i - VI - VII - III"]
    progresiones_felices = ["I - IV - V - I", "I - V - vi - IV", "I - V - vi - iii", "I - IV - vi - V", "I - V - vi - ii"]
    progresiones_relajadas = ["I - vi - IV - V", "I - V - vi - iii", "I - IV - vi - V", "I - IV - V - vi", "I - vi - IV - iii"]
    progresiones_euforicas = ["I - V - vi - IV", "IV - V - iii - vi", "I - iii - IV - V", "vi - IV - I - V", "I - IV - V - IV"]
    progresiones_sorprendidas = ["I - V - vi - IV", "IV - V - iii - vi", "I - iii - IV - V", "vi - IV - I - V", "I - IV - V - IV"]
    progresiones_enfadadas = ["i - VI - VII - i", "i - iv - V - i", "i - V - iv - VII", "vi - iv - I - V", "i - VII - VI - VII"]
    progresiones_epicas = ["I - IV - vi - V", "vi - IV - I - V", "I - V - IV - I", "IV - V - vi - IV", "I - V - iii - IV"]
    progresiones_romanticas = ["I - vi - ii - V", "I - IV - vi - iii", "vi - IV - I - V", "ii - V - I - vi", "I - V - vi - iii"]
    progresiones_jazz = ["ii - V - I", "I - vi - ii - V", "I - IV - iii - vi", "iii - vi - ii - V", "ii - V - iii - vi"]
    progresiones_blues = ["I - IV - I - V", "I - I - I - I", "IV - IV - I - I", "I - IV - I - I", "I - IV - I - IV"]

    # Asociamos las progresiones a las palabras clave, es un diccionario
    progresiones = {
        "triste": progresiones_tristes,
        "feliz": progresiones_felices,
        "relajada": progresiones_relajadas,
        "euforica": progresiones_euforicas,
        "sorprendida": progresiones_sorprendidas,
        "enfadada": progresiones_enfadadas,
        "epica": progresiones_epicas,
        "romantica": progresiones_romanticas,
        "jazz": progresiones_jazz,
        "blues": progresiones_blues
    }
    # he quitado todos lo acentos porque no se suele escrbiir con acentos en los programas.
    return progresiones
    
############################################################################################################################################################
def obtener_tonalidad():
    """
    # Pregunta al usuario la tonalidad de la canción y la valida.
    """
    # Esto es una variable que se le pide al usuario
    tonalidad = input("").strip() #Elimina espacios en la entrada (al final y al principio)
    
    # Estas son dos listas donde se valida la tonalidad
    notas_validas = ["C", "D", "E", "F", "G", "A", "B"] #Nombre de la escala
    tipos_validos = ["M", "m"] #Si la escala es mayor o menor
    try: #Asegurarse de que el usuario ha introducido una tonalidad válida
        nota = tonalidad[:-1]  # Todo menos el último carácter
        tipo = tonalidad[-1]   # Último carácter
        if nota in notas_validas and tipo in tipos_validos: #Si la nota y el tipo son válidos
            return tonalidad 
        else: 
            print("\033[1mTheoryBot\033[0m: Lo siento, esa tonalidad no es válida. Asegúrate de escribirla en el formato correcto (ej. \033[1mCM\033[0m, \033[1mAm\033[0m).\n") #La \n crea otra linia, es como un print() vacío.
            return obtener_tonalidad() # Volver a preguntar si la tonalidad no es válida
    except ValueError: #Si el usuario no ha introducido una tonalidad válida que no tiene nada que ver   
        print("\033[1mTheoryBot\033[0m: Lo siento, no entendí eso. Por favor, escribe la tonalidad en el formato correcto (ej. \033[1mCM\033[0m, \033[1mAm\033[0m).\n") #Aquí \033[1mCM\033[0m es para poner en negrita.
        return obtener_tonalidad() # Volver a preguntar si la tonalidad no es válida

############################################################################################################################################################
palabras_clave = ["quedo", "gusta", "progresion", "progresión", "tonalidad", "otra", "siguiente", "esta", "adios", "hasta luego", "gracias", "estructura", "esa"]

def detectar_palabras_clave(input_usuario, palabras_clave): 
    """
    # Detecta palabras clave en la entrada del usuario
    """
    for palabra in palabras_clave: #Recorremos la lista de palabras clave
        if palabra in input_usuario: #Si la palabra clave está en la entrada del usuario
            return palabra #La devolvemos, lo que quiere decir que la hemos detectado en la entrada del usuario y podemos actuar en consecuencia
    return None #Si no se ha detectado ninguna palabra clave, devolvemos None para indicar que no se ha detectado ninguna palabra clave

############################################################################################################################################################
def estructura_cancion():
    """
    # Le dice al usuario posibles estructuras de canciones dependiendo de la emoción
    """
    estructuras = { #Lista de estructuras de canciones (vaya tela a sido poner esto...)
        "triste": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "feliz": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "relajada": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "euforica": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "sorprendida": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "enfadada": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "epica": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo"],
        "romantica": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "jazz": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"],
        "blues": ["Intro - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Verso - Estribillo - Puente - Estribillo - Outro", "Intro - Verso - Estribillo - Verso - Estribillo - Puente - Estribillo - Outro"]  
    }
    return estructuras

############################################################################################################################################################


############################################################################################################################################################

def chatbot():
    """
    # Es el chat en sí
    Aquí es donde todas las variables de antes se juntan
    """
    ##############################################################################
    # Variables globales (puede que esten un poco desordenadas)

    pregunta_sensacion = False # Se ha respondido sobre la sensación
    tonalidad_actual = None # indicamos que la tonalidad inicialmente no se ha establecido
    progresiones = progresiones_emociones() # Progresiones de acordes y emociones asociadas
    indices_progresiones = {key: 0 for key in progresiones} # Índices para rastrear la progresión actual para cada emoción
    emocion_actual = None # Emoción actual del usuario
    nombre = None # Nombre del usuario
    pregunta_tonalidad = None # Pregunta sobre la tonalidad
    tonalidad_dicha = None # Tonalidad dicha por el usuario
    saludo_hecho = False # Saludo hecho por el bot
    pregunta_estructura = False # Estructura de la canción
    pregunta_estructura_gusta = False # Pregunta sobre si le gusta la estructura
    estructura_actual = None # Estructura actual de la canción
    propuesta_emocion = False # Propuesta de estructura, el chat a propuesto una estructura
    ##############################################################################
   
    print(f"\033[1mTheoryBot\033[0m: ¡Hola!, soy \033[1mTheoryBot\033[0m y estoy aquí para ayudarte ha crear tus canciones desde cero, \033[1mdime cuál es tu nombre?\033[0m") #Saludo del bot
    print(f"\033[1mTheoryBot\033[0m: Si en algun momento quieres volver a ver la progresión, la tonalidad o la estructura, solo tienes que decírmelo.\n") #Explicación de cómo recordar la progresión, tonalidad y estructura]")
    saludo_hecho = True # Saludo hecho por el bot

    while True:  # Bucle principal del ChatBot

        ########################################################################## Entrada del usuario y variables que se tienen que resetear al final de cada iteración.

        propuesta_progresion = False # Propuesta de progresión, el chat a propuesto una progresión
        input_usuario = input(f"\033[1m{nombre}\033[0m: ").strip().lower() # Entrada del usuario, se convierte a minúsculas para evitar confusiones
        respondido = False  # Resetear la variable al inicio de cada iteración
        palabra_clave = detectar_palabras_clave(input_usuario, palabras_clave) # Detectar palabras clave en la entrada del usuario

        if saludo_hecho and input_usuario:
            nombre = input_usuario.capitalize()  # Convertir la primera letra a mayúscula
            print(f"\033[1mTheoryBot\033[0m: ¡Hola, {nombre}! Dime en qué tonalidad quieres trabajar hoy y nos pondremos manos a la obra.\n")
            tonalidad_dicha = input_usuario # Guardamos la tonalidad dicha por el usuario
            pregunta_tonalidad = True #se ha preguntado sobre el chat bot
            saludo_hecho = False # Ya se ha saludado al usuario entonces se pone a False
            respondido = True # Se ha respondido al usuario

        if input_usuario in ["hola", "saludo", "ayuda"]:
            print(f"\033[1mTheoryBot\033[0m: ¡Hola! ¿En qué puedo ayudarte?\n") 
            respondido = True

        ########################################################################## Tonalidad
            
        if pregunta_tonalidad and tonalidad_dicha:  # Si el usuario pregunta por la tonalidad
            if tonalidad_actual is None:  # Llamar a obtener_tonalidad() si aún no se ha especificado.
                tonalidad_actual = obtener_tonalidad()  # Se llama a obtener_tonalidad() y se guarda en la variable tonalidad_actual
                print(f"\033[1mTheoryBot\033[0m: Muy buena elección, \033[1m{tonalidad_actual}\033[0m es una tonalidad interesante. Ahora vamos a por los acordes ¿Qué emoción quieres transmitir con la canción?")
                pregunta_sensacion = True  # Se ha preguntado sobre la sensación
                print(f"\033[1mTheoryBot\033[0m: Triste, feliz, relajada, eufórica, sorprendida, enfadada, épica, romántica, jazz o blues.\n") # Da las opciones de emociones
                propuesta_emocion = True
                respondido = True  # Se ha respondido al usuario
        
        if tonalidad_actual in ["CM", "DM", "EM", "FM", "GM", "AM", "BM"] and propuesta_emocion == True: #si la progresión es mayor
            print(f"\033[1mTheoryBot\033[0m: Veo que has escogido una tonalidad mayor,\033[1m{tonalidad_actual}\033[0m, te recomiendo que empieces con una progresión \033[1mfeliz o relajada\033[0m para sacarle el máximo provecho.\n")
            respondido = True
            propuesta_emocion = False

        if emocion_actual == None and tonalidad_actual in ["Cm", "Dm", "Em", "Fm", "Gm", "Am", "Bm"] and propuesta_emocion == True: #si la progresión es menor
            print(f"\033[1mTheoryBot\033[0m: Veo que has escogido una tonalidad menor, te recomiendo que empieces con una progresión \033[1mtriste o eufórica\033[0m para sacarle el máximo provecho.\n")
            respondido = True
            propuesta_emocion = False
            
        if input_usuario in ["tonalidad actual"] or palabra_clave == "tonalidad":   
            print(f"\033[1mTheoryBot\033[0m: La tonalidad actual es {tonalidad_actual}\n")
            respondido = True

        ########################################################################## Progresiones

      

        if pregunta_sensacion and input_usuario in progresiones:  # Si el usuario menciona una emoción "in progresiones" buscará esa palabra clave
            emocion_actual = input_usuario  # Guardamos la emoción actual en base a lo que ha dicho el usuario
            indice = indices_progresiones[emocion_actual]  # Obtener el índice actual de la progresión
            progresion = progresiones[emocion_actual][indice]  # Obtener la progresión actual
            indices_progresiones[emocion_actual] = (indice + 1) % len(progresiones[emocion_actual])  # Avanzar al siguiente índice, el % es para que no se pase del límite y vuelva al principio.
            print(f"\033[1mTheoryBot\033[0m: Que sensación más interesante, ahora te daré una progresión {emocion_actual}, si quieres otra dime otra, sino dime que te quedas con esa.")         
            print(f"\033[1mTheoryBot\033[0m: Una buena progresión {emocion_actual} podría ser: \033[1m{progresion}\033[0m. \n") # Mostrar una sugerenca de progresión
            propuesta_progresion = True
            respondido = True

        if propuesta_progresion == True and input_usuario in ["otra", "siguiente", "más", "no"] or palabra_clave == "otra":  # Si el usuario quiere ver otra progresión
            indice = indices_progresiones[emocion_actual]  # Obtener el índice actual de la progresión
            progresion = progresiones[emocion_actual][indice]  # Obtener la progresión actual
            indices_progresiones[emocion_actual] = (indice + 1) % len(progresiones[emocion_actual])  # Avanzar al siguiente índice
            print(f"\033[1mTheoryBot\033[0m: Aquí tienes otra progresión {emocion_actual}: \033[1m{progresion}\033[0m. \n") # Mostrar la siguiente progresión
            respondido = True

        if propuesta_progresion == True and palabra_clave == ["esta","quedo", "esa"] or input_usuario in ["me quedo con esta", "esta", "esta me gusta", "me quedo con esa"]:  # Si el usuario quiere quedarse con la progresión actual
            print(f"\033[1mTheoryBot\033[0m: Perfecto, ahora que ya tenemos los acordes vamos a por la estructura. \n") # Decir que la progresión actual es la elegida y pasar a la siguiente etapa
            pregunta_estructura = True # Se ha preguntado sobre la estructura y pasa al siguien bloque.
            propuesta_progresion = False # Hacer falsa la propuesta de progresión para que no se repita
            respondido = True

        if palabra_clave == "progresion" or palabra_clave == "progresión": # Si el usuario quiere ver la progresión actual
            print(f"\033[1mTheoryBot\033[0m: La progresión actual es: \033[1m{progresion}\033[0m. \n") 
            respondido = True 

        ########################################################################## Estructura

        if pregunta_estructura == True:
            print(f"\033[1mTheoryBot\033[0m: Una estructura para una canción \033[1m{emocion_actual}\033[0m podría ser: \033[1m{estructura_cancion()[emocion_actual][0]}\033[0m.    ")
            print(f"\033[1mTheoryBot\033[0m: Te gusta?     SI \ NO\n") # Aquí le dos opciones para no enrollarme poniendo un montón de opciones, que si las palabras clave, que si los sinónimos...
            pregunta_estructura = False # Se ha preguntado sobre la estructura, entonces se pone a False
            respondido = True
            pregunta_estructura_gusta = True

        if pregunta_estructura_gusta == True and input_usuario in ["no", "prefiero otra", "otra", "siguiente", "más"]:  # Si el usuario no le gusta la estructura
            print(f"\033[1mTheoryBot\033[0m: ¡Entendido! Aquí tienes otra estructura \033[1m{emocion_actual}\033[0m: \033[1m{estructura_cancion()[emocion_actual][1]}\033[0m.") # Mostrar otra estructura, el [1] es para mostrar la segunda estructura y se sabe que hay dos estructuras por emoción
            print(f"\033[1mTheoryBot\033[0m: Te gusta?     SI \ NO\n") # Aquí le dos opciones para no enrollarme poniendo un montón de opciones, que si las palabras clave, que si los sinónimos...
            estructura_actual = estructura_cancion()[emocion_actual][1]  # Guardar la estructura actual 
            pregunta_estructura_gusta = True # Se ha preguntado sobre la estructura pero no le gusta entonces volvemos a mostrale otra opción y volvemos arriba
            respondido = True

        if pregunta_estructura_gusta == True and input_usuario in ["si", "sí", "me gusta", "prefiero esta", "prefiero esta estructura"]:  # Si el usuario le gusta la estructura
            print(f"\033[1mTheoryBot\033[0m: ¡Genial! Ahora que ya tenemos la progresión y la estructura,\033[1m ¡ya tienes la base de tu canción!\033[0m")
            print(f"\033[1mTheoryBot\033[0m: Si necesitas que te recuerde algo no dudes en preguntarmelo!\n")
            pregunta_estructura_gusta = False
            respondido = True

        if palabra_clave == "estructura" or input_usuario in ["estructura"]: # Si el usuario quiere ver la estructura actual
            print(f"\033[1mTheoryBot\033[0m: La estructura actual es: \033[1m{estructura_actual}\033[0m. \n") 
            respondido = True

        ########################################################################## Cosas varias

        if input_usuario in ["gracias"]:
            print(f"\033[1mTheoryBot\033[0m: ¡De nada, {nombre}! Si necesitas algo más, no dudes en decírmelo.\n")
            respondido = True

        if palabra_clave == "adios" or palabra_clave == "hasta luego":
            print(f"\033[1mTheoryBot\033[0m: ¡Hasta luego, {nombre}! Que tengas un buen día y \033[1m¡mucha suerte con tu canción\033[0m!\n")
            break
        
        if not respondido:  # Mostrar el mensaje solo si no se ha respondido antes
            print("\033[1mTheoryBot\033[0m: Lo siento, no entendí eso. ¿Puedes repetirlo?  \n") 

        if input_usuario in ["feo", "tonto", "idiota", "estúpido", "inútil", "mierda", "gilipollas", "cabrón", "puta",]:
            print(f"\033[1mTheoryBot\033[0m: Eso tu \n")
            respondido = True


            
# Ejecutar el chatbot
if __name__ == "__main__":
    chatbot()

# ¡Gracias por leer!