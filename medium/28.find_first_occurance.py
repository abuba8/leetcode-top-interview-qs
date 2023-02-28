def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle not in haystack: return -1
    else: return haystack.find(needle)

x = strStr("sadbutsad", "sad")
print(x)
x = strStr("leetcode", "leeto")
print(x)
