def are_anagram(word1: str, word2: str):
    """
    We create frequency dictionaries for each word and compare if they're
    the same
    """

    word1_dict = {}
    for letter in word1:
        word1_dict[letter] = word1_dict.get(letter, 0) + 1

    word2_dict = {}
    for letter in word2:
        word2_dict[letter] = word2_dict.get(letter, 0) + 1

    # return Counter(word1) == Counter(word2)
    return word1_dict == word2_dict


if __name__ == "__main__":
    anagrams = [
        ("night", "thing"),
        ("skin", "sink"),
        ("study", "dusty"),
        ("aabbcc", "cbacba"),
    ]

    assert all([are_anagram(*words) for words in anagrams])
