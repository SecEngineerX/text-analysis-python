"""
Text Analyzer Module
Analyzes text (from sentences or files) for:
- Letters
- Digits
- Spaces
- Symbols
- Character breakdown
- Total characters and percentages
"""

import argparse

def text_analyzer(text: str) -> dict:
    """
    Analyzes the text and returns a dictionary with counts, percentages, and letters list.
    """
    analysis = {
        "letters": 0,
        "digits": 0,
        "spaces": 0,
        "symbols": 0,
        "letters_list": []
    }

    for char in text:
        if char.isalpha():
            analysis["letters"] += 1
            analysis["letters_list"].append(char)
        elif char.isdigit():
            analysis["digits"] += 1
        elif char.isspace():
            analysis["spaces"] += 1
        else:
            analysis["symbols"] += 1

    total_chars = len(text)
    analysis["total_chars"] = total_chars
    if total_chars > 0:
        analysis["percent_letters"] = analysis["letters"] / total_chars * 100
        analysis["percent_digits"] = analysis["digits"] / total_chars * 100
        analysis["percent_spaces"] = analysis["spaces"] / total_chars * 100
        analysis["percent_symbols"] = analysis["symbols"] / total_chars * 100
    else:
        analysis["percent_letters"] = 0
        analysis["percent_digits"] = 0
        analysis["percent_spaces"] = 0
        analysis["percent_symbols"] = 0

    return analysis


def print_analysis(sentence: str, result: dict):
    """
    Nicely format and print the analysis of a sentence or text block.
    """
    print(f"Sentence: {sentence.strip()}")
    print(f" Letters: {result['letters']} ({result['percent_letters']:.2f}%)")
    print(f" Digits: {result['digits']} ({result['percent_digits']:.2f}%)")
    print(f" Spaces: {result['spaces']} ({result['percent_spaces']:.2f}%)")
    print(f" Symbols: {result['symbols']} ({result['percent_symbols']:.2f}%)")
    print(f" Total Characters: {result['total_chars']}")
    print(f" Characters List: {', '.join(result['letters_list'])}")
    print("=" * 50)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze text files or sentences.")
    parser.add_argument("-f", "--file", help="Path to a text file to analyze")
    args = parser.parse_args()

    sentences = []

    if args.file:
        try:
            with open(args.file, "r") as f:
                sentences = f.readlines()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            exit(1)
    else:
        # default sentences if no file is provided
        sentences = [
            "I went to school today!",
            "Python is fun 123",
            "I love coding :)"
        ]

    for sentence in sentences:
        result = text_analyzer(sentence)
        print_analysis(sentence, result)

