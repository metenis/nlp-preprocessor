
"""
NLP Preprocessing Pipeline Entry Point.

This script orchestrates the text cleaning process by:
1. Loading raw text data.
2. Applying normalization (lowercasing, noise removal).
3. Removing stopwords.
4. Lemmatizing tokens.
5. Generating N-grams for context.

Usage:
    python main.py
"""

import nltk
import sys
import os

# Import custom processing modules from the 'src' package
from src.cleaner import remove_noise, remove_stopwords
from src.lemmatizer import lemmatize_text
from src.ngrams import get_ngrams

def download_nltk_resources():
    """
    Checks for required NLTK corpora and tokenizers, downloading them if missing.
    
    Specific attention is paid to 'punkt_tab', which is required for 
    newer versions of NLTK (3.8.2+) to handle sentence tokenization correctly.
    """
    required_resources = [
        ('tokenizers/punkt', 'punkt'),
        ('tokenizers/punkt_tab', 'punkt_tab'),
        ('corpora/stopwords', 'stopwords'),
        ('corpora/wordnet', 'wordnet')
    ]

    print("Checking NLTK dependencies...")
    for resource_path, download_name in required_resources:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            print(f"Downloading missing resource: {download_name}...")
            nltk.download(download_name, quiet=True)
    
    # Ensure OMW-1.4 is available for WordNet lemmatizer
    try:
        nltk.data.find('corpora/omw-1.4')
    except LookupError:
        nltk.download('omw-1.4', quiet=True)

def run_pipeline(file_path):
    """
    Reads a text file and processes it through the NLP cleaning pipeline.

    Args:
        file_path (str): Relative or absolute path to the input text file.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains:
                    - 'original': The raw input sentence.
                    - 'lemmas': The list of cleaned, root-form tokens.
                    - 'bigrams': A list of bigram tuples found in the sentence.
    """
    print(f"--- Loading data from: {file_path} ---")
    
    processed_data = []

    # Verify file existence before attempting to open
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        print("Please ensure the data file exists or update the path.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Read lines and strip leading/trailing whitespace immediately
            raw_lines = [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    # --- Pipeline Execution ---
    for sentence in raw_lines:
        # Skip empty lines to prevent processing errors
        if not sentence: 
            continue 

        print(f"\nOriginal: {sentence}")
        
        # Step A: Normalization
        # Lowercasing and removing punctuation/special characters
        cleaned_text = remove_noise(sentence)
        
        # Step B: Stopword Removal
        # Filters out high-frequency words (the, is, and) that add noise
        tokens = remove_stopwords(cleaned_text)
        
        # Step C: Lemmatization
        # Reduces words to their base form (e.g., 'running' -> 'run')
        lemmas = lemmatize_text(tokens)
        
        # Step D: N-Gram Generation
        # Captures local context (2-word phrases) from the lemmatized tokens
        bigrams = get_ngrams(lemmas, n=2)

        # Log results to console
        print(f"Tokens:   {lemmas}")
        print(f"Bigrams:  {bigrams}")
        
        # Structure the data for potential export (JSON/CSV)
        processed_data.append({
            "original": sentence,
            "lemmas": lemmas,
            "bigrams": bigrams
        })

    print("\n--- Processing Complete ---")
    return processed_data

if __name__ == "__main__":
    # 1. Initialize environment (Download NLTK data)
    download_nltk_resources()
    
    # 2. Define input path
    # Ensure this matches your project structure (data/input_data.txt)
    input_file = os.path.join("data", "input_data.txt")
    
    # 3. Execute Pipeline
    run_pipeline(input_file)