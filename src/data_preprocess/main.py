from facebook.parser.parser import Parse

# Data Preprocessing Parameters
raw_data_source_folders = [
    "../../data/facebook/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/"
]
output_folder = "../../data/facebook/clean/"

# Extract messages from raw data
messages = Parse() \
    .from_source_folders(raw_data_source_folders) \
    .and_debugging_enabled() \
    .execute()

# Build list of prompts out of the extracted and cleaned messages
# TODO