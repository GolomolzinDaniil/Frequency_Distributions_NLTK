import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import sys
import argparse

def process_text_file(input_path: str, output_path: str, language: str = 'russian') -> None:
    """
    Process text file: remove stopwords, convert to lowercase,
    sort unique words and save the result.
    
    Args:
        input_path: path to input .txt file
        output_path: path to output .txt file
        language: language for stopwords (default: 'russian')
    """

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        if not text:
            print("File is empty")
            return
        
        # Tokenization and punctuation removal
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in string.punctuation]

        # Convert to lowercase
        tokens = [word.lower() for word in tokens]

        filtered_tokens = [word for word in tokens if not word in stopwords.words(language)]

        # Sort unique words
        unique_sorted_words = sorted(set(filtered_tokens))

        # Save result
        with open(output_path, 'w', encoding='utf-8') as f:
            for word in unique_sorted_words:
                f.write(word + '\n')
        
        print(f"Processing completed.")

    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except LookupError:
        print("Error: required NLTK packages not found. Run download_packages.py")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    """Main function with command line argument processing"""
    parser = argparse.ArgumentParser(description='Process text file: remove stopwords, sort unique words')
    parser.add_argument('input_file', help='Path to input .txt file')
    parser.add_argument('output_file', help='Path to output .txt file')
    parser.add_argument('--language', '-l', default='russian', 
                       help='Language for stopwords (default: russian)')
    
    args = parser.parse_args()

    process_text_file(args.input_file, args.output_file, args.language)


if __name__ == "__main__":
    main()


