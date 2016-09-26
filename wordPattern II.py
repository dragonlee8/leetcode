class Solution(object):
    def helper(self, s, pattern, mapping, rmapping):
        if not pattern and not s:
            return True

        if not s or not pattern:
            return False

        if pattern[0] in mapping:
            if mapping[pattern[0]] != s[:len(mapping[pattern[0]])]:
                return False
            else:
                return self.helper(s[len(mapping[pattern[0]]):], pattern[1:], mapping, rmapping)

        for i in range(len(s)):
            word = ''.join(s[:i+1])
            if word in rmapping:
                continue

            mapping[pattern[0]] = word
            rmapping[word] = pattern[0]
            if self.helper(s[i+1:], pattern[1:], mapping, rmapping):
                return True

            del mapping[pattern[0]]
            del rmapping[word]

        return False

    def wordPattern(self, pattern, s):
        if not pattern and not s:
            return True
        if not pattern or not s:
            return False

        mapping, rmapping = {}, {}
        return self.helper(s, pattern, mapping, rmapping)

so = Solution()
print so.wordPattern('abab', 'redblueredblue')
