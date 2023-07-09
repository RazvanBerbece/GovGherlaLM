import os
import sys
from bs4 import BeautifulSoup
from .types.facebook_message import FacebookMessage
from .filter.filter import Filter

sys.path.append("..")

class Parse:
    """
    Class which handles parsing the exported facebook data from HTML to a list of FacebookMessages.
    """
    source_folder:  str = ""
    debugging:      bool = False

    def from_source_folder(self, source_folder):
        self.source_folder = source_folder
        return self
    
    def and_debugging_enabled(self):
        self.debugging = True
        return self
    
    def execute(self) -> list:
        """
        Go through all the .html files at the source folder location and:
            1. extract the FacebookMessages according to the given filtering strategies
            2. build a list of dicts which represent the final clean data (the prompts to use for finetuning)
        """
        messages = []
        filtered_messages = 0

        # Identifiers for parsing
        message_container_class = "_3-95 _a6-g"
        author_in_container_class = "_2ph_ _a6-h _a6-i"
        content_in_container_class = "_2ph_ _a6-p"
        timestamp_in_container_class = "_3-94 _a6-o"

        # Iterate through each file
        for filename in os.scandir(self.source_folder):
            if filename.is_file():
                if (self.debugging):
                    print(f"Parsing file {filename.name}")
                    
                # If the file exists, parse it using BeautifulSoup
                html_content = open(self.source_folder + filename.name, "r")
                soup = BeautifulSoup(html_content, "html.parser")
                message_containers = soup.find_all("div", class_=message_container_class)
                # For each sent message in the source HTML file
                for container in message_containers:
                    message = FacebookMessage()

                    # Extract content of current sent message
                    content_tags = container.find_all("div", class_=content_in_container_class)
                    for tag in content_tags:                        
                        message.content = tag.text

                    # Skip if content is not suitable for finetuning
                    if Filter.should_skip(message.content):
                        filtered_messages += 1
                        continue

                    # Extract author of current sent message
                    author_tags = container.find_all("div", class_=author_in_container_class)
                    for tag in author_tags:
                        message.author = tag.text

                    # Extract timestamp of current sent message
                    # TODO
                    
                    messages.append(message.get_dict())

        if (self.debugging):
            print(f"Extracted {len(messages)} messages and filtered {filtered_messages}")

        return messages
    