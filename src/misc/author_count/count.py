import json
import matplotlib.pyplot as plt

def generate_count_by_author_barchart(filepath_to_data, output_file):

    # Load JSON data
    f = open(filepath_to_data)
    messages = json.load(f)

    # Initial dictionary holding keys and values for author and message counts
    results = {}

    # Calculate the message counts per author
    for message in messages:
        if message["author"] in results:
            results[message["author"]] += 1
        else:
            results[message["author"]] = 0
    
    # Plot and store barchart
    plt.title("Message Counts by Author")
    plt.bar(*zip(*results.items()))
    plt.savefig(output_file)

    print(f"Saved message counts by author to {output_file}")
