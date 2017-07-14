from collections import Counter


class Main:
    def magic(self, jumble, word):
        # condition 1
        if len(jumble) < len(word):
            return False
        counter = Counter(word) - Counter(jumble)
        if '?' not in jumble:
            return not counter
        return sum(counter.itervalues()) <= jumble.count('?')

    def longest(self, jumble):
        with open("enable1.txt") as f:
            content = f.readlines()
            content = [c.strip() for c in content]
            max_word = content[0]
            for index, c in enumerate(content):
                if self.magic(jumble, c) and len(max_word) < len(c):
                    max_word = c
        return max_word.strip()
