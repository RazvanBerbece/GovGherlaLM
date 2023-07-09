from parser.parser import Parse

# Data Preprocessing Parameters
raw_data_source_folder = "../../data/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/"
output_folder = "../../data/clean/"

# Extract messages from raw data
messages = Parse() \
    .from_source_folder("../../data/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/") \
    .and_debugging_enabled() \
    .execute()

# Build list of prompts out of the extracted and cleaned messages
# TODO