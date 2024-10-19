# Debemos importar la librería de OpenAI
from openai import OpenAI

# Creamos un cliente que apunta a la dirección local de LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", # Este campo no se utiliza
  messages=[
    {"role": "system", "content": "Eres un asistente que ofrece información certera y no muy extensa sobre los temas consultados."},
    {"role": "user", "content": "Que es CMD? Responde con menos de 20 palabras"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)
