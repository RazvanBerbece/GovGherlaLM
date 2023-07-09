from facebook.parser.parser import ParseRawFacebookHtmlData

# Data Preprocessing Parameters
raw_data_source_folders = [
    "../../data/facebook/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/"
]
clean_list_output_file = "../../data/facebook/clean/messages/data.json"
prompts_output_folder = "../../data/facebook/clean/prompts/"

# Extract messages from raw data
messages = ParseRawFacebookHtmlData() \
    .from_source_folders(raw_data_source_folders) \
    .with_output_file(clean_list_output_file) \
    .and_debugging_enabled() \
    .execute() \

# Build list of prompts out of the extracted and cleaned messages
# TODO