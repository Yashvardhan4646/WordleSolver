# 🔎 Five-Letter Word Finder

A simple Python program that searches a text file for words matching specific letter positions. Enter up to five letters and leave any position blank to match any character at that position.

## ✨ Features

- **Position-based search:** Match letters at specific positions in a word.
- **Optional letters:** Leave inputs blank to ignore those positions.
- **Text-file based:** Reads words from `words.txt`.
- **Simple CLI:** Runs directly in the terminal without external libraries.
- **Beginner-friendly:** Demonstrates file handling, loops, conditions, and string manipulation in Python.

## 📁 Project Structure

```text
Five-Letter-Word-Finder/
├── main.py
├── words.txt
└── README.md
```

- `main.py` — Contains the word-search program.
- `words.txt` — Contains the words to search, with one word per line.
- `README.md` — Project documentation.

## 🛠️ Requirements

- Python 3.x
- A plain-text file named `words.txt`
## Credits for words file 'https://github.com/tabatkins/wordle-list/blob/main/words'

No third-party packages are required.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the URL with your repository's actual URL.

### 2. Open the project directory

```bash
cd Five-Letter-Word-Finder
```

### 3. Prepare the word list

Create a file named `words.txt` in the same directory as `main.py`.

Add one word per line:

```text
apple
angle
ample
apply
about
grape
```

### 4. Run the program

```bash
python main.py
```

On some Windows installations, you may need:

```bash
py main.py
```

## 💡 How to Use

The program asks you to enter five letters, one for each position.

```text
Enter first letter: a
Enter second letter:
Enter third letter: p
Enter fourth letter:
Enter fifth letter: e
```

The program prints every word matching the specified positions.

**Example output:**

```text
apple
ample
```

### Search Rules

| Input | Meaning |
|---|---|
| First letter | Match the first character |
| Second letter | Match the second character |
| Third letter | Match the third character |
| Fourth letter | Match the fourth character |
| Fifth letter | Match the fifth character |
| Blank input | Ignore that position |

For example, entering `a`, blank, `p`, blank, `e` matches five-letter words that begin with `a`, contain `p` as the third character, and end with `e`.

## ⚙️ How It Works

1. Opens `words.txt` in read mode.
2. Collects five letter inputs from the user.
3. Reads the file one line at a time.
4. Removes surrounding whitespace and newline characters.
5. Checks each character against the corresponding input.
6. Prints words that satisfy all specified positions.
7. Continues until the file has been processed.

## ⚠️ Notes and Limitations

- The default search is case-sensitive. For example, `A` and `a` are different.
- Blank inputs are treated as wildcards.
- The program checks the first five character positions. It does not enforce a five-character word length, so longer words may also match.
- Words shorter than five characters are skipped.
- The file `words.txt` must exist in the expected directory.

## 🔮 Possible Improvements

- Add case-insensitive searching.
- Support words of different lengths.
- Allow wildcard patterns in a single input, such as `a?p?e`.
- Display the total number of matches.
- Add support for filtering words by known and excluded letters.
- Build a graphical user interface.

## 📚 Concepts Used

- Python functions
- File handling (`open()`, `readline()`)
- `while` loops
- Conditional statements
- String indexing and comparison
- User input

## 📄 License

This project is open for learning and personal use. Add a license file if you intend to distribute it under specific terms.

---

