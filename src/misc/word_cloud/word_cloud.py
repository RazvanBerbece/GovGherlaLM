import json
import matplotlib.pyplot as plt
from .filter import get_corpus_without_linking_words
from wordcloud import WordCloud, STOPWORDS

def generate_word_cloud(filepath_to_data, output_file):

    # Load JSON data
    f = open(filepath_to_data)
    messages = json.load(f)

    corpus = ""
    
    # Compose the corpus by appending all text to the target string
    for message in messages:
        corpus += " " + message["content"]
    
    # Clean corpus of linking words
    corpus = get_corpus_without_linking_words(corpus)

    # Generate the cloud from the cleaned up corpus
    wordcloud = WordCloud(width = 4000, height = 3000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords=STOPWORDS) \
        .generate(corpus)
    
    # Plot
    plt.title("Word Cloud")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    wordcloud.to_file(output_file)
