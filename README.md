# Advanced NLP Text Preprocessor

A complete, modular Python pipeline for transforming raw text into structured data for Natural Language Processing.

# Overview

Preparing text data is the most time-consuming part of AI development. This repository provides a suite of tools to handle the entire preprocessing lifecycle. Unlike basic cleaning scripts, this toolkit handles morphological analysis (Lemmatization) and context extraction (N-grams) to preserve semantic meaning.

It is designed to be modular: use the whole pipeline via main.py or import specific functions into your own scripts.

# Key Features

Text Normalization: Robust lowercasing and punctuation removal.

Stopword Removal: Filters out high-frequency, low-information words (e.g., "and", "the", "is") using NLTK corpora.

Lemmatization: Converts words to their dictionary root (e.g., "running" → "run", "better" → "good") using WordNet. Superior to simple stemming.

N-Gram Generation: Creates Bigrams (2-word context) to capture phrases like "Machine Learning" or "New York".

Noise Removal: Strips digits, punctuation, and special characters.

Project Structure

nlp-preprocessor/
├── data/
│   └── input_data.txt       # Example input text
├── src/
│   ├── __init__.py
│   ├── cleaner.py           # Normalization & Stopword logic
│   ├── lemmatizer.py        # Morphological analysis (WordNet)
│   └── ngrams.py            # N-gram generation logic
├── main.py                  # The pipeline entry point
├── requirements.txt
└── README.md


Getting Started

Prerequisites

Python 3.8+

NLTK (Natural Language Toolkit)

Installation

Clone the repository:

git clone [https://github.com/metenis/nlp-preprocessor.git](https://github.com/metenis/nlp-preprocessor.git)


Install dependencies:

pip install -r requirements.txt


Run the pipeline:
The main.py script automatically checks for and downloads required NLTK data (including punkt, punkt_tab, stopwords, and wordnet) on the first run.

python main.py


# Usage Examples

1. The Full Pipeline (Cleaning + Lemmatization)

You can import individual modules to build custom workflows.

from src.cleaner import remove_noise, remove_stopwords
from src.lemmatizer import lemmatize_text

raw_text = "The detailed studies were running quickly!"

# Step 1: Lowercase & Remove Punctuation
step1 = remove_noise(raw_text) 
# -> "the detailed studies were running quickly"

# Step 2: Remove Stopwords
step2 = remove_stopwords(step1) 
# -> ['detailed', 'studies', 'running', 'quickly']

# Step 3: Lemmatize (Get roots)
final_output = lemmatize_text(step2)

print(final_output)
# Output: ['detailed', 'study', 'run', 'quickly']


2. Generating N-Grams

Useful for extracting context or common phrases.

from src.ngrams import get_ngrams

tokens = ['artificial', 'intelligence', 'is', 'powerful']

# Get Bigrams (n=2)
bigrams = get_ngrams(tokens, n=2)

print(bigrams)
# Output: [('artificial', 'intelligence'), ('intelligence', 'is'), ('is', 'powerful')]


Comparison: Lemmatization vs. Stemming

This repo uses Lemmatization for higher accuracy in downstream tasks.

Feature

Stemming (Not used)

Lemmatization (Used Here)

Method

Chops off the end of words

Looks up dictionary meaning

Input: "Caring"

Car (Incorrect meaning)

Care (Correct verb)

Input: "Better"

Better

Good

Speed

Fast

Slower but semantically accurate

# Contributing

Contributions are welcome!

Fork the project.

Create your feature branch (git checkout -b feature/NewFeature).

Commit your changes.

Push to the branch and open a Pull Request.

License

Distributed under the MIT License. See LICENSE for more information.
