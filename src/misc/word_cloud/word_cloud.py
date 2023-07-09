import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

def generate_word_cloud(filepath_to_data, output_file):

    # Load JSON data
    f = open(filepath_to_data)
    messages = json.load(f)

    corpus = ""
    
    # Compose the corpus by appending all text to the target string
    for message in messages:
        corpus += " " + message["content"]

    # Generate the cloud from the whole corpus
    wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords = STOPWORDS) \
        .generate(corpus)
    
    # Plot
    plt.title("Word Cloud")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    wordcloud.to_file(output_file)
