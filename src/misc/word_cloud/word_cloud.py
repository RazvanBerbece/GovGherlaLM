import json
import matplotlib.pyplot as plt
from .filter import get_corpus_without_stopwords
from wordcloud import WordCloud, STOPWORDS

def generate_word_cloud(filepath_to_data, output_file, include_names=True):

    # Load JSON data containing all available messages
    f = open(filepath_to_data)
    messages = json.load(f)

    corpus = ""
    
    # Compose the corpus by appending all message contents to the target string
    for message in messages:
        corpus += " " + message["content"]
    
    # Clean corpus of linking words
    clean_corpus = get_corpus_without_stopwords(corpus, with_names=include_names)

    # Generate the cloud from the cleaned up corpus
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords=STOPWORDS) \
        .generate(clean_corpus)
    
    # Plot
    plt.title("Word Cloud")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    wordcloud.to_file(output_file)

    print(f"Saved word cloud to {output_file}")
