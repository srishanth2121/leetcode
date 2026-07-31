class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words) :
            return False

        letter_to_word = {}
        word_to_letter = {}

        for letter,word in zip(pattern,words):
            if letter in letter_to_word:
                if letter_to_word[letter] != word:
                    return False
            else:
                    letter_to_word[letter] = word


            if word in word_to_letter:
                if word_to_letter[word] != letter:
                    return False
            else:
                    word_to_letter[word] = letter

        return True




        