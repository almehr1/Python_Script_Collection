import re
import collections

def analyze_text(text, top_n=10, remove_stopwords=False):
    """
    Analyzes a given text and provides various information about it.

    Args:
        text (str): The text to be analyzed.
        top_n (int, optional): The number of most common words to display (default: 10).
        remove_stopwords (bool, optional): Whether to remove stop words (default: False).

    Returns:
        dict: A dictionary containing the analysis results.
    """

    # Preprocess the text
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation and other non-word characters

    # Split the text into words
    words = text.split()

    # Remove stop words if specified
    if remove_stopwords:
        stop_words = set(open("stopwords.txt", "r").read().splitlines())
        words = [word for word in words if word not in stop_words]

    # Calculate word count and character count
    word_count = len(words)
    character_count = len(text)

    # Calculate average word length
    average_word_length = sum(len(word) for word in words) / word_count

    # Find most common words
    word_counts = collections.Counter(words)
    most_common_words = word_counts.most_common(top_n)

    # Calculate sentence count
    sentence_count = len(re.findall(r"[^\.!?]+(?<=\.|\?|!)", text))

    # Calculate average sentence length
    if sentence_count > 0:
        average_sentence_length = sum(len(sentence.split()) for sentence in text.split(".!?")) / sentence_count
    else:
        average_sentence_length = 0

    # Return the analysis results
    results = {
        "word_count": word_count,
        "character_count": character_count,
        "average_word_length": average_word_length,
        "most_common_words": most_common_words,
        "sentence_count": sentence_count,
        "average_sentence_length": average_sentence_length,
    }

    return results

