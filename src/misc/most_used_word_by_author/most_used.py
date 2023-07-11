import json
import matplotlib.pyplot as plt
from utils.filter.filter import get_corpus_without_stopwords

def generate_most_used_word_per_author(filepath_to_data, output_file, include_names=True):

    print(f"Generating and storing most used word per author to {output_file}")
    
    # Load JSON data containing all available messages
    f = open(filepath_to_data)
    messages = json.load(f)

    # Initial dictionary holding keys and values for author and message counts
    word_occurrence_per_author = {}
    for message in messages:
        content = message["content"]
        author = message["author"]
        clean_content = get_corpus_without_stopwords(content, with_names=include_names)
        for word in clean_content.split():
            if author in word_occurrence_per_author:
                if word in word_occurrence_per_author[author]:
                    word_occurrence_per_author[author][word] += 1
                else:
                    word_occurrence_per_author[author][word] = 0
            else:
                word_occurrence_per_author[author] = {}
                word_occurrence_per_author[author][word] = 0

    # Get the word of maximum occurence from each author and save them in a file
    results = {}
    for author in word_occurrence_per_author:
        max_occur_pair = max(word_occurrence_per_author[author].items(), key=lambda k: k[1])
        results[author] = max_occur_pair
    
    # Extract the names, words, and occurrences from the dictionary
    names = list(results.keys())
    words = [ item[0] for item in results.values() ]
    occurrences = [ item[1] for item in results.values() ]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the bar chart
    colors = ['steelblue', 'coral', 'limegreen', 'red']
    bars = ax.bar(names, occurrences, color=colors)

    # Set labels and title
    ax.set_ylabel("Occurrences")
    ax.set_title("Most Used Word per Author")

    # Display the word next to each name
    for bar, word in zip(bars, words):
        bar_height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, bar_height / 2, word,
            ha='center', va='center', color='white')

    # Store the plot
    plt.savefig(output_file)
