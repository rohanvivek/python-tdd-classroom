class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        input_str = list(reversed(input_str))

        return("".join(input_str))

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        if character.lower() in vowel:
            return True
        return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        words_list = sentence.split()
        word_len = []
        for n in words_list:
                word_len.append((len(n), n))
        return (max(word_len, key = lambda i : i[0])[1])

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        words_list = text.split()
        word_len = []
        for n in words_list:
                word_len.append((len(n)))
        return (word_len)
        
