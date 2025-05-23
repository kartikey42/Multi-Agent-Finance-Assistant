# -----------------------------
from openai import OpenAI

client = OpenAI()

def synthesize_response(risk_summary, earnings):
    earnings_text = ", ".join([f"{k} {v['surprise']}" for k, v in earnings.items()])
    prompt = f"{risk_summary} {earnings_text}. Provide a morning brief."
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
