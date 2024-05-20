import unittest
from main import find_most_frequent_word

class TestMostFrequentWord(unittest.TestCase):

    def test_find_most_frequent_word(self):
        # Тестовые данные
        mock_file_content = "Привет, мир. Это тестовый текст для поиска самого частого слова. Привет."
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "привет")

    def test_find_most_frequent_word_empty_file(self):
        # Тестовые данные
        mock_file_content = ""
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "")

    def test_find_most_frequent_word_multiple_occurrences(self):
        # Тестовые данные
        mock_file_content = "apple orange banana apple orange apple"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "apple")

    def test_find_most_frequent_word_case_sensitive(self):
        # Тестовые данные
        mock_file_content = "Apple apple aPPle aPple"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "apple")

    def test_find_most_frequent_word_special_characters(self):
        # Тестовые данные
        mock_file_content = "apple, orange, banana, apple, orange, apple, 123"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "apple")

    def test_find_most_frequent_word_long_text(self):
        # Тестовые данные
        mock_file_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "lorem")

    def test_find_most_frequent_word_numbers(self):
        # Тестовые данные
        mock_file_content = "one two three four one two three one"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "one")

    def test_find_most_frequent_word_punctuation(self):
        # Тестовые данные
        mock_file_content = "Hello, world! This is a test. Hello."
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "hello")

    def test_find_most_frequent_word_unicode(self):
        # Тестовые данные
        mock_file_content = "Привет мир. Привет Привет"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "привет")

    def test_find_most_frequent_word_spaces(self):
        # Тестовые данные
        mock_file_content = "apple   orange banana   apple orange"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "apple")

    def test_find_most_frequent_word_mixed_case(self):
        # Тестовые данные
        mock_file_content = "Apple aPPle aPple aPPle"
        most_frequent_word = find_most_frequent_word(mock_file_content)
        self.assertEqual(most_frequent_word, "apple")

if __name__ == '__main__':
    unittest.main()
