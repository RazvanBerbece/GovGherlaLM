import os
import re


def get_corpus_without_stopwords(corpus: str, with_names=True) -> str:
    """
    Returns a joined string containing only the useful words of the corpus.

    *Note:* If one wants to remove names as well from the corpus, one should create a file `names.txt` in
    the `utils/filter/stopwords` folder which contains lowercased 1 word names, each one on a new line in the file, and
    also set the `with_names` argument to `False`.
    """

    # Build list of words to be removed from corpus out of the provided files holding stopword lists
    stopwords = []
    for filename in os.scandir("utils/filter/stopwords/"):
        stopwords_filepath = "utils/filter/stopwords/" + filename.name
        # If names should be included, skip the names.txt stopwords file
        if filename.name == "names.txt" and with_names is True:
            continue
        with open(stopwords_filepath) as file:
            lines = [line.rstrip() for line in file]
            stopwords.extend(lines)

    # Build a list of words from the corpus minus the stopwords
    clean_words = [
        word
        for word in re.split("\W+", corpus)
        if word.lower() not in stopwords and len(word) > 1
    ]

    # Build the clean corpus by joining all clean words with spaces
    final_corpus = " ".join(clean_words)

    return final_corpus
