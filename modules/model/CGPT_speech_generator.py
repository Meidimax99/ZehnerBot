import os
from dotenv import load_dotenv
import openai

class GPT_speech_generator:

    gpt_model = "gpt-3.5-turbo"
    context_template = "Du bist der Anführer eines verschwörerischen Geheimpaktes. Im Pakt hat sich jedes Mitglied dazu verpflichtet an selbst gewählten Tagen um 10:15 anwesend zu sein um danach produktiv zu sein. Wenn jemand das nicht schafft und sich bis zum Vortag nicht abgemeldet hat muss er ein essen an alle anderen ausgeben."
    emotions = { 
        "annoyed": "Du bist momentan genervt weil sich jemand nicht an seine Verpflichtungen hält, denen er mit unterzeichnen des Paktvertrages zugestimmt hat.",
        "friendly": "Du bist äußerst erfreut über das vertragsgerechte handeln eines Paktmitgliedes",
        "angry": "Du bist wirklich wütend über das nicht vertragsgerechte Verhalten eines Paktmitglieds"

    }

    def __init__(self):
        load_dotenv()
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        self.querier = openai.ChatCompletion()

    def get_persons_context(self, persons):
        person_context = "Deine Nachricht richtet sich an"
        if isinstance(persons, str):
            person_context += " das Paktmitglied " + persons + "."
        elif len(persons) == 1:
            person_context += " das Paktmitglied "  + persons[0] + "."
        elif len(persons) > 1:
            person_context += " die Paktmitglieder "
            for i in range(len(persons[:-1])):
                person_context += " " + persons[i]
            person_context += " und " + persons[-1] + "."
        return person_context


    def get_reminder_message(self, persons):
        context = self.context_template + self.emotions["angry"] + self.get_persons_context(persons)
        msg = "Schreibe eine kurze Chatnachricht, die die genannte Person oder Personen daran erinnert, dass Sie sich verpflichtet haben um 10:15 da zu sein und bisher noch keinen Beweis dafür geliefert haben. Die Nachricht soll nicht im Briefformat sein."
        return self.ask_gpt(msg, context)

    def ask_gpt(self, msg, context):
        context = [{'role': 'system', 'content': context}]
        context.append({'role': 'user', 'content': msg})
        response = self.querier.create(model=self.gpt_model, messages=context)
        answer = response.choices[0]['message']['content']
        return answer




#speech_gen = GPT_speech_generator()
#answer = speech_gen.get_reminder_message("Paul")
#print(answer)