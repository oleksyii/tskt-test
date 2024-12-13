# how to find an anagram?
# to find all words that consist of the same letters! We don't really need to construct words. just classify whether or not tghe given set contains an anagram
import random
import string
from cmath import log
from typing import List
from collections import defaultdict
import time
import matplotlib.pyplot as plt
import numpy as np


def find_anagrams_slow(list_of_words: List[str]) -> List[List[str]]:
    """Takes O(n^2 * k*log(k))"""
    answers = defaultdict(set)
    for word_1 in list_of_words:
        sorted_word_1 = "".join(sorted(word_1))
        for word_2 in list_of_words[1:]:
            sorted_word_2 = "".join(sorted(word_2))
            if sorted_word_1 == sorted_word_2:
                # print(f"{word_1} is an anagram of {word_2}")
                answers[sorted_word_1].add(word_2)

        answers[sorted_word_1].add(word_1)

        # Remove the word, that is already processed
        list_of_words = list_of_words[1:]
    # Convert the dict of sets 'answers' into a list of lists
    result = [list(anagrams) for anagrams in answers.values()]
    return result


def find_anagrams(list_of_words: List[str]) -> List[List[str]]:
    """Takes O(k*log(n)) time where k average length of a word(fixed for us) and n is the number of words."""
    anagram_map = defaultdict(list)

    for word in list_of_words:
        # Sort the word to create a key
        sorted_word = "".join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())


def find_anagrams_optimized(list_of_words: List[str]) -> List[List[str]]:
    """
    Takes O(n * k) time.
    """
    anagram_map = defaultdict(list)

    for word in list_of_words:
        # Use a tuple of character counts as the key
        char_count = [0] * 26  # !!!!! Assuming only lowercase letters
        for char in word:
            char_count[ord(char) - ord("a")] += 1
        anagram_map[tuple(char_count)].append(word)

    return list(anagram_map.values())


def generate_anagram_strs(size: int, length: int = 5) -> List[str]:
    words = []
    for _ in range(size):
        word = "".join(random.choices(string.ascii_lowercase, k=length))
        words.append(word)
    return words


def plot_results_with_average(result_data: dict):
    sizes = list(result_data.keys())
    times = list(result_data.values())

    # Compute a moving average for smoothing
    window_size = 5
    moving_avg = np.convolve(times, np.ones(window_size) / window_size, mode="valid")

    plt.figure(figsize=(12, 6))

    # The raw data
    plt.plot(sizes, times, marker="o", linestyle="-", label="Measured Times", alpha=0.7)

    # The moving average
    avg_sizes = sizes[: len(moving_avg)]
    plt.plot(
        avg_sizes,
        moving_avg,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Average Trend",
    )

    plt.xlabel("Size of Input")
    plt.ylabel("Time Taken (seconds)")
    plt.title("Time Complexity Analysis with Trendline")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = find_anagrams_optimized(input)
    print(result)
    # print(generate_anagram_strs(10))
    # exit(0)
    # import gc

    # gc.disable()
    size = 0
    result_data = {}
    for i in range(500, 50000, 500):
        size = i
        strings = generate_anagram_strs(size)
        start = time.perf_counter()
        res = find_anagrams(strings)
        end = time.perf_counter()
        time_taken = end - start
        result_data[size] = time_taken
        print(f"Size: {size}, Time taken: {time_taken}")

    # gc.enable()
    plot_results_with_average(result_data)
    # print(f"Complexity of the algorithm is O({size * length * log(length)})")


if __name__ == "__main__":
    main()
