"""Functions to help edit essay homework using string manipulation."""
def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.
 
    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    return title.title()

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.
 
    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith('.')