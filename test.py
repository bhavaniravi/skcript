from skcript import Main
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['skcript.py', __file__])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class MagicTest(unittest.TestCase):

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
        """Test for false condition in a set of params"""
        dictionary = {"jubmle": "word",
                      "jumble1": "word1",
                      "uwtaqicy": "watch"}
        for key, value in dictionary.items:
            self.assertEqual(False, self.main.magic(key, value))

    def test_magic_for_false_without_wildcards(self):
        """Test for true condition in a set of params"""
        dictionary = {"edzlatsh": "hazel",
                      "code": "code"
                      }
        for key, value in dictionary.items():
            with self.subTest(key=key, value=value):
                self.assertEqual(True, self.main.magic(key, value))


if __name__ == '__main__':
    unittest.main()
