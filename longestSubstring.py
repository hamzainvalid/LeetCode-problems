def lengthOfLongestSubstring(s):
    counter = 0
    l1 = []
    while True:
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    continue
                else:
                    l1.append(s[i])
                    l1.append(s[j])
        for x in l1:
            if x != s[i] and x != s[j]:
                counter += 1
                break
        return counter

print(lengthOfLongestSubstring('abcabcbb'))