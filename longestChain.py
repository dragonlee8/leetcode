# Complete the function below.


def  longestChain(words):
    def cmp(a, b):
        return len(a) - len(b)
    
    words.sort(cmp)
    
    maxlen = 0
    mapping = {}
    result = 0
    dp = {}
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            newStr = ''.join(word[:i]+word[i+1:])
            if newStr in dp:
                dp[word] = max(dp[word], 1+ dp[newStr])
                result = max(result, dp[word])
                
    return result


