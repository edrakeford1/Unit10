"""
Program: Word Count Analyzer
Name: Elijah Drakeford
Purpose: Analyze a selected file count the words
Date: 03/29/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self):
        try:
            if not self._filepath.exists():
                raise FileNotFoundError
                
            with self._filepath.open("r", encoding = "utf-8") as file:
                for line in file:
                       
                    # Remove punctuation
                    translator = str.maketrans('', '', string.punctuation)
                    line = line.translate(translator)

                    # Convert to lowercase
                    line = line.lower()

                    # Split into words
                    words = line.split()

                    # Count words
                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1

            return True
            
        except FileNotFoundError:
            print("Error: File not found.")
            return False
            
    def print_report(self):
        print("\n--- Word Analyzer ---")

        for word in sorted(self._frequencies.keys()):
            print(f"{word}: {self._frequencies[word]}")

def main():

    # Dictionary of file choices
    files = {
        "1": ("Monte Cristo (Chapter 1)", "monte_cristo.txt"),
        "2": ("Princess Mars (Chapter 1)", "princess_mars.txt"),
        "3": ("Tarzan (Chapter 1)", "Tarzan.txt"),
        "4": ("Treasure Island (Chapter 1)", "treasure_island.txt"),
        "5": ("Exit", None)
    }

    while True:
        print("\n --- Word Analyzer ---")
        print("Please select a file to analyze:")

        for key, (name, _) in files.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("Invalid choice. Please select from 1-5.")
            continue

        filename = files[choice][1]

        analyzer = WordAnalyzer(filename)

        if analyzer.process_file():
            analyzer.print_report()

# Run program
if __name__ == "__main__":
    main()