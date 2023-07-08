import os
from bs4 import BeautifulSoup

class Parse:
    """
    Class which handles parsing the exported facebook data from HTML to a list of JSON samples 
    representing prompts to be used in the finetuning process.
    """
    source_folder:  str = ""
    output_folder:  str = ""
    filters:        list = []

    def from_source_folder(self, source_folder):
        self.source_folder = source_folder
        return self
    
    def to_output_folder(self, output_folder):
        self.output_folder = output_folder
        return self
    
    def with_filter_strategies(self, filters_list):
        self.filters = filters_list
        return self
    
    def execute(self) -> list:
        """
        Go through all the .html files at the source folder location and:
            1. extract the FacebookMessages according to the given filtering strategies
            2. build a list of dicts which represent the final clean data (the prompts to use for finetuning)
        """
        final_dataset = []

        # Move to directory holding the .html files
        # os.chdir(self.source_folder)

        # Iterate through each file
        for filename in os.scandir(self.source_folder):
            if filename.is_file():
                print(filename.path)

        return final_dataset
    
