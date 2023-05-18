from dataclasses import dataclass
from datetime import datetime
from ..model.CGPT_speech_generator import *

gptBackend = GPT_speech_generator()

@dataclass(kw_only=True)
class Controller:
    triggertime: str = "19:42"
    """The Applications controller"""

    def getTestText(self):
        return "Text from the controller!"
    
    def get_register_message(self, person, days) -> str:
        return gptBackend.get_register_message(person, days)
    
    def get_acknowledge_off_day_message(self, person, day):
        return gptBackend.get_acknowledge_off_day_message(person, day)

    def get_start_no_convidence_vote_message(self, person, day):
        return gptBackend.get_start_no_convidence_vote_message(person, day)

    def get_no_confidence_vote_positive_outcome_message(self, person):
        return gptBackend.get_no_confidence_vote_positive_outcome_message(person)

    def get_no_confidence_vote_negative_outcome_message(self, person):
        return gptBackend.get_no_confidence_vote_negative_outcome_message(person)

    def get_start_change_days_vote_message(self, person):
        return gptBackend.get_start_change_days_vote_message(person)
    
    def get_change_days_vote_positive_outcome_message(self, person):
        return gptBackend.get_change_days_vote_positive_outcome_message(person)

    def get_change_days_vote_negative_outcome_message(self, person):
        return gptBackend.get_change_days_vote_negative_outcome_message(person)

    def get_all_proofs_given_message(self):
        return gptBackend.get_all_proofs_given_message()

    def get_reminder_message(self, persons):
        return gptBackend.get_reminder_message(persons)
    
    
    def getWarning(self):
        print("Get warning from gpt")
        return gptBackend.get_reminder_message(None)
    
controller = Controller()




