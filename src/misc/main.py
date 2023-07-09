from author_count.count import generate_count_by_author_barchart
from word_cloud.word_cloud import generate_word_cloud

# Source folders
message_data_filepath = "../../data/facebook/clean/messages/data.json"

# Output files
count_barchart_output_file = "outputs/author_barchart.png"
word_cloud_output_file = "outputs/word_cloud.png"

generate_count_by_author_barchart(message_data_filepath, count_barchart_output_file)
generate_word_cloud(message_data_filepath, word_cloud_output_file)