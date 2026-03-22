import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_call_ai(transcription):
    """
    Inspirado en Kaggle: Extrae sentimiento e insights en milisegundos.
    """
    prompt = f"Analizá esta llamada de retail y devolvé JSON con: sentiment, summary, resolved (bool), tags (list). Transcripción: {transcription}"
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return completion.choices[0].message.content
