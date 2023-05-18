from dataclasses import dataclass

@dataclass(kw_only=True)
class DiscordUser:
    """A User Message"""
    name: str
    id: str

@dataclass(kw_only=True)
class UserMessage:
    """A User Message"""
    user: DiscordUser
    message: str
    timestamp: int = 0
    message_id: str
    

variable = UserMessage(user=DiscordUser(name="Test",id="ID"), message="Message")

