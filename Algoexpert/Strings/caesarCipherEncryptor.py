import unittest

# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
# Given a non-empty string of lowercase letters and a non-negative integer
# value representing a key, write a function that returns a new string obtained
# by shifting every letter in the input string by k positions in the alphabet.

# Time: O(n) | Space: O(n)
def caesarCipherEncryptor(string, key):

    result = ""
    for char in string:
        shift = key % 26
        new_value = ord(char) + shift
        if new_value > 122:
            result += chr(new_value-26)
        else:
            result += chr(new_value)
    
    return result

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("abc", 0), "abc")

    def test_case_2(self):
        self.assertEqual(caesarCipherEncryptor("abc", 3), "def")

    def test_case_3(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")

    def test_case_4(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 5), "cde")

    def test_case_5(self):
        self.assertEqual(caesarCipherEncryptor("abc", 26), "abc")

    def test_case_6(self):
        self.assertEqual(caesarCipherEncryptor("abc", 52), "abc")

    def test_case_7(self):
        self.assertEqual(caesarCipherEncryptor("abc", 57), "fgh")


if __name__ == "__main__":
    unittest.main()

