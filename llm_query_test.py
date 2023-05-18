import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
completion = openai.ChatCompletion()
gpt_model = 'gpt-3.5-turbo'
generic_context = 'Du bist ein verschwörerischer Kobold Maki, der Anführer eines Geheimpaktes ist. Du bist oberflächlich nett, kannst aber auch schnell wütend werden wenn sich Paktmitglieder nicht an ihre Abmachung halten.'
annoyed = "Du bist momentan genervt weil sich jemand nicht an seine Vepflichtungen, denen er im Paktvertrag."
persons = "Deine Nachricht richtet sich an Paul."

def ask_gpt(msg, emotion, system_context, persons):
    context = [{
            'role': 'system',
            'content': system_context + " " + emotion + " " + persons
            }]
    context.append({'role': 'user', 'content': msg})
    response = completion.create(model=gpt_model, messages=context)
    answer = response.choices[0]['message']['content']
    return answer






q = "Eines deiner Paktmitglieder ist möglicherweise zu spät. Schreibe eine kurze Nachricht, die das Paktmitglied daran erinnert, dass es versprochen hat bis 10:15 da zu sein"
print(ask_gpt(q, annoyed, generic_context, persons))