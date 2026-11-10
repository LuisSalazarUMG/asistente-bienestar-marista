import time
import re
import streamlit as st

# -------------------------------------------------
# | PROTOTIPO: ASISTENTE DE BIENESTAR ESTUDIANTIL |
# | Proyecto Terminal                             |
# -------------------------------------------------

# 1. Base de Datos Vectorial Simulada (Context Retriever)
# Representa la base de conocimientos de primeros auxilios psicológicos.
CORPUS_INSTITUCIONAL = {
    "ansiedad_examenes": (
        "Técnica de Grounding (5-4-3-2-1): Respira profundo. Nombra 5 cosas que puedas ver, "
        "4 que puedas tocar, 3 que puedas escuchar, 2 que puedas oler y 1 que puedas saborear. "
        "Recuerda que el estrés por exámenes es normal, tómate pausas de 5 minutos cada hora."
    ),
    "tristeza_aislamiento": (
        "Es normal sentirse abrumado o solo durante la etapa universitaria. Validar tus emociones "
        "es el primer paso. El departamento de psicología ofrece sesiones breves de orientación "
        "sin compromiso a largo plazo."
    ),
}

# 2. Módulo de Seguridad Estricta (Safety Filter)
# Evalúa expresiones regulares (regex) de alto riesgo ANTES de usar IA.
def safety_filter(user_input):
    risk_patterns = [
        r"morir", r"matarme", r"no quiero vivir", r"suicidio", r"hacerme daño", r"desaparecer"
    ]
    texto = user_input.lower()
    for pattern in risk_patterns:
        if re.search(pattern, texto):
            return True
    return False

# 3. Módulo de Recuperación (Context Retriever)
def retrieve_context(user_input):
    texto = user_input.lower()
    if any(word in texto for word in ["examen", "ansiedad", "estrés", "estresado", "pánico"]):
        return CORPUS_INSTITUCIONAL["ansiedad_examenes"]
    elif any(word in texto for word in ["triste", "solo", "deprimido", "llorar"]):
        return CORPUS_INSTITUCIONAL["tristeza_aislamiento"]
    return None

# 4. Cliente LLM Simulado (Generación)
# Para la presentación no requiere API Key real, emula la respuesta procesada.
def generate_response(user_input):
    # Paso A: Cortafuegos de seguridad
    if safety_filter(user_input):
        return (
            "PROTOCOLO DE EMERGENCIA ACTIVADO\n\n"
            "He detectado palabras de riesgo en tu mensaje. Tu vida es lo más importante y "
            "no estás solo en esto. Por tu seguridad, he pausado el asistente virtual.\n\n"
            "Por favor, comunícate de inmediato con:\n"
            "- Línea Nacional de Emergencias: 911\n"
            "Se ha enviado una alerta anónima al departamento de bienestar."
        )
    
    # Paso B: Recuperación RAG
    contexto = retrieve_context(user_input)
    
    # Paso C: Generación de respuesta
    if contexto:
        return (
            f"Entiendo cómo te sientes. Te comparto la siguiente información que puede ser de ayuda:\n\n"
            f"{contexto}\n\n"
            f"¿Te gustaría que te comparta el enlace directo para agendar una cita confidencial "
            f"con un psicólogo del campus?"
        )
    else:
        return (
            "Hola. Soy el Asistente de Bienestar Estudiantil de la Universidad Marista.\n\n"
            "Estoy aquí para escucharte y ofrecerte herramientas iniciales de contención. ¿Cómo te sientes hoy? "
            "(Recuerda que soy una Inteligencia Artificial y no emito diagnósticos médicos)."
        )

# -------------------------------------------
# | INTERFAZ DE USUARIO (Messaging Gateway) |
# -------------------------------------------
st.set_page_config(page_title="Bienestar Estudiantil")

st.title("Asistente de Bienestar Estudiantil")
st.caption("Prototipo de Proyecto Terminal - Arquitectura de Contención")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hola. Soy tu asistente de primer contacto. ¿En qué te puedo apoyar hoy?"}
    ]

# Mostrar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Capturar entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar y mostrar respuesta del bot
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simular tiempo de procesamiento de red y LLM
        with st.spinner("Procesando consulta..."):
            time.sleep(1.2) 
            bot_response = generate_response(prompt)
        
        # Efecto de máquina de escribir
        for chunk in bot_response.split():
            full_response += chunk + " "
            time.sleep(0.04)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})