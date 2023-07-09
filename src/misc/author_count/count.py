import json
import matplotlib.pyplot as plt

def generate_count_by_author_barchart(filepath_to_data, output_file):

    # Load JSON data
    f = open(filepath_to_data)
    messages = json.load(f)

    # Initial dictionary holding keys and values for message counts
    results = {
        "Marco": 0,
        "Antonio": 0,
        "Maco": 0,
        "Nino": 0
    }

    # Calculate the message counts per author
    for message in messages:
        if message["author"] == "Alex Macovei":
            results["Maco"] += 1
        elif message["author"] == "Nino Matase":
            results["Nino"] += 1
        elif message["author"] == "Antonio Berbece":
            results["Antonio"] += 1
        elif message["author"] == "Petruca Marco":
            results["Marco"] += 1
    
    # Store barchart
    plt.title("Message Counts by Author")
    plt.bar(*zip(*results.items()))
    plt.savefig(output_file)

