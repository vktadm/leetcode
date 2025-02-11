class Solution(object):
    """Given two strings ransomNote and magazine,
    return true if ransomNote can be constructed
    by using the letters from magazine and false otherwise.

    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Input: ransomNote = "aa", magazine = "aab"
    Output: true
    """
    def canConstruct(self, ransom_note, magazine):
        """
        :type ransom_note: str
        :type magazine: str
        :rtype: bool
        """
        # for letter in set(ransom_note):
        #     if ransom_note.count(letter) > magazine.count(letter):
        #         return False
        # return True

        magazine_count = {}

        # Count the frequency of each character in magazine
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1

        # Check if the ransomNote can be constructed from magazine
        for char in ransom_note:
            if char not in magazine_count or magazine_count[char] == 0:
                return False
            magazine_count[char] -= 1

        return True
