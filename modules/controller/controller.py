from dataclasses import dataclass
from datetime import datetime
from ..model.CGPT_speech_generator import *

gptBackend = GPT_speech_generator()

@dataclass(kw_only=True)
class Controller:
    triggertime: str = "10:15"
    """The Applications controller"""

    def getTestText(self):
        return "Text from the controller!"
    
    def getWarning(self):
        print("Get warning from gpt")
        return gptBackend.get_reminder_message(None)
    
controller = Controller()




