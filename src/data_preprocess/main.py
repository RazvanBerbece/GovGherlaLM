from parse.facebook.parser.parser import ParseRawFacebookHtmlData
from prompt_builder.prompt_builder import PromptBuilder

# Data Preprocessing Parameters
raw_data_source_folders = [
    "../../data/facebook/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/"
]

# Preprocessing output files
clean_messages_list_output_file = "../../data/facebook/clean/messages/data.json"
prompts_output_file = "../../data/facebook/clean/prompts/prompts.json"

# Extract messages from raw data
# facebook_data = ParseRawFacebookHtmlData() \
#     .from_source_folders(raw_data_source_folders) \
#     .with_output_file(clean_messages_list_output_file) \
#     .and_debugging_enabled() \
#     .execute() \

# Build list of prompts out of the extracted and cleaned messages
prompts = PromptBuilder() \
    .with_messages_and_authors_from_file(clean_messages_list_output_file) \
    .build_prompts() \
    .output_to_file(prompts_output_file)