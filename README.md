# Anagram Finder - README

This project demonstrates how to classify and group words from a given set into anagrams. It includes implementations of two algorithms for finding anagrams, as well as tools for analyzing their performance.

## Features
- **Find Anagrams:** Classifies a list of words into groups of anagrams.
- **Optimized Algorithm:** Uses character frequency counting for better performance.
- **Performance Analysis:** Visualizes time complexity with trendlines.

---

## How to Run the Code

### Prerequisites
Ensure you have Python 3.7 or later installed. Additionally, install the required libraries:

```bash
pip install -r requirements.txt
```

### Running the Script
1. Execute the script using Python:

```bash
python anagram_finder.py
```

The script will:
- Run the `find_anagrams` function on sample input.
- Generate random word sets of varying sizes.
- Plot the performance of the algorithm over increasing input sizes.

---

## Algorithms and Complexity

### 1. **Basic Anagram Finder**
**Function:** `find_anagrams`

#### Complexity:
- **Time Complexity:** Sorting each word: `O(k log k)`, where `k` is the average word length.
- **Space Complexity:** Requires `O(n * k)` for storing sorted keys and grouped words.


#### Explanation:
- Each word is sorted alphabetically to form a key.
- Words sharing the same key are grouped into anagrams.

### 2. **Optimized Anagram Finder**
**Function:** `find_anagrams_optimized`

#### Complexity:
- **Time Complexity:**
  - Character counting for each word: `O(k)`.
  - For `n` words, total complexity is `O(n * k)`.
- **Space Complexity:**
  - Requires `O(n * k)` for storing character count tuples and grouped words.

#### Explanation:
- Instead of sorting, uses a fixed-size array to count character frequencies.
- Character frequency tuples serve as keys, avoiding redundant sorting.

---

## Performance Analysis

### Input Generation
The `generate_anagram_strs` function creates random lowercase words of specified lengths. These are used as inputs to evaluate the performance of the algorithms.

### Results Visualization
The script measures execution time for varying input sizes and plots:
- Raw execution times.
- A smoothed trendline using a moving average.

### Observations
1. **Basic Algorithm:**
   - Performs well for small input sizes but scales poorly due to \(O(n \cdot k \log k)\).
2. **Optimized Algorithm:**
   - Demonstrates superior scaling due to linear \(O(n \cdot k)\) complexity.

---

## Example Output
Sample input:
```python
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
```
Output:
```python
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

