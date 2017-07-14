from collections import Counter
from utils import handle_wildcard
import click

class Main:
    """
    Main class with properties to find magic and longest
    """
    def magic(self, jumble, word):
        """
        Function to determine if a given word can be formed
        using the letters given.

        Args:
            param1(str): jumble.
            param2(str): word.

        Returns:
            bool : True if word can be formed, False otherwise.

        Raises:
            TypeError: if params are not string.
        """

        if len(jumble) < len(word):
            return False
        counter = Counter(word) - Counter(jumble)
        if '?' not in jumble:
            return not counter
        return handle_wildcard(counter, jumble)

    def longest(self, jumble):
        """
        Function to determine the longest word
        in the enable1 dictionary that can be formed.

        Args:
            param1: jumble.

        Returns:
            longest word in the enable1 dictionary
            that can be formed using jumble

        Raises:
            TypeError: if params are not string.

        In case of tie most recent match is returned
        """
        with open("enable1.txt") as f:
            content = f.readlines()
            content = [c.strip() for c in content]
            max_word = ""
            for index, c in enumerate(content):
                if self.magic(jumble, c) and len(c) >= len(max_word):
                    max_word = c
        return max_word.strip()

