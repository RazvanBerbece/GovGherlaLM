import json
import os
from .types.prompt import Prompt

class PromptBuilder:

    def __init__(self):
        self.messages = []
        self.authors = []
        self.prompts = []
    
    def with_messages_and_authors(self, messages: list, authors: list):
        self.messages = messages
        self.authors = authors
        return self
    
    def with_messages_and_authors_from_file(self, filepath: str):
        print(f"Reading message data from {filepath}")
        f = open(os.getcwd() + "/" + filepath)
        self.messages = json.load(f)
        # Discover all authors in conversation
        for message in self.messages:
            if message["author"] not in self.authors:
                self.authors.append(message["author"])
        return self
    
    def build_prompts(self):
        """
        Build a list of prompts out of the given list of messages containing their content and their author.
        Strategy: Read in message inputs and outputs from list two elements at a time ([1, 2, 3] -> (1, 2), (2, 3))
        """
        print(f"Building prompts")
        for message_1, message_2 in zip(self.messages[:-1], self.messages[1:]):
            prompt = Prompt(author_to_reply=message_2["author"],
            input=message_1["content"],
            input_author=message_1["author"],
            output=message_2["content"],
            other_authors=[ author for author in self.authors if author != message_2["author"] ]
            )
            self.prompts.append(prompt.get_dict())
        print(f"Created {len(self.prompts)} prompts")
        return self
    
    def output_to_file(self, filepath: str):
        print(f"Saving prompts to {filepath}")
        with open(os.getcwd() + "/" + filepath, "w+") as fout:
            json.dump(self.prompts, fout, indent=2, ensure_ascii=False)