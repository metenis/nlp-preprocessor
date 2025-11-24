"""
Lemmatization Module.

This module handles morphological analysis using WordNet.
It reduces words to their base/dictionary form (lemma), which is superior 
to stemming as it preserves actual meaning (e.g., 'better' -> 'good').
"""

from typing import List
from nltk.stem import WordNetLemmatizer

def lemmatize_text(tokens: List[str]) -> List[str]:
    """
    Converts a list of tokens to their root forms (lemmas).

    Args:
        tokens (List[str]): A list of words to be lemmatized.

    Returns:
        List[str]: A list of lemmatized words.
    """
    lemmatizer = WordNetLemmatizer()
    
    # We use pos='v' (verb) as the default part-of-speech tag.
    # This helps map 'running' -> 'run'. Without it, 'running' might remain 'running' (noun).
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
    
    return lemmas