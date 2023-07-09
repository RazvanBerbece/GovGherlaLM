import datetime

from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class FacebookMessage:
    '''Class which represents the data model of a facebook message in the group chat.'''
    author: str = ""
    content: str = ""
    # timestamp: datetime

    def get_dict(self) -> dict:
        return {
            "author": self.author,
            "content": self.content
        }