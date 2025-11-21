# Advanced NLP Text Preprocessor

**A complete, modular Python pipeline for transforming raw text into structured data for Natural Language Processing.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![NLTK](https://img.shields.io/badge/Dependency-NLTK-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Preparing text data is the most time-consuming part of AI development. This repository provides a suite of tools to handle the entire preprocessing lifecycle. Unlike basic cleaning scripts, this toolkit handles morphological analysis (**Lemmatization**) and context extraction (**N-grams**).

It is designed to be modular: use the whole pipeline or import specific functions as needed.

## Key Features

* **Text Normalization:** Robust lowercasing and unicode normalization.
* **Stopword Removal:** Filters out common non-informative words (e.g., "and", "the", "is") using NLTK corpuses.
* **Lemmatization:** Converts words to their dictionary root (e.g., "running" → "run", "better" → "good") using WordNet. This is superior to simple stemming.
* **N-Gram Generation:** Creates Bigrams (2-word context) and Trigrams (3-word context) to capture phrase meaning.
* **Noise Removal:** Strips punctuation, numbers, and special characters.

## sProject Structure

```text
nlp-preprocessor/
├── data/
│   └── raw_sentences.txt    # Example input
├── src/
│   ├── __init__.py
│   ├── preprocessing.py     # Core functions (lower, remove_stops, lemmatize)
│   └── ngrams.py            # N-gram generation logic
├── main.py                  # The pipeline runner
├── requirements.txt
└── README.md
