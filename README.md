# Chat Assistant

Este proyecto es un asistente de chat que utiliza LM Studio para ofrecer respuestas concisas a preguntas del usuario.

## Descripción

El archivo principal, `chat_assistant.py`, conecta con LM Studio a través de la API de OpenAI y proporciona respuestas directas limitadas a 20 palabras.

## Uso

1. **Requisitos previos**:
   - Python 3.x
   - LM Studio en funcionamiento en `http://localhost:1234/v1`

2. **Crear y activar el entorno virtual**:
   ```bash
   python -m venv llama-chat      # Crear entorno
   llama-chat\Scripts\activate     # Activar en Windows
   # o
   source llama-chat/bin/activate  # Activar en macOS/Linux
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el programa**:
   ```bash
   python chat_assistant.py
   ```

## Dependencias

El proyecto requiere las siguientes bibliotecas (listadas en `requirements.txt`):
- `openai`
- `Flask`
- (y otras)

## Contribuciones

Para contribuir, haz un fork del repositorio y envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.