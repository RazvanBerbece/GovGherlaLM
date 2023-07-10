import os
import re

def get_corpus_without_stopwords(corpus: str, with_names=True) -> str:

    # Build list of words to be removed from corpus out of the provided files holding stopword lists
    stopwords = []
    for filename in os.scandir("word_cloud/stopwords/"):
        stopwords_filepath = "word_cloud/stopwords/" + filename.name
        # If names should be included, skip the names.txt stopwords file
        if filename.name == "names.txt" and with_names is True:
            continue
        with open(stopwords_filepath) as file:
            lines = [line.rstrip() for line in file]
            stopwords.extend(lines)
    
    # Build a list of words from the corpus minus the stopwords
    clean_words = [ word for word in re.split("\W+", corpus) if word.lower() not in stopwords and len(word) > 1 ]

    # Build the clean corpus by joining all clean words with spaces
    final_corpus = " ".join(clean_words)

    return final_corpus