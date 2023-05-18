import os
from dotenv import load_dotenv
import openai
import json

class GPT_speech_generator:

    gpt_model = "gpt-3.5-turbo"

    def __init__(self):
        template_path = "./../data/prompts/prompt_template.txt"
        emotions_path = "./../data/prompts/emotions_dict.txt"
        
        load_dotenv()
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        self.querier = openai.ChatCompletion()

        with open(template_path, 'r') as t:
            self.context_template = t.read()

        with open(emotions_path, 'r') as e:
            self.emotions = json.loads(e.read())


    def get_persons_context(self, persons):
        person_context = "Deine Nachricht richtet sich an"

        if persons is None:
            person_context += " alle Paktmitglieder."
        elif isinstance(persons, str):
            person_context += " das Paktmitglied " + persons + "."
        elif len(persons) == 1:
            person_context += " das Paktmitglied "  + persons[0] + "."
        elif len(persons) > 1:
            person_context += " die Paktmitglieder "
            for i in range(len(persons[:-1])):
                person_context += " " + persons[i]
            person_context += " und " + persons[-1] + "."
        return person_context

    def get_last_attendance_context(self, persons, n):
        pass

    def get_register_message(self, person):
        context = self.context_template + self.emotions["festive"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, die die genannte Person im Pakt willkommen heißt."
        return self.ask_gpt(msg, emotion="festive", persons=person)

    def get_acknowledge_off_day_message(self, person, day):
        context = self.context_template + self.emotions["annoyed"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht die anerkennt das sich die genannte Person für den " + day + " abgemeldet hat."
        return self.ask_gpt(msg, emotion="annoyed", persons=person)

    def get_start_no_convidence_vote_message(self, person, day):
        context = self.context_template + self.emotions["angry"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, die alle Paktmitglieder zu einem Mißtrauensvotum gegen die genannte Person aufruft. Es geht um die Frage, dass die Person möglicherweise noch keinen ausreichenden Anwesenheitsbeweis für den " + day +" geliefert hat und jetzt alle anderen Urteilen sollen ob er den Vertrag gebrochen hat."
        return self.ask_gpt(msg, emotion="annoyed", persons=person)

    def get_no_confidence_vote_positive_outcome_message(self, person):
        context = self.context_template + self.emotions["friendly"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, in der du allen Paktmitgliedern erklärst, dass das Votum gegen die genannte Person zu seinen Gunsten ausgegangen ist und sein Anwesenheitsbeweis damit akzeptiert wird."
        return self.ask_gpt(msg, emotion="angry",persons=person)

    def get_no_confidence_vote_negative_outcome_message(self, person):
        context = self.context_template + self.emotions["angry"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, in der du allen Paktmitgliedern erklärst, dass das Votum gegen die genannte Person nicht zu seinen Gunsten ausgegangen ist und sein Anwesenheitsbeweis damit nicht akzeptiert wird. Als Folge muss er ein Essen ausgeben."
        return self.ask_gpt(msg, emotion="festive", persons=person)

    def get_start_change_days_vote_message(self, person):
        context = self.context_template + self.emotions["friendly"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, in der du alle darüber aufklärst das die genannte Person ihre Tage für die Zukunft gerne ändern würde und nun alle Paktierer abstimmen müssen ob das erlaubt ist, denn diese Möglichkeit ist so im Pakt vereinbart, solange alle zustimmen."
        return self.ask_gpt(msg, emotion="angry", persons=person)

    def get_change_days_vote_positive_outcome_message(self, person):
        context = self.context_template + self.emotions["friendly"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, in der du allen Paktmitgliedern erklärst, dass das Votum gegen die genannte Person zu seinen Gunsten ausgegangen ist und der Person erlaubt wird ihre Tage zu ändern."
        return self.ask_gpt(msg, emotion="annoyed", persons=person)

    def get_change_days_vote_negative_outcome_message(self, person):
        context = self.context_template + self.emotions["angry"] + self.get_persons_context(person)
        msg = "Schreibe eine Nachricht, in der du allen Paktmitgliedern erklärst, dass das Votum gegen die genannte Person nicht zu seinen Gunsten ausgegangen ist und es ihr damit nicht erlaubt ist ihre Tage zu ändern."
        return self.ask_gpt(msg, emotion="friendly", persons=person)

    def get_all_proofs_given_message(self):
        context = self.context_template + self.emotions["friendly"] + self.format_context
        msg = "Schreibe eine Nachricht, in der du erklärst das alle die für heute zugesagt haben inzwischen auch einen Beweis für heute eingereicht haben."
        return self.ask_gpt(msg, emotion="friendly")

    def get_reminder_message(self, persons):
        msg = "Schreibe eine Nachricht, die die genannte Person oder Personen daran erinnert, dass Sie sich verpflichtet haben um heute 10:15 da zu sein und bisher noch keinen Beweis dafür geliefert haben. Nenne die Person oder Personen bei Namen."
        return self.ask_gpt(msg, emotion="annoyed", persons=persons)

    def ask_gpt(self, msg, emotion="angry", persons=None, debug=True):
        context_str = self.context_template + self.get_persons_context(persons) + self.emotions[emotion]
        context = [{'role': 'system', 'content': context_str}]
        context.append({'role': 'user', 'content': msg})
        response = self.querier.create(model=self.gpt_model, messages=context)
        answer = response.choices[0]['message']['content']
        if debug:
            print("#"*50)
            print(context_str)
            print("-"*50)
            print(answer)
            #print(response["usage"])
            print("#"*50)
        return answer

# {name:{present:x, excused:x, proof:x} }



speech_gen = GPT_speech_generator()
answer = speech_gen.get_start_change_days_vote_message("Paul")
