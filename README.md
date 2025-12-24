# Text Analysis Python

**Overview**
- A modular Python tool for **character-level text analysis**, capable of computing counts of letters, digits, spaces, and symbols.
- Generates a structured summary for each input string and outputs a detailed list of characters. Built to be easily integrated into **text preprocessing, log analysis, and cybersecurity pipelines**.
---

## Problem Statement
- Raw text data is often unstructured, making automated analysis challenging. 
- Understanding the composition of text—letters, numbers, spaces, and symbols is a **fundamental skill in cybersecurity, data validation, and text analytics**. 
- This project provides a reusable, precise solution for extracting this information efficiently.
---

## Approach
- Accepts input as **sentences or text files**.
- Iterates over each character, classifying it into letters, digits, spaces, or symbols.
- Compiles counts and produces a **structured dictionary output**, making it ready for further processing or visualization.
- Designed with **modularity in mind**, allowing integration with larger Python pipelines or analytical workflows. 
---

## Installation & Usage.

```bash
# 1. Clone the repository:
   git clone https://github.com/SecEngineerX/text-analysis-python.git

# 2. Navigate to the project folder:
   cd text-analysis-python

# 3. Run the analyzer script:
   python3 text_analyzer.py

# 4. Replace sample_data.txt or provide your own text input to analyze.
```
## Sample Output

- Sentence: I went to school today!
- Letters: 18
- Digits: 0
- Spaces: 4
- Symbols: 1 
- Characters List:
```text
['I', 'w', 'e', 'n', 't', 't', 'o', 's', 'c', 'h', 'o', 'o', 'l', 't', 'o', 'd', 'a', 'y']
```
======================================================
