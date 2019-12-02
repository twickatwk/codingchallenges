import unittest

class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}

        array_of_words = self.split_words(input_string)

        for word in array_of_words:
            self.add_word(word)

    def split_words(self, input_string):
        words = []
        current_word_start_index = 0
        current_word_length = 0

        for i, char in enumerate(input_string):
            if i == len(input_string)-1:
                if char.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:current_word_start_index + current_word_length]
                    self.add_word(current_word)
                    break
            elif char == '.':
                if i < len(input_string) - 1 and input_string[i+1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[current_word_start_index:current_word_start_index + current_word_length]
                        self.add_word(current_word)
                        current_word_length = 0
            elif char.isalpha() or (current_word_length > 0 and char == '-') or (current_word_length > 0 and char == '\''):
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1
            else:
                word = input_string[current_word_start_index:current_word_start_index+current_word_length]
                if len(word) > 0:
                    words.append(word)
                current_word_length = 0
        
        return words

    # Helper method to add word into the word cloud
    def add_word(self, word):

        if word in self.words_to_counts:
            self.words_to_counts[word] += 1
        
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]
        
        else:
            self.words_to_counts[word] = 1



# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

