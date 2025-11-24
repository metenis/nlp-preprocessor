"""
N-Gram Generation Module.

This module provides functionality to generate N-grams from tokenized text.
N-grams are contiguous sequences of n items from a given sample of text 
and are crucial for capturing context in NLP tasks (e.g., distinguishing 
"New York" from just "New" and "York").
"""

from nltk.util import ngrams
from typing import List, Tuple

def get_ngrams(tokens: List[str], n: int = 2) -> List[Tuple[str, ...]]:
    """
    Generates a list of n-gram tuples from a sequence of tokens.

    Args:
        tokens (List[str]): The list of tokens (words) to process.
        n (int, optional): The number of tokens in each n-gram. 
                           Defaults to 2 (Bigrams).

    Returns:
        List[Tuple[str, ...]]: A list of tuples, where each tuple represents an n-gram.
                               Example (n=2): [('artificial', 'intelligence'), ('intelligence', 'is')]
    """
    # Return empty if tokens list is empty or shorter than n to avoid errors
    if not tokens or len(tokens) < n:
        return []

    # nltk.util.ngrams returns a generator; we convert it to a list 
    # for immediate consumption and easier debugging.
    return list(ngrams(tokens, n))