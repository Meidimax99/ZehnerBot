from dataclasses import dataclass

@dataclass
class DiscordUser:
    """A User Message"""
    name: str
    id: str

@dataclass
class UserMessage:
    """A User Message"""
    user: DiscordUser
    message: str
    timestamp: int = 0

