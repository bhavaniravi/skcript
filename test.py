from skcript import Main
import unittest
import pep8
import random


class TestCodeFormat(unittest.TestCase):
    """
    Unit test to maintain pep8 standards
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['skcript.py', __file__])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class MagicTest(unittest.TestCase):
    """
    Unit test for magic property of main method
    """

    def setUp(self):
        """ SetUp Main's object """
        self.main = Main()

    def test_magic_with_empty_string(self):
        """Test on empty Strings"""
        self.assertEqual(True, self.main.magic("", ""))

    def test_magic_with_jumble_empty(self):
        """Test on empty jumble param"""
        self.assertEqual(False, self.main.magic("", "road"))

    def test_magic_with_word_empty(self):
        """Test on empty word param"""
        self.assertEqual(True, self.main.magic("road", ""))

    def test_magic_for_false_without_wildcards(self):
        """
        Test for true condition in a set of params
        The test has n words each is shuffled and tested across words,
        after removing few indexes
        """
        words = ("python", "jumble", "easy", "difficult",
                 "answer",  "xylophone")
        for word in words:
            jumble = ''.join(random.sample(word, len(word)))[2:]
            with self.subTest(jumble=jumble, word=word):
                self.assertEqual(False, self.main.magic(jumble, word))

    def test_magic_for_true_without_wildcards(self):
        """
        Test for true condition in a set of params
        The test has n words each is shuffled
        and tested across words
        """
        words = ("python", "jumble", "easy", "difficult",
                 "answer",  "xylophone")

        for word in words:
            jumble = ''.join(random.sample(word, len(word)))
            with self.subTest(jumble=jumble, word=word):
                self.assertEqual(True, self.main.magic(jumble, word))

    def test_magic_for_true_with_wildcards(self):
        """
        Test for true outcomes in a set of params with wildcards
        The test has n words each is shuffled
        and tested across words
        """
        words = {"p???????": "python",
                 "j??????": "jumble",
                 "e???": "easy",
                 "d????????t": "difficult",
                 "a?????r": "answer"}
        for jumble, word in words.items():
            with self.subTest(jumble=jumble, word=word):
                self.assertEqual(True, self.main.magic(jumble, word))

    def test_magic_for_false_with_wildcards(self):
        """
        Test for False outcomes in a set of params with wildcards
        The test has n words each is shuffled
        and tested across words
        """
        words = {"p???": "python",
                 "j???": "jumble",
                 "e??": "easy",
                 "d???": "difficult",
                 "a???": "answer",
                 "a???": "a--"}
        for jumble, word in words.items():
            with self.subTest(jumble=jumble, word=word):
                self.assertEqual(False, self.main.magic(jumble, word))


def find_longest_word_in_enable():
    with open("enable1.txt") as f:
        content = f.readlines()
        content = [c.strip() for c in content]
        max_length_word = max(content, key=len)
        print(max_length_word)
        return len(max_length_word), max_length_word


class LongestTest(unittest.TestCase):
    def setUp(self):
        self.main = Main()

    # def test_empty_jumble(self):
    #     """Test for empty string"""
    #     self.assertEqual("", self.main.longest(""))

    def test_longest_wildcard(self):
        """To test longest word is found using wildcard and jumble of itself"""

        max_length_word = "ethylenediaminetetraacetates"
        max_len = len(max_length_word)

        # comment above 2 lines and
        # uncomment next line if content of enable1.txt is changed
        # max_len, max_length_word = find_longest_word_in_enable()
        self.assertEqual(max_length_word, self.main.longest("?" * max_len))
        jumble = ''.join(random.sample(max_length_word, max_len))
        self.assertEqual(max_length_word, self.main.longest(jumble))

    def test_for_outcomes(self):
        self.assertEqual("turquois", self.main.longest("uruqrnytrois"))
        self.assertEqual("greengrocery", self.main.longest("rryqeiaegicgeo??"))


if __name__ == '__main__':
    unittest.main()
