import os

def get_corpus_without_linking_words(corpus):

    # Build list of words to be removed from corpus from provided files holding stopword lists
    stopwords = []
    for filename in os.scandir("word_cloud/stopwords/"):
        with open("word_cloud/stopwords/" + filename.name) as file:
            lines = [line.rstrip() for line in file]
            stopwords.extend(lines)

    # Tokenise corpus
    tokens = corpus.split()

    # Build list of words out of words which are not stopwords
    words = [word for word in tokens if word.lower() not in stopwords and len(word) > 1]

    # Build corpus out of resulted list
    results = ' '.join(words)

    return results