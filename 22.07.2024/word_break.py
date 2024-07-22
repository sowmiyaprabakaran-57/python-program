def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]
print(word_break("leetcode", {"leet", "code"}))  
print(word_break("applepenapple", {"apple", "pen"}))  
print(word_break("catsandog", {"cats", "dog", "sand", "and", "cat"}))  
