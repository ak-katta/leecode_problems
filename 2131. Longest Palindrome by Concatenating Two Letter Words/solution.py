class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        length = 0
        used_center = False

        for word in list(word_count.keys()):
            rev = word[::-1]

            if word == rev:
                pairs = word_count[word] // 2
                length += pairs * 4
                word_count[word] -= pairs * 2

                if not used_center and word_count[word] > 0:
                    length += 2
                    used_center = True

            elif rev in word_count:
                pairs = min(word_count[word], word_count[rev])
                length += pairs * 4
                word_count[word] -= pairs
                word_count[rev] -= pairs

        return length
