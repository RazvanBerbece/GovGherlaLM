from author_count.count import generate_count_by_author_barchart
from most_used_word_by_author.most_used import \
    generate_most_used_word_per_author
from word_cloud.word_cloud import generate_word_cloud

# Source folders
message_data_filepath = "../../data/facebook/clean/messages/data.json"

# Output filepaths
count_barchart_output_file = "outputs/author_barchart.png"
word_cloud_output_file = "outputs/word_cloud.png"
word_per_author_output_file = "outputs/word_per_author.png"

# Generate outputs
generate_count_by_author_barchart(message_data_filepath, count_barchart_output_file)
generate_word_cloud(message_data_filepath, word_cloud_output_file, include_names=False)
generate_most_used_word_per_author(
    message_data_filepath, word_per_author_output_file, include_names=False
)
