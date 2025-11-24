"""
Text Cleaning and Normalization Module.

This module handles the initial preprocessing steps:
1. Noise Removal: Lowercasing and stripping punctuation.
2. Stopword Removal: Filtering out common, low-value words.
"""

import re
from typing import List
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_noise(text: str) -> str:
    """
    Normalizes text by converting to lowercase and removing punctuation.

    Args:
        text (str): The raw input string.

    Returns:
        str: The cleaned, lowercased string with no punctuation.
    """
    # 1. Uniformity: Convert to lowercase
    text = text.lower()
    
    # 2. Noise Removal: Remove punctuation characters using Regex
    # [^\w\s] matches any character that is NOT a word char (alphanumeric) or whitespace
    text = re.sub(r'[^\w\s]', '', text)
    
    return text

def remove_stopwords(text: str) -> List[str]:
    """
    Tokenizes text and removes standard English stopwords.

    Args:
        text (str): The cleaned text string (result of remove_noise).

    Returns:
        List[str]: A list of tokens with stopwords removed.
    """
    # Load English stopwords (e.g., 'the', 'is', 'in')
    # converting to a set provides O(1) lookup speed
    stop_words = set(stopwords.words('english'))
    
    # Convert string to individual tokens (words)
    tokens = word_tokenize(text)
    
    # Filter tokens that exist in the stop_words set
    filtered_tokens = [w for w in tokens if w not in stop_words]
    
    return filtered_tokens