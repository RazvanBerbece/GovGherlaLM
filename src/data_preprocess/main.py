from .parser.parser import Parse

prompts = Parse() \
    .from_source_folder("../../data/raw/facebook-100002107045945/messages/inbox/guvernulgherla_7283751518362871/") \
    .to_output_folder("../../data/clean/") \
    .with_filter_strategies([]) \
    .execute()