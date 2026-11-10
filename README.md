# Asistente Virtual de Primer Contacto para el Bienestar Estudiantil

## Descripción del Proyecto
Este repositorio contiene el prototipo de un Asistente Virtual conversacional diseñado para proporcionar herramientas iniciales de contención emocional a estudiantes universitarios. El objetivo principal de este sistema es fungir como un filtro de primer nivel (triage) que brinde apoyo inmediato en horarios no administrativos, orientando a los usuarios hacia los servicios de salud mental de la institución educativa de manera anónima y segura.

El proyecto se enmarca dentro del desarrollo de un Proyecto Terminal de Ingeniería en Inteligencia Artificial.

## Características Principales

El sistema está diseñado bajo estrictos protocolos de seguridad y limitación de alcance médico, implementando las siguientes arquitecturas:

* **Arquitectura RAG (Generación Aumentada por Recuperación):** El asistente restringe sus respuestas a un corpus de conocimiento predefinido y validado por profesionales (manuales de primeros auxilios psicológicos institucionales). Esto previene la alucinación del modelo y evita la generación de diagnósticos clínicos.
* **SafetyFilter (Módulo de Seguridad):** Un motor de reglas basado en expresiones regulares (Regex) que intercepta el mensaje del usuario antes de ser procesado por el modelo de Inteligencia Artificial. Si detecta intenciones de riesgo crítico (ej. autolesión o ideación suicida), el sistema interrumpe el flujo normal y emite automáticamente una alerta con los números de emergencia correspondientes.
* **Interfaz Conversacional:** Implementada mediante Streamlit, simula un entorno de mensajería asíncrona para evaluar la experiencia de usuario (UX) en situaciones de estrés.

## Requisitos del Sistema

Para ejecutar este prototipo en un entorno local, se requiere:

* Python 3.8 o superior.
* Gestor de paquetes `pip`.

Dependencias principales:
* `streamlit`

## Instrucciones de Instalación

1. Clonar este repositorio en su máquina local:
   ```bash
   git clone https://github.com/TU-USUARIO/asistente-bienestar-marista.git
   cd asistente-bienestar-marista
   ```

2. (Opcional pero recomendado) Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instalar las dependencias requeridas (si se cuenta con un archivo `requirements.txt`) o instalar Streamlit directamente:
   ```bash
   pip install streamlit
   ```

## Uso y Ejecución

Para iniciar la interfaz del asistente virtual, ejecute el siguiente comando en la raíz del proyecto:

```bash
streamlit run prototipo_chatbot_bienestar.py
```

El navegador web predeterminado abrirá automáticamente la aplicación (por defecto en `http://localhost:8501`). 

### Casos de Prueba Sugeridos
Para comprobar el funcionamiento de las validaciones, puede ingresar los siguientes escenarios en el chat:
* **Prueba de RAG (Contención):** Ingrese frases relacionadas con el estrés académico, como "Tengo mucha ansiedad por un examen".
* **Prueba de SafetyFilter (Alerta de Crisis):** Ingrese palabras restringidas para observar la interrupción del sistema, por ejemplo, "Ya no quiero vivir".

## Aviso Legal y de Salud

**ADVERTENCIA IMPORTANTE:** Este sistema es un prototipo tecnológico desarrollado con fines académicos. **No es un dispositivo médico, no emite diagnósticos clínicos ni psicológicos, y bajo ninguna circunstancia reemplaza la valoración, terapia o intervención de un profesional de la salud mental certificado.** 

Si usted o alguien que conoce se encuentra en una situación de crisis emocional severa, por favor comuníquese de inmediato con los servicios de emergencia de su localidad (ej. 911) o acuda al centro de salud más cercano.