from author_count.count import display_count_by_author_barchart

# Source folders
message_data_filepath = "../../data/facebook/clean/messages/data.json"

# Output files
count_barchart_output_file = "outputs/author_barchart.png"
word_cloud_output_file = "outputs/word_cloud.png"

display_count_by_author_barchart(message_data_filepath, count_barchart_output_file)