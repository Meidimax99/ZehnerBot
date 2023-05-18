from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True)
class Controller:
    triggertime: str = "17:30"
    """The Applications controller"""

    def getTestText(self):
        return "Text from the controller!"
    
controller = Controller()




