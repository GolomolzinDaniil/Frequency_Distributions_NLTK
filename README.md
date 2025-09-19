# Text Processing and Word Frequency Analysis with NLTK

## 1. What it does
This project provides two Python scripts for text preprocessing and frequency analysis:

1. **Text_Processing_with_NLTK.py**  
   - Removes stopwords  
   - Converts words to lowercase  
   - Filters out punctuation  
   - Extracts unique words  
   - Sorts them alphabetically  
   - Saves the result to a file  

2. **frequency_distributions_NLTK.py**  
   - Uses the preprocessed words  
   - Calculates word frequency distribution with NLTK  
   - Returns a frequency dictionary  
   - Visualizes the top 10 most frequent words in a bar chart  

---

## Files

- `download_packages.py` - Downloads required NLTK packages
- `Frequency_Distributions.py` - File for creating a frequency dictionary
- `Text_Processing_with_NLTK.py` - Main text processing script

## Installation

1. Install required Python packages:
```bash
pip install nltk
```

2. Download NLTK data packages:
```bash
python download_packages.py
```

## Usage

Process a text file:
```bash
python Frequency_Distributions.py input.txt output.txt

```

Process with specific language (default: russian):
```bash
python Frequency_Distributions.py input.txt output.txt --language english
```

## Example

Input file (`input.txt`):
```
NLTK helps with natural language processing.
This is a powerful tool for text analysis.
```

Output file (`output.txt`):
```
analysis
helps
language
natural
nltk
powerful
processing
text
tool
```

## Requirements

- Python 3.6+
- NLTK library
